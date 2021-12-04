#!/usr/bin/env python3

import os
from typing import Literal, final
from typing import Sequence
from typing import Union

import pytest


def _part1(inp: Sequence[str]) -> int:
	numbers = tuple(int(str(n).strip()) for n in inp[0].split(","))

	boards: list[list[int]] = []

	for board in inp[1:]:
		_board = []
		for line in board.strip().splitlines():
			line = line.strip()
			for num in line.split(" "):
				if num == "":
					continue
				else:
					_board.append(int(num.strip()))
		boards.append(_board)

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


def _part2(inp: Sequence[str]) -> int:
	numbers = tuple(int(str(n).strip()) for n in inp[0].split(","))

	boards: list[list[int]] = []

	for board in inp[1:]:
		_board = []
		for line in board.strip().splitlines():
			line = line.strip()
			for num in line.split(" "):
				if num == "":
					continue
				else:
					_board.append(int(num.strip()))
		boards.append(_board)

	breakTop = False
	for number in numbers:
		if breakTop:
			break

		for board in boards:
			if len(boards) == 1:
				breakTop = True
				break

			if number in board:
				board[board.index(number)] = None

			for i in range(5):
				if board[(i * 5):((i * 5) + 5)] == [None] * 5:
					if len(boards) == 1:
						return number * sum(value if value is not None else 0 for value in board)
					boards.remove(board)
					break
				else:
					rotated = list(board[(j * 5) + i] for i in range(5) for j in range(5))
					if rotated[(i * 5):((i * 5) + 5)] == [None] * 5:
						if len(boards) == 1:
							return number * sum(value if value is not None else 0 for value in board)
						else:
							boards.remove(board)
							break

	board = boards[0]
	for number in numbers:
		if number in board:
			board[board.index(number)] = None
		for i in range(5):
			if board[(i * 5):((i * 5) + 5)] == [None] * 5:
				return number * sum(value if value is not None else 0 for value in board)
			else:
				rotated = list(board[(j * 5) + i] for i in range(5) for j in range(5))
				if rotated[(i * 5):((i * 5) + 5)] == [None] * 5:
					return number * sum(value if value is not None else 0 for value in board)

	# def printBoard(board: list[int]) -> None:
	# 	print("board")
	# 	for i in range(5):
	# 		print("  ", end="")
	# 		for j in range(5):
	# 			print(str(board[i*5+j]).ljust(6), end="")
	# 		print()

	# assert len(boards) == 1
	# b = boards[0]

	# for number in numbers:
	# 	# print(f"\npicking {number=}")
	# 	if number in b:
	# 		# print("found nuber!")
	# 		b[b.index(number)] = None
	# 	# printBoard(b)

	# 	for i in range(5):
	# 		if b[(i * 5):((i * 5) + 5)] == [None] * 5:
	# 			print("board won horizontally")
	# 			printBoard(b)
	# 			s = sum(value if value is not None else 0 for value in b)
	# 			print(f"{s=} {number=}")
	# 			return number * s
	# 		else:
	# 			rotated = list(b[(j * 5) + i] for i in range(5) for j in range(5))
	# 			if rotated[(i * 5):(i * 5 + 5)] == [None] * 5:
	# 				print("board won vertically")
	# 				printBoard(b)
	# 				s = sum(value if value is not None else 0 for value in b)
	# 				print(f"{s=} {number=}")
	# 				return number * s

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
		# 11094 low
		# 13455 low
		# 16684 wrong?
		# 18538 high
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
