"""Unit tests for R1, R2, R3 and R7 (Developer A)."""
from catalog import is_valid_selection, round_half_up, subtotal


def test_r1_known_plans_are_valid():
    """R1: every plan in the table is valid."""
    for plan in ("BASIC", "STANDARD", "PREMIUM"):
        assert is_valid_selection(plan, [], 1)


def test_r1_unknown_plan_is_invalid():
    """R1: a plan that is not in the table is invalid."""
    assert not is_valid_selection("GOLD", [], 1)


def test_r2_unknown_extra_is_invalid():
    """R2: an extra that is not in the table is invalid."""
    assert not is_valid_selection("BASIC", ["SAUNA"], 1)


def test_r2_premium_extra_needs_premium_plan():
    """R2: a premium extra is only allowed with the PREMIUM plan."""
    assert not is_valid_selection("BASIC", ["SPA"], 1)
    assert not is_valid_selection("STANDARD", ["SPECIALIZED_PROGRAM"], 1)
    assert is_valid_selection("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 1)


def test_r3_subtotal():
    """R3: (plan price + extras) x members."""
    assert subtotal("BASIC", [], 1) == 30
    assert subtotal("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4) == 340


def test_r3_members_at_least_one():
    """R3: the number of members is at least 1."""
    assert not is_valid_selection("BASIC", [], 0)
    assert not is_valid_selection("BASIC", [], -2)


def test_r7_round_half_up():
    """R7: .5 always rounds up."""
    assert round_half_up(2.5) == 3
    assert round_half_up(411.7) == 412
    assert round_half_up(81.0) == 81
    assert round_half_up(80.4) == 80
