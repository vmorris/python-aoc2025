from aoc2025.day06 import solution
from aoc2025.util import get_input


input_data = get_input("tests/testinput.day06", type="split")


def test_solve_part1():
    expected = 4277556
    actual = solution.solve_part1(input_data)
    assert expected == actual


input_data2 = get_input("tests/testinput.day06", type="raw")


def test_solve_part2():
    expected = 3263827
    actual = solution.solve_part2(input_data2)
    assert expected == actual
