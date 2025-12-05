from aoc2025.day05 import solution
from aoc2025.util import get_input


input_data = get_input("tests/testinput.day05", type="group_nlnl")


def test_solve_part1():
    expected = 3
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 14
    actual = solution.solve_part2(input_data)
    assert expected == actual
