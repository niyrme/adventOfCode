import std/tables
from sequtils import zip
from strutils import parseInt, split

let DIRECTIONS = {'U': (x: 0, y: 1), 'R': (x: 1, y: 0), 'D': (x: 0, y: -1), 'L': (x: -1, y: 0)}.newTable

type
  Direction = tuple[dir: char, amnt: int]
  Pos = tuple[x, y: int]

#       y
#       ^
#       |
# -x <--+--> x
#       |
#       v
#      -y

proc manhattanDistance(a: openArray[int], b: openArray[int]): int =
  assert a.len == b.len
  for e in zip(a, b):
    result += abs(e[0] - e[1])

proc getVisited(directions: seq[Direction]): Table[Pos, bool] =
  result = initTable[Pos, bool]()
  var currentPos: Pos = (x: 0, y: 0)
  for dir in directions:
    let d = DIRECTIONS[dir.dir]
    for _ in 0..<dir.amnt:
      currentPos.x += d.x
      currentPos.y += d.y
      result[currentPos] = true

proc getIntersections(visited1, visited2: Table[Pos, bool]): seq[Pos] =
  for k, _ in visited1:
    if k in visited2:
      result.add(k)

proc part1(path: string): int =
  var
    f: File
    directions1: seq[Direction]
    directions2: seq[Direction]
  if open(f, path, fmRead):
    try:
      let
        l1 = split(f.readLine(), ',')
        l2 = split(f.readLine(), ',')
      for dir_zip in zip(l1, l2):
        let
          d0 = dir_zip[0]
          d1 = dir_zip[1]
        directions1.add((dir: d0[0], amnt: parseInt(d0[1..^1])))
        directions2.add((dir: d1[0], amnt: parseInt(d1[1..^1])))
    except EOFError:
      discard
    finally:
      close(f)

  let
    vis1 = getVisited(directions1)
    vis2 = getVisited(directions2)

    intersections = getIntersections(vis1, vis2)

  var smallest: int = int(high(BiggestInt))
  for inter in intersections:
    let dist = manhattanDistance([0, 0], [inter.x, inter.y])
    if dist < smallest:
      smallest = dist

  return smallest

proc toFirstIntersection(dir1, dir2: seq[Direction]): int =
  var
    currentPos: Pos = (x: 0, y: 0)
    visited = initTable[Pos, int]()
    step: int = 0
    intersections: seq[int]

  for dir in dir1:
    let d = DIRECTIONS[dir.dir]
    for _ in 0..<dir.amnt:
      step += 1
      currentPos.x += d.x
      currentPos.y += d.y
      var v = step
      if currentPos in visited:
        v = min(visited[currentPos], step)
      visited[currentPos] = v

  step = 0
  currentPos = (x: 0, y: 0)
  for dir in dir2:
    let d = DIRECTIONS[dir.dir]
    for _ in 0..<dir.amnt:
      step += 1
      currentPos.x += d.x
      currentPos.y += d.y
      if currentPos in visited:
        intersections.add(visited[currentPos] + step)

  return min(intersections)

proc part2(path: string): int =
  var
    f: File
    directions1: seq[Direction]
    directions2: seq[Direction]
  if open(f, path, fmRead):
    try:
      let
        l1 = split(f.readLine(), ',')
        l2 = split(f.readLine(), ',')
      for dir_zip in zip(l1, l2):
        let
          d0 = dir_zip[0]
          d1 = dir_zip[1]
        directions1.add((dir: d0[0], amnt: parseInt(d0[1..^1])))
        directions2.add((dir: d1[0], amnt: parseInt(d1[1..^1])))
    except EOFError:
      discard
    finally:
      close(f)

  return toFirstIntersection(directions1, directions2)

proc main(): int =
  let res1 = part1("./testInputPart1.txt")
  if res1 != 159:
    echo "Expected 159, got ", res1, " instead!"
    return 1

  let res2 = part2("./testInputPart2.txt")
  if res2 != 410:
    echo "Expected 410, got ", res2, " instead!"
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
