"""
567. Permutation in String
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Example 3:
Input: s1 = "abc", s2 = "dcba"
Output: true
Explanation: s2 contains "cba" which is a permutation of "abc".

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Notes:
- Key insight: Use sliding window technique to check if any window in s2 has the same character frequency as s1.
- Instead of checking all permutations (O(n!)), check character frequencies (O(n)).
- Optimize by maintaining a sliding window frequency map instead of recalculating for each window.
- Use two frequency maps: one for s1 (target) and one for the current window in s2.
- When window slides, update frequency map by removing leftmost character and adding rightmost character.
"""

from collections import Counter, defaultdict


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """
        Approach 1: Sliding Window with Counter Comparison (Current Implementation)
        Time Complexity: O(n * m) where n = len(s2), m = len(s1)
        Space Complexity: O(m) for the Counter objects
        
        For each window position, create a Counter and compare with s1's Counter.
        This is inefficient because we recreate the Counter for each window.
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_size = len(s1)
        
        for i in range(len(s2) - window_size + 1):
            window = s2[i:i + window_size]
            window_count = Counter(window)

            if window_count == s1_count:
                return True
        
        return False
    
    def check_inclusion_optimized(self, s1: str, s2: str) -> bool:
        """
        Approach 2: Optimized Sliding Window with Frequency Map
        Time Complexity: O(n) where n = len(s2)
        Space Complexity: O(1) - fixed size maps for 26 lowercase letters
        
        Maintain a sliding window frequency map and update it incrementally.
        Only update when characters enter or leave the window.
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = defaultdict(int)
        window_size = len(s1)
        
        # Initialize the first window
        for i in range(window_size):
            window_count[s2[i]] += 1
        
        # Check first window
        if window_count == s1_count:
            return True
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Remove leftmost character
            left_char = s2[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Add rightmost character
            right_char = s2[i]
            window_count[right_char] += 1
            
            # Check if window matches
            if window_count == s1_count:
                return True
        
        return False
    
    def check_inclusion_array(self, s1: str, s2: str) -> bool:
        """
        Approach 3: Sliding Window with Array (Most Efficient)
        Time Complexity: O(n) where n = len(s2)
        Space Complexity: O(1) - fixed size array of 26 elements
        
        Use array instead of dictionary for character frequency tracking.
        Faster for fixed character set (lowercase letters only).
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26
        window_size = len(s1)
        
        # Count characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Initialize first window
        for i in range(window_size):
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Check first window
        if window_count == s1_count:
            return True
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Remove leftmost character
            left_idx = ord(s2[i - window_size]) - ord('a')
            window_count[left_idx] -= 1
            
            # Add rightmost character
            right_idx = ord(s2[i]) - ord('a')
            window_count[right_idx] += 1
            
            # Check if window matches
            if window_count == s1_count:
                return True
        
        return False
    
    def check_inclusion_match_count(self, s1: str, s2: str) -> bool:
        """
        Approach 4: Sliding Window with Match Count Optimization
        Time Complexity: O(n) where n = len(s2)
        Space Complexity: O(1) - fixed size array
        
        Instead of comparing entire arrays each time, maintain a match count.
        Only check when match count equals the number of unique characters in s1.
        This reduces the number of full array comparisons.
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26
        window_size = len(s1)
        matches = 0
        
        # Count characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Count how many characters have matching frequencies
        for i in range(26):
            if s1_count[i] == 0:
                matches += 1
        
        # Initialize first window
        for i in range(window_size):
            idx = ord(s2[i]) - ord('a')
            window_count[idx] += 1
            
            if window_count[idx] == s1_count[idx]:
                matches += 1
            elif window_count[idx] == s1_count[idx] + 1:
                matches -= 1
        
        if matches == 26:
            return True
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Remove leftmost character
            left_idx = ord(s2[i - window_size]) - ord('a')
            window_count[left_idx] -= 1
            
            if window_count[left_idx] == s1_count[left_idx]:
                matches += 1
            elif window_count[left_idx] == s1_count[left_idx] - 1:
                matches -= 1
            
            # Add rightmost character
            right_idx = ord(s2[i]) - ord('a')
            window_count[right_idx] += 1
            
            if window_count[right_idx] == s1_count[right_idx]:
                matches += 1
            elif window_count[right_idx] == s1_count[right_idx] + 1:
                matches -= 1
            
            if matches == 26:
                return True
        
        return False


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality - permutation exists
    print("Test 1: Basic functionality - permutation exists")
    s1_1 = "ab"
    s2_1 = "eidbaooo"
    expected1 = True
    result1 = solution.check_inclusion(s1_1, s2_1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: No permutation exists
    print("Test 2: No permutation exists")
    s1_2 = "ab"
    s2_2 = "eidboaoo"
    expected2 = False
    result2 = solution.check_inclusion(s1_2, s2_2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Permutation at the end
    print("Test 3: Permutation at the end")
    s1_3 = "abc"
    s2_3 = "dcba"
    expected3 = True
    result3 = solution.check_inclusion(s1_3, s2_3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Permutation at the start
    print("Test 4: Permutation at the start")
    s1_4 = "ab"
    s2_4 = "abxxxxx"
    expected4 = True
    result4 = solution.check_inclusion(s1_4, s2_4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: s1 longer than s2
    print("Test 5: s1 longer than s2")
    s1_5 = "abc"
    s2_5 = "ab"
    expected5 = False
    result5 = solution.check_inclusion(s1_5, s2_5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Single character
    print("Test 6: Single character")
    s1_6 = "a"
    s2_6 = "ab"
    expected6 = True
    result6 = solution.check_inclusion(s1_6, s2_6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Same strings
    print("Test 7: Same strings")
    s1_7 = "abc"
    s2_7 = "abc"
    expected7 = True
    result7 = solution.check_inclusion(s1_7, s2_7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: Repeated characters in s1
    print("Test 8: Repeated characters in s1")
    s1_8 = "aab"
    s2_8 = "eidbaaoo"
    expected8 = True
    result8 = solution.check_inclusion(s1_8, s2_8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: No match with repeated characters
    print("Test 9: No match with repeated characters")
    s1_9 = "aab"
    s2_9 = "eidbaoo"
    expected9 = False
    result9 = solution.check_inclusion(s1_9, s2_9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Compare all approaches
    print("Test 10: Compare all approaches")
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("abc", "dcba", True),
        ("aab", "eidbaaoo", True),
        ("aab", "eidbaoo", False),
    ]
    
    for s1, s2, expected in test_cases:
        result1 = solution.check_inclusion(s1, s2)
        result2 = solution.check_inclusionOptimized(s1, s2)
        result3 = solution.check_inclusionArray(s1, s2)
        result4 = solution.check_inclusionMatchCount(s1, s2)
        
        assert result1 == expected, f"Approach 1 failed for s1='{s1}', s2='{s2}': expected {expected}, got {result1}"
        assert result2 == expected, f"Approach 2 failed for s1='{s1}', s2='{s2}': expected {expected}, got {result2}"
        assert result3 == expected, f"Approach 3 failed for s1='{s1}', s2='{s2}': expected {expected}, got {result3}"
        assert result4 == expected, f"Approach 4 failed for s1='{s1}', s2='{s2}': expected {expected}, got {result4}"
    
    # Test case 11: Edge case - single character strings
    print("Test 11: Edge case - single character strings")
    s1_11 = "a"
    s2_11 = "a"
    expected11 = True
    result11 = solution.check_inclusion(s1_11, s2_11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    
    # Test case 12: Edge case - single character not found
    print("Test 12: Edge case - single character not found")
    s1_12 = "a"
    s2_12 = "b"
    expected12 = False
    result12 = solution.check_inclusion(s1_12, s2_12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    
    # Test case 13: Large window
    print("Test 13: Large window")
    s1_13 = "abcdefghij"
    s2_13 = "ijhgfedcba"
    expected13 = True
    result13 = solution.check_inclusion(s1_13, s2_13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    
    # Test case 14: Multiple occurrences
    print("Test 14: Multiple occurrences")
    s1_14 = "hello"
    s2_14 = "ooolleoooleh"
    expected14 = False
    result14 = solution.check_inclusion(s1_14, s2_14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    
    # Test case 15: All same characters
    print("Test 15: All same characters")
    s1_15 = "aaa"
    s2_15 = "bbbaaabbb"
    expected15 = True
    result15 = solution.check_inclusion(s1_15, s2_15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()    