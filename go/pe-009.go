// 2018-11-18

package main

import (
    "fmt"
    "math"
)

// =====================================================================

func int_sqrt(n int) (int, bool) {
    // First attempt at the value, error dual returns.
    sqrt := math.Pow(float64(n), 0.5)
    if math.Ceil(sqrt) != math.Floor(sqrt) { return 0, true }
    return int(sqrt), false
}

// ---------------------------------------------------------------------

func main() {
    // Maybe there's a trick, but this is trivial to solve directly.
    var c int
    var err bool
    for a:=1; a<500; a++ {
        for b:=a; b<500; b++ {
            c, err = int_sqrt(a*a + b*b)
            if !err && a + b + c == 1000 { fmt.Println(a*b*c) }
        }
    }
}
