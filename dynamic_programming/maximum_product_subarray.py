"""
152. Maximum Product Subarray
Difficulty: Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Example 3:
Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] has the largest product 24.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Notes:
- Key insight: Unlike maximum sum subarray, we need to track both maximum AND minimum products.
- Why? Because multiplying a negative number can flip a minimum product into a maximum product.
- At each position, we can either:
  1. Start a new subarray with current number
  2. Extend previous subarray by multiplying with current number
- We track both max_prod and min_prod because:
  - If current number is positive: max_prod * num is max, min_prod * num is min
  - If current number is negative: min_prod * num becomes max, max_prod * num becomes min
- Edge cases: Single element, all negatives, zeros in array
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using constant extra space
- Alternative approaches:
  - Brute force: O(n^2) - check all subarrays
  - Two-pass: O(n) - track products from left and right (handles negatives)
"""

from typing import List


class Solution:
    def max_product_subarray(self, nums: List[int]) -> int:
        """
        Approach 1: Dynamic Programming with Max/Min Tracking (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Track both maximum and minimum products at each position.
        The minimum product is important because multiplying by a negative number
        can turn the minimum into the maximum.
        """
        if not nums:
            return 0
        
        # Initialize with first element
        result = max_prod = min_prod = nums[0]
        
        for num in nums[1:]:
            max_prod, min_prod = (
                max(max_prod * num, min_prod * num, num),
                min(max_prod * num, min_prod * num, num)
            )

            result = max(result, max_prod)
        
        return result
    
    def max_product_subarray_two_pass(self, nums: List[int]) -> int:
        """
        Approach 2: Two-Pass (Left to Right and Right to Left)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        The idea is that if there's an even number of negatives, the product is positive.
        If odd number of negatives, we need to exclude one negative. By going both directions,
        we ensure we catch the maximum product regardless of where the negatives are.
        """
        if not nums:
            return 0
        
        result = float('-inf')
        product = 1
        
        # Pass from left to right
        for num in nums:
            product *= num
            result = max(result, product)
            if product == 0:
                product = 1  # Reset on zero
        
        product = 1
        
        # Pass from right to left
        for num in reversed(nums):
            product *= num
            result = max(result, product)
            if product == 0:
                product = 1  # Reset on zero
        
        return result
    
    def max_product_subarray_brute_force(self, nums: List[int]) -> int:
        """
        Approach 3: Brute Force
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        Check all possible subarrays and find the maximum product.
        Only for understanding - not recommended for production.
        """
        if not nums:
            return 0
        
        result = float('-inf')
        n = len(nums)
        
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                result = max(result, product)
        
        return result
    
    def max_product_subarray_dp_array(self, nums: List[int]) -> int:
        """
        Approach 4: DP with Arrays (More Explicit)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Uses arrays to store max and min products at each position.
        More memory but easier to understand and debug.
        """
        if not nums:
            return 0
        
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        
        max_dp[0] = min_dp[0] = nums[0]
        result = nums[0]
        
        for i in range(1, n):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            result = max(result, max_dp[i])
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example with positive and negative
    print("Test 1: Basic example [2,3,-2,4]")
    nums1 = [2, 3, -2, 4]
    expected1 = 6  # [2, 3]
    result1 = solution.max_product_subarray(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Negative with zero
    print("Test 2: Negative with zero [-2,0,-1]")
    nums2 = [-2, 0, -1]
    expected2 = 0
    result2 = solution.max_product_subarray(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Multiple negatives
    print("Test 3: Multiple negatives [-2,3,-4]")
    nums3 = [-2, 3, -4]
    expected3 = 24  # [-2, 3, -4] = 24
    result3 = solution.max_product_subarray(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single element
    print("Test 4: Single element [5]")
    nums4 = [5]
    expected4 = 5
    result4 = solution.max_product_subarray(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All negatives
    print("Test 5: All negatives [-2,-3,-4]")
    nums5 = [-2, -3, -4]
    expected5 = 12  # [-3, -4] = 12
    result5 = solution.max_product_subarray(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: All positives
    print("Test 6: All positives [1,2,3,4]")
    nums6 = [1, 2, 3, 4]
    expected6 = 24  # [1, 2, 3, 4] = 24
    result6 = solution.max_product_subarray(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Contains zero
    print("Test 7: Contains zero [2,0,3,4]")
    nums7 = [2, 0, 3, 4]
    expected7 = 12  # [3, 4] = 12
    result7 = solution.max_product_subarray(nums7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Alternating positives and negatives
    print("Test 8: Alternating [1,-2,3,-4,5]")
    nums8 = [1, -2, 3, -4, 5]
    expected8 = 120  # [3, -4, 5] = -60, but [1, -2, 3, -4, 5] = 120
    result8 = solution.max_product_subarray(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Large negative at start
    print("Test 9: Large negative at start [-1,-2,-3]")
    nums9 = [-1, -2, -3]
    expected9 = 6  # [-1, -2, -3] = -6, but [-2, -3] = 6
    result9 = solution.max_product_subarray(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Single negative
    print("Test 10: Single negative [-5]")
    nums10 = [-5]
    expected10 = -5
    result10 = solution.max_product_subarray(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Zero in middle
    print("Test 11: Zero in middle [2,3,0,4,5]")
    nums11 = [2, 3, 0, 4, 5]
    expected11 = 20  # [4, 5] = 20
    result11 = solution.max_product_subarray(nums11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: All zeros
    print("Test 12: All zeros [0,0,0]")
    nums12 = [0, 0, 0]
    expected12 = 0
    result12 = solution.max_product_subarray(nums12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Complex case
    print("Test 13: Complex case [2,-5,-2,-4,3]")
    nums13 = [2, -5, -2, -4, 3]
    expected13 = 24  # [-5, -2, -4] = -40, but [-2, -4, 3] = 24
    result13 = solution.max_product_subarray(nums13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Compare all approaches
    print("\nTest 14: Comparing all approaches")
    test_cases = [
        [2, 3, -2, 4],
        [-2, 0, -1],
        [-2, 3, -4],
        [1, -2, 3, -4, 5],
        [2, -5, -2, -4, 3],
    ]
    
    for nums in test_cases:
        result1 = solution.max_product_subarray(nums)
        result2 = solution.max_product_subarray_two_pass(nums)
        result3 = solution.max_product_subarray_dp_array(nums)
        result4 = solution.max_product_subarray_brute_force(nums)
        
        assert result1 == result2, f"Two-pass mismatch for {nums}: {result1} vs {result2}"
        assert result1 == result3, f"DP array mismatch for {nums}: {result1} vs {result3}"
        assert result1 == result4, f"Brute force mismatch for {nums}: {result1} vs {result4}"
    
    print("  All approaches match! ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()