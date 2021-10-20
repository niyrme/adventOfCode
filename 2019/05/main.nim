from strutils import align, parseInt, split
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
      echo "Unknown mode ", mode, "!"
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

        # echo "Param 1 : ", param1
        # echo "Param 2 : ", param2
        # echo "Param 3 : ", param3

        var value: int
        if DE == 1:
          # echo "ADD ", param1, " + ", param2, " -> ", param3
          value = param1 + param2
        elif DE == 2:
          # echo "MUL ", param1, " * ", param2, " -> ", param3
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
        echo "Unsupported OP-code at index ", pc, ": ", DE
        quit(1)

  quit(2)

proc part1(path: string): int =
  var
    f: File
    instructions: seq[int]
  if open(f, path, fmRead):
    try:
      for instr in split(f.readLine(), ','):
        instructions.add(parseInt(instr))
    except EOFError:
      discard
    finally:
      close(f)

  # hard coded parameter
  var inp: seq[int] = @[1]
  return loopInput(instructions, inp)

proc part2(path: string): int =
  var
    f: File
    instructions: seq[int]
  if open(f, path, fmRead):
    try:
      for instr in split(f.readLine(), ','):
        instructions.add(parseInt(instr))
    except EOFError:
      discard
    finally:
      close(f)

  # hard coded parameter
  var inp: seq[int] = @[5]
  return loopInput(instructions, inp)

proc main(): int =
  # Tests
  var testsFailed = false
  for test in [(@[1101, 100, -1, 4, 0], 1101, 1), (@[1002, 4, 3, 4, 33], 1002, 2)]:
    var inp: seq[int]
    let ret = loopInput(test[0], inp)
    if ret != test[1]:
      echo "Part 1 | Test ", test[2], " failed, expected ", test[1], " got ", ret
      testsFailed = true

  if testsFailed:
    return 1

  echo "Part 1 -> "
  discard part1("./input.txt")
  echo "Part 2 -> "
  discard part2("./input.txt")
  return 0

quit(main())
