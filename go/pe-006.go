// 2018-11-18

package main

import (
    "fmt"
)

// =====================================================================

func main() {
    // Maybe there's a trick, but this is trivial to solve directly.
    nmax := 100
    sum, sum_square := 0, 0
    for n:=1; n<=nmax; n++ {
        sum += n
        sum_square += n*n
    }
    square_sum := sum*sum
    fmt.Println( square_sum - sum_square )
}
