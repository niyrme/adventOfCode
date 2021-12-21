#!/usr/bin/env python3

import functools
import itertools
import os
from collections import Counter
from typing import NamedTuple

import pytest


def mod(n: int) -> int:
	while n > 10:
		n -= 10
	return n


class Score(NamedTuple):
	pos: int
	score: int


def part1(inp: str) -> int:
	lines = inp.splitlines()
	p1Pos = int(lines[0][28])
	p2Pos = int(lines[1][28])

	p1 = Score(p1Pos, 0)
	p2 = Score(p2Pos, 0)

	die = itertools.cycle(range(1, 101))
	rolls = 0

	while True:
		newP1Pos = mod(p1.pos + sum(next(die) for _ in range(3)))
		rolls += 3
		newP1Score = p1.score + newP1Pos

		p1 = Score(newP1Pos, newP1Score)

		if p1.score >= 1000:
			break

		newP2Pos = mod(p2.pos + sum(next(die) for _ in range(3)))
		rolls += 3
		newP2Score = p2.score + newP2Pos

		p2 = Score(newP2Pos, newP2Score)

		if p2.score >= 1000:
			break

	return min(p1.score, p2.score) * rolls


def part2(inp: str) -> int:
	lines = inp.splitlines()

	p1Pos = int(lines[0][28])
	p2Pos = int(lines[1][28])

	rolls = Counter(
		i + j + k
		for i in (1, 2, 3)
		for j in (1, 2, 3)
		for k in (1, 2, 3)
	)

	@functools.lru_cache(maxsize=None)
	def compute(p1: Score, p2: Score) -> tuple[int, int]:
		wins = (0, 0)
		for k, ct in rolls.items():
			newP1Pos = mod(p1.pos + k)
			newP1Score = p1.score + newP1Pos

			if newP1Score >= 21:
				wins = (wins[0] + ct, wins[1])
			else:
				p2Wins, p1Wins = compute(p2, Score(newP1Pos, newP1Score))
				wins = (wins[0] + p1Wins * ct, wins[1] + p2Wins * ct)

		return wins

	# a failed attempt
	# def compute(p1: Score, p2: Score, roll: int, p1Turn: bool) -> None:
	# 	_p1 = p1
	# 	_p2 = p2
	#
	# 	if p1Turn:
	# 		newPos = mod(p1.pos + roll)
	# 		newScore = p1.score + newPos
	#
	# 		if newScore >= 21:
	# 			wins[1] += 1
	# 			return
	#
	# 		_p1 = Score(newPos, newScore)
	# 	else:
	# 		newPos = mod(p2.pos + roll)
	# 		newScore = p2.score + newPos
	#
	# 		if newScore >= 21:
	# 			wins[2] += 1
	# 			return
	#
	# 		_p2 = Score(newPos, newScore)
	#
	# 	for r in range(1, 4):
	# 		compute(_p1, _p2, r, (not p1Turn))


	wins = compute(Score(p1Pos, 0), Score(p2Pos, 0))

	return max(wins)


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 739785),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 444356092776315),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
