package main

import (
	"io/ioutil"
	"log"
	"strings"
)

func solve(path string) (ret interface{}) {
	d, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatalf("Error opening input.txt!\n%s", err.Error())
	}

	var lines []string = strings.Split(strings.TrimSpace(string(d)), "\n")

	return
}

func main() {
	var (
		expected1 interface{}
		expected2 interface{}
	)

	log.Println("Testing Part 1")
	if ret := solve("./testInputPart1.txt"); ret != expected1 {
		log.Fatalf("Test Failed! Expected %v, got %v instead", expected1, ret)
	}
	log.Println("Testing Part 2")
	if ret := solve("./testInputPart1.txt"); ret != expected2 {
		log.Fatalf("Test Failed! Expected %v, got %v instead", expected2, ret)
	}
}
