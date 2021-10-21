from strutils import `%`, parseInt, split

proc loopInput(instructions: seq[int]): int =
  var
    i = instructions
    pos = 0

  #  1 : add
  #  2 : multiply
  # 99 : exit/return
  #  _ : error
  while true:
    let
      code = i[pos]

      i1 = i[i[pos + 1]]
      i2 = i[i[pos + 2]]

      outPos = i[pos + 3]

    case code:
      of 1:
        i[outPos] = i1 + i2
      of 2:
        i[outPos] = i1 * i2
      of 99:
        return i[0]
      else:
        echo "Unsupported OP-code at index $1: $2" % [$pos, $code]
        quit(1)

    pos += 4

  quit(2)

proc parseFile(path: string): seq[int] =
  var f: File
  if open(f, path, fmRead):
    try:
      for instr in split(f.readLine(), ','):
        result.add(parseInt(instr))
    except EOFError:
      discard
    finally:
      close(f)

proc part1(path: string): int =
  var instructions = parseFile(path)

  instructions[1] = 12
  instructions[2] = 2
  return loopInput(instructions)

proc part2(path: string): int =
  let target = 19690720
  var instructions = parseFile(path)

  for noun in 0..<100:
    for verb in 0..<100:
      instructions[1] = noun
      instructions[2] = verb

      if loopInput(instructions) == target:
        return 100 * noun + verb

  echo "Failed to compute part 2\n"
  quit(1)

proc main(): int =
  echo "Part 1 -> ", part1("./input.txt")
  echo "Part 2 -> ", part2("./input.txt")
  return 0

quit(main())
