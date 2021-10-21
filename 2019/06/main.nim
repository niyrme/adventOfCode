import std/tables
from std/sets import `*`, toHashSet
from strutils import `%`, repeat, strip, split

type Orbit = tuple[com, body: string]

proc parseFile(path: string): seq[Orbit] =
  var
    f: File
  if open(f, path, fmRead):
    try:
      while true:
        let
          o = split(f.readLine(), ")")
          com = strip(o[0])
          body = strip(o[1])
        result.add((com, body))
    except EOFError:
      discard
    finally:
      close(f)

proc part1(path: string): int =
  var orbits = initTable[string, string]()
  orbits["COM"] = ""
  for orbit in parseFile(path):
    orbits[orbit[1]] = orbit[0]

  for v in orbits.values:
    var parent = v
    while parent != "":
      result += 1
      parent = orbits[parent]

proc part2(path: string): int =
  var orbits = initTable[string, string]()
  orbits["COM"] = ""
  for orbit in parseFile(path):
    orbits[orbit[1]] = orbit[0]

  var
    youHops = initTable[string, int]()
    orbit = orbits["YOU"]
    i = 0
  while orbit != "COM":
    youHops[orbit] = i
    i += 1
    orbit = orbits[orbit]

  var santaHops = initTable[string, int]()
  orbit = orbits["SAN"]
  i = 0
  while orbit != "COM":
    santaHops[orbit] = i
    i += 1
    orbit = orbits[orbit]

  var
    paths: seq[int]
    commons: seq[string]
  for k in youHops.keys:
    if santaHops.hasKey(k):
      commons.add(k)

  for k in commons:
    paths.add(youHops[k] + santaHops[k])

  return min(paths)

proc main(): int =
  var testsFailed = false
  for test in [
    (1, 1, part1, "./testInputPart1.txt", 42),
    (2, 1, part2, "./testInputPart2.txt", 4),
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
