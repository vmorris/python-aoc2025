from aoc2025.day02 import solution
from aoc2025.util import get_input


input_data = get_input("tests/testinput.day02", type="csv")


def test_solve_part1():
    expected = 1227775554
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 4174379265
    actual = solution.solve_part2(input_data)
    assert expected == actual