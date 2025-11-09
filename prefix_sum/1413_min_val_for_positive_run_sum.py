"""
1413. Minimum Value to Get Positive Step by Step Sum
Difficulty: Easy

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.

Example 3:
Input: nums = [1,-2,-3]
Output: 5

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100

Notes:
- Key insight: Track minimum prefix sum. If min_sum is negative, we need startValue >= 1 - min_sum.
- If min_sum >= 0, we only need startValue >= 1.
- This is a prefix sum problem with a greedy approach.
"""

from typing import List


class Solution:
    def min_start_value(self, nums: List[int]) -> int:
        """
        Approach 1: Prefix Sum with Minimum Tracking (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Track running sum and find minimum. Return 1 - min_sum to ensure all sums >= 1.
        """
        running_sum, min_sum = 0, 0

        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)

        return 1 - min_sum
    
    def min_start_value_explicit(self, nums: List[int]) -> int:
        """
        Approach 2: Explicit Prefix Sum Array
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Build prefix sum array explicitly, then find minimum.
        """
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        min_sum = min(prefix_sum[1:])  # Skip initial 0
        return max(1, 1 - min_sum)
    
    def min_start_value_binary_search(self, nums: List[int]) -> int:
        """
        Approach 3: Binary Search (Alternative)
        Time Complexity: O(n log(max_value))
        Space Complexity: O(1)
        
        Binary search for minimum startValue that satisfies condition.
        Less efficient but demonstrates binary search technique.
        """
        def is_valid(start_value):
            current_sum = start_value
            for num in nums:
                current_sum += num
                if current_sum < 1:
                    return False
            return True
        
        # Binary search range: [1, max_possible_value]
        # Worst case: all negative, need startValue = 1 - sum(nums)
        max_needed = 1 - sum(min(0, num) for num in nums) * len(nums)
        left, right = 1, max(1, max_needed)
        
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example")
    nums1 = [-3, 2, -3, 4, 2]
    expected1 = 5
    result1 = solution.min_start_value(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: All positive
    print("Test 2: All positive")
    nums2 = [1, 2]
    expected2 = 1
    result2 = solution.min_start_value(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Mixed positive and negative
    print("Test 3: Mixed positive and negative")
    nums3 = [1, -2, -3]
    expected3 = 5
    result3 = solution.min_start_value(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: All negative
    print("Test 4: All negative")
    nums4 = [-1, -2, -3]
    expected4 = 7
    result4 = solution.min_start_value(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single element positive
    print("Test 5: Single element positive")
    nums5 = [1]
    expected5 = 1
    result5 = solution.min_start_value(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Single element negative
    print("Test 6: Single element negative")
    nums6 = [-5]
    expected6 = 6
    result6 = solution.min_start_value(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_nums = [-3, 2, -3, 4, 2]
    expected = 5
    
    result_prefix = solution.min_start_value(test_nums)
    result_explicit = solution.min_start_value_explicit(test_nums)
    result_binary = solution.min_start_value_binary_search(test_nums)
    
    assert result_prefix == expected, f"Test 7.1 Prefix sum failed: expected {expected}, got {result_prefix}"
    assert result_explicit == expected, f"Test 7.2 Explicit failed: expected {expected}, got {result_explicit}"
    assert result_binary == expected, f"Test 7.3 Binary search failed: expected {expected}, got {result_binary}"
    
    # Test case 8: Large negative at start
    print("Test 8: Large negative at start")
    nums8 = [-10, 5, 3]
    expected8 = 11
    result8 = solution.min_start_value(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Large negative at end
    print("Test 9: Large negative at end")
    nums9 = [5, 3, -10]
    expected9 = 3
    result9 = solution.min_start_value(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Alternating positive and negative
    print("Test 10: Alternating positive and negative")
    nums10 = [1, -1, 1, -1, 1]
    expected10 = 1
    result10 = solution.min_start_value(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()