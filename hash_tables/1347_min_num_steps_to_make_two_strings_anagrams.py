"""
1347. Minimum Number of Steps to Make Two Strings Anagrams
Difficulty: Medium

You are given two strings s and t. In one step, you can append any character to either string.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, or t = "bba" which is anagram of s = "bab".

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams of each other.

Constraints:
- 1 <= s.length <= 5 * 10^4
- s.length == t.length
- s and t consist of lowercase English letters only.

Notes:
- Key insight: Count character frequencies in both strings. The minimum steps needed is the sum of 
  differences where s has more occurrences than t for each character.
- We only need to count characters where s has MORE occurrences than t, because we can only add/change 
  characters in t (not remove, but we can replace).
- Actually, since we can only append characters, we need to add characters to t to match s's frequencies.
- Wait, re-reading: "In one step, you can append any character to either string" - but the examples 
  show replacement. Let me reconsider...
- Actually, the problem allows us to change characters in t. The minimum steps = sum of (s_count[char] - t_count[char]) 
  for all chars where s_count[char] > t_count[char].
- Time complexity: O(n) where n is length of strings
- Space complexity: O(1) for alphabet size (26 letters), O(n) for counters
- Alternative approaches:
  - Counter approach: O(n) time, O(1) space - current approach
  - Manual dictionary: O(n) time, O(1) space - use dict instead of Counter
  - Single pass with difference: O(n) time, O(1) space - count differences directly
  - Two-pass approach: O(n) time, O(1) space - count s, then count t and subtract
  - Using arrays: O(n) time, O(1) space - use array[26] instead of dict
- Edge cases: Same strings, completely different characters, one character strings, all same character
"""

