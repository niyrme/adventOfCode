package main

import (
	"bufio"
	"log"
	"os"
	"sort"
)

func main() {
	f, err := os.Open("./input.txt")
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}
	defer f.Close()
	s := bufio.NewScanner(f)

	var (
		highestSeatID int = -1
		userSeatID    int = -1
		seatIDs       []int
	)

	for s.Scan() {
		var (
			rMin, rMax int = 0, 127
			cMin, cMax int = 0, 7
		)
		for _, c := range s.Text() {
			switch string(c) {
			case "F":
				rMax -= (rMax - rMin + 1) / 2
			case "B":
				rMin += (rMax - rMin + 1) / 2
			case "L":
				cMax -= (cMax - cMin + 1) / 2
			case "R":
				cMin += (cMax - cMin + 1) / 2
			}
		}

		if rMin != rMax || cMin != cMax {
			log.Printf("Smn wrong!\nrMin: %v | rMax: %v\ncMin: %v | cMax: %v", rMin, rMax, cMin, cMax)
		}

		seatRow, seatCol := rMin, cMin
		seatID := seatRow*8 + seatCol

		seatIDs = append(seatIDs, seatID)

		if seatID > highestSeatID {
			highestSeatID = seatID
		}
	}

	log.Printf("Highest possible seatID is: %v", highestSeatID)

	sort.Ints(seatIDs)

	i := 1
	for range seatIDs {
		if seatIDs[i+1]-seatIDs[i] != 1 {
			userSeatID = seatIDs[i] + 1
			break
		}
		i++
	}

	log.Printf("Users seatID is: %v", userSeatID)
}
