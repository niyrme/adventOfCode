from strutils import `%`

proc parseFile(path: string): seq[string] =
  var f: File
  if open(f, path, fmRead):
    try:
      while true:
        result.add(f.readLine())
    except EOFError:
      discard
    finally:
      close(f)

proc part1(path: string): int =
  discard

proc part2(path: string): int =
  discard

proc main(): int =
  var testsFailed = false
  let res1 = (part1("./testInputPart1.txt"), nil)
  if res1[0] != res1[1]:
    echo "Part 1 | Expected $1, got $2 instead!" % [$res1[0], $res1[1]]
    testsFailed = true

  let res2 = (part2("./testInputPart2.txt"), nil)
  if res2[0] != res2[1]:
    echo "Part 2 | Expected $1, got $2 instead!" % [$res2[0], $res2[1]]
    testsFailed = true

  if testsFailed:
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
