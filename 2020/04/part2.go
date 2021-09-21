package main

import (
	"log"
	"strconv"
	"strings"
)

func validatePassportPart2(passport []string) (valid bool) {
	valid = true

	// Check if passport contains each field
	for _, rF := range requiredFields {
		if strings.Count(strings.Join(passport, " "), rF) < 1 {
			return false
		}
	}

	for _, fields := range passport {
		// fields is one passport field. ex: 'byr:2000'
		fields = strings.TrimSpace(fields)

		if fields == "" {
			continue
		}
		if !valid {
			return
		}

		// check if a field is empty
		if strings.TrimSpace(strings.Split(fields, ":")[0]) == "" {
			return false
		}
		// check if value of a field is empty
		if strings.TrimSpace(strings.Split(fields, ":")[1]) == "" {
			return false
		}

		data := strings.Split(fields, ":")

		// Check each data
		// data[0] == field name
		// data[1] == field value
		switch data[0] {
		case "byr":
			fallthrough
		case "iyr":
			fallthrough
		case "eyr":
			// check byr, iyr or eyr
			if !checkYrs(data[0], data[1]) {
				valid = false
			}
		case "hgt":
			if !checkHgt(data[1]) {
				valid = false
			}
		case "hcl":
			if !checkHcl(data[1]) {
				valid = false
			}
		case "ecl":
			if !checkEcl(data[1]) {
				valid = false
			}
		case "pid":
			if len(strings.TrimSpace(data[1])) != 9 {
				valid = false
			}
		}
	}

	return
}

func find(slice []string, value string) bool {
	for _, v := range slice {
		if v == value {
			return true
		}
	}
	return false
}

func checkYrs(field, value string) (valid bool) {
	value = strings.TrimSpace(value)
	valid = false

	v, err := strconv.Atoi(value)
	if err != nil {
		log.Fatalf("Error converting value of '%v' to int! \n%s", field, err.Error())
	}

	switch field {
	case "byr":
		valid = v >= 1920 && v <= 2002
	case "iyr":
		valid = v >= 2010 && v <= 2020
	case "eyr":
		valid = v >= 2020 && v <= 2030
	}

	return
}
func checkHgt(value string) (valid bool) {
	value = strings.TrimSpace(value)
	valid = false

	unit := value[len(value)-2:] // determine wether 'hgt' is in 'cm' or 'in'
	if unit != "cm" && unit != "in" {
		return false
	}

	v, err := strconv.Atoi(value[:(len(value) - 2)])
	if err != nil {
		log.Fatalf("Error converting value of 'hgt' to int! \n%s", err.Error())
	}

	switch unit {
	case "cm":
		valid = v >= 150 && v <= 193
	case "in":
		valid = v >= 59 && v <= 76
	}
	return
}
func checkHcl(value string) bool {
	value = strings.TrimSpace(value)

	if value[0] == '#' && len(value[1:]) == 6 {
		for _, v := range value[1:] {
			if !find(strings.Split("0123456789abcdefABCDEF", ""), string(v)) {
				return false
			}
		}
		return true
	}
	return false
}
func checkEcl(value string) (valid bool) {
	value = strings.TrimSpace(value)
	valid = false

	switch value {
	case "amb":
		valid = true
	case "blu":
		valid = true
	case "brn":
		valid = true
	case "gry":
		valid = true
	case "grn":
		valid = true
	case "hzl":
		valid = true
	case "oth":
		valid = true
	}
	return
}
