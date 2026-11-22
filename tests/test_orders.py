import unittest
from datetime import datetime, timezone

from tillpoint import db, reports
from tillpoint.api import App
from tillpoint.catalog import Catalog, OutOfStock


class OrderDeskTest(unittest.TestCase):
    def setUp(self):
        self.conn = db.connect()
        self.app = App(self.conn)
        self.app.catalog.add_product("MUG", "Mug", 1200, stock=10)
        self.app.catalog.add_product("TEE", "T-shirt", 2500, stock=3)
        self.conn.execute("INSERT INTO coupons (code, kind, value) VALUES ('TEN', 'percent', 10)")

    def test_order_totals_with_tax(self):
        order = self.app.orders.create("ana", [("MUG", 2), ("TEE", 1)], region="CA")
        self.assertEqual(order["subtotal_cents"], 4900)
        self.assertEqual(order["tax_cents"], 355)
        self.assertEqual(order["total_cents"], 5255)
        self.assertEqual(self.app.catalog.get_product("MUG").stock, 8)

    def test_coupon_takes_ten_percent(self):
        order = self.app.orders.create("ana", [("MUG", 1)], coupon_code="TEN")
        self.assertEqual(order["discount_cents"], 120)
        self.assertEqual(order["total_cents"], 1080)

    def test_out_of_stock(self):
        with self.assertRaises(OutOfStock):
            self.app.orders.create("ana", [("TEE", 4)])
        self.assertEqual(self.app.catalog.get_product("TEE").stock, 3)
    def test_stale_catalog_cache_does_not_oversell(self):
        worker1 = Catalog(self.conn)
        worker2 = Catalog(self.conn)

        worker1.get_product("MUG")
        worker2.get_product("MUG")

        worker1.reserve("MUG", 7)

        with self.assertRaises(OutOfStock):
            worker2.reserve("MUG", 7)

        stock = self.conn.execute(
            "SELECT stock FROM products WHERE sku = 'MUG'"
        ).fetchone()["stock"]

        self.assertEqual(stock, 3)

    def test_payment_marks_order_paid(self):
        order = self.app.orders.create("ana", [("MUG", 1)])
        status, payload = self.app.handle("POST", "/webhooks/payments", {
            "id": "evt_1", "type": "payment.succeeded", "order_id": order["id"], "amount_cents": 1200})
        self.assertEqual((status, payload["status"]), (200, "paid"))
    def test_duplicate_payment_event_is_ignored(self):
        order = self.app.orders.create("ana", [("MUG", 1)])

        event = {
            "id": "evt_duplicate",
            "type": "payment.succeeded",
            "order_id": order["id"],
            "amount_cents": 1200,
        }

        self.app.payments.handle_event(event)
        self.app.payments.handle_event(event)

        self.assertEqual(self.app.payments.paid_cents(order["id"]), 1200)

    def test_cancel_paid_order_restocks(self):
        order = self.app.orders.create("ana", [("TEE", 2)])
        self.app.payments.handle_event(
            {"id": "evt_2", "type": "payment.succeeded", "order_id": order["id"], "amount_cents": 5000})
        self.app.orders.cancel(order["id"])
        self.assertEqual(self.app.catalog.get_product("TEE").stock, 3)
    def test_cancel_pending_order_restocks(self):
        order = self.app.orders.create("ana", [("TEE", 2)])
        self.assertEqual(self.app.catalog.get_product("TEE").stock, 1)

        self.app.orders.cancel(order["id"])

        self.assertEqual(self.app.catalog.get_product("TEE").stock, 3)
        self.assertEqual(self.app.orders.get(order["id"])["status"], "cancelled")

    def test_daily_sales(self):
        order = self.app.orders.create("ana", [("MUG", 1)])
        noon = datetime(2025, 3, 10, 12, 0, tzinfo=timezone.utc)
        self.app.payments.handle_event(
            {"id": "evt_3", "type": "payment.succeeded", "order_id": order["id"], "amount_cents": 1200}, now=noon)
        self.assertEqual(reports.daily_sales(self.conn, "2025-03-10"),
                      {"day": "2025-03-10", "revenue_cents": 1200, "orders": 1})
    def test_daily_sales_india_timezone(self):
        order = self.app.orders.create("ana", [("MUG", 1)])
        payment_time = datetime(2025, 3, 9, 19, 0, tzinfo=timezone.utc)

        self.app.payments.handle_event(
            {
                "id": "evt_india",
                "type": "payment.succeeded",
                "order_id": order["id"],
                "amount_cents": 1200,
            },
            now=payment_time,
        )

        self.assertEqual(
            reports.daily_sales(self.conn, "2025-03-10", utc_offset_minutes=330),
            {"day": "2025-03-10", "revenue_cents": 1200, "orders": 1},
        )
    def test_price_change(self):
        self.app.handle("PUT", "/products/MUG", {"price_cents": 1500})
        self.assertEqual(self.app.catalog.get_product("MUG").price_cents, 1500)

    def test_coupon_reduces_taxable_amount(self):
        order = self.app.orders.create(
            "ana",
            [("MUG", 1)],
            region="CA",
            coupon_code="TEN"
        )

        self.assertEqual(order["subtotal_cents"], 1200)
        self.assertEqual(order["discount_cents"], 120)
        self.assertEqual(order["tax_cents"], 78)
        self.assertEqual(order["total_cents"], 1158)

    def test_second_payment_is_flagged_for_refund(self):
        order = self.app.orders.create("ana", [("MUG", 1)])

        self.app.payments.handle_event({
            "id": "evt_first",
            "type": "payment.succeeded",
            "order_id": order["id"],
            "amount_cents": 1200,
        })

        self.app.payments.handle_event({
            "id": "evt_second",
            "type": "payment.succeeded",
            "order_id": order["id"],
            "amount_cents": 1200,
        })

        payments = self.conn.execute(
            "SELECT amount_cents, refund_required_cents FROM payments WHERE order_id = ? ORDER BY id",
            (order["id"],),
        ).fetchall()

        self.assertEqual(len(payments), 2)
        self.assertEqual(payments[0]["refund_required_cents"], 0)
        self.assertEqual(payments[1]["refund_required_cents"], 1200)
if __name__ == "__main__":
    unittest.main()


