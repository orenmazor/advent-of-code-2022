from advent_of_code_2022.day5 import parse_stacks


def test_parsing_stacks():
    """Confirm we can read the stack structure."""
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    assert ["Z", "N"] == parse_stacks(example)[1]
    assert ["M", "C", "D"] == parse_stacks(example)[2]
    assert ["P"] == parse_stacks(example)[3]
