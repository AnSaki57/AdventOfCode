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

	for _, value := range dirsinp {
		currnum += value
		currnum %= 100

		if currnum == 0 {
			count++
		}
	}

	println(count)
}
