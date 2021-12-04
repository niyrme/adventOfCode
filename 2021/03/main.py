#!/usr/bin/env python3

import os
from typing import Literal
from typing import Sequence
from typing import Union

import pytest


def _part1(inp: Sequence[str]) -> int:
	newInp = []

	for x in list(zip(*inp)):
		newInp.append("".join(x))

	bitString = ""
	for x in newInp:
		bitString += {
			True: "0",
			False: "1",
		}[str(x).count("0") > str(x).count("1")]

	return int(bitString, 2) * int("".join("1" if x == "0" else "0" for x in bitString), 2)


def mostCommon(bitStrings: Sequence[str], pos: int) -> Union[Literal[0, 1], None]:
	bitRow = "".join(list(zip(*bitStrings))[pos])

	count0 = bitRow.count("0")
	count1 = bitRow.count("1")

	if count0 > count1:
		return 0
	elif count0 < count1:
		return 1
	else:
		return None


def filterBits(bitStrings: Sequence[str], pos: int, expected: int) -> Sequence[str]:
	filtered = {bitString if bitString[pos] == str(expected) else None for bitString in bitStrings}
	try:
		filtered.remove(None)
	except KeyError:
		pass
	finally:
		return filtered


def _part2(inp: Sequence[str]) -> int:
	bits0 = filterBits(inp, 0, 0)
	bits1 = filterBits(inp, 0, 1)

	if len(bits0) > len(bits1):
		oxygen = bits0
		co2 = bits1
	elif len(bits0) < len(bits1):
		oxygen = bits1
		co2 = bits0
	else:
		oxygen = bits1
		co2 = bits0

	for i in range(1, len(inp[0])):
		# no need to filter if only one element
		if len(oxygen) > 1:
			oxygen = filterBits(oxygen, i, {None: 1, 0: 0, 1: 1}[mostCommon(oxygen, i)])
		if len(co2) > 1:
			co2 = filterBits(co2, i, {None: 0, 0: 1, 1: 0}[mostCommon(co2, i)])

	oxygenS = "".join(oxygen)
	co2S = "".join(co2)

	return int(oxygenS, 2) * int(co2S, 2)


def solve(inp: Sequence[str], part: Literal[1, 2]) -> int:
	return (_part1, _part2)[part - 1](tuple(str(line) for line in inp))


def main() -> int:
	ret = pytest.main([__file__, "--no-header"])
	if ret != pytest.ExitCode.OK:
		return ret
	inputPath = os.path.join(os.path.dirname(__file__), "input.txt")
	with open(inputPath) as inpF:
		inp = inpF.read().strip().splitlines()
		print(f"Part 1: {solve(inp, 1)}")
		print(f"Part 2: {solve(inp, 2)}")
	return 0


EXAMPLE_INPUT = ("00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010")
@pytest.mark.parametrize(
	("inp", "expected", "part"), (
		pytest.param(EXAMPLE_INPUT, 198, 1, id="1 | 1"),
		pytest.param(EXAMPLE_INPUT, 230, 2, id="2 | 1"),
	),
)
def test(inp: Sequence, expected: str, part: Literal[1, 2]):
	assert solve(inp, part) == expected


if __name__ == "__main__":
	raise SystemExit(main())
