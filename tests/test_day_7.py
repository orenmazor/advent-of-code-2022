"""Day 7 tests, the filesystem tree stuff."""
from advent_of_code_2022.day7 import parse_shell, find_closest


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

    total_fs = 70000000
    free = total_fs - dirs["['/']"]

    assert free == 21618835

    assert ("['/', 'd']", 24933642) == find_closest(dirs, 30000000 - free)


def test_tree_parser_full_sample():
    """Read a tree in and return a dictionary."""
    shell = open("tests/inputs/day7.txt").read()

    dirs = parse_shell(shell)

    small_dirs = {k: v for k, v in dirs.items() if v <= 100000}
    assert 1886043 == sum(small_dirs.values())

    total_fs = 70000000

    free = total_fs - dirs["['/']"]

    assert free == 26437126

    assert ("['/', 'trtl', 'jlfrcp', 'tsstr']", 3842121) == find_closest(
        dirs, 30000000 - free
    )
