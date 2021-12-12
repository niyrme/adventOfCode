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
	lines = parseInput(inp)
	penalty = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137,
	}

	closeToOpen = {
		")": "(",
		"]": "[",
		"}": "{",
		">": "<",
	}

	total = 0
	for line in lines:
		opened = []

		for c in line:
			if c in "([{<":
				opened.append(c)
			elif c in ")]}>":
				if opened.pop() != closeToOpen[c]:
					total += penalty[c]
	return total


def part2(inp: str) -> int:
	lines = parseInput(inp)
	penalty = {k: i + 1 for i, k in enumerate("([{<")}

	closeToOpen = {
		")": "(",
		"]": "[",
		"}": "{",
		">": "<",
	}

	totals = []
	for line in lines:
		opened = []

		for c in line:
			if c in "([{<":
				opened.append(c)
			elif c in ")]}>":
				if opened.pop() != closeToOpen[c]:
					break
		else:
			score = 0
			for o in reversed(opened):
				score = (score * 5) + penalty[o]

			totals.append(score)

	totals.sort()
	return totals[len(totals) // 2]


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 26397, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 288957, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
