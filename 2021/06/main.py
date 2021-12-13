#!/usr/bin/env python3

import os
from collections import Counter
from typing import Callable
from typing import Sequence

import pytest

# replace with whatever type is needed
T = int
def parseInput(inp: str) -> Sequence[T]:
	return tuple(T(line) for line in inp.split(","))


def getFishCount(inp: Sequence[int], days: int) -> int:
	fish = Counter(inp)

	for _ in range(days):
		_fish = Counter({8: fish[0], 6: fish[0]})
		_fish.update({k - 1: v for k, v in fish.items() if k > 0})
		fish = _fish

	return sum(fish.values())


part1: Callable[[int], int] = lambda inp: getFishCount(parseInput(inp), 80)
part2: Callable[[int], int] = lambda inp: getFishCount(parseInput(inp), 256)


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = "3,4,3,1,2"


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 5934, id="1"),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 26984457539, id="1"),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
