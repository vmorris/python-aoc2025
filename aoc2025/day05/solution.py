import logging
from intervaltree import IntervalTree, Interval
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_fresh_ranges(ranges):
    result = list()
    for r in ranges:
        min, max = map(int, r.split("-"))
        result.append(range(min, max + 1))
    return result


def solve_part1(entries):
    ingredient_id_ranges = entries[0]
    available_ingredients = map(int, entries[1])
    fresh_ids = generate_fresh_ranges(ingredient_id_ranges)
    result = 0
    for id in available_ingredients:
        # logger.info(f"Testing id {id}")
        for ids in fresh_ids:
            # logger.info(f"Checking range {ids}")
            if id in ids:
                # logger.info("FRESH!")
                result += 1
                break
    return result


def solve_part2(entries):
    ingredient_id_ranges = entries[0]
    fresh_ids = generate_fresh_ranges(ingredient_id_ranges)
    tree = IntervalTree()
    for id_range in fresh_ids:
        tree.add(Interval(id_range.start, id_range.stop))
    tree.merge_overlaps()
    result = 0
    for interval in tree:
        result += interval.end - interval.begin
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day05/input", type="group_nlnl")
    print(solve_part1(entries))
    print(solve_part2(entries))
