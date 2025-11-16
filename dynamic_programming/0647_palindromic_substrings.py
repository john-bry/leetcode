"""
647. Palindromic Substrings
Difficulty: Medium

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Example 3:
Input: s = "racecar"
Output: 10
Explanation: Ten palindromic strings: "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Notes:
- Key insight: A palindrome expands around its center. There are two types:
  1. Odd length: center is a single character (e.g., "aba")
  2. Even length: center is between two characters (e.g., "abba")
- Expand around centers approach:
  - For each position, expand outward to find all palindromes centered there
  - Check both odd-length (center at i) and even-length (center between i and i+1) palindromes
  - Count each palindrome found
- Time complexity: O(n²) - n centers, each expansion takes O(n) in worst case
- Space complexity: O(1) - only using a few variables
- Alternative approach: Dynamic Programming - O(n²) time and space
- The expand around centers approach is optimal for space complexity.
"""


class Solution:
    def count_substrings(self, s: str) -> int:
        """
        Approach: Expand Around Center (Optimal for Space)
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        palindromes = 0

        def expand_substring(l, r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count

        for i in range(len(s)):
            # Count odd-length palindromes (center at i)
            palindromes += expand_substring(i, i)
            # Count even-length palindromes (center between i and i+1)
            palindromes += expand_substring(i, i + 1)

        return palindromes
    
    def count_substrings_dp(self, s: str) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        
        return count


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    s1 = "abc"
    result1 = solution.count_substrings(s1)
    expected1 = 3
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    s2 = "aaa"
    result2 = solution.count_substrings(s2)
    expected2 = 6
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    s3 = "racecar"
    result3 = solution.count_substrings(s3)
    expected3 = 10
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - single character
    s4 = "a"
    result4 = solution.count_substrings(s4)
    expected4 = 1
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - two characters, same
    s5 = "aa"
    result5 = solution.count_substrings(s5)
    expected5 = 3  # "a", "a", "aa"
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - two characters, different
    s6 = "ab"
    result6 = solution.count_substrings(s6)
    expected6 = 2  # "a", "b"
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - all same characters
    s7 = "aaaa"
    result7 = solution.count_substrings(s7)
    expected7 = 10  # All substrings are palindromes: 4 single, 3 double, 2 triple, 1 quadruple
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - no palindromes longer than 1
    s8 = "abcdef"
    result8 = solution.count_substrings(s8)
    expected8 = 6  # Only single characters
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
