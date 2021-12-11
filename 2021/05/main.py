#!/usr/bin/env python3

import os
from collections import Counter
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


# not the actual python 2 cmp, because output is flipped
cmp: Callable[[int, int], int] = lambda a, b: int(a < b) - int(a > b)


def _part1(inp: Sequence[str]) -> int:
	board = Counter()
	for line in inp:
		frm, to = line.strip().split("->")
		x1, y1 = (int(d) for d in frm.split(","))
		x2, y2 = (int(d) for d in to.split(","))

		if x1 == x2 or y1 == y2:
			pos = (x1, y1)
			horizontalChange = cmp(x1, x2)
			verticalChange = cmp(y1, y2)
			while pos != (x2 + horizontalChange, y2 + verticalChange):
				board[pos] += 1
				pos = (pos[0] + horizontalChange, pos[1] + verticalChange)
	return sum(x > 1 for x in board.values())


def _part2(inp: Sequence[str]) -> int:
	board = Counter()
	for line in inp:
		frm, to = line.strip().split("->")
		x1, y1 = (int(d) for d in frm.split(","))
		x2, y2 = (int(d) for d in to.split(","))

		pos = (x1, y1)
		horizontalChange = cmp(x1, x2)
		verticalChange = cmp(y1, y2)
		while pos != (x2 + horizontalChange, y2 + verticalChange):
			board[pos] += 1
			pos = (pos[0] + horizontalChange, pos[1] + verticalChange)

	return sum(x > 1 for x in board.values())


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
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
def test(inp: Sequence[str], expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
