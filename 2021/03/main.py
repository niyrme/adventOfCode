#!/usr/bin/env python3

import os
from typing import Callable
from typing import Literal
from typing import Sequence
from typing import Type
from typing import TypeVar
from typing import Union

import pytest

T = TypeVar("T")


def _part1(inp: Sequence[T]) -> T:
	newInp = []

	for x in list(zip(*inp)):
		newInp.append("".join(x))

	c = ""
	for x in newInp:
		c += {
			True: "0",
			False: "1",
		}[str(x).count("0") > str(x).count("1")]

	return int(c, 2) * int("".join("1" if x == "0" else "0" for x in c), 2)


def mostCommon(bitStrings: Sequence[str], pos: int, default: int) -> Union[Literal[0, 1], None]:
	bitRow = "".join(list(zip(*bitStrings))[pos])

	count0 = bitRow.count("0")
	count1 = bitRow.count("1")

	if count0 > count1:
		return 0
	elif count0 < count1:
		return 1
	else:
		return None


def filterBits(bitStrings: Sequence[str], n: int, expected: int) -> Sequence[str]:
	filtered = []
	for bitString in bitStrings:
		if bitString[n] == str(expected):
			filtered.append(bitString)
	return filtered


def _part2(inp: Sequence[T]) -> T:
	bits0 = filterBits(inp, 0, 0)
	bits1 = filterBits(inp, 0, 1)

	if len(bits0) > len(bits1):
		oxygen = bits0
		co2 = bits1
	elif len(bits0) < len(bits1):
		co2 = bits0
		oxygen = bits1
	else:
		co2 = bits0
		oxygen = bits1

	for i in range(1, len(inp[0])):
		# no need to filter if only one element
		if len(oxygen) > 1:
			oxygen = filterBits(oxygen, i, {None: 1, 0: 0, 1: 1}[mostCommon(oxygen, i, 1)])
		if len(co2) > 1:
			co2 = filterBits(co2, i, {None: 0, 0: 1, 1: 0}[mostCommon(co2, i, 0)])

	oxygenS = "".join(oxygen)
	co2S = "".join(co2)

	return int(oxygenS, 2) * int(co2S, 2)


def solve(inp: Sequence[T], part: Literal[1, 2], typ: Type):
	return (_part1, _part2)[part - 1](tuple(typ(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		inpType = str
		print(f"Part 1: {solve(inp, 1, inpType)}")
		print(f"Part 2: {solve(inp, 2, inpType)}")
	return 0

@pytest.mark.parametrize(
	("inp", "expected", "func"), (
		pytest.param(("00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"), 198, _part1, id="1 | 1"),
		pytest.param(("00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"), 230, _part2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: T, func: Callable[[Sequence[T]], T]):
	assert func(inp) == expected
	# assert False


if __name__ == "__main__":
	raise SystemExit(main())
