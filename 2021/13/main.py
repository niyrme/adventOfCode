#!/usr/bin/env python3

import os
from typing import Sequence

import pytest

# replace with whatever type is needed
T = str
def parseInput(inp: str) -> Sequence[T]:
	return tuple(T(line) for line in inp.split("\n\n"))


def part1(inp: str) -> int:
	dots, folds = parseInput(inp)
	coords = set()

	for coord in dots.splitlines():
		x, y = coord.split(",")
		coords.add((int(x), int(y)))

	for fold in folds.splitlines():
		foldDir = fold[11]
		foldAmnt = int(fold[13:])

		if foldDir == "x":
			newCoords = set()
			for x, y in coords:
				newCoords.add((x if x < foldAmnt else (foldAmnt - (x - foldAmnt)), y))
			coords = newCoords
		else:
			newCoords = set()
			for x, y in coords:
				newCoords.add((x, y if y < foldAmnt else (foldAmnt - (y - foldAmnt))))
			coords = newCoords

		break

	return len(coords)


def part2(inp: str) -> str:
	dots, folds = parseInput(inp)
	coords = set()

	for coord in dots.splitlines():
		x, y = coord.split(",")
		coords.add((int(x), int(y)))

	for fold in folds.splitlines():
		foldDir = fold[11]
		foldAmnt = int(fold[13:])

		if foldDir == "x":
			newCoords = set()
			for x, y in coords:
				newCoords.add((x if x < foldAmnt else (foldAmnt - (x - foldAmnt)), y))
			coords = newCoords
		else:
			newCoords = set()
			for x, y in coords:
				newCoords.add((x, y if y < foldAmnt else (foldAmnt - (y - foldAmnt))))
			coords = newCoords

	maxX = -1
	maxY = -1
	for x, y in coords:
		maxX = max(maxX, x)
		maxY = max(maxY, y)

	outStr = "\n"
	for y in range(maxY + 1):
		for x in range(maxX + 1):
			if (x, y) in coords:
				outStr += "#"
			else:
				outStr += " "
		outStr += "\n"
	return outStr


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 17, id="1"),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		# pytest.param(EXAMPLE_INPUT, 0, id="1"),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
