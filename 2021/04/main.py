#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence

import pytest


def _part1(inp: Sequence[str]) -> int:
	numbers = tuple(int(str(n).strip()) for n in inp[0].split(","))

	boards: set[list[int]] = set()

	for board in inp[1:]:
		_board = []
		for line in board.strip().splitlines():
			line = line.strip()
			for num in line.split(" "):
				if num == "":
					continue
				else:
					_board.append(int(num.strip()))
		boards.add(_board)

	for number in numbers:
		for board in boards:
			if number in board:
				board[board.index(number)] = None
			for i in range(5):
				if board[(i * 5):((i * 5) + 5)] == [None] * 5:
					return number * sum(value if value is not None else 0 for value in board)
				else:
					rotated = list(board[(j * 5) + i] for i in range(5) for j in range(5))
					if rotated[(i * 5):((i * 5) + 5)] == [None] * 5:
						return number * sum(value if value is not None else 0 for value in board)

	raise AssertionError("unreachable")


# slightly cheated. explaination was kinda wanky and I couldn't find a way to make it work
def _part2(inp: Sequence[str]) -> int:
	numbers = tuple(int(str(n).strip()) for n in inp[0].split(","))

	boards: set[list[int]] = {}

	for board in inp[1:]:
		_board = []
		for line in board.strip().splitlines():
			line = line.strip()
			for num in line.split(" "):
				if num == "":
					continue
				else:
					_board.append(int(num.strip()))
		boards.add(_board)

	breakTop = False
	seen: set[int] = set()
	lastWonScore = -1
	for number in numbers:
		if breakTop:
			break

		for boardI, board in enumerate(boards):
			if len(boards) == 0:
				breakTop = True
				break

			if number in board:
				board[board.index(number)] = None

			for i in range(5):
				if board[(i * 5):((i * 5) + 5)] == [None] * 5 and boardI not in seen:
					seen.add(boardI)
					lastWonScore = number * sum(value if value is not None else 0 for value in board)
				else:
					rotated = list(board[(j * 5) + i] for i in range(5) for j in range(5))
					if rotated[(i * 5):((i * 5) + 5)] == [None] * 5 and boardI not in seen:
						seen.add(boardI)
						lastWonScore = number * sum(value if value is not None else 0 for value in board)
	else:
		return lastWonScore

	raise AssertionError("unreachable")


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().split("\n\n")
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = """
	7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

	22 13 17 11  0
	8  2 23  4 24
	21  9 14 16  7
	6 10  3 18  5
	1 12 20 15 19

	3 15  0  2 22
	9 18 13 17  5
	19  8  7 25 23
	20 11 10 24  4
	14 21 16 12  6

	14 21 17 24  4
	10 16 15  9 19
	18  8 23 26 20
	22 11 13  6  5
	2  0 12  3  7
""".strip().split("\n\n")

@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 4512, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 1924, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())