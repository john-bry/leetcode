"""
53. Maximum Subarray
Difficulty: Medium

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: [5,4,-1,7,8] has the largest sum = 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Notes:
- Key insight: This is Kadane's Algorithm - a classic dynamic programming problem.
- At each position, we decide whether to:
  1. Start a new subarray with the current number
  2. Extend the previous subarray by adding the current number
- The recurrence relation: cur_sum = max(num, cur_sum + num)
  - If cur_sum + num < num, it's better to start fresh (previous sum was negative)
  - Otherwise, extend the previous subarray
- Edge cases: All negative numbers, single element, all positive numbers
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using constant extra space
- Alternative approaches:
  - Brute force: O(n^2) - check all subarrays
  - Divide and conquer: O(n log n) - split array and combine results
  - DP with array: O(n) time, O(n) space - store max sum ending at each position
"""

from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        """
        Approach 1: Kadane's Algorithm (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Kadane's algorithm tracks the maximum sum ending at the current position.
        If the sum becomes negative, we reset it (start a new subarray).
        """
        if not nums:
            return 0
        
        # Initialize with first element
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            # Either extend previous subarray or start fresh
            cur_sum = max(num, cur_sum + num)
            # Track the maximum sum seen so far
            max_sum = max(cur_sum, max_sum)
        
        return max_sum
    
    def max_subarray_dp_array(self, nums: List[int]) -> int:
        """
        Approach 2: DP with Array (More Explicit)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Uses an array to store the maximum sum ending at each position.
        More memory but easier to understand and allows tracking the subarray.
        """
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] = maximum sum of subarray ending at index i
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, n):
            # Either extend previous subarray or start fresh
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum
    
    def max_subarray_brute_force(self, nums: List[int]) -> int:
        """
        Approach 3: Brute Force
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        Check all possible subarrays and find the maximum sum.
        Only for understanding - not recommended for production.
        """
        if not nums:
            return 0
        
        max_sum = float('-inf')
        n = len(nums)
        
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
        
        return max_sum
    
    def max_subarray_divide_conquer(self, nums: List[int]) -> int:
        """
        Approach 4: Divide and Conquer
        Time Complexity: O(n log n)
        Space Complexity: O(log n) for recursion stack
        
        Divide the array into two halves, find max subarray in each half,
        and find max subarray crossing the middle.
        """
        if not nums:
            return 0
        
        def max_crossing_sum(arr, left, mid, right):
            """Find maximum sum of subarray crossing the middle"""
            # Left side
            left_sum = float('-inf')
            cur_sum = 0
            for i in range(mid, left - 1, -1):
                cur_sum += arr[i]
                left_sum = max(left_sum, cur_sum)
            
            # Right side
            right_sum = float('-inf')
            cur_sum = 0
            for i in range(mid + 1, right + 1):
                cur_sum += arr[i]
                right_sum = max(right_sum, cur_sum)
            
            return left_sum + right_sum
        
        def max_subarray_rec(arr, left, right):
            if left == right:
                return arr[left]
            
            mid = (left + right) // 2
            
            # Max subarray in left half
            left_max = max_subarray_rec(arr, left, mid)
            
            # Max subarray in right half
            right_max = max_subarray_rec(arr, mid + 1, right)
            
            # Max subarray crossing middle
            cross_max = max_crossing_sum(arr, left, mid, right)
            
            return max(left_max, right_max, cross_max)
        
        return max_subarray_rec(nums, 0, len(nums) - 1)
    
    def max_subarray_optimized(self, nums: List[int]) -> int:
        """
        Approach 5: Space-Optimized Kadane's (Alternative Implementation)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Alternative implementation that resets sum when it becomes negative.
        """
        if not nums:
            return 0
        
        max_sum = cur_sum = nums[0]
        
        for num in nums[1:]:
            # If current sum is negative, reset it (start fresh)
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            
            max_sum = max(max_sum, cur_sum)
        
        return max_sum


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Classic example
    print("Test 1: Classic example [-2,1,-3,4,-1,2,1,-5,4]")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6  # [4,-1,2,1]
    result1 = solution.max_subarray(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Single element
    print("Test 2: Single element [1]")
    nums2 = [1]
    expected2 = 1
    result2 = solution.max_subarray(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: All positive
    print("Test 3: All positive [5,4,-1,7,8]")
    nums3 = [5, 4, -1, 7, 8]
    expected3 = 23  # [5,4,-1,7,8]
    result3 = solution.max_subarray(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: All negative
    print("Test 4: All negative [-5,-4,-3,-2,-1]")
    nums4 = [-5, -4, -3, -2, -1]
    expected4 = -1  # [-1] (least negative)
    result4 = solution.max_subarray(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Mixed with large negative
    print("Test 5: Mixed with large negative [1,-3,2,1,-1]")
    nums5 = [1, -3, 2, 1, -1]
    expected5 = 3  # [2,1]
    result5 = solution.max_subarray(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two elements
    print("Test 6: Two elements [-1,2]")
    nums6 = [-1, 2]
    expected6 = 2  # [2]
    result6 = solution.max_subarray(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Alternating pattern
    print("Test 7: Alternating pattern [1,-1,1,-1,1]")
    nums7 = [1, -1, 1, -1, 1]
    expected7 = 1  # Any single 1
    result7 = solution.max_subarray(nums7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Single negative
    print("Test 8: Single negative [-5]")
    nums8 = [-5]
    expected8 = -5
    result8 = solution.max_subarray(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Large positive at end
    print("Test 9: Large positive at end [-1,-2,-3,10]")
    nums9 = [-1, -2, -3, 10]
    expected9 = 10  # [10]
    result9 = solution.max_subarray(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Large positive at start
    print("Test 10: Large positive at start [10,-1,-2,-3]")
    nums10 = [10, -1, -2, -3]
    expected10 = 10  # [10]
    result10 = solution.max_subarray(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: All zeros
    print("Test 11: All zeros [0,0,0,0]")
    nums11 = [0, 0, 0, 0]
    expected11 = 0
    result11 = solution.max_subarray(nums11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Complex case
    print("Test 12: Complex case [8,-19,5,-4,20]")
    nums12 = [8, -19, 5, -4, 20]
    expected12 = 21  # [5,-4,20]
    result12 = solution.max_subarray(nums12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Compare all approaches
    print("\nTest 13: Comparing all approaches")
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [5, 4, -1, 7, 8],
        [1, -3, 2, 1, -1],
        [-5, -4, -3, -2, -1],
        [8, -19, 5, -4, 20],
    ]
    
    for nums in test_cases:
        result1 = solution.max_subarray(nums)
        result2 = solution.max_subarray_dp_array(nums)
        result3 = solution.max_subarray_optimized(nums)
        result4 = solution.max_subarray_brute_force(nums)
        result5 = solution.max_subarray_divide_conquer(nums)
        
        assert result1 == result2, f"DP array mismatch for {nums}: {result1} vs {result2}"
        assert result1 == result3, f"Optimized mismatch for {nums}: {result1} vs {result3}"
        assert result1 == result4, f"Brute force mismatch for {nums}: {result1} vs {result4}"
        assert result1 == result5, f"Divide & conquer mismatch for {nums}: {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 14: Edge case - empty array (should return 0)
    print("\nTest 14: Edge case - empty array")
    nums14 = []
    expected14 = 0
    result14 = solution.max_subarray(nums14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Large array with pattern
    print("Test 15: Large array pattern [1,2,3,...,100]")
    nums15 = list(range(1, 101))
    expected15 = sum(nums15)  # 5050
    result15 = solution.max_subarray(nums15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()