// 2018-11-18

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    // Maybe there's a trick, but this is trivial to solve directly.
    var c int
    var err bool
    for a:=1; a<500; a++ {
        for b:=a; b<500; b++ {
            c, err = helpers.IntSqrt(a*a + b*b)
            if !err && a + b + c == 1000 { fmt.Println(a*b*c) }
        }
    }
}
