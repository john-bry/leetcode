"""
300. Longest Increasing Subsequence
Difficulty: Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Notes:
- Key insight: Use DP to track longest subsequence ending at each position.
- Binary search approach maintains smallest tail of all increasing subsequences.
- Greedy: Always try to extend with smallest possible tail value.
"""

from typing import List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        """
        Approach 1: Binary Search with Greedy (Optimal)
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Maintain smallest tail of all increasing subsequences of length i+1.
        Use binary search to find position to replace or extend.
        """
        tails = []

        for num in nums:
            left, right = 0, len(tails)

            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        
        return len(tails)
    
    def length_of_lis_dp(self, nums: List[int]) -> int:
        """
        Approach 2: Dynamic Programming
        Time Complexity: O(n²)
        Space Complexity: O(n)
        
        dp[i] = length of longest increasing subsequence ending at index i.
        For each position, check all previous positions.
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    def length_of_lis_memoization(self, nums: List[int]) -> int:
        """
        Approach 3: Memoization (Top-down DP)
        Time Complexity: O(n²)
        Space Complexity: O(n²) for memoization
        
        Recursive approach with memoization.
        """
        if not nums:
            return 0
        
        memo = {}
        
        def lis_ending_at(i):
            if i in memo:
                return memo[i]
            
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, lis_ending_at(j) + 1)
            
            memo[i] = max_len
            return max_len
        
        result = 0
        for i in range(len(nums)):
            result = max(result, lis_ending_at(i))
        
        return result
    
    def length_of_lis_greedy(self, nums: List[int]) -> int:
        """
        Approach 4: Greedy with Patience Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Similar to binary search approach but more explicit about greedy strategy.
        Always try to extend with smallest possible value.
        """
        if not nums:
            return 0
        
        piles = []
        
        for num in nums:
            # Binary search for leftmost pile where we can place this card
            left, right = 0, len(piles)
            
            while left < right:
                mid = (left + right) // 2
                if piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num
        
        return len(piles)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example")
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    result1 = solution.length_of_lis(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Another example
    print("Test 2: Another example")
    nums2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    result2 = solution.length_of_lis(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: All same elements
    print("Test 3: All same elements")
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected3 = 1
    result3 = solution.length_of_lis(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single element
    print("Test 4: Single element")
    nums4 = [1]
    expected4 = 1
    result4 = solution.length_of_lis(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Decreasing sequence
    print("Test 5: Decreasing sequence")
    nums5 = [5, 4, 3, 2, 1]
    expected5 = 1
    result5 = solution.length_of_lis(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Increasing sequence
    print("Test 6: Increasing sequence")
    nums6 = [1, 2, 3, 4, 5]
    expected6 = 5
    result6 = solution.length_of_lis(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected = 4
    
    result_binary = solution.length_of_lis(test_nums)
    result_dp = solution.length_of_lis_dp(test_nums)
    result_memo = solution.length_of_lis_memoization(test_nums)
    result_greedy = solution.length_of_lis_greedy(test_nums)
    
    assert result_binary == expected, f"Test 7.1 Binary search failed: expected {expected}, got {result_binary}"
    assert result_dp == expected, f"Test 7.2 DP failed: expected {expected}, got {result_dp}"
    assert result_memo == expected, f"Test 7.3 Memoization failed: expected {expected}, got {result_memo}"
    assert result_greedy == expected, f"Test 7.4 Greedy failed: expected {expected}, got {result_greedy}"
    
    # Test case 8: Complex case
    print("Test 8: Complex case")
    nums8 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    expected8 = 6
    result8 = solution.length_of_lis(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Negative numbers
    print("Test 9: Negative numbers")
    nums9 = [-2, -1, 0, 1, 2]
    expected9 = 5
    result9 = solution.length_of_lis(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Mixed positive and negative
    print("Test 10: Mixed positive and negative")
    nums10 = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    expected10 = 6
    result10 = solution.length_of_lis(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()