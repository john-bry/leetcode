"""
387. First Unique Character in a String
Difficulty: Easy

Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur 
more than once.

Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: The character 'v' at index 2 is the first character that does not occur 
more than once.

Example 3:
Input: s = "aabb"
Output: -1
Explanation: There is no character that does not occur more than once.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.

Notes:
- Key insight: We need to find the first character that appears exactly once.
- Two-pass approach is common:
  - First pass: Count frequency of each character
  - Second pass: Find first character with frequency 1
- Time complexity: O(n) where n is length of string
- Space complexity: O(1) or O(k) where k is number of unique characters (at most 26 for lowercase)
- Edge cases: All characters repeated, single character, all unique characters
- Alternative approaches:
  - Counter (collections): Clean and Pythonic, O(n) time, O(k) space
  - Dictionary manually: More control, O(n) time, O(k) space
  - Two-pass with dict: Count then find, O(n) time, O(k) space
  - Single pass with dict tracking indices: O(n) time, O(k) space
  - Using index() and rindex(): O(n²) time, O(1) space (inefficient for large strings)
  - OrderedDict: Maintains insertion order, O(n) time, O(k) space
"""

from collections import Counter, OrderedDict


class Solution:
    def first_unique_char(self, s: str) -> int:
        """
        Approach 1: Counter (Current)
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters (at most 26)
        
        Use Counter to count frequencies, then find first character with count 1.
        """
        count = Counter(s)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
            
        return -1
    
    def first_unique_char_dict(self, s: str) -> int:
        """
        Approach 2: Dictionary (Manual)
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters
        
        Manually build frequency dictionary, then find first character with count 1.
        More explicit than Counter.
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1
    
    def first_unique_char_single_pass(self, s: str) -> int:
        """
        Approach 3: Single Pass with Index Tracking
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters
        
        Track first occurrence index and count in one pass.
        Then find minimum index among characters with count 1.
        """
        char_info = {}  # {char: [count, first_index]}
        
        for i, char in enumerate(s):
            if char not in char_info:
                char_info[char] = [1, i]
            else:
                char_info[char][0] += 1
        
        # Find minimum index among characters with count 1
        min_index = float('inf')
        for char, (count, index) in char_info.items():
            if count == 1:
                min_index = min(min_index, index)
        
        return min_index if min_index != float('inf') else -1
    
    def first_unique_char_ordered_dict(self, s: str) -> int:
        """
        Approach 4: OrderedDict
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters
        
        Use OrderedDict to maintain insertion order while counting.
        Then iterate through OrderedDict to find first character with count 1.
        """
        count = OrderedDict()
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1
    
    def first_unique_char_index_method(self, s: str) -> int:
        """
        Approach 5: Using index() and rindex()
        Time Complexity: O(n²) worst case
        Space Complexity: O(1)
        
        For each character, check if first index equals last index.
        If they're equal, character appears only once.
        Note: This is less efficient for large strings.
        """
        for i, char in enumerate(s):
            if s.index(char) == s.rindex(char):
                return i
        return -1
    
    def first_unique_char_optimized(self, s: str) -> int:
        """
        Approach 6: Optimized Two-Pass
        Time Complexity: O(n)
        Space Complexity: O(1) - fixed size array for 26 letters
        
        Use fixed-size array instead of dictionary for better space efficiency.
        Since we only have lowercase letters, we can use array of size 26.
        """
        # Array to store frequency of each character (a-z)
        freq = [0] * 26
        
        # First pass: count frequencies
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Second pass: find first character with frequency 1
        for i, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return i
        
        return -1
    
    def first_unique_char_set_approach(self, s: str) -> int:
        """
        Approach 7: Using Set for Seen Characters
        Time Complexity: O(n)
        Space Complexity: O(k) where k is number of unique characters
        
        Track seen characters and characters that appear more than once.
        Then find first character not in either set.
        """
        seen = set()
        repeated = set()
        
        for char in s:
            if char in seen:
                repeated.add(char)
            seen.add(char)
        
        for i, char in enumerate(s):
            if char not in repeated:
                return i
        
        return -1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example - 'leetcode'")
    s1 = "leetcode"
    expected1 = 0
    result1 = solution.first_unique_char(s1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Character in middle
    print("Test 2: Character in middle - 'loveleetcode'")
    s2 = "loveleetcode"
    expected2 = 2
    result2 = solution.first_unique_char(s2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: No unique character
    print("Test 3: No unique character - 'aabb'")
    s3 = "aabb"
    expected3 = -1
    result3 = solution.first_unique_char(s3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single character
    print("Test 4: Single character - 'a'")
    s4 = "a"
    expected4 = 0
    result4 = solution.first_unique_char(s4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All unique characters
    print("Test 5: All unique characters - 'abcde'")
    s5 = "abcde"
    expected5 = 0
    result5 = solution.first_unique_char(s5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Unique character at end
    print("Test 6: Unique character at end - 'aabbc'")
    s6 = "aabbc"
    expected6 = 4
    result6 = solution.first_unique_char(s6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Multiple unique characters (return first)
    print("Test 7: Multiple unique characters - 'abccba'")
    s7 = "abccba"
    expected7 = -1
    result7 = solution.first_unique_char(s7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Two characters, one unique
    print("Test 8: Two characters, one unique - 'ab'")
    s8 = "ab"
    expected8 = 0
    result8 = solution.first_unique_char(s8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Repeated pattern
    print("Test 9: Repeated pattern - 'aabbcc'")
    s9 = "aabbcc"
    expected9 = -1
    result9 = solution.first_unique_char(s9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Unique in middle of repeats
    print("Test 10: Unique in middle - 'aabcc'")
    s10 = "aabcc"
    expected10 = 2
    result10 = solution.first_unique_char(s10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Compare all approaches
    print("\nTest 11: Comparing all approaches")
    test_cases = [
        "leetcode",
        "loveleetcode",
        "aabb",
        "a",
        "abcde",
        "aabbc",
        "abccba",
        "ab",
        "aabbcc",
        "aabcc",
        "z",
        "zz",
        "abcdefghijklmnopqrstuvwxyz",
        "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",
    ]
    
    for s in test_cases:
        result1 = solution.first_unique_char(s)
        result2 = solution.first_unique_char_dict(s)
        result3 = solution.first_unique_char_single_pass(s)
        result4 = solution.first_unique_char_ordered_dict(s)
        result5 = solution.first_unique_char_index_method(s)
        result6 = solution.first_unique_char_optimized(s)
        result7 = solution.first_unique_char_set_approach(s)
        
        assert result1 == result2, f"Dict mismatch for '{s}': {result1} vs {result2}"
        assert result1 == result3, f"Single pass mismatch for '{s}': {result1} vs {result3}"
        assert result1 == result4, f"OrderedDict mismatch for '{s}': {result1} vs {result4}"
        assert result1 == result5, f"Index method mismatch for '{s}': {result1} vs {result5}"
        assert result1 == result6, f"Optimized mismatch for '{s}': {result1} vs {result6}"
        assert result1 == result7, f"Set approach mismatch for '{s}': {result1} vs {result7}"
    
    print("  All approaches match! ✓")
    
    # Test case 12: Long string with unique at end
    print("\nTest 12: Long string with unique at end")
    s12 = "a" * 1000 + "b"
    expected12 = 1000
    result12 = solution.first_unique_char(s12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Long string with unique at start
    print("Test 13: Long string with unique at start")
    s13 = "a" + "b" * 1000
    expected13 = 0
    result13 = solution.first_unique_char(s13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Alternating pattern
    print("Test 14: Alternating pattern - 'ababab'")
    s14 = "ababab"
    expected14 = -1
    result14 = solution.first_unique_char(s14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: All same character
    print("Test 15: All same character - 'aaaa'")
    s15 = "aaaa"
    expected15 = -1
    result15 = solution.first_unique_char(s15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Unique character after many repeats
    print("Test 16: Unique after repeats - 'aaabbbcccde'")
    s16 = "aaabbbcccde"
    expected16 = 9
    result16 = solution.first_unique_char(s16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()