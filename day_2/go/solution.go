package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	FORWARD = "forward"
	UP      = "up"
	DOWN    = "down"
)

type command struct {
	Action string
	Number int
}

func parse(instr string) []*command {
	var out []*command
	instr = strings.TrimSpace(instr)
	for _, c := range strings.Split(instr, "\n") {
		r := strings.Split(c, " ")
		n, _ := strconv.Atoi(r[1])
		out = append(out, &command{Action: r[0], Number: n})
	}
	return out
}

func part1(commands []*command) int {
	var h, d int

	for _, c := range commands {
		switch c.Action {
		case FORWARD:
			h += c.Number
		case DOWN:
			d += c.Number
		case UP:
			d -= c.Number
		}
	}

	return h * d
}

func part2(commands []*command) int {
	var h, d, a int

	for _, c := range commands {
		switch c.Action {
		case FORWARD:
			h += c.Number
			d += c.Number * a
		case DOWN:
			a += c.Number
		case UP:
			a -= c.Number
		}
	}

	return h * d
}

func main() {
	f, _ := os.ReadFile("./day_2/input.txt")
	input := parse(string(f))
	fmt.Println("Part 1:", part1(input))
	fmt.Println("Part 2:", part2(input))
}
