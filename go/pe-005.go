// 2018-11-18

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    // Keep track of the maximum power we've seen for each prime.
    max_powers := make(map[int]int)
    for n:=2; n<=20; n++ {
        for prime, power := range helpers.FactorPowers(n) {
            if max_powers[prime] < power { max_powers[prime] = power }
        }
    }
    // Tally all those powers then spit out the result.
    tally := 1
    for prime, power := range max_powers {
        for i:=0; i<power; i++ { tally *= prime }
    }
    fmt.Println(tally)
}
