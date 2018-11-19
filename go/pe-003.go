
// Was going to use a helper function, but it ended up being unnecessary

package main

import "fmt"

// =====================================================================

func factors(n int) []int {
    factors := []int{}
    for p := 2; n > 1 ; p++ {
        // If n % p == 0, p must be prime. We have already checked
        // against everything smaller.
        for n % p == 0 {
            n = n/p
            factors = append(factors, p)
        }
    }
    return factors
}

// =====================================================================

func main() {
    for _, f := range factors(600851475143) { fmt.Println(f) }
}
