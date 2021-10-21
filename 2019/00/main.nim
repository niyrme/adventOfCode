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

  for test in [
    (1, 1, part1, "./testInputPart1.txt", 0),
    (2, 1, part2, "./testInputPart2.txt", 0),
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
