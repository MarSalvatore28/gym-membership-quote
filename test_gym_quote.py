"""Tests for the Gym Membership Quote."""
from gym_quote import INVALID, GymQuote


def test_unknown_plan_is_invalid():
    """R1: a plan that is not in the table is invalid."""
    assert GymQuote("GOLD", [], 1).total() == INVALID
