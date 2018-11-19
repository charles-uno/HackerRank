
package helpers

import (
    "sort"
)

// =====================================================================

func Min(arr []int) int {
    sort.Ints(arr)
    return arr[0]
}

// ---------------------------------------------------------------------

func Max(arr []int) int {
    sort.Ints(arr)
    return arr[len(arr)-1]
}

// =====================================================================

func Factors(n int) []int {
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

// ---------------------------------------------------------------------

func FactorPowers(n int) map[int]int {
    factor_powers := make(map[int]int)
    for _, p := range Factors(n) {
        factor_powers[p] += 1
    }
    return factor_powers
}
