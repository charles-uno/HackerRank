// 2018-11-19

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    i, tri := 0, 0
    for {
        i += 1
        tri += i
        ndiv := helpers.NumDivisors(tri)
        if ndiv > 500 {
            fmt.Println(tri)
            break
        }
    }
}
