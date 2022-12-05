"""Day 4. the one with the section clearing"""
from typing import Tuple


def unpack_section(section: str) -> list:
    """Unpack str section descriptions."""
    parts = section.split("-")
    return list(range(int(parts[0]), int(parts[1]) + 1))


def unpack_section_pair(pair_of_sections: str) -> Tuple[list, list]:
    sections = pair_of_sections.split(",")
    return (unpack_section(sections[0]), unpack_section(sections[1]))


def check_for_section_overlap(pair_of_sections: str) -> bool:
    sections = unpack_section_pair(pair_of_sections)

    if set(sections[0]).issubset(set(sections[1])):
        return True

    if set(sections[1]).issubset(set(sections[0])):
        return True

    return False


def find_all_overlaps(sections: str) -> list:
    overlaps = []
    for section_pairs in sections.split("\n"):
        if section_pairs:
            if check_for_section_overlap(section_pairs):
                overlaps.append(section_pairs)

    return overlaps
