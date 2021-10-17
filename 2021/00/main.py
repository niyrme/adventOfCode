def _part1(path: str):
	with open(path, "r") as f:
		...


def _part2(path: str):
	with open(path, "r") as f:
		...


def solve(path: str, part: int):
	{1: _part1, 2: _part2}[part](path)


if __name__ == "__main__":
	solve("./input.txt")
