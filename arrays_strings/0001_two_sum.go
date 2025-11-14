package main

import (
	"fmt"
	"testing"
)

/*
1. Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Notes:
- Key insight: For each number, we need to find its complement (target - num) in the array.
- Hash map approach: Store numbers and their indices as we iterate. For each number, check if its complement exists.
- One-pass approach: Check for complement before adding current number to map (handles duplicates correctly).
- Two-pass approach: First pass builds the map, second pass finds the pair (need to check index != i).
- Brute force: Check all pairs - O(n²) time, O(1) space.
- Hash map: O(n) time, O(n) space - optimal for this problem.
*/

// twoSum is the main solution using hash map (one-pass)
// Approach 1: Hash Map (One Pass) - Optimal
// Time Complexity: O(n)
// Space Complexity: O(n)
func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if idx, ok := numMap[complement]; ok {
			return []int{idx, i}
		}
		numMap[num] = i
	}
	return []int{}
}

// twoSumBruteForce uses brute force approach
// Approach 2: Brute Force
// Time Complexity: O(n²)
// Space Complexity: O(1)
func twoSumBruteForce(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

// twoSumTwoPass uses hash map with two passes
// Approach 3: Hash Map (Two Pass)
// Time Complexity: O(n)
// Space Complexity: O(n)
func twoSumTwoPass(nums []int, target int) []int {
	numMap := make(map[int]int)
	// First pass: build the map
	for i, num := range nums {
		numMap[num] = i
	}
	// Second pass: find the pair
	for i, num := range nums {
		complement := target - num
		if idx, ok := numMap[complement]; ok && idx != i {
			return []int{i, idx}
		}
	}
	return []int{}
}

// twoSumSorted assumes array is sorted (alternative approach)
// Note: This doesn't apply to the original problem, but useful for variations
// Approach 4: Two Pointers (for sorted arrays)
// Time Complexity: O(n)
// Space Complexity: O(1)
func twoSumSorted(nums []int, target int) []int {
	left, right := 0, len(nums)-1
	for left < right {
		sum := nums[left] + nums[right]
		if sum == target {
			return []int{left, right}
		} else if sum < target {
			left++
		} else {
			right--
		}
	}
	return []int{}
}

// Test cases
func TestTwoSum(t *testing.T) {
	// Test case 1: Basic example
	nums1 := []int{2, 7, 11, 15}
	target1 := 9
	expected1 := []int{0, 1}
	result1 := twoSum(nums1, target1)
	if !equalSlices(result1, expected1) {
		t.Errorf("Test 1 failed: expected %v, got %v", expected1, result1)
	}

	// Test case 2: Another example
	nums2 := []int{3, 2, 4}
	target2 := 6
	expected2 := []int{1, 2}
	result2 := twoSum(nums2, target2)
	if !equalSlices(result2, expected2) {
		t.Errorf("Test 2 failed: expected %v, got %v", expected2, result2)
	}

	// Test case 3: Duplicate numbers
	nums3 := []int{3, 3}
	target3 := 6
	expected3 := []int{0, 1}
	result3 := twoSum(nums3, target3)
	if !equalSlices(result3, expected3) {
		t.Errorf("Test 3 failed: expected %v, got %v", expected3, result3)
	}

	// Test case 4: Negative numbers
	nums4 := []int{-1, -2, -3, -4, -5}
	target4 := -8
	expected4 := []int{2, 4}
	result4 := twoSum(nums4, target4)
	if !equalSlices(result4, expected4) {
		t.Errorf("Test 4 failed: expected %v, got %v", expected4, result4)
	}

	// Test case 5: Zero target
	nums5 := []int{1, 2, 3, -1, -2}
	target5 := 0
	expected5 := []int{1, 4}
	result5 := twoSum(nums5, target5)
	if !equalSlices(result5, expected5) {
		t.Errorf("Test 5 failed: expected %v, got %v", expected5, result5)
	}

	// Test case 6: Large numbers (using int64 compatible values)
	nums6 := []int{1000000000, 2000000000, -1000000000, -2000000000}
	target6 := 0
	expected6 := []int{0, 2}
	result6 := twoSum(nums6, target6)
	if !equalSlices(result6, expected6) {
		t.Errorf("Test 6 failed: expected %v, got %v", expected6, result6)
	}

	// Test case 7: Compare all approaches
	testCases := [][]int{
		{2, 7, 11, 15},
		{3, 2, 4},
		{3, 3},
		{1, 5, 3, 7, 2},
	}
	targets := []int{9, 6, 6, 8}

	for i, nums := range testCases {
		target := targets[i]
		result1 := twoSum(nums, target)
		result2 := twoSumBruteForce(nums, target)
		result3 := twoSumTwoPass(nums, target)

		if !equalSlices(result1, result2) {
			t.Errorf("Brute force mismatch for test case %d: %v vs %v", i+1, result1, result2)
		}
		if !equalSlices(result1, result3) {
			t.Errorf("Two pass mismatch for test case %d: %v vs %v", i+1, result1, result3)
		}
	}

	fmt.Println("All tests passed!")
}

// Helper function to compare slices
func equalSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	// For two sum, order doesn't matter, so check both orders
	if (a[0] == b[0] && a[1] == b[1]) || (a[0] == b[1] && a[1] == b[0]) {
		return true
	}
	return false
}

// Example usage
func ExampleTwoSum() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println(result)
	// Output: [0 1]
}

// Benchmark tests
func BenchmarkTwoSum(b *testing.B) {
	nums := make([]int, 1000)
	for i := range nums {
		nums[i] = i
	}
	target := 1998
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		twoSum(nums, target)
	}
}

func BenchmarkTwoSumBruteForce(b *testing.B) {
	nums := make([]int, 1000)
	for i := range nums {
		nums[i] = i
	}
	target := 1998
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		twoSumBruteForce(nums, target)
	}
}

func main() {
	// Example usage
	fmt.Println("Example usage:")
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Printf("twoSum(%v, %d) = %v\n", nums, target, result)

	// Run manual test cases
	fmt.Println("\nRunning manual test cases...")
	testCases := []struct {
		nums     []int
		target   int
		expected []int
		name     string
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}, "Basic example"},
		{[]int{3, 2, 4}, 6, []int{1, 2}, "Another example"},
		{[]int{3, 3}, 6, []int{0, 1}, "Duplicate numbers"},
		{[]int{-1, -2, -3, -4, -5}, -8, []int{2, 4}, "Negative numbers"},
		{[]int{1, 2, 3, -1, -2}, 0, []int{1, 4}, "Zero target"},
	}

	for _, tc := range testCases {
		result := twoSum(tc.nums, tc.target)
		if equalSlices(result, tc.expected) {
			fmt.Printf("✓ %s: PASSED\n", tc.name)
		} else {
			fmt.Printf("✗ %s: FAILED - expected %v, got %v\n", tc.name, tc.expected, result)
		}
	}

	fmt.Println("\nTo run full tests, use: go test")
	fmt.Println("To run benchmarks, use: go test -bench=.")
}
