#!/usr/bin/env python3

import os

import pytest


def part1(inp: str) -> int:
	target = inp.strip()[13:]
	yRange = target.split(", ")[1]

	yStart = yRange[2:].split("..")[1]

	y = abs(int(yStart)) - 1
	return y * y - (y - 1) * y // 2


def part2(inp: str) -> int:
	# TODO
	# - get direction in which landing area is (+x / -x / both?)
	# - iterate y from (-99 to maxY)
	#   - maxY is the maximum y value until the probe misses after 1 step
	# - same for x?
	# NOTE: probe starts at (0, 0), not any number. the velocity is different just
	raise NotImplementedError


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = "target area: x=20..30, y=-10..-5".strip()


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 45),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 112),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
