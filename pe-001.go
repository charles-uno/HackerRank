
// First Go program, let's take it easy.

package main

import "fmt"

// =====================================================================

func is_multiple_of_3_or_5(n int) bool {
    return n % 3 == 0 || n % 5 == 0
}

// =====================================================================

func main() {
    sum := 0
    for n := 0; n < 1000; n++ {
        if is_multiple_of_3_or_5(n) { sum += n }
    }
    fmt.Println(sum)
}
