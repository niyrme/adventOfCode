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
  let res1 = (part1("./testInputPart1.txt"), 34241)

  var testsFailed = false
  if res1[0] != res1[1]:
    echo "Part 1 | Expected $1, got $2 instead!" % [$res1[1], $res1[0]]
    testsFailed = true

  let res2 = (part2("./testInputPart2.txt"), 51314)
  if res2[0] != res2[1]:
    echo "Part 2 | Expected $1, got $2 instead!" % [$res2[1], $res2[0]]
    testsFailed = true

  if testsFailed:
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
