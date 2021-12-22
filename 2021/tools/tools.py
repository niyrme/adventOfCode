from __future__ import annotations

import argparse
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Generator
from typing import Sequence
from typing import Union

SELF = os.path.dirname(__file__)


def _getCookieHeaders() -> dict[str, str]:
	with open(os.path.join(SELF, "../.env")) as env:
		header = env.read().strip()
	return {"Cookie": header}


def _getInput(year: int, day: int) -> str:
	url = f"https://adventofcode.com/{year}/day/{day}/input"
	req = urllib.request.Request(url, headers=_getCookieHeaders())
	return urllib.request.urlopen(req).read().decode()


def getYrD() -> tuple[int, int]:
	cwd = os.getcwd()
	day = int(os.path.basename(cwd))
	year = int(os.path.basename(os.path.dirname(cwd)))

	return (year, day)


def downloadInput() -> int:
	parser = argparse.ArgumentParser()
	parser.parse_args()

	year, day = getYrD()
	print(f"getting input for: {year}/{day}")
	for _ in range(5):
		try:
			s = _getInput(year, day)
		except urllib.error.URLError as e:
			print(f"not ready: {e}")
			time.sleep(1)
		else:
			break
	else:
		raise SystemExit("connection timed out")

	with open("input.txt", "w") as inp:
		inp.write(s)

	return 0


def _postAnswer(year: int, day: int, part: int, answer: Union[str, int]) -> str:
	params = urllib.parse.urlencode({"level": part, "answer": answer})
	req = urllib.request.Request(
		f"https://adventofcode.com/{year}/day/{day}/answer",
		method="POST",
		data=params.encode(),
		headers=_getCookieHeaders(),
	)
	return urllib.request.urlopen(req).read().decode()


RE_TOO_QUICK = re.compile(r"You gave an answer too recently.*to wait\.")
RE_WRONG = re.compile(r"That's not the right answer.*?\.")
RE_ALREADY_DONE = re.compile(r"You don't seem to be solving.*?")
RIGHT_MSG = "That's the right answer!"


def _sumbit252(year: int) -> int:
	parser = argparse.ArgumentParser()
	parser.parse_args()

	answerResp = _postAnswer(year, 25, 2, 0)
	if "Congratulations!" in answerResp:
		print("\033[42mCongratulations!\033[m")
		return 0
	else:
		print(f"{answerResp=}")
		return 1


def submit(args: Sequence[str] = None) -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("part", type=int)
	parser.add_argument("answer", type=str)
	parsedArgs = parser.parse_args(args)

	year, day = getYrD()
	try:
		answer = int(parsedArgs.answer)
	except ValueError:
		answer = parsedArgs.answer

	print(f"{answer=}")

	answerResp = _postAnswer(year, day, parsedArgs.part, answer)

	for errRe in (
		(RE_WRONG, 31),
		(RE_TOO_QUICK, 33),
		(RE_ALREADY_DONE, 35),
	):
		errMatch = errRe[0].search(answerResp)
		if errMatch is not None:
			print(f"\033[{errRe[1]}m{errMatch[0]}\033[m")
			return 1

	if RIGHT_MSG in answerResp:
		print(f"\033[32m{RIGHT_MSG}\033[m")

		if day == 25:
			time.sleep(0.5)
			return _sumbit252(year)
		else:
			return 0
	else:
		print(f"{answerResp=}")
		return 1


# Helper functions for code
def neighbours4(x: int, y: int) -> Generator[tuple[int, int], None, None]:
	yield x, y - 1
	yield x + 1, y
	yield x, y + 1
	yield x - 1, y


def neighbours8(x: int, y: int) -> Generator[tuple[int, int], None, None]:
	for yD in (-1, 0, 1):
		for xD in (-1, 0, 1):
			if xD == yD == 0:
				continue
			yield (x + xD, y + yD)


def parseCoordsInt(s: str) -> dict[tuple[int, int], int]:
	coords = dict()
	for y, line in enumerate(s.splitlines()):
		for x, char in enumerate(line):
			coords[(x, y)] = int(char)
	return coords


def parseCoordsSymbol(s: str, symb: str = "#") -> set[tuple[int, int]]:
	coords = set()
	for y, line in enumerate(s.splitlines()):
		for x, char in enumerate(line):
			if char == symb:
				coords.add((x, y))
	return coords
