"""Day 3 tests."""
from advent_of_code_2022.day3 import (
    priority,
    pockets,
    find_repeated_item,
    sum_priorities,
)

from advent_of_code_2022.day3part2 import sum_badges


def test_day_3_pockets():
    assert ("foo", "bar") == pockets("foobar")
    assert ("vJrwpWtwJgWr", "hcsFMMfFFhFp") == pockets("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL") == pockets(
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    )


def test_day_3_repeat_letter():
    assert "p" == find_repeated_item("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert "L" == find_repeated_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")


def test_day_3_priority_conversion():
    assert 1 == priority("a")
    assert 26 == priority("z")
    assert 27 == priority("A")
    assert 52 == priority("Z")


def test_day_3_example():
    example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert 157 == sum_priorities(example)


def test_day_3_real_thing():
    example = open("tests/inputs/day3.txt").read()
    assert 7889 == sum_priorities(example)


def test_day_3_example_grouping():
    example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert 70 == sum_badges(example)


def test_day_3_real_thing_grouping():

    example = open("tests/inputs/day3.txt").read()
    assert 157 == sum_badges(example)
