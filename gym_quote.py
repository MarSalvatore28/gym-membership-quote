"""Gym Membership Quote: monthly cost of a gym membership."""
from adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)
from catalog import PREMIUM_EXTRAS, is_valid_selection, round_half_up, subtotal

INVALID = -1


class GymQuote:
    """Quote for one gym membership selection. It does no input or output."""

    def __init__(self, plan, extras, members):
        self.plan = plan
        self.extras = list(extras)
        self.members = members

    def breakdown(self):
        """Return each step of the calculation, or None if the selection is invalid."""
        if not is_valid_selection(self.plan, self.extras, self.members):
            return None
        amount = subtotal(self.plan, self.extras, self.members)
        after_group = apply_group_discount(amount, self.members)
        after_offer = apply_special_offer(after_group)
        has_premium = any(extra in PREMIUM_EXTRAS for extra in self.extras)
        after_surcharge = apply_premium_surcharge(after_offer, has_premium)
        return {
            "subtotal": amount,
            "group_discount": amount - after_group,
            "special_offer": after_group - after_offer,
            "premium_surcharge": after_surcharge - after_offer,
            "total": round_half_up(after_surcharge),
        }

    def total(self):
        """R7: return the rounded total, or -1 if the selection is invalid."""
        steps = self.breakdown()
        if steps is None:
            return INVALID
        return steps["total"]
