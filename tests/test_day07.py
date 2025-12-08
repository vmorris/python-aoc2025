from aoc2025.day07 import solution
from aoc2025.util import get_input


input_data = get_input("tests/testinput.day07", type="str")


def test_solve_part1():
    expected = 21
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 40
    actual = solution.solve_part2(input_data)
    assert expected == actual
