#!/usr/bin/env python3

from typing import Callable
from typing import Sequence
from typing import Type
from typing import TypeVar

import pytest

T = TypeVar("T")


def _part1(depths: Sequence[T]) -> T:
	incs = 0
	for i in range(1, len(depths)):
		if depths[i - 1] < depths[i]:
			incs += 1
	return incs
	# one liner solution
	# return tuple((depths[i - 1] < depths[i]) for i in range(1, len(depths))).count(True)


def _part2(depths: Sequence[T]) -> T:
	sums: list[int] = []
	for i in range(len(depths) - 2):
		sums.append(sum((depths[i], depths[i + 1], depths[i + 2])))

	return _part1(sums)
	# one liner solution
	# return _part1(sum((depths[i], depths[i + 1], depths[i + 2])) for i in range(len(depths) - 2))


def solve(inp: Sequence[T], part: int, typ: Type):
	return (_part1, _part2)[part - 1](tuple(typ(line) for line in inp))


def main() -> int:
	with open("./input.txt") as inpF:
		inp = inpF.read().strip().splitlines()
		print(solve(inp, 1, int))
		print(solve(inp, 2, int))
	return 0


@pytest.mark.parametrize(
	("inp", "expected", "func"), (
		pytest.param(
			(199, 200, 208, 210, 200, 207, 240, 269, 260, 263),
			7,
			_part1,
			id="1 | 1",
		),
		pytest.param(
			(199, 200, 208, 210, 200, 207, 240, 269, 260, 263),
			5,
			_part2,
			id="2 | 1",
		),
	),
)
def test(inp: Sequence, expected, func: Callable[[Sequence[T]], T]):
	assert func(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
