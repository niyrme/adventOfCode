#!/usr/bin/env python3

import os
from typing import Callable
from typing import Literal
from typing import Sequence

import pytest


# replace with whatever type is needed
T = str
parseInput: Callable[[str], Sequence[T]] = lambda inp: tuple(T(line) for line in inp.splitlines())


def part1(inp: str) -> int:
	commands = parseInput(inp)
	x = 0
	depth = 0

	for command in commands:
		cmd, value = str(command).lower().split(" ")
		_value = int(value)
		if cmd == "forward":
			x += _value
		elif cmd == "down":
			depth += _value
		elif cmd == "up":
			depth -= _value
	return x * depth


def part2(inp: str) -> int:
	commands = parseInput(inp)
	x = 0
	depth = 0
	aim = 0

	for command in commands:
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


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 150, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 900, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
