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
	return sum(map(
		lambda line: sum(list(map(
			lambda x: len(x.strip()) in (2, 3, 4, 7),
			line.split("|")[1].strip().split(),
		))),
		lines,
	))


def part2(inp: str) -> int:
	lines = parseInput(inp)
	count = 0

	for line in lines:
		ins, outs = line.strip().split("|")
		_outs = ["".join(sorted(s)) for s in outs.split()]
		_numbers = {*ins.split(), *_outs}
		numbers = {"".join(sorted(p)) for p in _numbers}

		mapNums = dict()
		mapNums[1], = (s for s in numbers if len(s) == 2)
		mapNums[7], = (s for s in numbers if len(s) == 3)
		mapNums[4], = (s for s in numbers if len(s) == 4)
		mapNums[8], = (s for s in numbers if len(s) == 7)

		len6 = {s for s in numbers if len(s) == 6}
		mapNums[6], = (s for s in len6 if (len(set(s) & set(mapNums[1])) == 1))
		mapNums[9], = (s for s in len6 if (len(set(s) & set(mapNums[4])) == 4))
		mapNums[0], = len6 - {mapNums[6], mapNums[9]}

		len5 = {s for s in numbers if len(s) == 5}
		mapNums[5], = (s for s in len5 if (len(set(s) & set(mapNums[6]))) == 5)
		mapNums[3], = (s for s in len5 if (len(set(s) & set(mapNums[1]))) == 2)
		mapNums[2], = len5 - {mapNums[5], mapNums[3]}

		mapS = {v: k for k, v in mapNums.items()}

		count += sum(10 ** (3 - i) * mapS[_outs[i]] for i in range(4))

	return count


def main() -> int:
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip()
		print(f"Part 1: {part1(inp)}")
		print(f"Part 2: {part2(inp)}")
	return 0


EXAMPLE_INPUT = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".strip()
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 26, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 61229, 2, id="2 | 1"),
	),
)
def test(inp: str, expected: int, part: Literal[1, 2]):
	assert (part1, part2)[part - 1](inp) == expected


if __name__ == "__main__":
	raise SystemExit(main())
