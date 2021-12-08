package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse(instr string) []string {
	return strings.Split(strings.TrimSpace(instr), "\n")
}

func part1(input []string) int {
	var gamma, epsi []string
	nBits := len(input[0])
	for i := 0; i < nBits; i++ {
		var zeros, ones int
		for j := 0; j < len(input); j++ {
			switch string(input[j][i]) {
			case "0":
				zeros += 1
			case "1":
				ones += 1
			}
		}
		if ones > zeros {
			epsi = append(epsi, "0")
			gamma = append(gamma, "1")
		} else {
			epsi = append(epsi, "1")
			gamma = append(gamma, "0")
		}
	}

	epsiInt, _ := strconv.ParseInt(strings.Join(epsi, ""), 2, 0)
	gammaInt, _ := strconv.ParseInt(strings.Join(gamma, ""), 2, 0)

	return int(epsiInt * gammaInt)
}

func main() {
	f, _ := os.ReadFile("./day_3/input.txt")
	input := parse(string(f))
	fmt.Println("Part 1:", part1(input))
}
