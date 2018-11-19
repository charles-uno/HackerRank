
package main

import (
    "fmt"
    "helpers"
)

// Three digits isn't much. Let's brute force this one.

// NOTE -- There are certainly ways we could have done this prettier.
// Onward and upward! 

// =====================================================================

func is_palindrome(n int) bool {
    digits := []int{}
    for n>0 {
        digits = append(digits, n % 10)
        n = n/10
    }
    for i, dig := range digits {
        if dig != digits[len(digits)-i-1] { return false }
    }
    return true
}

// =====================================================================

func main() {
    palindromes := []int{}
    for i:=100; i<1000; i++ {
        for j:=i; j<1000; j++ {
            if is_palindrome(i*j) { palindromes = append(palindromes, i*j) }
        }
    }
    fmt.Println( helpers.Max(palindromes) )
}
