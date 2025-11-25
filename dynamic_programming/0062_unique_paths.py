"""
62. Unique Paths
Difficulty: Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: m = 3, n = 7
Output: 28
Explanation: There are 28 unique paths from (0,0) to (2,6).

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6

Constraints:
- 1 <= m, n <= 100

Notes:
- Key insight: To reach (m-1, n-1), you need exactly (m-1) downs and (n-1) rights.
- This is a combinatorial problem: C(m+n-2, m-1) = C(m+n-2, n-1)
- DP approach: dp[i][j] = number of ways to reach (i, j)
- Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1] (can come from top or left)
- Base case: First row and column have only 1 path (all rights or all downs)
- Time complexity: O(m * n) for DP, O(min(m, n)) for mathematical approach
- Space complexity: 
  - 2D DP: O(m * n)
  - 1D DP: O(n) or O(m)
  - Mathematical: O(1)
- Alternative approaches:
  - 2D DP: O(m * n) time, O(m * n) space - current approach
  - 1D DP: O(m * n) time, O(min(m, n)) space - space optimized
  - Mathematical: O(min(m, n)) time, O(1) space - using combinations
  - Recursive with memo: O(m * n) time, O(m * n) space - top-down
- Edge cases: m=1, n=1, m=1, n>1, m>1, n=1
"""

from math import comb
from typing import Dict


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        """
        Approach 1: Dynamic Programming with 2D Array (Current)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Build a 2D DP table where dp[i][j] represents the number of ways
        to reach position (i, j) from (0, 0).
        """
        dp = [[0] * n for _ in range(m)]

        # Base case: first row - only one way (all rights)
        for j in range(n):
            dp[0][j] = 1

        # Base case: first column - only one way (all downs)
        for i in range(m):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    
    def unique_paths_space_optimized(self, m: int, n: int) -> int:
        """
        Approach 2: Space-Optimized DP (1D Array)
        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n))
        
        Use a 1D array instead of 2D. We only need the previous row.
        """
        # Use the smaller dimension for space optimization
        if m < n:
            m, n = n, m
        
        # dp[j] represents number of ways to reach current row, column j
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[n-1]
    
    def unique_paths_mathematical(self, m: int, n: int) -> int:
        """
        Approach 3: Mathematical (Combinatorial)
        Time Complexity: O(min(m, n))
        Space Complexity: O(1)
        
        To reach (m-1, n-1), we need (m-1) downs and (n-1) rights.
        Total moves = (m-1) + (n-1) = m + n - 2
        Number of ways = C(m+n-2, m-1) = C(m+n-2, n-1)
        """
        # Use min(m-1, n-1) for efficiency
        total_moves = m + n - 2
        choose = min(m - 1, n - 1)
        
        # Calculate combination: C(total_moves, choose)
        result = 1
        for i in range(choose):
            result = result * (total_moves - i) // (i + 1)
        
        return result
    
    def unique_paths_mathematical_comb(self, m: int, n: int) -> int:
        """
        Approach 4: Mathematical using math.comb (Python 3.8+)
        Time Complexity: O(min(m, n))
        Space Complexity: O(1)
        
        Same as approach 3 but using Python's built-in comb function.
        """
        return comb(m + n - 2, min(m - 1, n - 1))
    
    def unique_paths_recursive(self, m: int, n: int) -> int:
        """
        Approach 5: Recursive with Memoization
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) for memoization and recursion stack
        
        Top-down approach with memoization.
        """
        memo: Dict[tuple[int, int], int] = {}
        
        def dp(i: int, j: int) -> int:
            # Base case: reached destination
            if i == 0 and j == 0:
                return 1
            
            # Out of bounds
            if i < 0 or j < 0:
                return 0
            
            # Check memo
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Recurrence: can come from top or left
            memo[(i, j)] = dp(i-1, j) + dp(i, j-1)
            return memo[(i, j)]
        
        return dp(m-1, n-1)
    
    def unique_paths_alternative_dp(self, m: int, n: int) -> int:
        """
        Approach 6: Alternative DP Initialization
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Initialize entire grid to 1, then update inner cells.
        """
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example m=3, n=7
    print("Test 1: m=3, n=7")
    result1 = solution.unique_paths(3, 7)
    expected1 = 28
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: m=3, n=2
    print("Test 2: m=3, n=2")
    result2 = solution.unique_paths(3, 2)
    expected2 = 3
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: m=7, n=3
    print("Test 3: m=7, n=3")
    result3 = solution.unique_paths(7, 3)
    expected3 = 28
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: m=3, n=3
    print("Test 4: m=3, n=3")
    result4 = solution.unique_paths(3, 3)
    expected4 = 6
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single row m=1, n=7
    print("Test 5: Single row m=1, n=7")
    result5 = solution.unique_paths(1, 7)
    expected5 = 1
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Single column m=7, n=1
    print("Test 6: Single column m=7, n=1")
    result6 = solution.unique_paths(7, 1)
    expected6 = 1
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Single cell m=1, n=1
    print("Test 7: Single cell m=1, n=1")
    result7 = solution.unique_paths(1, 1)
    expected7 = 1
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Compare all approaches
    print("\nTest 8: Comparing all approaches")
    test_cases = [
        (3, 7),
        (3, 2),
        (7, 3),
        (3, 3),
        (1, 7),
        (7, 1),
        (1, 1),
        (5, 5),
        (10, 10),
    ]
    
    for m, n in test_cases:
        result1 = solution.unique_paths(m, n)
        result2 = solution.unique_paths_space_optimized(m, n)
        result3 = solution.unique_paths_mathematical(m, n)
        result4 = solution.unique_paths_mathematical_comb(m, n)
        result5 = solution.unique_paths_recursive(m, n)
        result6 = solution.unique_paths_alternative_dp(m, n)
        
        assert result1 == result2, f"Space optimized failed for m={m}, n={n}: {result1} vs {result2}"
        assert result1 == result3, f"Mathematical failed for m={m}, n={n}: {result1} vs {result3}"
        assert result1 == result4, f"Mathematical comb failed for m={m}, n={n}: {result1} vs {result4}"
        assert result1 == result5, f"Recursive failed for m={m}, n={n}: {result1} vs {result5}"
        assert result1 == result6, f"Alternative DP failed for m={m}, n={n}: {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 9: Large grid
    print("\nTest 9: Large grid m=10, n=10")
    result9 = solution.unique_paths(10, 10)
    expected9 = 48620
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Rectangular grid m=5, n=10
    print("Test 10: Rectangular grid m=5, n=10")
    result10 = solution.unique_paths(5, 10)
    expected10 = 715
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Very small grid m=2, n=2
    print("Test 11: Very small grid m=2, n=2")
    result11 = solution.unique_paths(2, 2)
    expected11 = 2
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Wide grid m=2, n=10
    print("Test 12: Wide grid m=2, n=10")
    result12 = solution.unique_paths(2, 10)
    expected12 = 10
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Tall grid m=10, n=2
    print("Test 13: Tall grid m=10, n=2")
    result13 = solution.unique_paths(10, 2)
    expected13 = 10
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Medium grid m=7, n=4
    print("Test 14: Medium grid m=7, n=4")
    result14 = solution.unique_paths(7, 4)
    expected14 = 84
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Verify mathematical formula
    print("Test 15: Verify mathematical formula")
    m15, n15 = 5, 6
    result15_dp = solution.unique_paths(m15, n15)
    result15_math = solution.unique_paths_mathematical(m15, n15)
    assert result15_dp == result15_math, f"Test 15 failed: DP={result15_dp}, Math={result15_math}"
    print(f"  Result: DP and Math match ({result15_dp}) ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()