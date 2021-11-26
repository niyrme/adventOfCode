import sys
from typing import Callable
from typing import NamedTuple
from typing import Sequence


def _part1(inp: Sequence):
	...


def _part2(inp: Sequence):
	...


def solve(path: str, part: int):
	with open(path, "r") as i:
		return (_part1, _part2)[part - 1]((line.strip() for line in i.readlines()))


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
		print(solve("./input.txt", 1))
		print(solve("./input.txt", 2))
		return 0


if __name__ == "__main__":
	raise SystemExit(main())
