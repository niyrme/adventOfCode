from strutils import `%`, align, parseInt, split
from system import pop

proc loopInput(instructions: seq[int], params: var seq[int]): int =
  var
    pc = 0

    i = instructions

  proc param(n, mode: int): int=
    if mode == 0:
      return i[i[pc + n]]
    elif mode == 1:
      return i[pc + n]
    else:
      echo "Unknown mode $1!" % $mode
      quit(1)

  #  1 : ADD | `i[[pos+1]] * i[[pos+2]] -> i[pos+3]`
  #  2 : MUL | `i[[pos+1]] * i[[pos+2]] -> i[pos+3]`
  #  3 : IN  | store at `i[pos+1]`
  #  4 : OUT | output from `i[pos+1]`
  # 99 : RET | return `i[0]`
  #  _ : ERR | panic!

  # ABCDE
  #  1002
  # DE - two-digit opcode,      02 == opcode 2
  #  C - mode of 1st parameter,  0 == position mode
  #  B - mode of 2nd parameter,  1 == immediate mode
  #  A - mode of 3rd parameter,  0 == position mode

  while true:
    let
      strCode = align($i[pc], 5, '0')

      A: int = parseInt($strCode[0])
      B: int = parseInt($strCode[1])
      C: int = parseInt($strCode[2])
      DE: int = parseInt(strCode[3..4])

    var
      param1: int
      param2: int
      param3: int

    case DE:
      of 1, 2:
        param1 = param(1, C)
        param2 = param(2, B)
        param3 = param(3, 1)

        var value: int
        if DE == 1:
          value = param1 + param2
        elif DE == 2:
          value = param1 * param2

        i[param3] = value
        pc += 4
      of 3:
        param1 = i[pc + 1]

        i[param1] = pop(params)

        pc += 2
      of 4:
        echo "OUT ", param(1, C)
        pc += 2
      of 5, 6:
        param1 = param(1, C)
        param2 = param(2, B)

        if
          (DE == 5 and param1 != 0) or
          (DE == 6 and param1 == 0):
          pc = param2
        else:
          pc += 3
      of 7, 8:
        param1 = param(1, C)
        param2 = param(2, B)

        var value = 0
        if
          (DE == 7 and param1 < param2) or
          (DE == 8 and param1 == param2):
          value = 1

        i[i[pc + 3]] = value

        pc += 4
      of 99:
        return i[0]
      else:
        echo "Unsupported OP-code at index $1: $2" % [$pc, $DE]
        quit(1)

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
  let instructions = parseFile(path)

  # hard coded parameter
  var inp: seq[int] = @[1]
  return loopInput(instructions, inp)

proc part2(path: string): int =
  let instructions = parseFile(path)

  # hard coded parameter
  var inp: seq[int] = @[5]
  return loopInput(instructions, inp)

proc main(): int =
  # Tests
  var testsFailed = false
  for test in [
    (1, 1, @[1101, 100, -1, 4, 0], 1101),
    (1, 2, @[1002, 4, 3, 4, 33], 1002),
  ]:
    var inp: seq[int]
    let res = loopInput(test[2], inp)
    if res != test[3]:
      echo "Part $1 | Test $2 failed | Expected $3, got $4" % [$test[0], $test[1], $test[3], $res]
      testsFailed = true

  if testsFailed:
    return 1

  echo "Part 1 -> "
  discard part1("./input.txt")
  echo "Part 2 -> "
  discard part2("./input.txt")
  return 0

quit(main())
