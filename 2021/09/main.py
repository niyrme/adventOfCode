#!/usr/bin/env python3

from collections import defaultdict
import os
from math import prod
from typing import Literal
from typing import Generator
from typing import Sequence

import pytest


def neighbours(x: int, y: int) -> Generator[tuple[int, int], None, None]:
	yield (x + 1, y)
	yield (x - 1, y)
	yield (x, y + 1)
	yield (x, y - 1)


def _part1(inp: Sequence[str]) -> int:
	coords: dict[tuple[int, int], int] = defaultdict(lambda: 9)
	for y, line in enumerate(inp):
		for x, char in enumerate(line):
			coords[(x, y)] = int(char)

	return sum((i + 1) * int(all(coords[at] > i for at in neighbours(x, y))) for (x, y), i in tuple(coords.items()))


def _part2(inp: Sequence[str]) -> int:
	coords: dict[tuple[int, int], int] = defaultdict(lambda: 9)
	for y, line in enumerate(inp):
		for x, char in enumerate(line):
			coords[(x, y)] = int(char)

	sizes = []

	for (x, y), i in tuple(coords.items()):
		if all(coords[at] > i for at in neighbours(x, y)):
			seen = set()
			todo = [(x, y)]
			while todo:
				x, y = todo.pop()
				seen.add((x, y))

				for other in neighbours(x, y):
					if other not in seen and coords[other] != 9:
						todo.append(other)

			sizes.append(len(seen))

	return prod(sorted(sizes)[-3:])


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


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


EXAMPLE_INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip().splitlines()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 15, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 1134, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[str], expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
