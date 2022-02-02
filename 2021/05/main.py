#!/usr/bin/env python3

import os
from collections import Counter

import pytest


def compute(inp: str, skipDiagonal: bool) -> int:
	board = Counter()
	for line in inp.splitlines():
		src, dst = line.strip().split("->")
		x1, y1 = (int(d) for d in src.split(","))
		x2, y2 = (int(d) for d in dst.split(","))

		# skip line not horizontal or vertical
		if (skipDiagonal is True) and (not (x1 == x2 or y1 == y2)):
			continue

		pos = (x1, y1)
		# inline cmp function from python 2
		changeX = int(x2 > x1) - int(x2 < x1)
		changeY = int(y2 > y1) - int(y2 < y1)
		while pos != (x2 + changeX, y2 + changeY):
			board[pos] += 1
			pos = (pos[0] + changeX, pos[1] + changeY)
	return sum(x > 1 for x in board.values())


def part1(inp: str) -> int:
	return compute(inp, True)


def part2(inp: str) -> int:
	return compute(inp, False)


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()

@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 5),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 12),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
