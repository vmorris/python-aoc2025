import logging
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_ids(product_id_ranges):
    ids = list()
    for _range in product_id_ranges:
        start, end = _range.split("-")
        for id in range(int(start), int(end)+1):
            ids.append(str(id))
    return ids

def is_valid_id_p1(product_id):
    half = len(product_id) // 2
    if product_id[:half] == product_id[half:]:  # first half matches second half
        return True
    return False

def solve_part1(entries):
    product_id_ranges = entries[0]
    product_ids = get_ids(product_id_ranges)
    count = 0
    for id in product_ids:
        if is_valid_id_p1(id):
            count += int(id)
    return count

def chunk_string(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def is_valid_id_p2(product_id):
    half = len(product_id) // 2
    for i in range(1, half+1):
        chunks = list(chunk_string(product_id, i))
        if all(s == chunks[0] for s in chunks):
            return True
    return False

def solve_part2(entries):
    product_id_ranges = entries[0]
    product_ids = get_ids(product_id_ranges)
    count = 0
    for id in product_ids:
        if is_valid_id_p2(id):
            count += int(id)
    return count


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day02/input", type="csv")
    print(solve_part1(entries))
    print(solve_part2(entries))