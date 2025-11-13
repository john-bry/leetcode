"""
213. House Robber II
Difficulty: Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
Explanation: Rob house 2 (money = 3).

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Notes:
- Key insight: Since houses are arranged in a circle, we can't rob both the first and last house.
- Solution: Break the problem into two linear subproblems:
  1. Rob houses from 0 to n-2 (exclude last house)
  2. Rob houses from 1 to n-1 (exclude first house)
- Take the maximum of these two results.
- For each linear subproblem, use the same DP approach as House Robber I.
- Recurrence for linear: dp[i] = max(nums[i] + dp[i-2], dp[i-1])
- Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Approach 1: Memoization (Top-down DP)
        Time Complexity: O(n)
        Space Complexity: O(n) for memoization and recursion stack
        
        Break the circular problem into two linear problems and use memoization.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Two cases: exclude first house or exclude last house
        first = self.rob_linear(nums, 0, n - 2)
        second = self.rob_linear(nums, 1, n - 1)

        return max(first, second)

    def rob_linear(self, nums, start, end):
        """Helper function to solve linear house robber problem"""
        memo = {}

        def dp(i):
            if i > end:
                return 0
            if i in memo:
                return memo[i]

            rob_current = nums[i] + dp(i + 2)
            skip_current = dp(i + 1)

            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return dp(start)
    
    def rob_tabulation(self, nums: List[int]) -> int:
        """
        Approach 2: Tabulation (Bottom-up DP)
        Time Complexity: O(n)
        Space Complexity: O(n) for DP array
        
        Use tabulation for both linear subproblems.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear_tabulation(nums, start, end):
            """Helper function using tabulation"""
            if start > end:
                return 0
            if start == end:
                return nums[start]
            
            length = end - start + 1
            dp = [0] * length
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            
            for i in range(2, length):
                dp[i] = max(nums[start + i] + dp[i - 2], dp[i - 1])
            
            return dp[length - 1]
        
        # Two cases: exclude first house or exclude last house
        first = rob_linear_tabulation(nums, 0, n - 2)
        second = rob_linear_tabulation(nums, 1, n - 1)
        
        return max(first, second)
    
    def rob_optimized(self, nums: List[int]) -> int:
        """
        Approach 3: Space-Optimized DP (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use space-optimized DP for both linear subproblems.
        Only track the last two values instead of entire array.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear_optimized(nums, start, end):
            """Helper function using space-optimized DP"""
            if start > end:
                return 0
            if start == end:
                return nums[start]
            
            # prev2 = max profit up to i-2, prev1 = max profit up to i-1
            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])
            
            for i in range(start + 2, end + 1):
                current = max(nums[i] + prev2, prev1)
                prev2, prev1 = prev1, current
            
            return prev1
        
        # Two cases: exclude first house or exclude last house
        first = rob_linear_optimized(nums, 0, n - 2)
        second = rob_linear_optimized(nums, 1, n - 1)
        
        return max(first, second)
    
    def rob_iterative(self, nums: List[int]) -> int:
        """
        Approach 4: Iterative with Two Variables
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Alternative space-optimized approach using two variables.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear_iterative(nums, start, end):
            """Helper function using iterative approach"""
            if start > end:
                return 0
            
            rob_prev = 0  # Max profit if we rob previous house
            rob_current = 0  # Max profit if we rob current house
            
            for i in range(start, end + 1):
                # Either rob current house (can't rob previous) or skip current
                rob_prev, rob_current = rob_current, max(rob_current, rob_prev + nums[i])
            
            return rob_current
        
        # Two cases: exclude first house or exclude last house
        first = rob_linear_iterative(nums, 0, n - 2)
        second = rob_linear_iterative(nums, 1, n - 1)
        
        return max(first, second)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example with circle
    print("Test 1: Basic example with circle")
    nums1 = [2, 3, 2]
    expected1 = 3
    result1 = solution.rob(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Another example
    print("Test 2: Another example")
    nums2 = [1, 2, 3, 1]
    expected2 = 4
    result2 = solution.rob(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Three houses
    print("Test 3: Three houses")
    nums3 = [1, 2, 3]
    expected3 = 3
    result3 = solution.rob(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single house
    print("Test 4: Single house")
    nums4 = [5]
    expected4 = 5
    result4 = solution.rob(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Two houses
    print("Test 5: Two houses")
    nums5 = [2, 3]
    expected5 = 3
    result5 = solution.rob(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: All zeros
    print("Test 6: All zeros")
    nums6 = [0, 0, 0, 0]
    expected6 = 0
    result6 = solution.rob(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: First and last are both high value
    print("Test 7: First and last are both high value")
    nums7 = [2, 1, 1, 2]
    expected7 = 3  # Can't rob both first and last, so rob middle two: 1 + 1 = 2, or one of the ends: 2
    result7 = solution.rob(nums7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: First house is best
    print("Test 8: First house is best")
    nums8 = [10, 1, 1, 1]
    expected8 = 11  # Rob houses 0, 2: 10 + 1 = 11
    result8 = solution.rob(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Last house is best
    print("Test 9: Last house is best")
    nums9 = [1, 1, 1, 10]
    expected9 = 11  # Rob houses 1, 3: 1 + 10 = 11
    result9 = solution.rob(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Edge case - empty array
    print("Test 10: Edge case - empty array")
    nums10 = []
    expected10 = 0
    result10 = solution.rob(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    # Test case 11: Large values
    print("Test 11: Large values")
    nums11 = [100, 200, 300, 100]
    expected11 = 400  # Rob houses 1, 2: 200 + 300 = 500, or houses 0, 2: 100 + 300 = 400
    result11 = solution.rob(nums11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    
    # Test case 12: Alternating pattern
    print("Test 12: Alternating pattern")
    nums12 = [1, 3, 1, 3, 1]
    expected12 = 6  # Rob houses 1, 3: 3 + 3 = 6
    result12 = solution.rob(nums12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    
    # Test case 13: All same value
    print("Test 13: All same value")
    nums13 = [5, 5, 5, 5, 5]
    expected13 = 10  # Rob any two non-adjacent: 5 + 5 = 10
    result13 = solution.rob(nums13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    
    # Test case 14: Complex pattern
    print("Test 14: Complex pattern")
    nums14 = [1, 3, 1, 3, 100]
    expected14 = 103  # Rob houses 1, 4: 3 + 100 = 103
    result14 = solution.rob(nums14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    
    # Test case 15: Compare all approaches
    print("Test 15: Compare all approaches")
    test_cases = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 3],
        [2, 1, 1, 2],
        [1, 3, 1, 3, 1],
    ]
    
    for nums in test_cases:
        result1 = solution.rob(nums)
        result2 = solution.rob_tabulation(nums)
        result3 = solution.rob_optimized(nums)
        result4 = solution.rob_iterative(nums)
        
        assert result1 == result2, f"Tabulation mismatch for {nums}: {result1} vs {result2}"
        assert result1 == result3, f"Optimized mismatch for {nums}: {result1} vs {result3}"
        assert result1 == result4, f"Iterative mismatch for {nums}: {result1} vs {result4}"
    
    # Test case 16: Large array
    print("Test 16: Large array")
    nums16 = [1] * 50 + [100]
    expected16 = 124  # Exclude first house, rob houses 1,3,5,...,47,50: 24 ones + 100 = 124
    result16 = solution.rob(nums16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    
    # Test case 17: First house is the only good one
    print("Test 17: First house is the only good one")
    nums17 = [100, 1, 1, 1, 1]
    expected17 = 101  # Rob houses 0, 2: 100 + 1 = 101
    result17 = solution.rob(nums17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()