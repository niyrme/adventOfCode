#!/usr/bin/env python3

import os
import time
from collections import defaultdict
from collections import Counter
from typing import Sequence

import pytest

# replace with whatever type is needed
T = str
def parseInput(inp: str) -> Sequence[T]:
	return tuple(T(line) for line in inp.split("\n\n"))


def part1(inp: str) -> int:
	templ, _pairs = parseInput(inp)

	pairs = defaultdict(str)
	for pair in _pairs.splitlines():
		frm, to = pair.split(" -> ")
		pairs[frm.strip()] = to.strip()

	for _ in range(10):
		n = ""

		i = 0
		for i in range(len(templ)):
			el = templ[i:i+2]
			n += templ[i]
			n += pairs[el]
			n += "" if i <= len(templ) else templ[i + 1]

		templ = n

	elemC = Counter(templ)
	return max(elemC.values()) - min(elemC.values())


def part2(inp: str) -> int:
	# FIXME: optimization problem
	# me too 3Head
	templ, _pairs = parseInput(inp)

	pairs = defaultdict(str)
	for pair in _pairs.splitlines():
		frm, to = pair.split(" -> ")
		pairs[frm.strip()] = to.strip()

	for iterc in range(40):
		start = time.time()
		n = ""

		i = 0
		for i in range(len(templ)):
			el = templ[i:i+2]
			n += pairs[el]
			n += templ[i]
			n += pairs[el]
			n += "" if i <= len(templ) else templ[i + 1]

		templ = n
		print(f"i={iterc:<3} {(time.time()-start):.3f}")
		start = time.time()

	elemC = Counter(templ)
	return max(elemC.values()) - min(elemC.values())


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 1588, id="1"),
	),
)
def testPart1(inp: str, expected: int):
	assert part1(inp) == expected


@pytest.mark.parametrize(
	("inp", "expected"), (
		pytest.param(EXAMPLE_INPUT, 2188189693529, id="1"),
	),
)
def testPart2(inp: str, expected: int):
	assert part2(inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
