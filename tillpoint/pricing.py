"""Order maths: subtotal, coupon discount, tax, total. Integer cents throughout."""

# Sales tax in basis points (1/100 of a percent) by region.
TAX_BPS = {"NONE": 0, "CA": 725, "NY": 888, "TX": 625, "DE": 1900}


class CouponRejected(Exception):
    pass


def subtotal(lines):
    """lines: iterable of (unit_price_cents, qty)."""
    return sum(price * qty for price, qty in lines)


def discount_for(coupon, subtotal_cents):
    """Discount in cents for a coupon row (or None) against a subtotal. Never more than the subtotal."""
    if coupon is None:
        return 0
    if subtotal_cents < coupon["min_subtotal_cents"]:
        raise CouponRejected(f"{coupon['code']} needs a subtotal of at least {coupon['min_subtotal_cents']}")
    if coupon["max_uses"] is not None and coupon["uses"] >= coupon["max_uses"]:
        raise CouponRejected(f"{coupon['code']} has been used up")
    if coupon["kind"] == "percent":
        amount = round_half_up(subtotal_cents * coupon["value"], 100)
    else:
        amount = coupon["value"]
    return min(amount, subtotal_cents)


def tax_for(taxable_cents, region):
    if region not in TAX_BPS:
        raise ValueError(f"unknown region {region!r}")
    return round_half_up(taxable_cents * TAX_BPS[region], 10_000)


def round_half_up(numerator, denominator):
    return (2 * numerator + denominator) // (2 * denominator)


def price_order(lines, region, coupon=None):
    """Return dict(subtotal_cents, discount_cents, tax_cents, total_cents)."""
    sub = subtotal(lines)
    discount = discount_for(coupon, sub)
    taxable_amount = sub - discount
    tax = tax_for(taxable_amount, region)

    return {
        "subtotal_cents": sub,
        "discount_cents": discount,
        "tax_cents": tax,
        "total_cents": taxable_amount + tax,
    }