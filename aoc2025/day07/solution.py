import copy
from pprint import pprint
import logging
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TachyonManifold:
    def __init__(self, data):
        self.manifold = copy.deepcopy(data)
        self.row_index = 1
        self._start_beam()

    def get_start_index(self):
        return self.manifold[0].index("S")

    def _start_beam(self):
        index = self.get_start_index()
        _row = list(self.manifold[self.row_index])
        _row[index] = 0
        self.manifold[self.row_index] = _row

    def step_beam(self):
        split_count = 0
        timeline_count = 0
        # split
        prev_row = list(self.manifold[self.row_index])
        self.row_index += 1
        _row = list(self.manifold[self.row_index])
        # logger.info(f"1. row_index: {self.row_index}, row: {_row}")
        for i, element in enumerate(_row):
            if element == "^" and type(prev_row[i]) == int:
                if type(_row[i - 1]) == int:
                    # logger.info(
                    # f"  Found int on left side of split. index: {i-1}, element: {_row[i-1]}"
                    # )
                    _row[i - 1] += prev_row[i]
                    # logger.info(f"2. row_index: {self.row_index}, row: {_row}")
                else:
                    _row[i - 1] = prev_row[i] + 1
                    # logger.info(f"3. row_index: {self.row_index}, row: {_row}")
                _row[i + 1] = prev_row[i] + 1
                # logger.info(f"4. row_index: {self.row_index}, row: {_row}")
                split_count += 1
            if element == "." and type(prev_row[i]) == int:
                _row[i] = prev_row[i]
                # logger.info(f"5. row_index: {self.row_index}, row: {_row}")
        self.manifold[self.row_index] = _row
        # time
        prev_row = list(self.manifold[self.row_index])
        self.row_index += 1
        _row = list(self.manifold[self.row_index])
        # logger.info(f"A. row_index: {self.row_index}, row: {_row}")
        for i, element in enumerate(_row):
            if type(prev_row[i]) == int:
                _row[i] = prev_row[i]
                # logger.info(f"B. row_index: {self.row_index}, row: {_row}")
        self.manifold[self.row_index] = _row

        return split_count, timeline_count

    def __str__(self):
        result = "\n"
        for row in self.manifold:
            result += "".join([str(i) for i in row])
            result += "\n"
        return result


def solve_part1(entries):
    manifold = TachyonManifold(entries)
    result = 0
    try:
        while True:
            split, _ = manifold.step_beam()
            result += split
    except IndexError:
        pass
    # logger.info(manifold)
    return result


def solve_part2(entries):
    manifold2 = TachyonManifold(entries)
    result = 0
    for row_index, row in enumerate(manifold2.manifold):
        _row = copy.copy(row)
        manifold2.manifold[row_index] = _row

    try:
        while True:
            _, timeline = manifold2.step_beam()
            result += timeline
    except IndexError:
        pass
    # pprint(manifold.manifold)
    # 3125 too low - test passes
    # 4554 too low - test fails now (too high), 4555 is too low too
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day07/input", type="str")
    print(solve_part1(entries))
    print(solve_part2(entries))
