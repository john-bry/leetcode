"""
242. Valid Anagram
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings contain the same characters with the same frequencies.

Example 2:
Input: s = "rat", t = "car"
Output: false
Explanation: The strings have different characters.

Example 3:
Input: s = "a", t = "ab"
Output: false
Explanation: Different lengths.

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Notes:
- Key insight: Two strings are anagrams if they have the same character frequencies.
- Hash map approach: Count character frequencies in both strings and compare.
- Time complexity: O(n) where n is the length of the strings.
- Space complexity: O(k) where k is the number of unique characters (at most 26 for lowercase English letters).
- Alternative approaches:
  - Sorting: Sort both strings and compare - O(n log n) time, O(1) or O(n) space depending on implementation.
  - Counter: Use Python's Counter from collections - O(n) time, O(k) space, more Pythonic.
- Early return optimization: Check lengths first - if different, cannot be anagrams.
"""

from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """
        Approach: Hash Map (Character Frequency Counting)
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters
        """
        if len(s) != len(t):
            return False
        
        s_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] -= 1
            if s_dict[char] < 0:
                return False
        
        # Check all counts are zero
        return all(count == 0 for count in s_dict.values())
    
    def is_anagram_counter(self, s: str, t: str) -> bool:
        """
        Approach: Using Counter (More Pythonic)
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        return Counter(s) == Counter(t)
    
    def is_anagram_sort(self, s: str, t: str) -> bool:
        """
        Approach: Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(n) for sorted strings
        """
        return sorted(s) == sorted(t)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    result1 = solution.is_anagram(s1, t1)
    expected1 = True
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    result2 = solution.is_anagram(s2, t2)
    expected2 = False
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    s3 = "a"
    t3 = "ab"
    result3 = solution.is_anagram(s3, t3)
    expected3 = False
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - empty strings (edge case)
    s4 = ""
    t4 = ""
    result4 = solution.is_anagram(s4, t4)
    expected4 = True
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - same string
    s5 = "listen"
    t5 = "listen"
    result5 = solution.is_anagram(s5, t5)
    expected5 = True
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - different frequencies
    s6 = "aacc"
    t6 = "ccac"
    result6 = solution.is_anagram(s6, t6)
    expected6 = True
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - character not in first string
    s7 = "ab"
    t7 = "ac"
    result7 = solution.is_anagram(s7, t7)
    expected7 = False
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()