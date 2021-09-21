package main

import (
	"strings"
)

func countAnswersPart2(answers string) (total int) {
	answ := strings.Split(strings.ToLower(answers), "|")

	if len(answ) == 0 {
		return 0
	} else if len(answ) == 1 {
		return 1
	}

	total = 0
	occurrences := map[string]int{}

	// "Trim" slice (remove trailing empty elements)
	answ = removeEmpty(answ)

	for _, answer := range answ {
		for _, char := range answer {
			occurrences[string(char)]++
		}
	}

	for _, occ := range occurrences {
		if occ == len(answ) {
			total++
		}
	}

	//log.Printf("total: %v | answ: %v / len(answ): %v | occurrences: %v", total, answ, len(answ), occurrences)

	return
}
