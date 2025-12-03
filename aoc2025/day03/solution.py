import copy
import logging
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Bank:
    def __init__(self, batteries):
        self.batteries = self._initialize_bank(batteries)

    def _initialize_bank(self, batteries):
        return list(map(int, list(batteries)))

    def get_largest_batteries_part1(self):
        first_digit = max(self.batteries[:-1])
        index = self.batteries.index(first_digit)
        last_digit = max(self.batteries[index + 1 :])
        return first_digit * 10 + last_digit

    def get_largest_batteries_part2(self):
        _batteries = copy.copy(self.batteries)
        result = list()
        length = 11
        while length >= 0:
            if length == 0:
                digit = max(_batteries)
            else:
                digit = max(_batteries[:-length])
            length -= 1
            result.append(digit)
            index = _batteries.index(digit)
            _batteries = _batteries[index + 1 :]
        return int("".join(map(str, result)))


def solve_part1(entries):
    banks = list()
    total = 0
    for entry in entries:
        banks.append(Bank(entry))
    for bank in banks:
        total += bank.get_largest_batteries_part1()
    return total


def solve_part2(entries):
    banks = list()
    total = 0
    for entry in entries:
        banks.append(Bank(entry))
    for bank in banks:
        result = bank.get_largest_batteries_part2()
        total += result
    return total


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day03/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
