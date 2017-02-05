package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	solve(bufio.NewScanner(os.Stdin))
}

func solve(src *bufio.Scanner) {
	src.Scan()
	t, _ := strconv.Atoi(src.Text())
	for i := 1; i < t+1; i++ {
		src.Scan()
		lxLine := src.Text()
		lx := strings.Split(lxLine, " ")

		l, _ := strconv.Atoi(lx[0])
		x, _ := strconv.Atoi(lx[1])

		src.Scan()
		seq := strings.TrimSpace(src.Text())
		result := solveCase(l, x, seq)

		fmt.Println(fmt.Sprintf("Case #%d: %s", i, result))
	}
}

var TABLE = map[string]map[string]string{
	"1": {"1": "1", "i": "i", "j": "j", "k": "k"},
	"i": {"1": "i", "i": "-1", "j": "k", "k": "-j"},
	"j": {"1": "j", "i": "-k", "j": "-1", "k": "i"},
	"k": {"1": "k", "i": "j", "j": "-i", "k": "-1"},
}

func solveCase(l int, x int, seq string) string {
	if multiplyAll(x, seq) == "-1" {
		if shortestIJ(l, x, seq) {
			return "Yes"
		}
	}

	return "No"
}

func shortestIJ(l int, x int, seq string) bool {
	i, found := reduceTo(0, "i", l, x, seq)

	if found {
		_, found := reduceTo(i, "j", l, x, seq)

		return found
	}

	return false
}

func reduceTo(start int, char string, l int, x int, seq string) (int, bool) {
	idx := start
	a := string(seq[start%l])
	length := l * x

	for idx < length {
		idx += 1
		if a == char {
			return idx, true
		}
		a = multiply(a, string(seq[idx%l]))
	}
	return idx, false
}

func multiplyAll(x int, seq string) string {
	a := string(seq[0])

	for i := 1; i < len(seq); i++ {
		a = multiply(a, string(seq[i]))
	}

	x %= 4

	if x == 0 {
		return "1"
	} else if x == 1 {
		return a
	} else if x == 2 {
		return multiply(a, a)
	} else if x == 3 {
		return multiply(multiply(a, a), a)
	} else {
		panic("Should never get here.")
	}
}
func multiply(x string, y string) string {
	negative := false

	if strings.Contains(x, "-") {
		negative = (negative != true)
		x = string(x[1])
	}
	if strings.Contains(y, "-") {
		negative = (negative != true)
		y = string(y[1])
	}
	z := TABLE[x][y]

	if negative {
		if strings.Contains(z, "-") {
			return string(z[1])
		} else {
			return "-" + z
		}
	}
	return z
}
