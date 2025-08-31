// tribo.go
// Converted from Python tribonacci program
// Author: Claude (Anthropic AI Assistant)
// 
// This program generates tribonacci sequences where each number is the sum
// of the three preceding numbers. The conversion maintains exact behavior
// compatibility with the original Python version.

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
		return []int{} // empty slice equivalent to Python's []
	} else if n == 1 {
		return []int{0} // equivalent to Python's [0]
	} else if n == 2 {
		return []int{0, 1} // equivalent to Python's [0, 1]
	} else {
		// Initialize with [1, 1, 1] as in Python version
		fibSeq := []int{1, 1, 1}
		
		// Generate remaining numbers in sequence
		for i := 3; i < n; i++ {
			nextNum := fibSeq[i-1] + fibSeq[i-2] + fibSeq[i-3]
			fibSeq = append(fibSeq, nextNum)
		}
		return fibSeq
	}
}

func main() {
	// Test the function with the same call as Python version
	result := tribonacci(20)
	fmt.Println(result)
	
	// Additional test cases to verify edge case compatibility
	fmt.Println("Testing edge cases:")
	fmt.Printf("n=0: %v\n", tribonacci(0))
	fmt.Printf("n=1: %v\n", tribonacci(1))
	fmt.Printf("n=2: %v\n", tribonacci(2))
	fmt.Printf("n=3: %v\n", tribonacci(3))
	fmt.Printf("n=4: %v\n", tribonacci(4))
	fmt.Printf("n=5: %v\n", tribonacci(5))
	fmt.Printf("n=10: %v\n", tribonacci(10))
	fmt.Printf("n=20: %v\n", tribonacci(20))
}