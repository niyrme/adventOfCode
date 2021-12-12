#!/usr/bin/env python3

import os
import statistics
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


# replace with whatever type is needed
T = int
parseInput: Callable[[str], Sequence[T]] = lambda inp: tuple(T(line) for line in inp.split(","))


def part1(inp: str) -> int:
	nums = parseInput(inp)
	return int(sum(abs(num - statistics.median(nums)) for num in nums))


def part2(inp: str) -> int:
	nums = parseInput(inp)
	getN: Callable[[int], int] = lambda n: sum(abs(num - n) * (abs(num - n) + 1) // 2 for num in nums)
	median = statistics.median(nums)
	num = getN(median)

	direction = {
		True: -1,
		False: 1,
	}[getN(median - 1) < num]

	while getN(median + direction) < num:
		median += direction
		num = getN(median)

	return int(num)


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = "16,1,2,0,4,2,7,1,2,14"
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 37, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 168, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
