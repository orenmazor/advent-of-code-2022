from advent_of_code_2022.day8 import (
    parse_grove,
    count_visible_trees,
    best_scenic_score,
    scenic_score_for_tree,
)


def test_tree_grove_parsing():
    grove = parse_grove("123\n456\n789")

    assert (3, 3) == grove.shape
    assert grove.tolist() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_counting_visible_trees_part1():
    grove = """30373
25512
65332
33549
35390"""

    grove = parse_grove(grove)

    assert 21 == count_visible_trees(grove)


def test_counting_visible_trees_from_input():
    grove = open("tests/inputs/day8.txt").read()
    grove = parse_grove(grove)

    assert 1814 == count_visible_trees(grove)


def test_finding_base_scenic_score():
    grove = """30373
25512
65332
33549
35390"""
    grove = parse_grove(grove)

    assert 8 == best_scenic_score(grove)


def test_finding_base_scenic_score_at_position():
    grove = """30373
25512
65332
33549
35390"""
    grove = parse_grove(grove)

    assert 4 == scenic_score_for_tree(grove, 2, 1)
    assert 8 == scenic_score_for_tree(grove, 2, 3)


def test_finding_scenic_score():

    grove = open("tests/inputs/day8.txt").read()
    grove = parse_grove(grove)

    assert 330786 == best_scenic_score(grove)
