#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence
from typing import TypeVar

import pytest

T = TypeVar("T")


def _part1(inp: Sequence[T]) -> int:
	raise NotImplementedError


def _part2(inp: Sequence[T]) -> int:
	raise NotImplementedError


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(T(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param((), 0, 1, id="1 | 1"),
		pytest.param((), 0, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: T, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
