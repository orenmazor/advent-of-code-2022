"""Day 7 tests, the filesystem tree stuff."""
from advent_of_code_2022.day7 import parse_shell


def test_tree_parser():
    """Read a tree in and return a dictionary."""
    shell = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    dirs = parse_shell(shell)

    small_dirs = {k: v for k, v in dirs.items() if v <= 100000}
    assert 95437 == sum(small_dirs.values())


def test_tree_parser_full_sample():
    """Read a tree in and return a dictionary."""
    shell = open("tests/inputs/day7.txt").read()

    dirs = parse_shell(shell)

    small_dirs = {k: v for k, v in dirs.items() if v <= 100000}
    assert 1886043 == sum(small_dirs.values())
