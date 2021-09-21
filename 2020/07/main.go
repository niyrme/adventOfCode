package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

var (
	bags []*Bag = make([]*Bag, 0)
)

type Bag struct {
	Pattern  string
	Color    string
	Contains map[*Bag]int
}

func getBagFromString(str string) (int, *Bag) {
	// str structure: <count> <pattern> <color> "bags"
	str = strings.TrimSpace(str)
	strSplit := strings.Split(str, " ")

	count, err := strconv.Atoi(strSplit[0])
	if err != nil {
		panic(err.Error())
	}

	var (
		pattern string = strSplit[1]
		color   string = strSplit[2]
	)

	for _, bag := range bags {
		if bag.Pattern == pattern && bag.Color == color {
			return count, bag
		}
	}
	return 0, nil
}

func addBagsFromString(bag *Bag, str string) {
	str = strings.TrimSpace(str)
	str = strings.TrimRight(str, ".")
	if str == "no other bags" {
		return
	}

	if strings.Contains(str, ",") {
		_bags := strings.Split(str, ",")
		for _, _bagStr := range _bags {
			_count, _bag := getBagFromString(_bagStr)
			bag.Contains[_bag] = _count
		}
	} else {
		_count, _bag := getBagFromString(str)
		bag.Contains[_bag] = _count
	}
}

func containsShinyGold(bag *Bag) bool {
	if bag == nil {
		return false
	}

	for {
		if bag.Pattern == "shiny" && bag.Color == "gold" {
			return true
		}
		if len(bag.Contains) > 0 {
			for _bag := range bag.Contains {
				if containsShinyGold(_bag) {
					return true
				}
			}
		}
		return false
	}
}

func countBagsInside(bag *Bag) (count int) {
	count = 0
	for _bagInside, _bagCount := range bag.Contains {
		count += _bagCount
		for i := 0; i < _bagCount; i++ {
			count += countBagsInside(_bagInside)
		}
	}

	return
}

func fromFile(path string) (int, int) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input file! \n%s", err.Error())
	}

	var (
		lines []string = strings.Split(strings.TrimSpace(string(d)), "\n")
	)

	// FIXME: compress into a single loop
	for _, line := range lines {
		line = strings.TrimRight(line, ".")
		lineSplit := strings.SplitN(line, " ", 5)

		/*	lineSplit structure
			0: pattern
			1: color
			2: "bags"
			3: "contain"
			4: "no other bags" | list of bags seperated by ','
		*/

		var (
			pattern string = lineSplit[0]
			color   string = lineSplit[1]
		)

		bags = append(bags, &Bag{
			Pattern:  pattern,
			Color:    color,
			Contains: make(map[*Bag]int),
		})
	}

	for i, line := range lines {
		line = strings.TrimRight(line, ".")
		lineSplit := strings.SplitN(line, " ", 5)

		var (
			contains string = lineSplit[4]
		)

		addBagsFromString(bags[i], contains)
	}

	var (
		shinyGolds int = 0
		bagsInGold int = 0
	)
	for _, bag := range bags {
		if bag.Pattern == "shiny" && bag.Color == "gold" {
			bagsInGold = countBagsInside(bag)
			fmt.Printf("Shiny Gold bag contains %03v other bags\n", bagsInGold)
			continue
		}

		if containsShinyGold(bag) {
			shinyGolds++
		}
	}
	fmt.Printf("Bags that contain at least one shiny gold bag: %v\n", shinyGolds)

	return shinyGolds, bagsInGold
}

func main() {
	fromFile("./input.txt")
}
