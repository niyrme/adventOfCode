#!/usr/bin/env python3

import os
from collections import Counter
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


# replace with whatever type is needed
T = int
parseInput: Callable[[str], Sequence[T]] = lambda inp: tuple(T(line) for line in inp.split(","))


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
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 5934, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 26984457539, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
