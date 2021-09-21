package main

import (
	"strings"
)

func validatePassportPart1(passport string) bool {
	isValid := true

	for _, field := range requiredFields {
		c := strings.Count(passport, field)
		if c != 1 {
			isValid = false
		}
	}

	return isValid
}
