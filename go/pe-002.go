
// First attempt at slices and range

package main

import "fmt"

// =====================================================================

func fibonacci_upto(n int) []int {
    i, j := 0, 1
    fib := []int{}
    for j < n {
        fib = append(fib, j)
        i, j = j, i+j
    }
    return fib
}

// =====================================================================

func main() {
    sum := 0
    for _, n := range fibonacci_upto(4000000) {
        if n%2 == 0 { sum += n }
    }
    fmt.Println(sum)
}
