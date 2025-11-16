"""
3. Longest Substring Without Repeating Characters
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Notes:
- Key insight: Use sliding window technique with a set to track characters in current window.
- Sliding window approach:
  - Use two pointers (left and right) to maintain a window
  - Expand window by moving right pointer
  - When duplicate found, shrink window from left until duplicate is removed
  - Track maximum window size
- Time complexity: O(n) - each character is visited at most twice (once by right pointer, once by left)
- Space complexity: O(min(n, m)) where m is the size of the character set (at most 26 for lowercase English)
- Alternative approach: Use hash map to store last index of each character for O(1) lookups.
- The sliding window approach is optimal for this problem.
"""


class Solution:
    def longest_substring_without_repeating_chars(self, s: str) -> int:
        """
        Approach: Sliding Window with Set (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is character set size
        """
        n = len(s)
        if n <= 1:
            return n

        max_substr, cur_substr = 1, 1
        l, r = 0, 0
        chars = set()

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            cur_substr = r - l + 1
            max_substr = max(max_substr, cur_substr)
            r += 1

        return max_substr
    
    def length_of_longest_substring_hash_map(self, s: str) -> int:
        """
        Approach: Sliding Window with Hash Map
        Time Complexity: O(n)
        Space Complexity: O(min(n, m))
        """
        char_map = {}
        max_len = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_map:
                # Move start pointer to after the last occurrence of current character
                start = max(start, char_map[s[end]] + 1)
            
            char_map[s[end]] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    s1 = "abcabcbb"
    result1 = solution.longest_substring_without_repeating_chars(s1)
    expected1 = 3
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    s2 = "bbbbb"
    result2 = solution.longest_substring_without_repeating_chars(s2)
    expected2 = 1
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    s3 = "pwwkew"
    result3 = solution.longest_substring_without_repeating_chars(s3)
    expected3 = 3
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - empty string
    s4 = ""
    result4 = solution.longest_substring_without_repeating_chars(s4)
    expected4 = 0
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - single character
    s5 = "a"
    result5 = solution.longest_substring_without_repeating_chars(s5)
    expected5 = 1
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - all unique characters
    s6 = "abcdef"
    result6 = solution.longest_substring_without_repeating_chars(s6)
    expected6 = 6
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - spaces and special characters
    s7 = "a b c d"
    result7 = solution.longest_substring_without_repeating_chars(s7)
    expected7 = 5  # "a b c" or " b c d"
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - repeating at end
    s8 = "dvdf"
    result8 = solution.longest_substring_without_repeating_chars(s8)
    expected8 = 3  # "vdf"
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()