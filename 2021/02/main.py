#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence

import pytest


def _part1(inp: Sequence[str]) -> int:
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


def _part2(inp: Sequence[str]) -> int:
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


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = ("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2")
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 150, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 900, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[str], expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
