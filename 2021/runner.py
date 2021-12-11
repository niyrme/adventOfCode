#!/usr/bin/env python3

import argparse
import os
import sys

import pytest


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("day", type=int, help="day to run. must be in range 1-25, runs all if not given")
	parser.add_argument("-T", "--skip-tests", action="store_true", help="skip tests", dest="skipTests")
	args = parser.parse_args()

	if not 0 < args.day < 26:
		print(f"day must be in range 1-25, got {args.day}")
		return 1

	dayStr = str(args.day).rjust(2, "0")

	if dayStr not in os.listdir(os.path.dirname(__file__)):
		print(f"Day {dayStr} not found", file=sys.stderr)
		return 1

	print(f"Running {dayStr}")
	if args.skipTests is False:
		ret: pytest.ExitCode = pytest.main([f"{dayStr}/main.py", "-q"])
		if ret != pytest.ExitCode.OK:
			print(f"{dayStr} failed with exit code {int(ret)}\n", file=sys.stderr)
			return int(ret)

	r = __import__(dayStr, fromlist=("main", )).main.main()
	print()
	return r


if __name__ == "__main__":
	raise SystemExit(main())
