#!/usr/bin/env python3

import os
from typing import Callable
from typing import Literal
from typing import Sequence
from typing import Type
from typing import TypeVar

import pytest

T = TypeVar("T")


def _part1(inp: Sequence[T]) -> T:
	x = 0
	depth = 0

	for command in inp:
		cmd, value = str(command).lower().split(" ")
		_value = int(value)
		if cmd == "forward":
			x += _value
		elif cmd == "down":
			depth += _value
		elif cmd == "up":
			depth -= _value
	return x * depth


def _part2(inp: Sequence[T]) -> T:
	x = 0
	depth = 0
	aim = 0

	for command in inp:
		cmd, value = str(command).lower().split(" ")
		_value = int(value)
		if cmd == "forward":
			x += _value
			depth += aim * _value
		elif cmd == "down":
			aim += _value
		elif cmd == "up":
			aim -= _value
	return x * depth


def solve(inp: Sequence[T], part: Literal[1, 2], typ: Type):
	return (_part1, _part2)[part - 1](tuple(typ(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1, str)}")
		print(f"Part 2: {solve(inp, 2, str)}")
	return 0


@pytest.mark.parametrize(
	("inp", "expected", "func"), (
		pytest.param(("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"), 150, _part1, id="1 | 1"),
		pytest.param(("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"), 900, _part2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: T, func: Callable[[Sequence[T]], T]):
	assert func(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
