package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type pwdPart1 struct {
	polMin, polMax uint8
	key, passw     string
}

func isPwdValidPart1(p pwdPart1) bool {
	c := strings.Count(p.passw, p.key)

	return p.polMin <= uint8(c) && uint8(c) <= p.polMax
}

func part1() {
	f, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalf("Error reading input file! \n%s", err.Error())
	}

	defer f.Close()

	s := bufio.NewScanner(f)

	validPwds := 0

	for s.Scan() {
		var p pwdPart1

		polPasw := strings.Split(s.Text(), ":")
		polKey := strings.Split(polPasw[0], "-")
		keyPos := len(polKey[1]) - 1
		keyStr := polKey[1]

		polMin, err := strconv.Atoi(strings.TrimSpace(polKey[0]))
		if err != nil {
			log.Fatalf("Error converting string to int\n%s", err.Error())
		}
		polMax, err := strconv.Atoi(strings.TrimSpace(polKey[1][0:keyPos]))
		if err != nil {
			log.Fatalf("Error converting string to int\n%s", err.Error())
		}

		p.polMin = uint8(polMin)
		p.polMax = uint8(polMax)
		p.passw = strings.TrimSpace(polPasw[1])
		p.key = strings.TrimSpace(string(keyStr[keyPos]))

		if isPwdValidPart1(p) {
			validPwds++
		}
	}

	log.Printf("Number of valid passwords: %v", validPwds)
}
