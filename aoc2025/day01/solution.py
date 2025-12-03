import logging
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class lock:
    def __init__(self, length):
        self.length = length
        self.position = 50
    def rotate_dial(self, rotation):
        # rotates the lock dial left or right given inputs like "L1" or "R33" and returns the number of times the position passes through zero
        rotation_value = int(rotation[1:])
        step_counter = 0
        zero_counter = 0
        while step_counter < rotation_value: # rotate one step at a time
            if rotation[0] == "L":  # negative rotation
                self.position -= 1
                if self.position == 0:
                    zero_counter += 1
                if self.position < 0: # over-rotated
                    self.position = self.length - 1
            elif rotation[0] == "R":  # positive rotation
                self.position += 1
                if self.position == self.length:  # over-rotated
                    self.position = 0
                    zero_counter += 1
            step_counter += 1
        return zero_counter

    def get_position(self):
        return self.position

def solve_part1(entries):
    length = 100
    l = lock(length)
    logger.debug(f" - The dial starts by pointing at {l.get_position()}")
    count = 0
    for rotation in entries:
        l.rotate_dial(rotation)
        logger.debug(f" - The dial is rotated {rotation} to point at {l.get_position()}")
        if l.get_position() == 0:
            count += 1
    return count


def solve_part2(entries):
    length = 100
    l = lock(length)
    logger.debug(f" - The dial starts by pointing at {l.get_position()}")
    count = 0
    for rotation in entries:
        passed_zero = l.rotate_dial(rotation)
        count += passed_zero
        if passed_zero == 0:
            logger.debug(f" - The dial is rotated {rotation} to point at {l.get_position()}")
        else:
            logger.debug(f" - The dial is rotated {rotation} to point at {l.get_position()}; during the rotation the dial passed zero {passed_zero} times.")
    return count


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day01/input")
    print(solve_part1(entries))
    print(solve_part2(entries))