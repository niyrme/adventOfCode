package main

import (
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func part1(path string, preamble int) int {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var (
		lines   []string = strings.Split(strings.TrimSpace(string(d)), "\n")
		numbers []int
	)

	for _, line := range lines {
		if num, err := strconv.Atoi(line); err != nil {
			log.Fatalln(err.Error())
		} else {
			numbers = append(numbers, num)
		}
	}

	for i := range numbers {
		if i < preamble {
			continue
		}

		lastX := numbers[i-preamble : i]

		fits := false
	outer:
		for xi, x := range lastX {
			for yi, y := range lastX {
				if (x+y == numbers[i]) && (xi != yi) {
					fits = true
					break outer
				}
			}
		}

		if !fits {
			return numbers[i]
		}
	}

	log.Fatalln("UNREACHABLE")
	return -1
}

func minMax(arr []int) (min, max int) {
	min = arr[0]
	max = arr[0]

	for _, v := range arr {
		if v > max {
			max = v
		}
		if v < min {
			min = v
		}
	}

	return
}

func sum(arr []int) (sum int) {
	for _, v := range arr {
		sum += v
	}
	return
}

func part2(path string, invalid int) (weakness int) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var (
		lines   []string = strings.Split(strings.TrimSpace(string(d)), "\n")
		numbers []int
	)

	for _, line := range lines {
		if num, err := strconv.Atoi(line); err != nil {
			log.Fatalln(err.Error())
		} else {
			numbers = append(numbers, num)
		}
	}

outer:
	for i := range numbers {
		var nums []int
		nums = append(nums, numbers[i])
		j := 1

		for {
			if sum(nums) == invalid {
				min, max := minMax(nums)
				return min + max
			} else if sum(nums) > invalid {
				continue outer
			} else {
				nums = append(nums, numbers[i+j])
				j++
			}
		}
	}

	log.Fatalln("UNREACHABLE")
	return -1
}

type test struct {
	part     int
	id       int
	path     string
	expected int
	preamble int
	f        func(string, int) int
}

func _main() int {
	testsFailed := false
	if res := part1("./testInput.txt", 5); res != 127 {
		log.Printf("Part 1 | Test failed | Expected 127, got %v\n", res)
		testsFailed = true
	}
	if res := part2("./testInput.txt", 127); res != 62 {
		log.Printf("Part 2 | Test failed | Expected 62, got %v\n", res)
		testsFailed = true
	}

	if testsFailed {
		return 1
	} else {
		invalid := part1("./input.txt", 25)
		log.Printf("Part 1: %d\n", invalid)
		log.Printf("Part 2: %d\n", part2("./input.txt", invalid))
		return 0
	}
}

func main() {
	os.Exit(_main())
}
