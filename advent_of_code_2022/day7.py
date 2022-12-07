"""Day 7: the one with the fs."""
from collections import defaultdict
from typing import Dict


def find_closest(dirs: Dict[str, int], target: int):
    """fuck it. ship it."""
    sorted_dirs = sorted(dirs.items(), key=lambda x: x[1])

    for directory, size in sorted_dirs:
        if size >= target:
            return (directory, size)


def parse_shell(steps: str):
    """Receivers a series of steps and returns a filesystem list."""

    current_dir = []
    dirs = defaultdict(int)
    for item in steps.split("\n"):
        if not item:
            continue
        if item.startswith("$"):
            # a command
            if "$ ls" == item:
                # these are leaves
                pass

            elif "$ cd .." == item:
                current_dir.pop()

            elif item.startswith("$ cd "):
                dir_name = item.replace("$ cd ", "")
                current_dir.append(dir_name)

        else:
            size = item.split(" ")[0]
            if size == "dir":
                continue

            for depth in range(len(current_dir)):
                subset = current_dir[0 : depth + 1]
                dirs[str(subset)] += int(size)

    return dirs
