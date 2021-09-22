package main

import (
	"errors"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

type OP struct {
	opCode  string
	opValue int
}

var opRegx *regexp.Regexp = regexp.MustCompile(`^(\w\w\w) ([+-]\d+)`)

func getLines(text string) []string {
	return strings.Split(strings.TrimSpace(string(text)), "\n")
}

func getCode(codeLines []string) (code []OP) {
	code = make([]OP, 0)

	for i := range codeLines {
		if matchOp := opRegx.FindStringSubmatch(codeLines[i]); matchOp != nil {
			if value, err := strconv.Atoi(strings.TrimSpace(matchOp[2])); err != nil {
				log.Fatalln(err.Error())
			} else {
				code = append(code, OP{
					opCode:  strings.TrimSpace(matchOp[1]),
					opValue: value,
				})
			}
		}
	}

	return
}

func execOp(ip *int, acc *int, op OP) {
	switch op.opCode {
	case "acc":
		*acc += op.opValue
	case "jmp":
		*ip += op.opValue - 1
	case "nop":
	default:
		log.Fatalf("Unknown opcode '%s'", op.opCode)
	}
}

func solvePart1(path string) (acc int) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input file! \n%s", err.Error())
	}

	var (
		visited map[int]bool = make(map[int]bool)
		code    []OP         = getCode(getLines(string(d)))
	)

	acc = 0
	for ip := 0; ip < len(code); ip++ {
		if visited[ip] {
			return
		} else {
			visited[ip] = true
		}

		execOp(&ip, &acc, code[ip])
	}

	return
}

func run(code []OP, flip int) (int, map[int]bool, error) {
	var (
		acc int = 0
		ip  int = 0

		visited map[int]bool      = make(map[int]bool)
		_flip   map[string]string = map[string]string{"jmp": "nop", "nop": "jmp"}
	)

	for ip < len(code) {
		if visited[ip] {
			break
		} else {
			visited[ip] = true
		}

		var op OP = code[ip]

		if ip == flip {
			op.opCode = _flip[op.opCode]
		}

		switch op.opCode {
		case "acc":
			acc += op.opValue
			ip++
		case "jmp":
			ip += op.opValue
		case "nop":
			ip++
		default:
			log.Fatalf("Unknown opcode '%s'", op.opCode)
		}
	}

	if ip == len(code) {
		return acc, make(map[int]bool), nil
	} else {
		return 0, visited, errors.New("")
	}
}

func solvePart2(path string) (int, error) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input file! \n%s", err.Error())
	}

	var (
		lines []string = strings.Split(strings.TrimSpace(string(d)), "\n")
		code  []OP     = getCode(lines)

		acc     int
		visited map[int]bool
	)

	acc, visited, err = run(code, -1)
	if err == nil {
		return acc, nil
	}

	for i := range visited {
		switch code[i].opCode {
		case "jmp":
			fallthrough
		case "nop":
			acc, _, err = run(code, i)
			if err == nil {
				return acc, nil
			}
		}
	}

	return 0, errors.New("Failed to solve!")
}

func main() {
	log.Println("Testing Part 1")
	if ret := solvePart1("./testInputPart1.txt"); ret != 5 {
		log.Fatalf("Test failed! Expected 5, got %v instead", ret)
	}
	log.Println("Testing Part 2")
	if res, err := solvePart2("./testInputPart2.txt"); err != nil {
		log.Fatalln(err.Error())
	} else if res != 8 {
		log.Fatalf("Test failed! Expected 8, got %v instead", res)
	}

	log.Printf("Part 1: %v", solvePart1("./input.txt"))
	if res, err := solvePart2("./input.txt"); err != nil {
		log.Fatalln(err.Error())
	} else {
		log.Printf("Part 2: %v", res)
	}
}
