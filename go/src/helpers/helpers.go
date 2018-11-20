
package helpers

import (
    "math"
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

// ---------------------------------------------------------------------

func Sum(seq []int) int {
    sum := 0
    for _, s := range seq { sum += s }
    return sum
}

// ---------------------------------------------------------------------

func IntSqrt(n int) (int, bool) {
    // First attempt at the value, error dual returns.
    sqrt := math.Pow(float64(n), 0.5)
    if math.Ceil(sqrt) != math.Floor(sqrt) { return 0, true }
    return int(sqrt), false
}

// ---------------------------------------------------------------------

func FloorSqrt(n int) int {
    return int( math.Pow(float64(n), 0.5) )
}

// =====================================================================

func isprime(i int, primes []int) bool {
    // There's got to be a better way to do this.
    for _, p := range primes {
        if i % p == 0 { return false }
    }
    return true
}

// ---------------------------------------------------------------------

func NthPrime(n int) int {
    primes := []int{}
    i := 2
    for len(primes) < n {
        if isprime(i, primes) { primes = append(primes, i) }
        i += 1
    }
    return primes[len(primes)-1]
}

// ---------------------------------------------------------------------

func PrimesUpto(n int) []int {
    sieve := make([]bool, n)
    for i:=2; i<n; i++ { sieve[i] = true }
    for i:=2; i<n; i++ {
        if !sieve[i] { continue }
        for j:=2*i; j<n; j+=i { sieve[j] = false }
    }
    primes := []int{}
    for i, s := range sieve {
        if s { primes = append(primes, i) }
    }
    return primes
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

// ---------------------------------------------------------------------

func NumDivisors(n int) int {
    if n == 0 { return 0 }
    num_divisors := 1
    for _, power := range FactorPowers(n) {
        num_divisors *= power+1
    }
    return num_divisors
}
