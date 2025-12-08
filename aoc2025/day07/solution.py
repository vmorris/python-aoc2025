import copy
import logging
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TachyonManifold:
    def __init__(self, data):
        self.manifold = data
        self.row_index = 1
        self._start_beam()

    def get_start_index(self):
        return self.manifold[0].index("S")

    def _start_beam(self):
        index = self.get_start_index()
        _row = list(self.manifold[self.row_index])
        _row[index] = "|"
        self.manifold[self.row_index] = _row

    def step_beam(self):
        split_count = 0
        timeline_count = 0
        # split
        prev_row = list(self.manifold[self.row_index])
        self.row_index += 1
        _row = list(self.manifold[self.row_index])
        for i, element in enumerate(_row):
            if element == "^" and prev_row[i] == "|":
                _row[i - 1] = "|"
                _row[i + 1] = "|"
                split_count += 1
            if element == "." and prev_row[i] == "|":
                _row[i] = "|"
        self.manifold[self.row_index] = _row
        # time
        prev_row = list(self.manifold[self.row_index])
        self.row_index += 1
        _row = list(self.manifold[self.row_index])
        for i, element in enumerate(_row):
            if prev_row[i] == "|":
                _row[i] = "|"
        self.manifold[self.row_index] = _row

        return split_count, timeline_count

    def __str__(self):
        result = "\n"
        for row in self.manifold:
            result += "".join(row)
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
    manifold = TachyonManifold(entries)
    result = 0
    try:
        while True:
            _, timeline = manifold.step_beam()
            result += timeline
    except IndexError:
        pass
    logger.info(manifold)
    # 3125 too low - test passes
    # 4554 too low - test fails now (too high), 4555 is too low too
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day07/input", type="str")
    print(solve_part1(entries))
    print(solve_part2(entries))
