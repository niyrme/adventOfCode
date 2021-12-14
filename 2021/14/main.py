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
		templ = "".join(
			templ[i] + pairs[templ[i:i+2]] + ("" if i <= len(templ) else templ[i+1])
			for i in range(len(templ))
		)

	elemC = Counter(templ)
	return max(elemC.values()) - min(elemC.values())


def part2(inp: str) -> int:
	templ, _patterns = parseInput(inp)

	patterns = dict()
	for pattern in _patterns.splitlines():
		frm, to = pattern.split(" -> ")
		patterns[frm] = to

	pairCounts = Counter()
	for i in range(len(templ) - 1):
		pairCounts[templ[i:i + 2]] += 1

	for _ in range(40):
		newPairs = Counter()
		charCounts = Counter()

		for k, v in pairCounts.items():
			pat = patterns[k]
			newPairs[f"{k[0]}{pat}"] += v
			newPairs[f"{pat}{k[1]}"] += v

			charCounts[k[0]] += v
			charCounts[pat] += v

		pairCounts = newPairs

	charCounts[templ[-1]] += 1

	vals = charCounts.values()

	return max(vals) - min(vals)


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
