// 2018-11-19

package main

import (
    "fmt"
    "helpers"
)

// =====================================================================

func main() {
    fmt.Println( helpers.Sum( helpers.PrimesUpto(2000000) ) )
}
