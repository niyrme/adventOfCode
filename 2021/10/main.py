#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence

import pytest


def _part1(inp: Sequence[str]) -> int:
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
	for line in inp:
		opened = []

		for c in line:
			if c in "([{<":
				opened.append(c)
			elif c in ")]}>":
				if opened.pop() != closeToOpen[c]:
					total += penalty[c]
	return total


def _part2(inp: Sequence[str]) -> int:
	penalty = {k: i + 1 for i, k in enumerate("([{<")}

	closeToOpen = {
		")": "(",
		"]": "[",
		"}": "{",
		">": "<",
	}

	totals = []
	for line in inp:
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


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
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
""".strip().splitlines()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 26397, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 288957, 2, id="2 | 1"),
	),
)
def test(inp: Sequence[str], expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
