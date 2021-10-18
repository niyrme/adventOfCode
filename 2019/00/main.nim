proc part1(path: string): int =
  discard

proc part2(path: string): int =
  discard

proc main(): int =
  let res1 = part1("./testInputPart1.txt")
  if res1 != nil:
    echo "Expected nil, got ", res1, " instead!"
    return 1

  let res2 = part2("./testInputPart2.txt")
  if res2 != nil:
    echo "Expected nil, got ", res2, " instead!"
    return 1

  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
