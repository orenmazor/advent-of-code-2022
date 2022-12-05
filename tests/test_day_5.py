from advent_of_code_2022.day5 import parse_stacks, parse_moves


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
