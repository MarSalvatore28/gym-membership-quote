"""Unit tests for R4, R5 and R6 (Developer B)."""
import pytest

from adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


def test_r4_no_discount_for_one_member():
    """R4: one member pays the full amount."""
    assert apply_group_discount(100, 1) == 100


def test_r4_ten_percent_for_two_or_more():
    """R4: 2 or more members get 10% off."""
    assert apply_group_discount(100, 2) == pytest.approx(90)
    assert apply_group_discount(340, 4) == pytest.approx(306)


def test_r5_over_400_subtracts_50():
    """R5: more than 400 subtracts 50."""
    assert apply_special_offer(594) == 544


def test_r5_over_200_subtracts_20():
    """R5: more than 200 and up to 400 subtracts 20."""
    assert apply_special_offer(306) == 286
    assert apply_special_offer(400) == 380


def test_r5_200_or_less_has_no_offer():
    """R5: 200 or less keeps the amount; the two offers never add up."""
    assert apply_special_offer(200) == 200
    assert apply_special_offer(81) == 81


def test_r6_premium_surcharge():
    """R6: a premium extra adds 15%."""
    assert apply_premium_surcharge(100, True) == pytest.approx(115)
    assert apply_premium_surcharge(100, False) == 100
