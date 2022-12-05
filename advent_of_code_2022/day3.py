"""Solve day 3."""
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


def sum_priorities(rucksacks: str):
    """Iterate over all rucksacks and sum their priority items."""
    sum = 0
    for rucksack in rucksacks.split("\n"):
        if rucksack:
            sum += priority(find_repeated_item(rucksack))

    return sum
