"""Solve day 3."""
from itertools import islice

from typing import Tuple


def pockets(rucksack_contents: str) -> Tuple[str, str]:
    length_of_string = len(rucksack_contents)
    midpoint = int(length_of_string / 2)
    return (rucksack_contents[0:midpoint], rucksack_contents[midpoint:])


def find_repeated_item(rucksack_contents: str) -> str:
    first, second = pockets(rucksack_contents)

    first = set(list(first))
    second = set(list(second))

    intersect = first.intersection(second)
    intersect = list(intersect)
    assert len(intersect) == 1

    return intersect[0]


def priority(item: str) -> int:
    """Return the priority of the item."""
    priority = ord(item)

    # handle upper cases
    if priority < 97:
        return priority - 38

    # handle lower cases
    else:
        return priority - 96


def sum_badges(rucksacks: str) -> int:
    """Iterate over all rucksacks and sum their priority items."""
    accum = 0

    iterator = iter(rucksacks.split("\n"))
    while group := list(islice(iterator, 3)):
        if len(group) != 3:
            continue
        intersection_item = set(group[0]) & set(group[1]) & set(group[2])
        intersection_item = list(intersection_item)

        assert len(intersection_item) == 1

        intersection_item = intersection_item[0]

        accum += priority(intersection_item)

    return accum
