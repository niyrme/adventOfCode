package main

import (
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func part1(input interface{}) interface{} {}

func part2(input interface{}) interface{} {}

func solve(part int, path string) interface{} {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var lines []string = strings.Split(strings.TrimSpace(string(d)), "\n")

	return map[int]func(interface{}) interface{}{
		1: part1,
		2: part2,
	}[part](lines)
}

type test struct {
	part     int
	id       int
	input    []interface{}
	expected interface{}
	f        func(interface{}) interface{}
}

func _main() int {
	var tests []test = []test{
		{1, 1, []interface{}{}, nil, part1},
		{2, 1, []interface{}{}, nil, part2},
	}

	testsFailed := false

	for _, test := range tests {
		if ret := test.f(test.input); ret != test.expected {
			log.Println("Part %d | Test %d failed | Expected %v, got %v", test.part, test.id, test.expected, ret)
			testsFailed = true
		}
	}

	if testsFailed {
		return 1
	} else {
		return 0
	}
}

func main() {
	os.Exit(_main())
}
