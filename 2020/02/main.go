package main

func xor(x, y bool) bool {
	return (x || y) && !(x && y)
}

func main() {
	part1()
	part2()
}
