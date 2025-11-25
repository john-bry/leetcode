"""
1143. Longest Common Subsequence
Difficulty: Medium

Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Notes:
- Key insight: If characters match, include in LCS and recurse on remaining strings.
  If they don't match, take max of excluding one character from each string.
- Recurrence relation:
  - If text1[i] == text2[j]: dp[i][j] = 1 + dp[i-1][j-1]
  - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Time complexity: O(m * n) where m and n are lengths of strings
- Space complexity:
  - 2D DP: O(m * n)
  - 1D DP: O(min(m, n))
  - Memoization: O(m * n)
- Alternative approaches:
  - Memoization (top-down): O(m * n) time, O(m * n) space - current
  - Tabulation (bottom-up): O(m * n) time, O(m * n) space - standard approach
  - Space-optimized: O(m * n) time, O(min(m, n)) space - use 1D array
  - Recursive without memo: O(2^(m+n)) time - exponential, for comparison only
- Edge cases: Empty strings, identical strings, no common subsequence, single character
"""

from typing import Dict


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Approach 1: Dynamic Programming with Memoization (Current)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Top-down approach with memoization.
        Recursively solve subproblems and cache results.
        """
        memo = {}

        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                result = 1 + dp(i - 1, j - 1)
            else:
                result = max(dp(i - 1, j), dp(i, j - 1))

            memo[(i, j)] = result
            return result

        return dp(len(text1) - 1, len(text2) - 1)
    
    def longest_common_subsequence_tabulation(self, text1: str, text2: str) -> int:
        """
        Approach 2: Tabulation (Bottom-up DP)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Build DP table from bottom up.
        dp[i][j] = LCS of text1[0:i] and text2[0:j]
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    def longest_common_subsequence_space_optimized(self, text1: str, text2: str) -> int:
        """
        Approach 3: Space-Optimized DP (1D Array)
        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n))
        
        Use 1D array instead of 2D. Only need previous row.
        """
        m, n = len(text1), len(text2)
        
        # Use smaller string for space optimization
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        
        # dp[j] represents LCS of current row, column j
        prev = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        
        return prev[n]
    
    def longest_common_subsequence_recursive(self, text1: str, text2: str) -> int:
        """
        Approach 4: Recursive without Memoization (Inefficient)
        Time Complexity: O(2^(m+n)) - exponential
        Space Complexity: O(m + n) for recursion stack
        
        Pure recursive approach without memoization.
        Only for understanding - not recommended for production.
        """
        def lcs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + lcs(i - 1, j - 1)
            else:
                return max(lcs(i - 1, j), lcs(i, j - 1))
        
        return lcs(len(text1) - 1, len(text2) - 1)
    
    def longest_common_subsequence_alternative(self, text1: str, text2: str) -> int:
        """
        Approach 5: Alternative Tabulation Structure
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Same as tabulation but with explicit base case handling.
        """
        m, n = len(text1), len(text2)
        
        # Initialize with base cases
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match - extend LCS
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters don't match - take max of excluding one
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    def longest_common_subsequence_optimized_2d(self, text1: str, text2: str) -> int:
        """
        Approach 6: Space-Optimized with Two Rows
        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n))
        
        Maintain only two rows (previous and current) instead of full 2D table.
        """
        m, n = len(text1), len(text2)
        
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        
        prev_row = [0] * (n + 1)
        curr_row = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    curr_row[j] = prev_row[j-1] + 1
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j-1])
            prev_row, curr_row = curr_row, prev_row
            curr_row = [0] * (n + 1)  # Reset current row
        
        return prev_row[n]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: text1='abcde', text2='ace'")
    result1 = solution.longest_common_subsequence("abcde", "ace")
    expected1 = 3  # "ace"
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Identical strings
    print("Test 2: text1='abc', text2='abc'")
    result2 = solution.longest_common_subsequence("abc", "abc")
    expected2 = 3  # "abc"
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: No common subsequence
    print("Test 3: text1='abc', text2='def'")
    result3 = solution.longest_common_subsequence("abc", "def")
    expected3 = 0
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: One character common
    print("Test 4: text1='abc', text2='defa'")
    result4 = solution.longest_common_subsequence("abc", "defa")
    expected4 = 1  # "a"
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Empty string
    print("Test 5: text1='', text2='abc'")
    result5 = solution.longest_common_subsequence("", "abc")
    expected5 = 0
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Both empty
    print("Test 6: text1='', text2=''")
    result6 = solution.longest_common_subsequence("", "")
    expected6 = 0
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Single character strings
    print("Test 7: text1='a', text2='a'")
    result7 = solution.longest_common_subsequence("a", "a")
    expected7 = 1
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Single character different
    print("Test 8: text1='a', text2='b'")
    result8 = solution.longest_common_subsequence("a", "b")
    expected8 = 0
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Compare all approaches
    print("\nTest 9: Comparing all approaches")
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("abc", "defa"),
        ("", "abc"),
        ("a", "a"),
        ("abcdef", "ace"),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"),
    ]
    
    for text1, text2 in test_cases:
        result1 = solution.longest_common_subsequence(text1, text2)
        result2 = solution.longest_common_subsequence_tabulation(text1, text2)
        result3 = solution.longest_common_subsequence_space_optimized(text1, text2)
        result4 = solution.longest_common_subsequence_alternative(text1, text2)
        result5 = solution.longest_common_subsequence_optimized_2d(text1, text2)
        
        # Skip recursive for longer strings (too slow)
        if len(text1) <= 10 and len(text2) <= 10:
            result6 = solution.longest_common_subsequence_recursive(text1, text2)
            assert result1 == result6, f"Recursive failed for '{text1}' and '{text2}': {result1} vs {result6}"
        
        assert result1 == result2, f"Tabulation failed for '{text1}' and '{text2}': {result1} vs {result2}"
        assert result1 == result3, f"Space optimized failed for '{text1}' and '{text2}': {result1} vs {result3}"
        assert result1 == result4, f"Alternative failed for '{text1}' and '{text2}': {result1} vs {result4}"
        assert result1 == result5, f"Optimized 2D failed for '{text1}' and '{text2}': {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 10: Long strings
    print("\nTest 10: Long strings")
    text1_10 = "abcdefghijklmnopqrstuvwxyz"
    text2_10 = "acegikmoqsuwy"
    result10 = solution.longest_common_subsequence(text1_10, text2_10)
    expected10 = 13  # "acegikmoqsuwy"
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Reversed strings
    print("Test 11: Reversed strings")
    text1_11 = "abc"
    text2_11 = "cba"
    result11 = solution.longest_common_subsequence(text1_11, text2_11)
    expected11 = 1  # "a" or "b" or "c"
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: One string is substring
    print("Test 12: One string is substring")
    text1_12 = "abcdef"
    text2_12 = "bcd"
    result12 = solution.longest_common_subsequence(text1_12, text2_12)
    expected12 = 3  # "bcd"
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: All same characters
    print("Test 13: All same characters")
    text1_13 = "aaaa"
    text2_13 = "aaa"
    result13 = solution.longest_common_subsequence(text1_13, text2_13)
    expected13 = 3  # "aaa"
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Complex case
    print("Test 14: Complex case")
    text1_14 = "oxcpqrsvwf"
    text2_14 = "shmtulqrypy"
    result14 = solution.longest_common_subsequence(text1_14, text2_14)
    expected14 = 2  # "qr" or similar
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Different lengths
    print("Test 15: Different lengths")
    text1_15 = "abc"
    text2_15 = "abcdefgh"
    result15 = solution.longest_common_subsequence(text1_15, text2_15)
    expected15 = 3  # "abc"
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()