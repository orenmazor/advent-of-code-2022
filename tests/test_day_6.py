from advent_of_code_2022.day6 import find_start


def test_base_example():
    example = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    position = find_start(example)
    assert position == 7


def test_subsequent_examples():
    assert 5 == find_start("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert 6 == find_start("nppdvjthqldpwncqszvftbrmjlhg")
    assert 10 == find_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert 11 == find_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")


def test_day6_part1():
    message = open("tests/inputs/day6.txt").read()

    assert 1855 == find_start(message)


def test_day6_part2_examples():
    assert 23 == find_start("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
    assert 23 == find_start("nppdvjthqldpwncqszvftbrmjlhg", 14)
    assert 29 == find_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
    assert 26 == find_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)


def test_day6_part2():
    message = open("tests/inputs/day6.txt").read()

    assert 3256 == find_start(message, 14)
