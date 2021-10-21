from math import floor
from strutils import `%`, parseInt

proc calcFuel(fuel: int): int =
  let c = int(floor(float(fuel) / 3) - 2)
  if c > 0:
    result = c + calcFuel(c)
  else:
    result = 0

proc parseFile(path: string): seq[int] =
  var f: File
  if open(f, path, fmRead):
    try:
      while true:
        result.add(parseInt(f.readLine()))
    except EOFError:
      discard
    finally:
      close(f)

proc part1(path: string): int =
  for x in parseFile(path):
    result += int(floor(float(x) / 3) - 2)

proc part2(path: string): int =
  for x in parseFile(path):
    result += calcFuel(x)

proc main(): int =
  var testsFailed = false
  for test in [
    (1, 1, part1, "./testInputPart1.txt", 34241),
    (2, 1, part2, "./testInputPart2.txt", 51314),
  ]:
    let res = test[2](test[3])
    if res != test[4]:
      echo "Part $1 | Test $2 failed | Expected $3, got $4" % [$test[0], $test[1], $test[4], $res]
      testsFailed = true

  if testsFailed:
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
