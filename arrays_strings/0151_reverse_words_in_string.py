"""
151. Reverse Words in a String
Difficulty: Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated 
by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include 
any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in 
the reversed string.

Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Notes:
- Key insight: Split string into words, reverse the list, then join with single space.
- Python's split() automatically handles multiple spaces and leading/trailing spaces.
- Time complexity: O(n) where n is length of string
- Space complexity: O(n) for storing words
- Alternative approaches:
  - Split and reverse: O(n) time, O(n) space - current approach (simple and clean)
  - Two-pointer reverse: O(n) time, O(1) space - reverse entire string then reverse each word
  - Stack-based: O(n) time, O(n) space - push words onto stack, pop to reverse
  - Manual parsing: O(n) time, O(n) space - manually extract words without split()
  - Built-in methods: O(n) time, O(n) space - using split() and join()
- Edge cases: Leading spaces, trailing spaces, multiple spaces, single word, single character
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Approach 1: Split and Reverse (Current)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Split string into words, reverse the list, then join with single space.
        Python's split() automatically handles multiple spaces and leading/trailing spaces.
        """
        words = s.split()
        reverse = words[::-1]
        return " ".join(reverse)
    
    def reverseWordsTwoPointer(self, s: str) -> str:
        """
        Approach 2: Two-Pointer Reverse
        Time Complexity: O(n)
        Space Complexity: O(n) for result string
        
        Reverse entire string first, then reverse each word individually.
        More complex but demonstrates two-pointer technique.
        """
        # Remove extra spaces and reverse entire string
        s = s.strip()
        s = " ".join(s.split())  # Normalize spaces
        chars = list(s)
        
        # Reverse entire string
        left, right = 0, len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        # Reverse each word
        start = 0
        for i in range(len(chars)):
            if chars[i] == ' ':
                # Reverse word from start to i-1
                left, right = start, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = i + 1
            elif i == len(chars) - 1:
                # Last word
                left, right = start, i
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
        
        return "".join(chars)
    
    def reverseWordsStack(self, s: str) -> str:
        """
        Approach 3: Stack-Based
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Extract words and push onto stack, then pop to reverse order.
        """
        words = []
        i = 0
        n = len(s)
        
        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            
            # Extract word
            if i < n:
                start = i
                while i < n and s[i] != ' ':
                    i += 1
                words.append(s[start:i])
        
        # Pop words from stack to reverse
        result = []
        while words:
            result.append(words.pop())
        
        return " ".join(result)
    
    def reverseWordsManual(self, s: str) -> str:
        """
        Approach 4: Manual Parsing
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Manually extract words without using split().
        """
        words = []
        i = 0
        n = len(s)
        
        while i < n:
            # Skip leading spaces
            while i < n and s[i] == ' ':
                i += 1
            
            if i >= n:
                break
            
            # Extract word
            start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        
        # Reverse and join
        return " ".join(reversed(words))
    
    def reverseWordsBuiltin(self, s: str) -> str:
        """
        Approach 5: Built-in Methods (One-liner)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Most concise version using built-in methods.
        """
        return " ".join(reversed(s.split()))
    
    def reverse_words(self, s: str) -> str:
        """
        Approach 6: Original Implementation
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Original implementation with same logic as Approach 1.
        """
        words = s.split()
        reverse = words[::-1]
        return " ".join(reverse)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example 'the sky is blue'")
    s1 = "the sky is blue"
    expected1 = "blue is sky the"
    result1 = solution.reverseWords(s1)
    assert result1 == expected1, f"Test 1 failed: expected '{expected1}', got '{result1}'"
    print(f"  Result: '{result1}' ✓")
    
    # Test case 2: Leading and trailing spaces
    print("Test 2: Leading and trailing spaces '  hello world  '")
    s2 = "  hello world  "
    expected2 = "world hello"
    result2 = solution.reverseWords(s2)
    assert result2 == expected2, f"Test 2 failed: expected '{expected2}', got '{result2}'"
    print(f"  Result: '{result2}' ✓")
    
    # Test case 3: Multiple spaces between words
    print("Test 3: Multiple spaces 'a good   example'")
    s3 = "a good   example"
    expected3 = "example good a"
    result3 = solution.reverseWords(s3)
    assert result3 == expected3, f"Test 3 failed: expected '{expected3}', got '{result3}'"
    print(f"  Result: '{result3}' ✓")
    
    # Test case 4: Compare all approaches
    print("\nTest 4: Comparing all approaches")
    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "  test  ",
        "single",
    ]
    
    for s in test_cases:
        result1 = solution.reverseWords(s)
        result2 = solution.reverseWordsTwoPointer(s)
        result3 = solution.reverseWordsStack(s)
        result4 = solution.reverseWordsManual(s)
        result5 = solution.reverseWordsBuiltin(s)
        result6 = solution.reverse_words(s)
        
        assert result1 == result2, f"Two-pointer failed for '{s}': {result1} vs {result2}"
        assert result1 == result3, f"Stack failed for '{s}': {result1} vs {result3}"
        assert result1 == result4, f"Manual failed for '{s}': {result1} vs {result4}"
        assert result1 == result5, f"Builtin failed for '{s}': {result1} vs {result5}"
        assert result1 == result6, f"Original failed for '{s}': {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 5: Single word
    print("\nTest 5: Single word 'hello'")
    s5 = "hello"
    expected5 = "hello"
    result5 = solution.reverseWords(s5)
    assert result5 == expected5, f"Test 5 failed: expected '{expected5}', got '{result5}'"
    print(f"  Result: '{result5}' ✓")
    
    # Test case 6: Single character
    print("Test 6: Single character 'a'")
    s6 = "a"
    expected6 = "a"
    result6 = solution.reverseWords(s6)
    assert result6 == expected6, f"Test 6 failed: expected '{expected6}', got '{result6}'"
    print(f"  Result: '{result6}' ✓")
    
    # Test case 7: All spaces
    print("Test 7: All spaces '     '")
    s7 = "     "
    expected7 = ""
    result7 = solution.reverseWords(s7)
    assert result7 == expected7, f"Test 7 failed: expected '{expected7}', got '{result7}'"
    print(f"  Result: '{result7}' ✓")
    
    # Test case 8: Two words
    print("Test 8: Two words 'hello world'")
    s8 = "hello world"
    expected8 = "world hello"
    result8 = solution.reverseWords(s8)
    assert result8 == expected8, f"Test 8 failed: expected '{expected8}', got '{result8}'"
    print(f"  Result: '{result8}' ✓")
    
    # Test case 9: Many spaces
    print("Test 9: Many spaces 'a    b     c'")
    s9 = "a    b     c"
    expected9 = "c b a"
    result9 = solution.reverseWords(s9)
    assert result9 == expected9, f"Test 9 failed: expected '{expected9}', got '{result9}'"
    print(f"  Result: '{result9}' ✓")
    
    # Test case 10: Numbers and letters
    print("Test 10: Numbers and letters 'test1 test2 test3'")
    s10 = "test1 test2 test3"
    expected10 = "test3 test2 test1"
    result10 = solution.reverseWords(s10)
    assert result10 == expected10, f"Test 10 failed: expected '{expected10}', got '{result10}'"
    print(f"  Result: '{result10}' ✓")
    
    # Test case 11: Mixed case
    print("Test 11: Mixed case 'Hello World Python'")
    s11 = "Hello World Python"
    expected11 = "Python World Hello"
    result11 = solution.reverseWords(s11)
    assert result11 == expected11, f"Test 11 failed: expected '{expected11}', got '{result11}'"
    print(f"  Result: '{result11}' ✓")
    
    # Test case 12: Long string
    print("Test 12: Long string")
    s12 = "a b c d e f g h i j k l m n o p"
    expected12 = "p o n m l k j i h g f e d c b a"
    result12 = solution.reverseWords(s12)
    assert result12 == expected12, f"Test 12 failed: expected '{expected12}', got '{result12}'"
    print(f"  Result: '{result12}' ✓")
    
    # Test case 13: Single space between words
    print("Test 13: Single space between words 'one two three'")
    s13 = "one two three"
    expected13 = "three two one"
    result13 = solution.reverseWords(s13)
    assert result13 == expected13, f"Test 13 failed: expected '{expected13}', got '{result13}'"
    print(f"  Result: '{result13}' ✓")
    
    # Test case 14: Leading spaces only
    print("Test 14: Leading spaces only '   hello'")
    s14 = "   hello"
    expected14 = "hello"
    result14 = solution.reverseWords(s14)
    assert result14 == expected14, f"Test 14 failed: expected '{expected14}', got '{result14}'"
    print(f"  Result: '{result14}' ✓")
    
    # Test case 15: Trailing spaces only
    print("Test 15: Trailing spaces only 'hello   '")
    s15 = "hello   "
    expected15 = "hello"
    result15 = solution.reverseWords(s15)
    assert result15 == expected15, f"Test 15 failed: expected '{expected15}', got '{result15}'"
    print(f"  Result: '{result15}' ✓")
    
    # Test case 16: Empty string (edge case)
    print("Test 16: Empty string ''")
    s16 = ""
    expected16 = ""
    result16 = solution.reverseWords(s16)
    assert result16 == expected16, f"Test 16 failed: expected '{expected16}', got '{result16}'"
    print(f"  Result: '{result16}' ✓")
    
    # Test case 17: One word with spaces
    print("Test 17: One word with spaces '  hello  '")
    s17 = "  hello  "
    expected17 = "hello"
    result17 = solution.reverseWords(s17)
    assert result17 == expected17, f"Test 17 failed: expected '{expected17}', got '{result17}'"
    print(f"  Result: '{result17}' ✓")
    
    # Test case 18: Complex spacing
    print("Test 18: Complex spacing '  a   b  c   d  '")
    s18 = "  a   b  c   d  "
    expected18 = "d c b a"
    result18 = solution.reverseWords(s18)
    assert result18 == expected18, f"Test 18 failed: expected '{expected18}', got '{result18}'"
    print(f"  Result: '{result18}' ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
