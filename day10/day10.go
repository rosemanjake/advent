// Note: Because the go module needs to be in the root of the workspace
// per VSC's launch.json config, when you run Go, you need to
// actually open the containing folder in VSC

package main

import (
	"fmt"
	"os"
	"strings"
)

var brackets = map[rune]rune{
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

var scoredict2 = map[rune]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

// error checking function
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// helper function because there is no in-built contains()
func contains(s []string, str string) bool {
	for _, v := range s {
		if v == str {
			return true
		}
	}

	return false
}

// Does this []rune contain a particular rune?
func r_contains(a []rune, c rune) bool {
	for _, v := range a {
		if v == c {
			return true
		}
	}

	return false
}

func main() {
	data := getInput("day10.txt")
	lines := strings.Split(data, "\n")
	part1solution := fmt.Sprintf("Solution for part 1 = %d", part1(lines))
	fmt.Println(part1solution)
}

func get_badchars(line string) []rune {
	stack := []rune{}
	openers := [4]rune{}
	closers := [4]rune{}

	i := 0
	for k, v := range brackets {
		openers[i] = k
		closers[i] = v
		i++
	}

	for _, char := range line {
		if r_contains(openers[:], char) {
			stack = append(stack, char)
		} else if r_contains(closers[:], char) {
			if char != brackets[stack[len(stack)-1]] {
				return []rune{char}
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}

	return stack
}

func part1(lines []string) int {
	badchars := []rune{}
	for _, line := range lines {
		currbadchars := get_badchars(line)
		if len(currbadchars) == 1 {
			badchars = append(badchars, currbadchars[0])
		} else {
			badchars = append(badchars, currbadchars...)
		}
	}

	total := 0

	for _, char := range badchars {
		switch char {
		case ')':
			total = total + 3
		case ']':
			total = total + 57
		case '}':
			total = total + 1197
		case '>':
			total = total + 25137
		}
	}

	return total
}

func getInput(filename string) string {
	dat, err := os.ReadFile(filename)
	check(err)
	return string(dat)
}
