import logging
import math
import operator
import re
from aoc2025.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def solve_part1(entries):
    operations = entries[-1]
    problems = entries[:-1]
    grand_total = 0
    for i, operation in enumerate(operations):
        if operation == "*":
            op = operator.mul
            result = 1
        if operation == "+":
            op = operator.add
            result = 0
        for row in problems:
            result = op(result, int(row[i]))
        grand_total += result
    return grand_total


def generate_problems(entries):
    # The pattern captures one non-whitespace char (\S) followed immediately by
    # one or more whitespace chars (\s+). The '*' symbol is greedy in the repetition.
    pattern = r"\S\s+"
    operations = re.findall(pattern, entries[-1])
    problems = entries[:-1]
    result = list()
    for operation in operations:
        terms = list(operation.rstrip())
        _problems = list()
        # logger.info(f"len: {len(operation)}, op: {operation}")
        for problem in problems:
            terms.append(problem[: len(operation) - 1])
            _problems.append(problem[len(operation) :])
        result.append(terms)
        problems = _problems
    # logger.info(result)
    return result


def solve_part2(entries):
    _rows = entries.split("\n")
    rows = list()
    for row in _rows:
        rows.append(row + " ")
    # collect each set of problems
    problems = generate_problems(rows)
    grand_total = 0
    # go through each problem and apply cephalopod math rules
    for i, problem in enumerate(problems):
        op = problem.pop(0)
        problem_terms = [[] for _ in range(len(problem[0]))]
        for digits in problem:
            digits = digits[::-1]  # reverse the digits
            # logger.info(f"reversed digits: {digits}")
            for i in range(len(digits)):
                if digits[i] != " ":
                    problem_terms[i].append(digits[i])
        for i, term in enumerate(problem_terms):
            problem_terms[i] = int("".join(term))
        if op == "*":
            total = 1
            for term in problem_terms:
                total *= term
        if op == "+":
            total = 0
            for term in problem_terms:
                total += term
        grand_total += total
    return grand_total


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2025/day06/input", type="split")
    print(solve_part1(entries))
    entries = get_input("aoc2025/day06/input", type="raw")
    print(solve_part2(entries))
