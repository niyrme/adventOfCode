package main

import (
	"strings"
)

func countAnswersPart1(answers string) int {
	ans := map[string]bool{}
	for _, a := range answers {
		answer := strings.ToLower(string(a))
		if strings.Count("abcdefghijklmnopqrstuvwxyz", answer) != 1 {
			continue
		}

		if !ans[answer] {
			ans[answer] = true
		}
	}

	return len(ans)
}
