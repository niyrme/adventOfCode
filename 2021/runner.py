#!/usr/bin/env python3

import argparse
import os
import sys


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("day", help="day to run. must be in range 1-25, runs all if not given", type=int)
	args = parser.parse_args()

	if not 0 < args.day < 26:
		print(f"day must be in range 1-25, got {args.day}")
		return 1

	dayStr = str(args.day).rjust(2, "0")

	if dayStr not in os.listdir(os.path.dirname(__file__)):
		print(f"Day {dayStr} not found", file=sys.stderr)
		return 1

	return __import__(dayStr, fromlist=("main", )).main.main()


if __name__ == "__main__":
	raise SystemExit(main())
