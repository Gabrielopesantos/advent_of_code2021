package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// file, _ := os.Open("./day_01/input.txt")
// defer file.Close()

// scanner := bufio.NewScanner(file)
// var records []int
// for scanner.Scan() {
// 	n, _ := strconv.Atoi(scanner.Text())
// 	records = append(records, n)

func parse(instr string) ([]int, error) {
	var out []int
	instr = strings.TrimSpace(instr)
	for _, val := range strings.Split(instr, "\n") {
		n, err := strconv.Atoi(val)
		if err != nil {
			return nil, err
		}
		out = append(out, n)
	}
	return out, nil
}

func solve(input []int, wSize int) int {
	count := 0

	for i := wSize; i < len(input); i++ {
		if input[i] > input[i-wSize] {
			count += 1
		}
	}

	return count
}

func main() {
	f, _ := os.ReadFile("./day_1/input.txt")
	input, _ := parse(string(f))

	fmt.Println("Part 1:", solve(input, 1))
	fmt.Println("Part 2:", solve(input, 3))
}
