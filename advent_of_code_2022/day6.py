from typing import Tuple


def marker_test(substring: str) -> bool:
    """Currently a marker test is whether the substring
    has nonrepeating characters.
    """
    return len(set(substring)) == len(substring)


def find_start(buffer: str, marker_length: int = 4) -> int:
    """Receive a buffer of arbitrary size and return possible marker position."""

    for idx in range(marker_length, len(buffer)):
        potential_marker = buffer[idx - marker_length : idx]
        if marker_test(potential_marker):
            return idx

    raise Exception("no marker found. is this....possible?")
