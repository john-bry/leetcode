"""
5. Longest Palindromic Substring
Difficulty: Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

Notes:
- Key insight: A palindrome expands around its center. There are two types:
  1. Odd length: center is a single character (e.g., "aba")
  2. Even length: center is between two characters (e.g., "abba")
- Expand around centers: For each position, expand outward checking if characters match.
- Time: O(n²) - n centers, each expansion takes O(n) in worst case.
- Space: O(1) - only store start and max_len.
- Alternative: DP approach uses O(n²) space but same time complexity.
- Manacher's algorithm: O(n) time but more complex to implement.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach 1: Expand Around Centers (Optimal for space)
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        For each position, expand outward to find longest palindrome.
        Check both odd-length (center at i) and even-length (center between i and i+1).
        """
        if not s:
            return ""

        start, max_len = 0, 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)  # Odd length palindrome
            len2 = self.expand(s, i, i + 1)  # Even length palindrome
            cur_len = max(len1, len2)

            if cur_len > max_len:
                max_len = cur_len
                start = i - (cur_len - 1) // 2

        return s[start : start + max_len]

    def expand(self, s, left, right):
        """Helper function to expand around center and return palindrome length"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
    
    def longest_palindrome_dp(self, s: str) -> str:
        """
        Approach 2: Dynamic Programming
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        
        Use DP table where dp[i][j] = True if s[i:j+1] is palindrome.
        Build from smaller substrings to larger ones.
        """
        if not s:
            return ""
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start : start + max_len]
    
    def longest_palindrome_brute_force(self, s: str) -> str:
        """
        Approach 3: Brute Force
        Time Complexity: O(n³)
        Space Complexity: O(1)
        
        Check all possible substrings and verify if they're palindromes.
        Not recommended for large inputs.
        """
        if not s:
            return ""
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        
        return longest
    
    def longest_palindrome_optimized(self, s: str) -> str:
        """
        Approach 4: Optimized Expand Around Centers
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        Similar to approach 1 but with cleaner code structure.
        """
        if not s:
            return ""
        
        def expand_around_center(left: int, right: int) -> tuple:
            """Returns (start, length) of longest palindrome from center"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now outside the palindrome
            start = left + 1
            length = right - left - 1
            return start, length
        
        start, max_len = 0, 1
        
        for i in range(len(s)):
            # Check odd-length palindromes (center at i)
            start1, len1 = expand_around_center(i, i)
            # Check even-length palindromes (center between i and i+1)
            start2, len2 = expand_around_center(i, i + 1)
            
            if len1 > max_len:
                start, max_len = start1, len1
            if len2 > max_len:
                start, max_len = start2, len2
        
        return s[start : start + max_len]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example")
    s1 = "babad"
    expected1 = "bab"  # or "aba"
    result1 = solution.longestPalindrome(s1)
    assert result1 in ["bab", "aba"], f"Test 1 failed: expected 'bab' or 'aba', got '{result1}'"
    
    # Test case 2: Even length palindrome
    print("Test 2: Even length palindrome")
    s2 = "cbbd"
    expected2 = "bb"
    result2 = solution.longestPalindrome(s2)
    assert result2 == expected2, f"Test 2 failed: expected '{expected2}', got '{result2}'"
    
    # Test case 3: Single character
    print("Test 3: Single character")
    s3 = "a"
    expected3 = "a"
    result3 = solution.longestPalindrome(s3)
    assert result3 == expected3, f"Test 3 failed: expected '{expected3}', got '{result3}'"
    
    # Test case 4: Two characters
    print("Test 4: Two characters")
    s4 = "ac"
    expected4 = "a"  # or "c"
    result4 = solution.longestPalindrome(s4)
    assert result4 in ["a", "c"], f"Test 4 failed: expected 'a' or 'c', got '{result4}'"
    
    # Test case 5: All same characters
    print("Test 5: All same characters")
    s5 = "aaaa"
    expected5 = "aaaa"
    result5 = solution.longestPalindrome(s5)
    assert result5 == expected5, f"Test 5 failed: expected '{expected5}', got '{result5}'"
    
    # Test case 6: No palindrome longer than 1
    print("Test 6: No palindrome longer than 1")
    s6 = "abc"
    expected6 = "a"  # or "b" or "c"
    result6 = solution.longestPalindrome(s6)
    assert len(result6) == 1 and result6 in s6, f"Test 6 failed: expected single char, got '{result6}'"
    
    # Test case 7: Palindrome at the end
    print("Test 7: Palindrome at the end")
    s7 = "racecar"
    expected7 = "racecar"
    result7 = solution.longestPalindrome(s7)
    assert result7 == expected7, f"Test 7 failed: expected '{expected7}', got '{result7}'"
    
    # Test case 8: Palindrome at the beginning
    print("Test 8: Palindrome at the beginning")
    s8 = "abccba"
    expected8 = "abccba"
    result8 = solution.longestPalindrome(s8)
    assert result8 == expected8, f"Test 8 failed: expected '{expected8}', got '{result8}'"
    
    # Test case 9: Multiple palindromes
    print("Test 9: Multiple palindromes")
    s9 = "aabbaa"
    expected9 = "aabbaa"
    result9 = solution.longestPalindrome(s9)
    assert result9 == expected9, f"Test 9 failed: expected '{expected9}', got '{result9}'"
    
    # Test case 10: Long string
    print("Test 10: Long string")
    s10 = "a" * 100 + "b" + "a" * 100
    expected10 = "a" * 100 + "b" + "a" * 100
    result10 = solution.longestPalindrome(s10)
    assert result10 == expected10, f"Test 10 failed: expected length {len(expected10)}, got length {len(result10)}"
    
    # Test case 11: Compare all approaches
    print("Test 11: Compare all approaches")
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "racecar",
        "abccba",
        "abc",
    ]
    
    for s in test_cases:
        result1 = solution.longestPalindrome(s)
        result2 = solution.longest_palindrome_dp(s)
        result3 = solution.longest_palindrome_optimized(s)
        
        # All should return palindromes of same length
        assert len(result1) == len(result2), f"DP mismatch for '{s}': {len(result1)} vs {len(result2)}"
        assert len(result1) == len(result3), f"Optimized mismatch for '{s}': {len(result1)} vs {len(result3)}"
        
        # Verify they are all palindromes
        assert result1 == result1[::-1], f"Result 1 not palindrome: '{result1}'"
        assert result2 == result2[::-1], f"Result 2 not palindrome: '{result2}'"
        assert result3 == result3[::-1], f"Result 3 not palindrome: '{result3}'"
    
    # Test case 12: Edge case - empty string
    print("Test 12: Edge case - empty string")
    s12 = ""
    expected12 = ""
    result12 = solution.longestPalindrome(s12)
    assert result12 == expected12, f"Test 12 failed: expected '{expected12}', got '{result12}'"
    
    # Test case 13: Numbers in string
    print("Test 13: Numbers in string")
    s13 = "12321"
    expected13 = "12321"
    result13 = solution.longestPalindrome(s13)
    assert result13 == expected13, f"Test 13 failed: expected '{expected13}', got '{result13}'"
    
    # Test case 14: Mixed characters
    print("Test 14: Mixed characters")
    s14 = "a1b2b1a"
    expected14 = "a1b2b1a"
    result14 = solution.longestPalindrome(s14)
    assert result14 == expected14, f"Test 14 failed: expected '{expected14}', got '{result14}'"
    
    # Test case 15: Palindrome in middle
    print("Test 15: Palindrome in middle")
    s15 = "xyzabccbaxyz"
    expected15 = "abccba"
    result15 = solution.longestPalindrome(s15)
    assert result15 == expected15, f"Test 15 failed: expected '{expected15}', got '{result15}'"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()