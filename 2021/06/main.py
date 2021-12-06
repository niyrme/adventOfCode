#!/usr/bin/env python3

import collections
import os
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


def getFishCount(inp: Sequence[int], days: int) -> int:
	fish = collections.Counter(inp)

	for _ in range(days):
		_fish = collections.Counter({8: fish[0], 6: fish[0]})
		_fish.update({k - 1: v for k, v in fish.items() if k > 0})
		fish = _fish

	return sum(fish.values())


_part1: Callable[[int], int] = lambda inp: getFishCount(inp, 80)
_part2: Callable[[int], int] = lambda inp: getFishCount(inp, 256)


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(int(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header", "-s"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().split(",")
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = "3,4,3,1,2".split(",")


@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 5934, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 26984457539, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[str], expected: int, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
