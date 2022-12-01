from collections import defaultdict
from typing import Dict, List, Tuple


def parse_elf_inventory(inventory: str) -> Dict[str, List[int]]:
    """Accept a raw input and returns it broken down by elf."""
    elf_inventory = defaultdict(list)

    current_elf = 1
    for row in inventory.split("\n"):
        if row:
            elf_inventory[current_elf].append(int(row))
        else:
            current_elf += 1

    return elf_inventory


def total_calories_per_elf(inventory: str) -> Dict[str, int]:
    """Accept a raw input and convert it to per-elf."""
    elf_inventory = parse_elf_inventory(inventory)

    elves = {elf_id: sum(inventory) for elf_id, inventory in elf_inventory.items()}

    # sort the dictionary keys
    sorted_elves = reversed(sorted(elves.items(), key=lambda elf: elf[1]))

    return dict(sorted_elves)


def elf_with_max_calories(inventory: str) -> Tuple[str, int]:
    """Find the elf with the most calories."""
    elf_inventory = total_calories_per_elf(inventory)
    loaded_elf = max(elf_inventory, key=elf_inventory.get)

    return (loaded_elf, elf_inventory[loaded_elf])
