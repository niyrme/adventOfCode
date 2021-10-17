from main import solve

import pytest


@pytest.mark.parameterize(
	("path", "expected"), (
		("./testInputPart1.txt", {}),
		("./testInputPart2.txt", {}),
	)
)
def testDay00(path: str, expected):
	result = solve(path)
	assert result == expected, f"Expected {expected}, got {result} instead"
