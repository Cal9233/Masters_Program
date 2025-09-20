/**
 * Tribonacci - Converted from Python
 *
 * This program generates tribonacci sequences where each number is the sum
 * of the three preceding numbers. The conversion maintains exact behavior
 * compatibility with the original Python version.
 *
 * @author Calvin Malagon
 * @version 1.0
 * @since 2025
 */

package main

import "fmt"

// tribonacci generates a tribonacci sequence of length n
// Returns:
// - empty slice for n <= 0
// - [0] for n == 1
// - [0, 1] for n == 2
// - tribonacci sequence starting with [1, 1, 1] for n >= 3
func tribonacci(n int) []int {
	if n <= 0 {
		return []int{} // empty slice
	} else if n == 1 {
		return []int{0} // [0]
	} else if n == 2 {
		return []int{0, 1} // [0, 1]
	} else {
		// Initialize [1, 1, 1]
		fibSeq := []int{1, 1, 1}

		// Generate remaining numbers in sequence
		for i := 3; i < n; i++ {
			nextNum := fibSeq[i-1] + fibSeq[i-2] + fibSeq[i-3]
			fibSeq = append(fibSeq, nextNum)
		}
		return fibSeq
	}
}

// Main function to test tribonacci with n = 20
func main() {
	result := tribonacci(20)
	fmt.Println(result)
}
