"""
Template for Dynamic Programming problems
"""

from typing import Dict, List, Optional


class Solution:
    """
    Problem: [Problem Name]
    Difficulty: Easy/Medium/Hard
    
    Problem Statement:
    [Describe the problem here]
    
    Example:
    Input: [example input]
    Output: [example output]
    Explanation: [explanation]
    """
    
    def top_down_memoization(self, n: int) -> int:
        """
        Approach 1: Top-down with memoization
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            
            # Base cases
            if i <= 1:
                return i
            
            # Recurrence relation
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)
    
    def bottom_up_tabulation(self, n: int) -> int:
        """
        Approach 2: Bottom-up with tabulation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def space_optimized(self, n: int) -> int:
        """
        Approach 3: Space-optimized DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    def knapsack_01(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        Approach 4: 0/1 Knapsack DP
        Time Complexity: O(n * capacity)
        Space Complexity: O(n * capacity)
        """
        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n][capacity]
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Approach 5: LCS DP
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Fibonacci
    n1 = 5
    expected1 = 5
    result1 = solution.top_down_memoization(n1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Knapsack
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    expected2 = 9
    result2 = solution.knapsack_01(weights, values, capacity)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: LCS
    text1 = "abcde"
    text2 = "ace"
    expected3 = 3
    result3 = solution.longest_common_subsequence(text1, text2)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
