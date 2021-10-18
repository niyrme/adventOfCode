from math import floor
from strutils import parseInt

proc calcFuel(fuel: int): int =
  let c = int(floor(float(fuel) / 3) - 2)
  if c > 0:
    result = c + calcFuel(c)
  else:
    result = 0

proc part1(path: string): int =
  var f: File
  if open(f, path, fmRead):
    try:
      while true:
        result += int(floor(float(parseInt(f.readLine())) / 3) - 2)
    except EOFError:
      discard
    finally:
      close(f)
  return result

proc part2(path: string): int =
  var f: File
  if open(f, path, fmRead):
    try:
      while true:
        result += calcFuel(parseInt(f.readLine()))
    except EOFError:
      discard
    finally:
      close(f)
  return result

proc main(): int =
  let res1 = part1("./testInputPart1.txt")

  if res1 != 34241:
    echo "Expected 34241, got ", res1, " instead!"
    return 1

  let res2 = part2("./testInputPart2.txt")
  if res2 != 51314:
    echo "Expected 51314, got ", res2, " instead!"
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
