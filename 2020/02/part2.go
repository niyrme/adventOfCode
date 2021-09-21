package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type pwdPart2 struct {
	pol1, pol2 uint8
	key, passw string
}

func isPwdValidPart2(p pwdPart2) bool {
	bool1 := string(p.passw[p.pol1-1]) == p.key
	bool2 := string(p.passw[p.pol2-1]) == p.key

	return xor(bool1, bool2)
}

func part2() {
	f, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalf("Error reading input file! \n%s", err.Error())
	}

	defer f.Close()

	s := bufio.NewScanner(f)

	validPwds := 0

	for s.Scan() {
		var p pwdPart2

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

		p.pol1 = uint8(polMin)
		p.pol2 = uint8(polMax)
		p.passw = strings.TrimSpace(polPasw[1])
		p.key = strings.TrimSpace(string(keyStr[keyPos]))

		if isPwdValidPart2(p) {
			validPwds++
		}
	}

	log.Printf("Number of valid passwords: %v", validPwds)
}
