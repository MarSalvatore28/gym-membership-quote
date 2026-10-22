"""Unit tests for R8, the command line."""
from cli import parse_extras, run


def fake_input(*answers):
    """Return a function that gives the answers one by one, like input()."""
    queue = list(answers)
    return lambda _prompt: queue.pop(0)


def test_r8_parse_extras():
    """R8: extras are typed separated by commas."""
    assert parse_extras(" spa, group_classes ") == ["SPA", "GROUP_CLASSES"]
    assert not parse_extras("")


def test_r8_confirm_yes_returns_total():
    """R8: answering y returns the total and shows each step."""
    shown = []
    assert run(fake_input("basic", "group_classes", "2", "y"), shown.append) == 81
    assert any("Group discount" in line for line in shown)


def test_r8_confirm_no_returns_minus_one():
    """R8: answering n cancels the quote."""
    assert run(fake_input("basic", "", "1", "n"), lambda _line: None) == -1


def test_r8_invalid_members_returns_minus_one():
    """R8: a number of members that is not a number is invalid."""
    assert run(fake_input("basic", "", "two"), lambda _line: None) == -1