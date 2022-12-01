"""Cover the test cases for day 1."""

from advent_of_code_2022.day1 import elf_with_max_calories


def test_puzzle_1():
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


def test_puzzle_1_main_input():
    """The actual test case."""
