"""Day 2 puzzle."""
from advent_of_code_2022.day2part2 import (
    apply_strategy_guide,
    normalize_hand,
    find_needed_hand,
)


def test_hand_normalizing() -> None:
    """Make sure we can process all the hands."""
    assert normalize_hand("A Y") == ("Rock", "Draw")
    assert normalize_hand("B X") == ("Paper", "Lose")
    assert normalize_hand("C Z") == ("Scissors", "Win")


def test_hand_finding() -> None:
    """Check we can find the right hand to satisfy the condition."""
    assert find_needed_hand(normalize_hand("A Y")) == "Rock"
    assert find_needed_hand(normalize_hand("B X")) == "Rock"
    assert find_needed_hand(normalize_hand("C Z")) == "Rock"


def test_day2_part1() -> None:
    """Check day 2 sample input."""
    guide = """A Y
B X
C Z"""
    score = apply_strategy_guide(guide)
    assert 12 == score


def test_day2_part1_actual() -> None:
    """Check day 2 part 1."""
    score = apply_strategy_guide(open("tests/inputs/day2a.txt").read())
    assert 11998 == score
