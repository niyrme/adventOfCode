#!/usr/bin/env python3

import os
import statistics
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


_part1: Callable[[int], int] = lambda inp: int(sum(abs(num - statistics.median(inp)) for num in inp))


def _part2(inp: Sequence[int]) -> int:
	getN: Callable[[int], int] = lambda n: sum(abs(num - n) * (abs(num - n) + 1) // 2 for num in inp)
	median = statistics.median(inp)
	num = getN(median)

	direction = {
		True: -1,
		False: 1,
	}[getN(median - 1) < num]

	while getN(median + direction) < num:
		median += direction
		num = getN(median)

	return int(num)


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(int(line) for line in inp))


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().split(",")
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = "16,1,2,0,4,2,7,1,2,14".split(",")
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 37, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 168, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[int], expected: int, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
