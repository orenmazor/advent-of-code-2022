"""Day 8, the treehouse day."""
from numpy import array, ndindex, prod
from typing import List


def parse_grove(raw_grove: str) -> List[List[int]]:
    raw_grove = raw_grove.strip()

    return array([[int(tree) for tree in list(row)] for row in raw_grove.split("\n")])


def best_scenic_score(grove: array) -> int:
    """Given a grove, return the best scenic score possible."""
    return max(
        [scenic_score_for_tree(grove, x, y) for x, y in ndindex(len(grove), len(grove))]
    )


def count_visible_trees(grove: array) -> int:
    """Accepts a grove and returns the number of visible trees."""
    # we're assuming its a square but check
    assert grove.shape[0] == grove.shape[1]

    return sum(
        [is_tree_visible(grove, x, y) for x, y in ndindex(len(grove), len(grove))]
    )


def is_tree_visible(grove: array, column_index: int, row_index: int) -> bool:
    """Check that tree is visible.

    do this by checking the base case (is it an edge).

    then checking its siblings left to right to see if it's a maximum.

    finally, look at the top/bottom.
    """
    tree_value = grove[row_index][column_index]

    left_neighbours = grove[row_index][0:column_index]
    right_neighbours = grove[row_index][column_index + 1 :]

    def _has_clear_sight_over_neighbours(tree: int, neighbours: List[int]):
        if all(tree > neighbour for neighbour in neighbours):
            return True

    if _has_clear_sight_over_neighbours(tree_value, left_neighbours):
        return True

    if _has_clear_sight_over_neighbours(tree_value, right_neighbours):
        return True

    # now check the vertical
    column = grove[:, column_index]
    top_neighbours = column[0:row_index]
    bottom_neighbours = column[row_index + 1 :]

    if _has_clear_sight_over_neighbours(tree_value, top_neighbours):
        return True

    if _has_clear_sight_over_neighbours(tree_value, bottom_neighbours):
        return True

    return False


def scenic_score_for_tree(grove: array, column_index: int, row_index: int) -> int:
    """Find the score of the given tree."""
    tree = grove[row_index][column_index]

    left_neighbours = grove[row_index][0:column_index]
    right_neighbours = grove[row_index][column_index + 1 :]

    column = grove[:, column_index]
    top_neighbours = column[0:row_index]
    bottom_neighbours = column[row_index + 1 :]

    def _visible_neighbours(tree_value: int, neighbours: List[int]) -> int:
        visible_neighbours = 0
        for neighbour in neighbours:
            # we definitely see it so count it
            visible_neighbours += 1

            # if the tree is a blockage, we are done
            if tree_value <= neighbour:
                break

        return visible_neighbours

    # note we gotta rotate the arrays that will be reviewed backwards
    result = prod(
        [
            _visible_neighbours(tree, left_neighbours[::-1]),
            _visible_neighbours(tree, right_neighbours),
            _visible_neighbours(tree, top_neighbours[::-1]),
            _visible_neighbours(tree, bottom_neighbours),
        ]
    )
    return result
