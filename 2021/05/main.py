#!/usr/bin/env python3

from collections import defaultdict
import os
from typing import Literal
from typing import Sequence

import pytest

T = str


def _part1(inp: Sequence[T]) -> int:
	board = defaultdict(int)
	for line in inp:
		frm, to = line.strip().split("->")
		_x1, _y1 = frm.split(",")
		_x2, _y2 = to.split(",")

		x1 = int(_x1.strip())
		x2 = int(_x2.strip())
		y1 = int(_y1.strip())
		y2 = int(_y2.strip())

		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)

		if x1 == x2:
			for y in range(y1, y2 + 1):
				board[(x1, y)] += 1
		elif y1 == y2:
			for x in range(x1, x2 + 1):
				board[(x, y1)] += 1

	return sum([1 if x > 1 else 0 for x in board.values()])


def _part2(inp: Sequence[T]) -> int:
	board = defaultdict(int)
	for line in inp:
		frm, to = line.strip().split("->")
		_x1, _y1 = frm.split(",")
		_x2, _y2 = to.split(",")

		x1 = int(_x1.strip())
		x2 = int(_x2.strip())
		y1 = int(_y1.strip())
		y2 = int(_y2.strip())

		# from (x1, y1)
		# to   (x2, y2)

		print(f"\n{line=}")
		if x1 == y1 and x2 == y2:
			print(f"  Diagonal 1: {(x1, y1)} -> {(x2, y2)}")
			for xy in range(x1, x2):
				print(f"    adding {(xy, xy)}")
				board[(xy, xy)] += 1
		elif x1 == y2 and y1 == x2:
			print(f"  Diagonal 2: {(x1, x2)} -> {(y1, y2)}")
			new = (x1, y1)
			while new != (x2, y2):
				board[new] += 1
				print(f"    adding {new}")
				if x1 > x2:
					new = (new[0] - 1, new[1] + 1)
				else:
					new = (new[0] + 1, new[1] - 1)
			board[new] += 1
			print(f"    adding {new}")
		elif x1 == x2:
			print(f"  Vertical:   y={x1}: {y1} -> {y2}")
			for y in range(min(y1, y2), max(y1, y2) + 1):
				print(f"    adding {(x1, y)}")
				board[(x1, y)] += 1
		elif y1 == y2:
			print(f"  Horizontal: x={y1}: {x1} -> {x2}")
			for x in range(min(x1, x2), max(x1, x2) + 1):
				print(f"    adding {(x, y1)}")
				board[(x, y1)] += 1

	# print()
	# from pprint import pp
	# pp(board)
	for k in sorted(board.keys()):
		print(f"{k=} v={board[k]}")

	return sum([1 if x > 1 else 0 for x in board.values()])


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(T(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
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
5,5 -> 8,2
""".strip().splitlines()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 5, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 12, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: T, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
