"""Catalog of plans and extras, validation, subtotal and rounding (R1, R2, R3, R7)."""
from decimal import ROUND_HALF_UP, Decimal

PLANS = {"BASIC": 30, "STANDARD": 45, "PREMIUM": 70}
EXTRAS = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}
PREMIUM_EXTRAS = {"SPA", "SPECIALIZED_PROGRAM"}


def is_valid_selection(plan, extras, members):
    """R1, R2, R3: return True if the plan, extras and members can be quoted."""
    if plan not in PLANS:
        return False
    if isinstance(members, bool) or not isinstance(members, int) or members < 1:
        return False
    if len(set(extras)) != len(extras):
        return False
    for extra in extras:
        if extra not in EXTRAS:
            return False
        if extra in PREMIUM_EXTRAS and plan != "PREMIUM":
            return False
    return True


def subtotal(plan, extras, members):
    """R3: (plan price + price of the extras) x number of members."""
    return (PLANS[plan] + sum(EXTRAS[extra] for extra in extras)) * members


def round_half_up(amount):
    """R7: round half up to a whole number (2.5 -> 3, while round() gives 2)."""
    exact = Decimal(str(round(amount, 6)))
    return int(exact.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
