#!/usr/bin/env python3

import os
from typing import Generator
from typing import Literal
from typing import Sequence

import pytest


def neighbours(x: int, y: int) -> Generator[tuple[int, int], None, None]:
	for _x in (-1, 0, 1):
		for _y in (-1, 0, 1):
			if _x == _y == 0:
				continue
			yield (x + _x, y + _y)


def _part1(inp: Sequence[str]) -> int:
	coords: dict[tuple[int, int], int] = dict()
	for y, line in enumerate(inp):
		for x, char in enumerate(line):
			coords[(x, y)] = int(char)

	flashes = 0
	for _ in range(100):
		todo: list[tuple[int, int]] = []
		for coord in coords:
			coords[coord] += 1
			if coords[coord] > 9:
				todo.append(coord)

		while todo:
			current = todo.pop()
			if coords[current] == 0:
				continue
			coords[current] = 0
			flashes += 1
			for _coord in neighbours(*current):
				if _coord in coords and coords[_coord] != 0:
					coords[_coord] += 1
					if coords[_coord] > 9:
						todo.append(_coord)

	return flashes


def _part2(inp: Sequence[str]) -> int:
	coords: dict[tuple[int, int], int] = dict()
	for y, line in enumerate(inp):
		for x, char in enumerate(line):
			coords[(x, y)] = int(char)

	step = 0
	while True:
		step += 1
		todo: list[tuple[int, int]] = []
		for coord in coords:
			coords[coord] += 1
			if coords[coord] > 9:
				todo.append(coord)

		while todo:
			current = todo.pop()
			if coords[current] == 0:
				continue
			coords[current] = 0
			for coord in neighbours(*current):
				if coord in coords and coords[coord] != 0:
					coords[coord] += 1
					if coords[coord] > 9:
						todo.append(coord)

		if all(octo == 0 for octo in coords.values()):
			return step


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
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip().splitlines()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 1656, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 195, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[str], expected: int, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
