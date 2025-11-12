"""
198. House Robber
Difficulty: Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Example 3:
Input: nums = [2,1,1,2]
Output: 4
Explanation: Rob house 1 (money = 2) and house 4 (money = 2).

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Notes:
- Key insight: At each house, decide whether to rob it or skip it.
- If we rob house i, we can't rob house i-1, so we take nums[i] + max from houses 0 to i-2.
- If we skip house i, we take max from houses 0 to i-1.
- Recurrence: dp[i] = max(nums[i] + dp[i-2], dp[i-1])
- Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
"""

from typing import Dict, List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Approach 1: Memoization (Top-down DP)
        Time Complexity: O(n)
        Space Complexity: O(n) for memoization and recursion stack
        
        Use memoization to cache results of subproblems.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        memo = {}

        def helper(i):
            end = len(nums) - 1
            if i > end:
                return 0
            if i == end:
                return nums[end]
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + helper(i + 2), helper(i + 1))

            return memo[i]
        
        return helper(0)
    
    def robRecursive(self, nums: List[int]) -> int:
        """
        Approach 2: Recursive (Without Memoization)
        Time Complexity: O(2^n) - exponential, very slow
        Space Complexity: O(n) - recursion stack
        
        Pure recursive approach without memoization.
        Only for understanding - not recommended for production.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            return max(nums[i] + helper(i - 2), helper(i - 1))
        
        return helper(len(nums) - 1)
    
    def robTabulation(self, nums: List[int]) -> int:
        """
        Approach 3: Tabulation (Bottom-up DP)
        Time Complexity: O(n)
        Space Complexity: O(n) for DP array
        
        Build solution from bottom up using a DP array.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[n - 1]
    
    def robOptimized(self, nums: List[int]) -> int:
        """
        Approach 4: Space-Optimized DP (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Only need to track the last two values instead of entire array.
        Most efficient approach.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 = max profit up to i-2, prev1 = max profit up to i-1
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, current
        
        return prev1
    
    def robIterative(self, nums: List[int]) -> int:
        """
        Approach 5: Iterative with Two Variables
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Alternative space-optimized approach using two variables.
        """
        if not nums:
            return 0
        
        rob_prev = 0  # Max profit if we rob previous house
        rob_current = 0  # Max profit if we rob current house
        
        for num in nums:
            # Either rob current house (can't rob previous) or skip current
            rob_prev, rob_current = rob_current, max(rob_current, rob_prev + num)
        
        return rob_current
    
    def robMemoizationHelper(self, nums: List[int]) -> int:
        """
        Approach 6: Memoization with Helper Function (Cleaner)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Cleaner version of memoization approach.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        memo: Dict[int, int] = {}
        
        def helper(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
            return memo[i]
        
        return helper(len(nums) - 1)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example")
    nums1 = [1, 2, 3, 1]
    expected1 = 4
    result1 = solution.rob(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Another example
    print("Test 2: Another example")
    nums2 = [2, 7, 9, 3, 1]
    expected2 = 12
    result2 = solution.rob(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Adjacent houses with same value
    print("Test 3: Adjacent houses with same value")
    nums3 = [2, 1, 1, 2]
    expected3 = 4
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
    
    # Test case 7: Increasing values
    print("Test 7: Increasing values")
    nums7 = [1, 2, 3, 4, 5]
    expected7 = 9  # Rob houses 1, 3, 5
    result7 = solution.rob(nums7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: Decreasing values
    print("Test 8: Decreasing values")
    nums8 = [5, 4, 3, 2, 1]
    expected8 = 9  # Rob houses 0, 2, 4
    result8 = solution.rob(nums8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Compare all approaches
    print("Test 9: Compare all approaches")
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
        [1, 2, 3, 4, 5],
    ]
    
    for nums in test_cases:
        result1 = solution.rob(nums)
        result2 = solution.robTabulation(nums)
        result3 = solution.robOptimized(nums)
        result4 = solution.robIterative(nums)
        result5 = solution.robMemoizationHelper(nums)
        
        # Skip recursive for larger inputs (too slow)
        if len(nums) <= 5:
            result6 = solution.robRecursive(nums)
            assert result1 == result6, f"Recursive mismatch for {nums}"
        
        assert result1 == result2, f"Tabulation mismatch for {nums}: {result1} vs {result2}"
        assert result1 == result3, f"Optimized mismatch for {nums}: {result1} vs {result3}"
        assert result1 == result4, f"Iterative mismatch for {nums}: {result1} vs {result4}"
        assert result1 == result5, f"Memoization helper mismatch for {nums}: {result1} vs {result5}"
    
    # Test case 10: Edge case - empty array
    print("Test 10: Edge case - empty array")
    nums10 = []
    expected10 = 0
    result10 = solution.rob(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    # Test case 11: Large values
    print("Test 11: Large values")
    nums11 = [100, 200, 300, 100, 200]
    expected11 = 500  # Rob houses 0, 2, 4
    result11 = solution.rob(nums11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    
    # Test case 12: Alternating pattern
    print("Test 12: Alternating pattern")
    nums12 = [1, 3, 1, 3, 1, 3]
    expected12 = 9  # Rob houses 1, 3, 5
    result12 = solution.rob(nums12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    
    # Test case 13: First house is best
    print("Test 13: First house is best")
    nums13 = [10, 1, 1, 1]
    expected13 = 11  # Rob houses 0, 3
    result13 = solution.rob(nums13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    
    # Test case 14: Last house is best
    print("Test 14: Last house is best")
    nums14 = [1, 1, 1, 10]
    expected14 = 11  # Rob houses 0, 3
    result14 = solution.rob(nums14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    
    # Test case 15: Complex pattern
    print("Test 15: Complex pattern")
    nums15 = [6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3]
    expected15 = 39  # Rob houses 0, 2, 5, 8, 10
    result15 = solution.rob(nums15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()