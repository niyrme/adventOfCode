package main

import (
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	d, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		log.Fatalf("Error opening input file! \n%s", err.Error())
	}

	var (
		totalP1 int = 0
		totalP2 int = 0
		answers []string
	)

	answers = strings.Split(string(d), "\n")
	answers = append(answers, "\n")

	ans := ""
	for _, answer := range answers {
		ans += strings.TrimSpace(answer) + "|"

		if strings.TrimSpace(answer) == "" {
			totalP1 += countAnswersPart1(ans)
			totalP2 += countAnswersPart2(ans)
			ans = ""
		}
	}

	log.Printf("Sum of questions where anyone answered with 'yes' is: %v", totalP1)
	log.Printf("Sum of questions where everyone answered with 'yes' is: %v", totalP2)
}

func removeEmpty(slice []string) []string {
	var out []string
	for _, item := range slice {
		i := strings.TrimSpace(item)
		if i != "" {
			out = append(out, i)
		}
	}

	return out
}
