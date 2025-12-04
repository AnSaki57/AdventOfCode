// Not yet go-ified

package main

import (
	"fmt"
	"strconv"
)

func main() {
	var dirsinp []int
	fmt.Scan("%s")

	for {
		var dir string
		fmt.Scanf("%s", &dir)

		if dir == "x" {
			break
		}

		sign := 0
		if len(dir) > 0 {
			if dir[0] == 'L' {
				sign = -1
			} else {
				sign = 1
			}
		}

		dirnum, err := strconv.Atoi(dir[1:])
		if err == nil {
			dirnum *= sign
			dirsinp = append(dirsinp, dirnum)
		}
	}

	// Get count
	var currnum int = 50
	var count int = 0

	for index, value := range dirsinp {
		nextnum := currnum + value

		if nextnum < 0 && currnum == 0 {
			count--
		}

		for {
			if nextnum < 0 {
				nextnum += 100
				count++
			} else if nextnum > 99 {
				nextnum -= 100
				count++
			} else {
				break
			}
		}

		if nextnum == 0 && value < 0 {
			count++
		}

		if index < 100 {
			println(value, nextnum, count)
		}
		currnum = nextnum
	}

	println(count)
}
