"""Cover the test cases for day 1."""

from advent_of_code_2022.day1 import (
    elf_with_max_calories,
    total_calories_per_elf,
)


def test_puzzle_1_part_1_test():
    """Test case 1 is the primary test case provided."""
    inventory = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    loaded_elf, calories = elf_with_max_calories(inventory)

    assert loaded_elf == 4
    assert calories == 24000


def test_puzzle_1_part_2_test():
    """Find the top 3 elves from the test case."""
    inventory = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    elves = list(total_calories_per_elf(inventory).items())

    assert elves[0] == (4, 24000)
    assert elves[1] == (3, 11000)
    assert elves[2] == (5, 10000)


def test_puzzle_1_part_1():
    """The actual test case."""
    inventory = open("tests/inputs/day1a.txt").read()
    loaded_elf, calories = elf_with_max_calories(inventory)

    assert loaded_elf == 134
    assert calories == 71924


def test_puzzle_1_main_input_part_b():
    """The actual second part of the puzzle."""
    inventory = open("tests/inputs/day1a.txt").read()
    elves = list(total_calories_per_elf(inventory).items())

    assert elves[0] == (134, 71924)
    assert elves[1] == (153, 69893)
    assert elves[2] == (7, 68589)

    assert elves[0][1] + elves[1][1] + elves[2][1] == 210406
