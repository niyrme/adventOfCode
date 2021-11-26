import sys
from typing import Callable
from typing import NamedTuple
from typing import Sequence


def _part1(inp: Sequence):
	...


def _part2(inp: Sequence):
	...


def solve(inp: Sequence, part: int):
	return (_part1, _part2)[part - 1](inp)


class Test(NamedTuple):
	part: int
	test: int
	func: Callable
	inp: Sequence
	expected: None


def main() -> int:
	testsFailed = False

	for test in (
		Test(1, 1, _part1, tuple(), None),
		Test(2, 1, _part2, tuple(), None),
	):
		res = test.func(test.inp)
		if res != test.expected:
			print(f"Part {test.part} | Test {test.test} failed | Expected {test.expected}, got {res}", file=sys.stderr)
			testsFailed = True

	if testsFailed is True:
		return 1
	else:
		with open("./input.txt") as inp:
			print(solve(inp.read().strip().splitlines(), 1))
			print(solve(inp.read().strip().splitlines(), 2))
		return 0


if __name__ == "__main__":
	raise SystemExit(main())
