import logging
from typing import List
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def build_adjacent_positions(self) -> List[Position]:
        result = list()
        result.append(Position(self.x - 1, self.y - 1))
        result.append(Position(self.x, self.y - 1))
        result.append(Position(self.x + 1, self.y - 1))
        result.append(Position(self.x - 1, self.y))
        result.append(Position(self.x + 1, self.y))
        result.append(Position(self.x - 1, self.y + 1))
        result.append(Position(self.x, self.y + 1))
        result.append(Position(self.x + 1, self.y + 1))
        return result

    def __str__(self):
        return f"Position({self.x},{self.y})"


class FloorLayout:
    def __init__(self, entries):
        self.layout = list()
        for entry in entries:
            self.layout.append(list(entry))
        self.min_x = 0
        self.min_y = 0
        self.max_x = len(entries[0])
        self.max_y = len(entries)

    def __str__(self):
        result = ""
        for row in self.layout:
            result += f"{row}\n"
        return result

    def get_position(self, position: Position):
        return self.layout[position.y][position.x]

    def position_is_roll(self, position: Position):
        if self.get_position(position) != "@":
            return False
        return True

    def count_adjacent_rolls(self, position: Position):
        if not self.position_is_roll(position):
            raise ValueError
        result = 0
        adjacent_positions = position.build_adjacent_positions()
        for pos in adjacent_positions:
            # logger.info(f" - checking adjacent position {pos}")
            if (
                pos.x < self.min_x
                or pos.x >= self.max_x
                or pos.y < self.min_y
                or pos.y >= self.max_y
            ):
                # logger.info(" - skipping")
                continue
            if self.position_is_roll(pos):
                # logger.info(" - ROLL LOCATED!")
                result += 1
        return result

    def remove_roll(self, position: Position):
        self.layout[position.y][position.x] = "."


def solve_part1(entries):
    layout = FloorLayout(entries)
    max_x = len(entries[0])
    max_y = len(entries)
    result = 0
    for y in range(max_y):
        for x in range(max_x):
            p = Position(x, y)
            # logger.info(f"Checking position {p}")
            try:
                if layout.count_adjacent_rolls(p) < 4:
                    result += 1
            except ValueError:
                pass
    return result


def solve_part2(entries):
    layout = FloorLayout(entries)
    max_x = len(entries[0])
    max_y = len(entries)
    result = 0
    rolls_removed = True
    while rolls_removed:
        to_remove = list()
        for y in range(max_y):
            for x in range(max_x):
                p = Position(x, y)
                # logger.info(f"Checking position {p}")
                try:
                    if layout.count_adjacent_rolls(p) < 4:
                        result += 1
                        to_remove.append(p)
                except ValueError:
                    pass
        if to_remove:
            for p in to_remove:
                layout.remove_roll(p)
        else:
            rolls_removed = False
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day04/input", type="char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
