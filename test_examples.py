"""Integration tests: the worked examples table of the workshop (R9)."""
import pytest

from gym_quote import GymQuote

EXAMPLES = [
    ("BASIC", [], 1, 31),
    ("STANDARD", ["PERSONAL_TRAINING"], 1, 70),
    ("BASIC", ["GROUP_CLASSES"], 2, 81),
    ("BASIC", ["GROUP_CLASSES"], 3, 122),
    ("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286),
    ("PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"], 4, 626),
    ("BASIC", ["SPA"], 1, -1),
    ("GOLD", [], 1, -1),
    ("BASIC", [], 0, -1),
]


@pytest.mark.parametrize("plan, extras, members, expected", EXAMPLES)
def test_worked_example(plan, extras, members, expected):
    """R9: every row of the table gives the expected result."""
    assert GymQuote(plan, extras, members).total() == expected
