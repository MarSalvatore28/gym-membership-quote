"""Gym Membership Quote: monthly cost of a gym membership."""

INVALID = -1


class GymQuote:
    """Quote for one gym membership selection."""

    def __init__(self, plan, extras, members):
        self.plan = plan
        self.extras = list(extras)
        self.members = members

    def total(self):
        """Return the total of the quote, or -1 if the selection is invalid."""
        return INVALID
