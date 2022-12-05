from typing import Dict, List
from collections import defaultdict
from itertools import islice


def parse_stacks(stacks_raw: str) -> Dict[str, List[str]]:
    """given a stack structure

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

        we want to return a dictionary in the form of

        1 -> Z, N
        2 -> M, C, D
        3 -> P
    """

    stacks = defaultdict(list)

    for row in stacks_raw.split("\n"):
        for idx, container in enumerate(row):
            if container.isalpha():
                stacks[idx].append(container)

    # because of whitespace, our stack indices
    # are going to be way off
    # so we need to re-normalize them
    # so sort the stacks first by key
    stacks = sorted(stacks.items())
    # then replace all of our keys
    normalized_stacks = {}
    for idx, col in enumerate(stacks, start=1):
        # make sure we reverse our stacks because we built it top down
        # and we want our sorting to be bottom-up
        # because these are stacks
        col[1].reverse()
        normalized_stacks[idx] = col[1]

    return normalized_stacks