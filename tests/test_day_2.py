"""Day 2 puzzle."""
from advent_of_code_2022.day2 import apply_strategy_guide, normalize_hand, find_winner


def test_hand_normalizing() -> None:
    """Make sure we can process all the hands."""

    assert normalize_hand("A Y") == ("Rock", "Paper")
    assert normalize_hand("B X") == ("Paper", "Rock")
    assert normalize_hand("C Z") == ("Scissors", "Scissors")


def test_victory_evaluation() -> None:
    """Check victory conditions."""
    assert find_winner(normalize_hand("A Y")) == "Paper"
    assert find_winner(normalize_hand("B X")) == "Paper"
    assert find_winner(normalize_hand("C X")) == "Rock"
    assert find_winner(normalize_hand("A B")) == "Paper"


def test_day2_part1() -> None:
    """Check day 2 sample input."""
    guide = """A Y
B X
C Z"""
    score = apply_strategy_guide(guide)
    assert 15 == score


def test_day2_part1_actual() -> None:
    """Check day 2 part 1."""
    score = apply_strategy_guide(open("tests/inputs/day2a.txt").read())
    assert 8933 == score