from collections import Counter
from typing import Dict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Approach 1: Counter Approach (Current)
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        Count character frequencies in both strings, then sum the differences
        where s has more occurrences than t.
        """
        s_count = Counter(s)
        t_count = Counter(t)
        min_steps = 0

        for char in s_count:
            if s_count[char] > t_count.get(char, 0):
                min_steps += s_count[char] - t_count.get(char, 0)

        return min_steps
    
    def minStepsManualDict(self, s: str, t: str) -> int:
        """
        Approach 2: Manual Dictionary
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        Use manual dictionary instead of Counter.
        """
        s_count: Dict[str, int] = {}
        t_count: Dict[str, int] = {}
        
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        min_steps = 0
        for char in s_count:
            if s_count[char] > t_count.get(char, 0):
                min_steps += s_count[char] - t_count.get(char, 0)
        
        return min_steps
    
    def minStepsSinglePass(self, s: str, t: str) -> int:
        """
        Approach 3: Single Pass with Difference Counting
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        Count differences in a single pass by incrementing for s and decrementing for t.
        """
        count = Counter(s)
        
        # Subtract counts from t
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        # Sum only positive differences (where s has more)
        min_steps = sum(diff for diff in count.values() if diff > 0)
        
        return min_steps
    
    def minStepsArray(self, s: str, t: str) -> int:
        """
        Approach 4: Array-Based Counting
        Time Complexity: O(n)
        Space Complexity: O(1) - fixed size array
        
        Use array of size 26 instead of dictionary for better space efficiency.
        """
        s_count = [0] * 26
        t_count = [0] * 26
        
        for char in s:
            s_count[ord(char) - ord('a')] += 1
        
        for char in t:
            t_count[ord(char) - ord('a')] += 1
        
        min_steps = 0
        for i in range(26):
            if s_count[i] > t_count[i]:
                min_steps += s_count[i] - t_count[i]
        
        return min_steps
    
    def minStepsAlternative(self, s: str, t: str) -> int:
        """
        Approach 5: Alternative Counter Logic
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        Alternative way to calculate using Counter operations.
        """
        s_count = Counter(s)
        t_count = Counter(t)
        
        # Calculate difference: s_count - t_count (only positive)
        diff = s_count - t_count
        return sum(diff.values())
    
    def minStepsTwoPass(self, s: str, t: str) -> int:
        """
        Approach 6: Two-Pass Explicit
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        More explicit two-pass approach with clearer variable names.
        """
        s_freq = {}
        t_freq = {}
        
        # First pass: count s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        # Second pass: count t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        # Calculate minimum steps
        steps = 0
        for char, count in s_freq.items():
            t_char_count = t_freq.get(char, 0)
            if count > t_char_count:
                steps += count - t_char_count
        
        return steps
    
    def min_steps(self, s: str, t: str) -> int:
        """
        Approach 7: Original Implementation
        Time Complexity: O(n)
        Space Complexity: O(1) for alphabet size
        
        Original implementation with same logic as Approach 1.
        """
        s_count = Counter(s)
        t_count = Counter(t)
        min_steps = 0

        for char in s_count:
            if s_count[char] > t_count.get(char, 0):
                min_steps += s_count[char] - t_count.get(char, 0)

        return min_steps


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example s=\"bab\", t=\"aba\"")
    s1, t1 = "bab", "aba"
    expected1 = 1
    result1 = solution.minSteps(s1, t1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Another example
    print("Test 2: Another example s=\"leetcode\", t=\"practice\"")
    s2, t2 = "leetcode", "practice"
    expected2 = 5
    result2 = solution.minSteps(s2, t2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Already anagrams
    print("Test 3: Already anagrams s=\"anagram\", t=\"mangaar\"")
    s3, t3 = "anagram", "mangaar"
    expected3 = 0
    result3 = solution.minSteps(s3, t3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Same strings
    print("Test 4: Same strings s=\"abc\", t=\"abc\"")
    s4, t4 = "abc", "abc"
    expected4 = 0
    result4 = solution.minSteps(s4, t4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single character
    print("Test 5: Single character s=\"a\", t=\"a\"")
    s5, t5 = "a", "a"
    expected5 = 0
    result5 = solution.minSteps(s5, t5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        ("bab", "aba"),
        ("leetcode", "practice"),
        ("anagram", "mangaar"),
        ("abc", "abc"),
        ("a", "a"),
        ("abc", "def"),
    ]
    
    for s, t in test_cases:
        result1 = solution.minSteps(s, t)
        result2 = solution.minStepsManualDict(s, t)
        result3 = solution.minStepsSinglePass(s, t)
        result4 = solution.minStepsArray(s, t)
        result5 = solution.minStepsAlternative(s, t)
        result6 = solution.minStepsTwoPass(s, t)
        result7 = solution.min_steps(s, t)
        
        assert result1 == result2, f"Manual dict failed for s={s}, t={t}: {result1} vs {result2}"
        assert result1 == result3, f"Single pass failed for s={s}, t={t}: {result1} vs {result3}"
        assert result1 == result4, f"Array failed for s={s}, t={t}: {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed for s={s}, t={t}: {result1} vs {result5}"
        assert result1 == result6, f"Two pass failed for s={s}, t={t}: {result1} vs {result6}"
        assert result1 == result7, f"Original failed for s={s}, t={t}: {result1} vs {result7}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: Completely different characters
    print("\nTest 7: Completely different s=\"abc\", t=\"def\"")
    s7, t7 = "abc", "def"
    expected7 = 3  # All 3 characters need to be changed
    result7 = solution.minSteps(s7, t7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: One character different
    print("Test 8: One character different s=\"abc\", t=\"abd\"")
    s8, t8 = "abc", "abd"
    expected8 = 1  # 'c' needs to be changed to 'c' (but 'd' in t needs to be 'c')
    result8 = solution.minSteps(s8, t8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: All same character
    print("Test 9: All same character s=\"aaa\", t=\"aaa\"")
    s9, t9 = "aaa", "aaa"
    expected9 = 0
    result9 = solution.minSteps(s9, t9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Different frequencies
    print("Test 10: Different frequencies s=\"aabb\", t=\"ab\"")
    s10, t10 = "aabb", "ab"
    expected10 = 2  # Need 2 more 'a' and 2 more 'b'... wait, strings are same length
    # Actually, if lengths are same, we need to replace characters
    # s has 2 a's and 2 b's, t has 1 a and 1 b
    # So we need to change 1 character in t to 'a' and 1 to 'b' = 2 steps
    result10 = solution.minSteps(s10, t10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Multiple occurrences
    print("Test 11: Multiple occurrences s=\"aabbcc\", t=\"abcabc\"")
    s11, t11 = "aabbcc", "abcabc"
    expected11 = 0  # Both have 2 a's, 2 b's, 2 c's
    result11 = solution.minSteps(s11, t11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Complex case
    print("Test 12: Complex case s=\"friend\", t=\"family\"")
    s12, t12 = "friend", "family"
    result12 = solution.minSteps(s12, t12)
    # s: f=1, r=1, i=1, e=1, n=1, d=1
    # t: f=1, a=1, m=1, i=1, l=1, y=1
    # Need: r, e, n (3 chars) but t has a, m, l, y (4 chars) that s doesn't have
    # Actually, we only count where s has more: r, e, n = 3
    expected12 = 3
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Repeated characters
    print("Test 13: Repeated characters s=\"aab\", t=\"abb\"")
    s13, t13 = "aab", "abb"
    # s: a=2, b=1
    # t: a=1, b=2
    # s has 1 more 'a', t has 1 more 'b'
    # We need to change 1 'b' in t to 'a' = 1 step
    expected13 = 1
    result13 = solution.minSteps(s13, t13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: All different
    print("Test 14: All different s=\"abcd\", t=\"efgh\"")
    s14, t14 = "abcd", "efgh"
    expected14 = 4  # All 4 characters need to be changed
    result14 = solution.minSteps(s14, t14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Large difference
    print("Test 15: Large difference s=\"aaaa\", t=\"bbbb\"")
    s15, t15 = "aaaa", "bbbb"
    expected15 = 4  # All 4 'b's need to be changed to 'a's
    result15 = solution.minSteps(s15, t15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Partial match
    print("Test 16: Partial match s=\"abcde\", t=\"abcfg\"")
    s16, t16 = "abcde", "abcfg"
    # s: a=1, b=1, c=1, d=1, e=1
    # t: a=1, b=1, c=1, f=1, g=1
    # s has d and e, t has f and g
    # Need to change f and g to d and e = 2 steps
    expected16 = 2
    result16 = solution.minSteps(s16, t16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    # Test case 17: Same characters different order
    print("Test 17: Same characters different order s=\"listen\", t=\"silent\"")
    s17, t17 = "listen", "silent"
    expected17 = 0  # Anagrams
    result17 = solution.minSteps(s17, t17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    print(f"  Result: {result17} ✓")
    
    # Test case 18: One extra character
    print("Test 18: One extra character s=\"abc\", t=\"abcd\"")
    # Wait, constraint says s.length == t.length, so this shouldn't happen
    # Let me use a valid case instead
    print("Test 18: Different distribution s=\"aabb\", t=\"abab\"")
    s18, t18 = "aabb", "abab"
    expected18 = 0  # Same character counts
    result18 = solution.minSteps(s18, t18)
    assert result18 == expected18, f"Test 18 failed: expected {expected18}, got {result18}"
    print(f"  Result: {result18} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
