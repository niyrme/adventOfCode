package main

import (
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func solve(path string) (ret interface{}) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var lines []string = strings.Split(strings.TrimSpace(string(d)), "\n")

	return
}

type test struct {
	part     int
	id       int
	path     string
	expected interface{}
}

func _main() int {
	var tests []test = []test{
		{1, 1, "./testInputPart1.txt", nil},
		{2, 1, "./testInputPart2.txt", nil},
	}

	testsFailed := false

	for _, test := range tests {
		if ret := solve(test.path); ret != test.expected {
			log.Println("Part %v | Test %v failed | Expected %v, got %v", test.part, test.id, test.expected, ret)
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
