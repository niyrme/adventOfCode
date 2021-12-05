#!/usr/bin/env python3

import os
from collections import defaultdict
from typing import Literal
from typing import Sequence

import pytest


def _part1(inp: Sequence[str]) -> int:
	board = defaultdict(int)
	for line in inp:
		frm, to = line.strip().split("->")
		x1, y1 = (int(d) for d in frm.split(","))
		x2, y2 = (int(d) for d in to.split(","))

		if x1 == x2:
			for y in range(min(y1, y2), max(y1, y2) + 1):
				board[(x1, y)] += 1
		elif y1 == y2:
			for x in range(min(x1, x2), max(x1, x2) + 1):
				board[(x, y1)] += 1

	return sum([1 if x > 1 else 0 for x in board.values()])


def _part2(inp: Sequence[str]) -> int:
	cmp = lambda a, b: int(a < b) - int(a > b)

	board = defaultdict(int)
	for line in inp:
		frm, to = line.strip().split("->")
		x1, y1 = (int(d) for d in frm.split(","))
		x2, y2 = (int(d) for d in to.split(","))

		pos = (x1, y1)
		horizontalChange = cmp(x1, x2)
		verticalChange = cmp(y1, y2)
		while pos != (x2, y2):
			board[pos] += 1
			pos = (pos[0] + horizontalChange, pos[1] + verticalChange)
		board[pos] += 1

	return sum([1 if x > 1 else 0 for x in board.values()])


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header", "-s"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
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
5,5 -> 8,2""".strip().splitlines()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 5, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 12, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
