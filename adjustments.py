"""Discounts and surcharge applied to an amount (R4, R5, R6)."""

GROUP_DISCOUNT_RATE = 0.10
PREMIUM_SURCHARGE_RATE = 0.15


def apply_group_discount(amount, members):
    """R4: with 2 or more members the amount gets a 10% discount."""
    if members >= 2:
        return amount * (1 - GROUP_DISCOUNT_RATE)
    return amount


def apply_special_offer(amount):
    """R5: subtract 50 if the amount is over 400, otherwise 20 if it is over 200."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


def apply_premium_surcharge(amount, has_premium):
    """R6: add 15% if the selection includes a premium extra."""
    if has_premium:
        return amount * (1 + PREMIUM_SURCHARGE_RATE)
    return amount
