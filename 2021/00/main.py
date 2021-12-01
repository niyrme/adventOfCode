from typing import Callable
from typing import Sequence
from typing import Type
from typing import TypeVar

import pytest

T = TypeVar("T")


def _part1(inp: Sequence[T]) -> T:
	...


def _part2(inp: Sequence[T]) -> T:
	...


def solve(inp: Sequence[T], part: int, typ: Type):
	lns: list[typ] = []
	for line in inp:
		lns.append(typ(line))
	return (_part1, _part2)[part - 1](lns)


def main() -> int:
	with open("./input.txt") as inpF:
		inp = inpF.read().strip().splitlines()
		print(solve(inp, 1, int))
		print(solve(inp, 2, int))
	return 0


@pytest.mark.parametrize(
	("inp", "expected", "fn"), (
		pytest.param(
			(),
			0,
			_part1,
			id="1 | 1"
		),
		pytest.param(
			(),
			0,
			_part2,
			id="2 | 1"
		),
	),
)
def test(inp: Sequence, expected, fn: Callable[[Sequence[T]], T]):
	assert fn(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
