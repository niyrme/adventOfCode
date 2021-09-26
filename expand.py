#!/usr/bin/env python3

import argparse
import os
from typing import Sequence


def addDay(year: int, day: int) -> None:
	day = str(day).rjust(2, '0')

	print(f"Adding {year}/{day}")

	ipth = os.path.join(str(year), "00")
	opth = os.path.join(str(year), str(day))
	os.makedirs(opth, exist_ok=True)

	for file in os.listdir(f"{ipth}"):
		if os.path.isdir(file):
			continue
		with (
			open(f"{ipth}/{file}", "r") as i,
			open(f"{opth}/{file}", "w+") as o,
		): o.write(i.read())


def main(args: Sequence[str] = None) -> int:
	argparser = argparse.ArgumentParser()
	argparser.add_argument(
		"-d", "--day",
		action="store",
		type=int,
		dest="day",
		help="the day to add (newest by default)",
	)
	argparser.add_argument(
		"-y", "--year",
		action="store",
		type=int,
		dest="year",
		help="the year which should be added to (newest by default)",
	)

	parsedArgs = argparser.parse_args(args)

	if parsedArgs.year:
		year = parsedArgs.year
	else:
		newest = 0
		for _year in os.listdir("."):
			if not os.path.isdir(_year):
				continue

			try:
				if int(_year) > newest:
					newest = int(_year)
			except ValueError:
				continue
			except Exception:
				raise
		year = newest

	if parsedArgs.day:
		day = parsedArgs.day
	else:
		newest = 0
		for _day in os.listdir(str(year)):
			if not os.path.isdir(f"{year}/{_day}"):
				continue

			if int(_day) > newest:
				newest = int(_day)
		day = newest + 1

	if not 0 < day < 26:
		print("The days in Advent of Code only go from 1 to 25")
		return 1

	addDay(year, day)

	return 0


if __name__ == "__main__":
	raise SystemExit(main())
