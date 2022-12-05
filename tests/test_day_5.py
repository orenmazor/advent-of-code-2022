"""day 5 tests."""

from advent_of_code_2022.day5 import (
    parse_stacks,
    parse_moves,
    apply_move,
    apply_all_moves,
    get_stack_tops,
)


def test_parsing_stacks():
    """Confirm we can read the stack structure."""
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    assert ["Z", "N"] == parse_stacks(example)[1]
    assert ["M", "C", "D"] == parse_stacks(example)[2]
    assert ["P"] == parse_stacks(example)[3]


def test_parsing_moves():
    """Confirm we can read the movements."""
    example = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    assert (1, 2, 1) == parse_moves(example)[0]
    assert (3, 1, 3) == parse_moves(example)[1]


def test_applying_move():
    """Confirm we can apply a move to a stack."""
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    stack = parse_stacks(example)

    stack = apply_move(stack, (1, 2, 1))
    assert ["Z", "N", "D"] == stack[1]


def test_day5_example():
    """Confirm we can find the top crates."""
    example_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    result = apply_all_moves(example_input)

    assert "CMZ" == get_stack_tops(result)


def test_day5_main():
    """The actual part 1."""
    example_input = open("tests/inputs/day5.txt").read()
    result = apply_all_moves(example_input)

    assert "TLFGBZHCN" == get_stack_tops(result)


def test_day5_main_with_createmover_9001():
    """The actual part 1."""
    example_input = open("tests/inputs/day5.txt").read()
    result = apply_all_moves(example_input, crate_mover_version=9001)

    assert "QRQFHFWCL" == get_stack_tops(result)
