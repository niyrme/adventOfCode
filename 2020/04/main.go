package main

import (
	"io/ioutil"
	"log"
	"strings"
)

var requiredFields []string = []string{
	"byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid",
	//"cid",
}

func main() {
	var (
		validPassports int = 0
		vldPassports   []string
		passports      []string
	)

	d, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	passports = strings.Split(string(d), "\n")
	passports = append(passports, "\n")

	pass := ""
	for _, passport := range passports {
		pass += strings.TrimSpace(passport) + " "

		if strings.TrimSpace(passport) == "" {
			if validatePassportPart1(pass) {
				validPassports++
				vldPassports = append(vldPassports, pass)
			}
			pass = ""
		}
	}

	log.Printf("Number of valid passports in part 1: %v", validPassports)

	validPassports = 0
	for _, p := range vldPassports {
		if validatePassportPart2(strings.Split(p, " ")) {
			validPassports++
		}
	}

	log.Printf("Number of valid passports in part 2: %v", validPassports)
}
