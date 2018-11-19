
// Was going to use a helper function, but it ended up being unnecessary

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    for _, f := range helpers.Factors(600851475143) { fmt.Println(f) }
}
