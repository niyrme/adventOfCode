package main

import (
	"io/ioutil"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func part1(adapters []int) int {
	jolts := make(map[int]int)
	jolts[1] = 0
	jolts[2] = 0
	jolts[3] = 1

	currentJolts := 0

	sort.Ints(adapters)

	for _, adapter := range adapters {
		jolts[adapter-currentJolts] += 1
		currentJolts = adapter
	}

	return jolts[1] * jolts[3]
}

func streak(n int) int {
	if n < 2 {
		log.Fatalln("n < 2")
	}
	if v, ok := map[int]int{2: 1, 3: 2, 4: 4}[n]; ok {
		return v
	} else {
		return streak(n-1) + streak(n-2) + streak(n-3)
	}
}

func part2(adapters []int) (combinations int) {
	combinations = 1

	var (
		previous int = 0
		_streak  int = 1
	)

	sort.Ints(adapters)

	for _, adapter := range adapters {
		if adapter == (previous + 1) {
			_streak += 1
		} else if _streak > 1 {
			combinations = combinations * streak(_streak)
			_streak = 1
		}
		previous = adapter
	}

	if _streak > 1 {
		combinations = combinations * streak(_streak)
	}

	return
}

func solve(part int, path string) int {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var (
		lines    []string = strings.Split(strings.TrimSpace(string(d)), "\n")
		adapters []int
	)

	for _, line := range lines {
		if n, err := strconv.Atoi(line); err != nil {
			log.Fatalln(err.Error())
		} else {
			adapters = append(adapters, n)
		}
	}

	return []func([]int) int{part1, part2}[part-1](adapters)
}

type test struct {
	part     int
	id       int
	input    []int
	f        func([]int) int
	expected int
}

func _main() int {
	var tests []test = []test{
		{1, 1, []int{16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4}, part1, 35},
		{1, 2, []int{28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3}, part1, 220},
		{2, 1, []int{16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4}, part2, 8},
		{2, 2, []int{28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3}, part2, 19208},
	}

	testsFailed := false

	for _, test := range tests {
		if ret := test.f(test.input); ret != test.expected {
			log.Printf("Part %d | Test %d failed | Expected %d, got %d\n", test.part, test.id, test.expected, ret)
			testsFailed = true
		}
	}

	if testsFailed {
		return 1
	} else {
		log.Printf("Part 1: %d", solve(1, "./input.txt"))
		log.Printf("Part 2: %d", solve(2, "./input.txt"))
		return 0
	}
}

func main() {
	os.Exit(_main())
}
