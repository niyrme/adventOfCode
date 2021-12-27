#!/usr/bin/env python3

import os
from enum import Enum

import pytest


class Direction(Enum):
	RIGHT = (1, 0)
	DOWN = (0, 1)


def part1(inp: str) -> int:
	lines = inp.splitlines()
	coords: dict[tuple[int, int], Direction] = dict()
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if char in (">", "v"):
				coords[(x, y)] = {
					"v": Direction.DOWN,
					">": Direction.RIGHT,
				}[char]

	i = 0
	while True:
		i += 1

		newCoords1: dict[tuple[int, int], Direction] = dict()
		for (x, y), direction in coords.items():
			if direction == Direction.RIGHT:
				pos = (
					(x + direction.value[0]) % len(lines[0]),
					(y + direction.value[1]) % len(lines),
				)
				if pos in coords:
					pos = (x, y)
				newCoords1[pos] = direction
			else:
				newCoords1[(x, y)] = direction

		newCoords2: dict[tuple[int, int], Direction] = dict()
		for (x, y), direction in newCoords1.items():
			if direction == Direction.DOWN:
				pos = (
					(x + direction.value[0]) % len(lines[0]),
					(y + direction.value[1]) % len(lines),
				)
				if pos in newCoords1:
					pos = (x, y)
				newCoords2[pos] = direction
			else:
				newCoords2[(x, y)] = direction

		if newCoords2 == coords:
			break
		else:
			coords = newCoords2

	return i


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
	return 0


EXAMPLE_INPUT = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip()


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 58),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
