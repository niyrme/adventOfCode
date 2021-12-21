#!/usr/bin/env python3

import argparse
import os
import sys

import pytest


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("day", type=int, help="day to run. must be in range 1-25, runs all if not given")
	parser.add_argument("-p", "--part", type=int, help="specific part to run", choices=(1, 2), dest="part")
	parser.add_argument("-T", "--skip-tests", action="store_true", help="skip tests", dest="skipTests")
	parser.add_argument("-t", "--tests", action="store_true", help="only run tests", dest="runTests")
	args = parser.parse_args()

	if not 0 < args.day < 26:
		print(f"day must be in range 1-25, got {args.day}")
		return 1

	dayStr = str(args.day).rjust(2, "0")

	if dayStr not in os.listdir(os.path.dirname(__file__)):
		print(f"Day {dayStr} not found", file=sys.stderr)
		return 1

	print(f"Running {dayStr}")

	testArgs = [f"{dayStr}/main.py", "-q"]
	if args.part is not None:
		for arg in ("-k", f"testPart{args.part}"):
			testArgs.append(arg)

	if args.runTests:
		testRet: pytest.ExitCode = pytest.main(testArgs)
		if testRet not in (pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED):
			print(f"{dayStr} tests failed with exit code {int(testRet)}\n", file=sys.stderr)
			return int(testRet)
		return 0

	if args.skipTests is False:
		testRet: pytest.ExitCode = pytest.main(testArgs)
		if testRet not in (pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED):
			print(f"{dayStr} tests failed with exit code {int(testRet)}\n", file=sys.stderr)
			return int(testRet)

	dayMain = __import__(dayStr, fromlist=("main",)).main

	if args.part is not None:
		inp = open(f"{dayStr}/input.txt", "r")

		if args.part == 1:
			partFn = dayMain.part1
		else:
			partFn = dayMain.part2

		print(f"Part {args.part}: {partFn(inp.read())}")
		inp.close()

		ret = 0
	else:
		ret = dayMain.main()
		print()

	return ret


if __name__ == "__main__":
	raise SystemExit(main())
