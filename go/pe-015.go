// 2018-11-19

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    // A lot going on under the hood here. We can't calculate the
    // factorials directly, since the numbers get too big. So we keep
    // track of prime factors.
    fmt.Println( helpers.Choose(40, 20) )
}
