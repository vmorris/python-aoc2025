import logging
from aoc2025.util import get_input
from itertools import combinations
from math import dist
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[rb] = ra
            return True  # circuits merged
        return False  # boxes already in the same circuit


def get_edges(boxes):
    edges = []
    for i, j in combinations(range(len(boxes)), 2):  # collect all pairs of boxes
        distance = dist(boxes[i], boxes[j])
        edges.append((distance, i, j))
    edges.sort()
    return edges


def solve_part1(entries, to_connect):
    boxes = entries
    distances = get_edges(boxes)  # sorted edges between each pair of boxes
    uf = UnionFind()
    connections = 0
    for _, a, b in distances:
        if connections == to_connect:
            break
        uf.union(a, b)
        connections += 1

    sizes = Counter(uf.find(i) for i in range(len(boxes)))
    largest_three = sizes.most_common(3)
    result = 1
    for _, length in largest_three:
        result *= length
    return result


def solve_part2(entries):
    boxes = entries
    distances = get_edges(boxes)  # sorted edges between each pair of boxes
    uf = UnionFind()
    components = len(boxes)
    for _, a, b in distances:
        if uf.union(a, b):  # only reduces components if they were in separate circuits
            components -= 1
        if components == 1:  # we found the final merging connection
            print(boxes[a])
            print(boxes[b])
            return boxes[a][0] * boxes[b][0]  # multiply the X values for each box


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day08/input", type="csv-ints")
    print(solve_part1(entries, 1000))
    print(solve_part2(entries))
