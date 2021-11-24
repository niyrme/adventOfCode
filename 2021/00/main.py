import sys


def _part1(path: str):
	with open(path, "r") as f:
		...


def _part2(path: str):
	with open(path, "r") as f:
		...


def solve(path: str, part: int):
	{1: _part1, 2: _part2}[part](path)


def main() -> int:
	testsFailed = False

	for test in (
		(1, 1, "./testInputPart1.txt", None),
		(2, 1, "./testInputPart2.txt", None),
	):
		res = solve(test[2])
		if res != test[3]:
			print(f"Part {test[0]} | Test {test[1]} failed | Expected {test[3]}, got {res}", file=sys.stderr)
			testsFailed = True

	if testsFailed is True:
		return 1
	else:
		print(solve("./input.txt"))
		return 0


if __name__ == "__main__":
	raise SystemExit(main())
