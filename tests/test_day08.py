from aoc2025.day08 import solution
from aoc2025.util import get_input


input_data = get_input("tests/testinput.day08", type="csv-ints")


def test_solve_part1():
    expected = 40
    actual = solution.solve_part1(input_data, 10)
    assert expected == actual


def test_solve_part2():
    expected = 25272
    actual = solution.solve_part2(input_data)
    assert expected == actual
