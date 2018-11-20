// 2018-11-19

package main

import (
    "fmt"
)

// =====================================================================

func next_link(n int) int {
    if n%2 == 0 {
        return n/2
    } else {
        return 3*n+1
    }
}

// ---------------------------------------------------------------------

func nlinks(n int, nlinks_seen map[int]int) int {
    if nlinks_seen[n] == 0 {
        nlinks_seen[n] = nlinks(next_link(n), nlinks_seen)+1
    }
    return nlinks_seen[n]
}

// ---------------------------------------------------------------------

func main() {
    // Keep track of everything we've seen.
    nlinks_seen := make(map[int]int)
    nlinks_seen[1] = 1
    // Make sure to see everything up to a million.
    for i:=1; i<1000000; i++ {
        nlinks(i, nlinks_seen)
    }
    // Which is biggest?
    max_key, max_val := 0, 0
    for key, val := range nlinks_seen {
        if val > max_val { max_key, max_val = key, val }
    }
    fmt.Println(max_key, max_val)
}
