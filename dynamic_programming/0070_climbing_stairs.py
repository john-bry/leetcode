"""
70. Climbing Stairs
Difficulty: Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Example 3:
Input: n = 4
Output: 5
Explanation: There are five ways to climb to the top.
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 2 steps
3. 1 step + 2 steps + 1 step
4. 2 steps + 1 step + 1 step
5. 2 steps + 2 steps

Constraints:
- 1 <= n <= 45
"""

from typing import Dict


class Solution:
    def climb_stairs_recursive(self, n: int) -> int:
        """
        Approach 1: Recursive (Top-down)
        Time Complexity: O(2^n) - without memoization
        Space Complexity: O(n) - recursion stack
        """
        if n <= 2:
            return n
        
        return self.climb_stairs_recursive(n - 1) + self.climb_stairs_recursive(n - 2)
    
    def climb_stairs_memoization(self, n: int, memo: Dict[int, int] = None) -> int:
        """
        Approach 2: Recursive with Memoization
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 2:
            return n
        
        memo[n] = self.climb_stairs_memoization(n - 1, memo) + self.climb_stairs_memoization(n - 2, memo)
        return memo[n]
    
    def climb_stairs_tabulation(self, n: int) -> int:
        """
        Approach 3: Bottom-up Tabulation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def climb_stairs_optimized(self, n: int) -> int:
        """
        Approach 4: Space-Optimized DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    def climb_stairs_fibonacci(self, n: int) -> int:
        """
        Approach 5: Fibonacci Pattern Recognition
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        This problem follows the Fibonacci sequence:
        F(1) = 1, F(2) = 2, F(3) = 3, F(4) = 5, F(5) = 8, ...
        """
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: n = 2
    n1 = 2
    expected1 = 2
    result1 = solution.climb_stairs_optimized(n1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: n = 3
    n2 = 3
    expected2 = 3
    result2 = solution.climb_stairs_optimized(n2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: n = 4
    n3 = 4
    expected3 = 5
    result3 = solution.climb_stairs_optimized(n3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: n = 5
    n4 = 5
    expected4 = 8
    result4 = solution.climb_stairs_optimized(n4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: n = 1
    n5 = 1
    expected5 = 1
    result5 = solution.climb_stairs_optimized(n5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
