#!/usr/bin/env python3

import os
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


# replace with whatever type is needed
T = int
parseInput: Callable[[str], Sequence[T]] = lambda inp: tuple(T(line) for line in inp.splitlines())


def part1(inp: str) -> int:
	depths = parseInput(inp)
	return tuple(
		(depths[i - 1] < depths[i])
		for i in range(1, len(depths))
	).count(True)


def part2(inp: str) -> int:
	depths = parseInput(inp)
	return part1("\n".join(
		str(sum(depths[i:(i + 3)]))
		for i in range(len(depths) - 2)
	))


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
199
200
208
210
200
207
240
269
260
263
""".strip()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 7, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 5, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
