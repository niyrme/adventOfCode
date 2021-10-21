from strutils import `%`, count

proc checkPassword1(passwd: int): bool =
  let pwd = $passwd
  if pwd.len != 6:
    return false

  var containsDouble = false
  for digit in '0'..'9':
    if count(pwd, digit) > 1:
      containsDouble = true
      break
  if not containsDouble:
    return false

  var previous = '0'
  for digit in pwd:
    if digit < previous:
      return false
    previous = digit

  return true

# cheated! new rule has very bad wording
proc checkPassword2(passwd: int): bool =
  let pwd = $passwd
  if pwd.len != 6:
    return false

  var doubles: seq[int]
  for digit in '0'..'9':
    let c = count(pwd, digit)
    if c > 1:
      doubles.add(c)
  if not (2 in doubles):
    return false

  var previous = '0'
  for digit in pwd:
    if digit < previous:
      return false
    previous = digit

  return true

proc part1(): int =
  for passwd in 245182..790572:
    if checkPassword1(passwd):
      result += 1

proc part2(): int =
  for passwd in 245182..790572:
    if checkPassword2(passwd):
      result += 1

proc main(): int =
  # Tests
  var testsFailed = false
  for test in [(111111, true, 1), (223450, false, 2), (123789, false, 3)]:
    if checkPassword1(test[0]) != test[1]:
      echo "Part 1 | Test $1 Failed | Expected $2, got $3" % [$test[2], $test[1], $test[0]]
      testsFailed = true
  for test in [(112233, true, 1), (123444, false, 2), (111122, true, 3)]:
    if checkPassword2(test[0]) != test[1]:
      echo "Part 2 | Test $1 Failed | Expected $2, got $3" % [$test[2], $test[1], $test[0]]
      testsFailed = true

  if testsFailed:
    return 1
  echo "Part 1 -> ", part1()
  echo "Part 2 -> ", part2()
  return 0

quit(main())
