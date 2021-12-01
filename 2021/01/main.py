from typing import Callable
from typing import Sequence
from typing import TypeVar

import pytest

T = TypeVar("T")


def _part1(depths: Sequence[T]) -> T:
	prev = 0
	incs = -1
	for i in depths:
		if i > prev:
			incs += 1
		prev = i
	return incs


def _part2(depths: Sequence[T]) -> T:
	sums: list[int] = []
	for i in range(len(depths) - 2):
		sums.append(sum((depths[i], depths[i + 1], depths[i + 2])))

	return _part1(sums)
	# one liner solution
	# return _part1(sum((depths[i], depths[i+1], depths[i+2])) for i in range(len(depths)-2))


def solve(inp: Sequence[T], part: int):
	linesInt: list[int] = []
	for line in inp:
		linesInt.append(int(line))
	return (_part1, _part2)[part - 1](linesInt)
	# one liner solution
	# return (_part1, _part2)[part - 1]((int(line) for line in inp))


def main() -> int:
	with open("./input.txt") as inpF:
		inp = inpF.read().strip().splitlines()
		print(solve(inp, 1))
		print(solve(inp, 2))
	return 0


@pytest.mark.parametrize(
	("inp", "expected", "func"), (
		pytest.param(
			(199, 200, 208, 210, 200, 207, 240, 269, 260, 263),
			7,
			_part1,
			id="1 | 1"
		),
		pytest.param(
			(199, 200, 208, 210, 200, 207, 240, 269, 260, 263),
			5,
			_part2,
			id="2 | 1"
		),
	),
)
def test(inp: Sequence, expected, func: Callable[[Sequence[T]], T]):
	assert func(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
