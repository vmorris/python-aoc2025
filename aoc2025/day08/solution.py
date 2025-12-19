import logging
from aoc2025.util import get_input
from collections import defaultdict
from operator import methodcaller
from math import dist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JunctionBox:
    def __init__(self, coords, name):
        self.location = coords[0], coords[1], coords[2]
        self.name = name
        self.connections = list()

    def distance(self, other: JunctionBox):
        return dist(self.location, other.location)

    def connect(self, other: JunctionBox):
        logger.debug(f"Connecting {self} to {other}")
        self.connections.append(other)
        other.connections.append(self)

    def is_connected(self, other: JunctionBox):
        if other in self.connections and self in other.connections:
            return True
        if other in self.connections and not self in other.connections:
            raise RuntimeError("Missing connection.")
        if self in other.connections and not other in self.connections:
            raise RuntimeError("Missing connection.")
        return False

    def __hash__(self) -> int:
        return hash(self.location)

    def __repr__(self):
        return f"{self.location}"


class CircuitTracker:
    """
    Tracks which junction boxes are electrically connected.
    Each connected group is a 'circuit'.
    """

    def __init__(self):
        self._parent = {}

    def circuit_of(self, box):
        """Return the representative circuit for a box."""
        if box not in self._parent:
            self._parent[box] = box
        if self._parent[box] != box:
            self._parent[box] = self.circuit_of(self._parent[box])
        return self._parent[box]

    def connect(self, box_a, box_b):
        """
        Connect two boxes.
        Returns True if this created a new connection,
        False if they were already in the same circuit.
        """
        root_a = self.circuit_of(box_a)
        root_b = self.circuit_of(box_b)

        if root_a == root_b:
            return False

        self._parent[root_b] = root_a
        return True

    def circuits(self):
        """Return all circuits as {root: set(boxes)}."""
        groups = defaultdict(set)
        for box in self._parent:
            groups[self.circuit_of(box)].add(box)
        return groups

    def circuit_sizes(self):
        """Return a list of circuit sizes."""
        return sorted((len(group) for group in self.circuits().values()), reverse=True)


def find_closest_boxes(distance_matrix):
    minimum = 99999
    box_a = None
    box_b = None
    b_index = None
    for box, other_boxes in distance_matrix.items():
        for i, other in enumerate(other_boxes):
            other_box = other[0]
            if box.is_connected(other_box):
                continue
            dist = other[1]
            if dist > 0 and dist < minimum:
                minimum = dist
                box_a = box
                box_b = other_box
                b_index = i
    return box_a, box_b, b_index


def solve_part1(entries, pairs):
    circuits = list()
    distance_matrix = dict()

    for i, entry in enumerate(entries):
        box = JunctionBox(entry, name=f"Box_{i}")
        circuit = Circuit(box, name=f"Circuit_{i}")
        circuits.append(circuit)
        distance_matrix[box] = list()

    for box in distance_matrix.keys():
        for other in distance_matrix.keys():
            distance_matrix[box].append([other, box.distance(other)])

    connections = 0
    while connections < pairs:
        logger.debug("-----------------------------------")
        box_a, box_b, b_index = find_closest_boxes(distance_matrix)
        circuit_a = None
        circuit_b = None
        for circuit in circuits:
            if box_a in circuit:
                circuit_a = circuit
            if box_b in circuit:
                circuit_b = circuit
        assert circuit_a is not None
        assert circuit_b is not None
        if circuit_a == circuit_b:
            logger.debug(
                f"{box_a} and {box_b} are already in the same circuit. Skipping."
            )
            continue
        logger.debug("Before merge:")
        logger.debug(f" - {circuit_a}: {circuit_a.junction_boxes}")
        logger.debug(f" - {circuit_b}: {circuit_b.junction_boxes}")
        box_a.connect(box_b)
        circuit_a.merge(circuit_b)
        circuits.remove(circuit_b)
        logger.debug("After merge:")
        logger.debug(f" - {circuit_a}: {circuit_a.junction_boxes}")
        connections += 1

    sorted_circuits = sorted(circuits, key=methodcaller("length"), reverse=True)

    for circuit in sorted_circuits:
        # if circuit.length() > 0:
        print(f"{circuit}: {circuit.length()}")
    return


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day08/input")
    print(solve_part1(entries), 1000)
    print(solve_part2(entries))
