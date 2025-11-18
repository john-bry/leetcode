"""
91. Decode Ways
Difficulty: Medium

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

Notes:
- Key insight: This is a dynamic programming problem similar to climbing stairs.
- At each position, we can either:
  1. Decode single digit (if not '0')
  2. Decode two digits (if between 10-26)
- Memoization approach: Top-down DP with memoization
- Time complexity: O(n) - each position is visited once
- Space complexity: O(n) - memoization dictionary and recursion stack
- Alternative approaches:
  - Tabulation (bottom-up): O(n) time, O(n) space
  - Space-optimized: O(n) time, O(1) space (only need last two values)
- Edge cases: Leading zeros, '0' in middle, valid two-digit numbers (10-26)
"""


class Solution:
    def num_decodings(self, s: str) -> int:
        """
        Approach: Memoization (Top-down DP)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        memo = {}
       
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            result = dp(i + 1)

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                result += dp(i + 2)

            memo[i] = result
            
            return result

        return dp(0)
    
    def num_decodings_tabulation(self, s: str) -> int:
        """
        Approach: Tabulation (Bottom-up DP)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has 1 way
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            # Single digit decode
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Two digit decode
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
    
    def num_decodings_optimized(self, s: str) -> int:
        """
        Approach: Space-Optimized DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2 = 1  # dp[i-2]
        prev1 = 1  # dp[i-1]
        
        for i in range(1, n):
            current = 0
            
            # Single digit decode
            if s[i] != '0':
                current += prev1
            
            # Two digit decode
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += prev2
            
            prev2, prev1 = prev1, current
        
        return prev1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    s1 = "12"
    result1 = solution.num_decodings(s1)
    expected1 = 2
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    s2 = "226"
    result2 = solution.num_decodings(s2)
    expected2 = 3
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    s3 = "06"
    result3 = solution.num_decodings(s3)
    expected3 = 0
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - single digit
    s4 = "1"
    result4 = solution.num_decodings(s4)
    expected4 = 1
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - leading zero
    s5 = "0"
    result5 = solution.num_decodings(s5)
    expected5 = 0
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - all valid two-digit
    s6 = "10"
    result6 = solution.num_decodings(s6)
    expected6 = 1  # Only "10" -> "J"
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - zero in middle
    s7 = "2101"
    result7 = solution.num_decodings(s7)
    expected7 = 1  # "21" -> "U", "01" invalid, so only one way
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - complex case
    s8 = "11106"
    result8 = solution.num_decodings(s8)
    expected8 = 2  # "1 1 10 6" or "11 10 6"
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9 - all single digits
    s9 = "1234"
    result9 = solution.num_decodings(s9)
    expected9 = 3  # "1 2 3 4", "12 3 4", "1 23 4"
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10 - invalid two-digit
    s10 = "27"
    result10 = solution.num_decodings(s10)
    expected10 = 1  # Only "2 7", "27" > 26 is invalid
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()