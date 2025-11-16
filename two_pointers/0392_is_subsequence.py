"""
392. Is Subsequence
Difficulty: Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" is a subsequence of "ahbgdc" because we can find 'a', 'b', and 'c' in order in "ahbgdc".

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: "axc" is not a subsequence of "ahbgdc" because 'x' is not present in "ahbgdc".

Example 3:
Input: s = "", t = "ahbgdc"
Output: true
Explanation: An empty string is a subsequence of any string.

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.

Notes:
- Key insight: Use two pointers to traverse both strings simultaneously.
- Two pointers approach: 
  - Pointer i for string s, pointer j for string t
  - If characters match, advance both pointers
  - If they don't match, only advance pointer j in t
  - If we reach the end of s, it's a subsequence
- Time complexity: O(n) where n is the length of t
- Space complexity: O(1) - only using two pointers
- Alternative approach: Recursive solution, but less efficient.
- The two pointers approach is optimal and intuitive.
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        Approach: Two Pointers (Optimal)
        Time Complexity: O(n) where n is length of t
        Space Complexity: O(1)
        """
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
    
    def is_subsequence_recursive(self, s: str, t: str) -> bool:
        """
        Approach: Recursive
        Time Complexity: O(n) where n is length of t
        Space Complexity: O(n) - recursion stack
        """
        def helper(s_idx: int, t_idx: int) -> bool:
            if s_idx == len(s):
                return True
            if t_idx == len(t):
                return False
            
            if s[s_idx] == t[t_idx]:
                return helper(s_idx + 1, t_idx + 1)
            else:
                return helper(s_idx, t_idx + 1)
        
        return helper(0, 0)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    s1 = "abc"
    t1 = "ahbgdc"
    result1 = solution.is_subsequence(s1, t1)
    expected1 = True
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    s2 = "axc"
    t2 = "ahbgdc"
    result2 = solution.is_subsequence(s2, t2)
    expected2 = False
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3 - empty s
    s3 = ""
    t3 = "ahbgdc"
    result3 = solution.is_subsequence(s3, t3)
    expected3 = True
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - empty t
    s4 = "abc"
    t4 = ""
    result4 = solution.is_subsequence(s4, t4)
    expected4 = False
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - both empty
    s5 = ""
    t5 = ""
    result5 = solution.is_subsequence(s5, t5)
    expected5 = True
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - s is longer than t
    s6 = "abc"
    t6 = "ab"
    result6 = solution.is_subsequence(s6, t6)
    expected6 = False
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - same string
    s7 = "abc"
    t7 = "abc"
    result7 = solution.is_subsequence(s7, t7)
    expected7 = True
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - single character
    s8 = "a"
    t8 = "b"
    result8 = solution.is_subsequence(s8, t8)
    expected8 = False
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9 - single character match
    s9 = "a"
    t9 = "abc"
    result9 = solution.is_subsequence(s9, t9)
    expected9 = True
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10 - characters not in order
    s10 = "ace"
    t10 = "abcde"
    result10 = solution.is_subsequence(s10, t10)
    expected10 = True
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()