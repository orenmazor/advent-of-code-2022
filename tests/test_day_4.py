from advent_of_code_2022.day4 import (
    unpack_section,
    find_all_overlaps,
    unpack_section_pair,
    check_for_section_overlap,
)


def test_unpacking_sections():
    assert [1, 2, 3] == unpack_section("1-3")


def test_unpacking_section_pairs():
    assert ([1, 2, 3], [4, 5, 6]) == unpack_section_pair("1-3,4-6")


def test_section_overlap():
    assert True == check_for_section_overlap("1-3,2-3")
    assert False == check_for_section_overlap("1-3,2-4")


def test_day4_part_1():
    overlaps = find_all_overlaps(open("tests/inputs/day4.txt").read())
    assert 459 == len(overlaps)
