#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence

import pytest


def _part1(depths: Sequence[int]) -> int:
	incs = 0
	for i in range(1, len(depths)):
		if depths[i - 1] < depths[i]:
			incs += 1
	return incs
	# one liner solution
	# return tuple((depths[i - 1] < depths[i]) for i in range(1, len(depths))).count(True)


def _part2(depths: Sequence[int]) -> int:
	sums: list[int] = []
	for i in range(len(depths) - 2):
		sums.append(sum((depths[i], depths[i + 1], depths[i + 2])))

	return _part1(sums)
	# one liner solution
	# return _part1(sum((depths[i], depths[i + 1], depths[i + 2])) for i in range(len(depths) - 2))


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(int(line) for line in inp))


def main() -> int:
	ret: pytest.ExitCode = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return int(ret)
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = (199, 200, 208, 210, 200, 207, 240, 269, 260, 263)
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 7, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 5, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: int, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
