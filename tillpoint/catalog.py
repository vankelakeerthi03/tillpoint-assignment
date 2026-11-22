"""Product catalog with a per-process read cache."""
from dataclasses import dataclass


class OutOfStock(Exception):
    def __init__(self, sku, wanted, available):
        super().__init__(f"{sku}: wanted {wanted}, {available} available")
        self.sku, self.wanted, self.available = sku, wanted, available


class UnknownProduct(Exception):
    pass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price_cents: int
    stock: int


class Catalog:
    def __init__(self, conn):
        self.conn = conn
        self._cache = {}

    def add_product(self, sku, name, price_cents, stock=0):
        self.conn.execute(
            "INSERT INTO products (sku, name, price_cents, stock) VALUES (?, ?, ?, ?)",
            (sku, name, price_cents, stock),
        )
        self._cache.pop(sku, None)

    def get_product(self, sku):
        product = self._cache.get(sku)
        if product is None:
            row = self.conn.execute("SELECT * FROM products WHERE sku = ?", (sku,)).fetchone()
            if row is None:
                raise UnknownProduct(sku)
            product = Product(row["sku"], row["name"], row["price_cents"], row["stock"])
            self._cache[sku] = product
        return product

    def update_price(self, sku, price_cents):
        if price_cents < 0:
            raise ValueError("price must not be negative")
        cur = self.conn.execute("UPDATE products SET price_cents = ? WHERE sku = ?", (price_cents, sku))
        if cur.rowcount == 0:
            raise UnknownProduct(sku)
        self._cache.pop(sku, None)

    def reserve(self, sku, qty):
        """Take qty units out of stock, or raise OutOfStock."""
        cur = self.conn.execute(
            "UPDATE products SET stock = stock - ? WHERE sku = ? AND stock >= ?",
            (qty, sku, qty),
        )
        self._cache.pop(sku, None)

        if cur.rowcount == 0:
            row = self.conn.execute(
                "SELECT stock FROM products WHERE sku = ?", (sku,)
            ).fetchone()

            if row is None:
                raise UnknownProduct(sku)

            raise OutOfStock(sku, qty, row["stock"])
    def release(self, sku, qty):
        """Put qty units back into stock."""
        self.conn.execute("UPDATE products SET stock = stock + ? WHERE sku = ?", (qty, sku))
        self._cache.pop(sku, None)
