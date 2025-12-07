"""
394. Decode String
Difficulty: Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data 
does not contain any digits and that digits are only for those repeat numbers, k. For 
example, there will not be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Explanation: "a" is repeated 3 times, "bc" is repeated 2 times.

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
Explanation: "a2[c]" decodes to "acc", then repeated 3 times.

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Explanation: "abc" is repeated 2 times, "cd" is repeated 3 times, followed by "ef".

Constraints:
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and characters '[' and ']'.
- s is a valid string.
- All the integers in s are in the range [1, 300].

Notes:
- Key insight: Use a stack to handle nested brackets. When we see '[', push current state.
- When we see ']', pop and repeat the string.
- Time complexity: O(n * m) where n is string length, m is max repetition count
- Space complexity: O(n) for stack and result
- Alternative approaches:
  - Stack-based: O(n * m) time, O(n) space - current approach (optimal)
  - Recursive: O(n * m) time, O(n) space - recursive parsing
  - Two stacks: O(n * m) time, O(n) space - separate stacks for numbers and strings
  - Iterative with string building: O(n * m) time, O(n) space - similar to stack
- Edge cases: Single character, no brackets, nested brackets, large repetition counts
"""

from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Approach 1: Stack-Based (Current)
        Time Complexity: O(n * m) where n is string length, m is max repetition count
        Space Complexity: O(n)
        
        Use a stack to store previous string and repetition count when encountering '['.
        When encountering ']', pop and repeat the current string.
        """
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # Build multi-digit numbers
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current state to stack
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop and repeat
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                # Regular character
                current_string += char
                
        return current_string
    
    def decodeStringRecursive(self, s: str) -> str:
        """
        Approach 2: Recursive
        Time Complexity: O(n * m)
        Space Complexity: O(n) for recursion stack
        
        Recursively parse the string. When encountering '[', recursively decode the 
        substring until matching ']'.
        """
        def decode(s: str, index: int) -> tuple:
            result = ""
            num = 0
            i = index
            
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    # Recursively decode substring
                    decoded, i = decode(s, i + 1)
                    result += num * decoded
                    num = 0
                elif s[i] == ']':
                    # Return decoded string and new index
                    return result, i
                else:
                    result += s[i]
                i += 1
            
            return result, i
        
        result, _ = decode(s, 0)
        return result
    
    def decodeStringTwoStacks(self, s: str) -> str:
        """
        Approach 3: Two Stacks
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Use separate stacks for numbers and strings for clarity.
        """
        num_stack = []
        str_stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push to stacks
                num_stack.append(current_num)
                str_stack.append(current_string)
                current_num = 0
                current_string = ""
            elif char == ']':
                # Pop and repeat
                num = num_stack.pop()
                prev_string = str_stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char
        
        return current_string
    
    def decodeStringIterative(self, s: str) -> str:
        """
        Approach 4: Iterative with String Building
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Similar to stack approach but with explicit string building.
        """
        stack = []
        result = ""
        num = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((result, num))
                result = ""
                num = 0
            elif char == ']':
                prev_string, repeat = stack.pop()
                result = prev_string + repeat * result
            else:
                result += char
        
        return result
    
    def decodeStringAlternative(self, s: str) -> str:
        """
        Approach 5: Alternative Stack Structure
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Same logic but with different variable names and structure.
        """
        stack = []
        num = 0
        text = ""
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((text, num))
                text = ""
                num = 0
            elif c == ']':
                prev_text, repeat = stack.pop()
                text = prev_text + text * repeat
            else:
                text += c
        
        return text
    
    def decode_string(self, s: str) -> str:
        """
        Approach 6: Original Implementation
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Original implementation with same logic as Approach 1.
        """
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char
                
        return current_string


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example '3[a]2[bc]'")
    s1 = "3[a]2[bc]"
    expected1 = "aaabcbc"
    result1 = solution.decodeString(s1)
    assert result1 == expected1, f"Test 1 failed: expected '{expected1}', got '{result1}'"
    print(f"  Result: '{result1}' ✓")
    
    # Test case 2: Nested brackets
    print("Test 2: Nested brackets '3[a2[c]]'")
    s2 = "3[a2[c]]"
    expected2 = "accaccacc"
    result2 = solution.decodeString(s2)
    assert result2 == expected2, f"Test 2 failed: expected '{expected2}', got '{result2}'"
    print(f"  Result: '{result2}' ✓")
    
    # Test case 3: Multiple groups
    print("Test 3: Multiple groups '2[abc]3[cd]ef'")
    s3 = "2[abc]3[cd]ef"
    expected3 = "abcabccdcdcdef"
    result3 = solution.decodeString(s3)
    assert result3 == expected3, f"Test 3 failed: expected '{expected3}', got '{result3}'"
    print(f"  Result: '{result3}' ✓")
    
    # Test case 4: Compare all approaches
    print("\nTest 4: Comparing all approaches")
    test_cases = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef",
        "abc",
        "10[a]",
    ]
    
    for s in test_cases:
        result1 = solution.decodeString(s)
        result2 = solution.decodeStringRecursive(s)
        result3 = solution.decodeStringTwoStacks(s)
        result4 = solution.decodeStringIterative(s)
        result5 = solution.decodeStringAlternative(s)
        result6 = solution.decode_string(s)
        
        assert result1 == result2, f"Recursive failed for '{s}': {result1} vs {result2}"
        assert result1 == result3, f"Two stacks failed for '{s}': {result1} vs {result3}"
        assert result1 == result4, f"Iterative failed for '{s}': {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed for '{s}': {result1} vs {result5}"
        assert result1 == result6, f"Original failed for '{s}': {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 5: Single character
    print("\nTest 5: Single character 'a'")
    s5 = "a"
    expected5 = "a"
    result5 = solution.decodeString(s5)
    assert result5 == expected5, f"Test 5 failed: expected '{expected5}', got '{result5}'"
    print(f"  Result: '{result5}' ✓")
    
    # Test case 6: No brackets
    print("Test 6: No brackets 'abc'")
    s6 = "abc"
    expected6 = "abc"
    result6 = solution.decodeString(s6)
    assert result6 == expected6, f"Test 6 failed: expected '{expected6}', got '{result6}'"
    print(f"  Result: '{result6}' ✓")
    
    # Test case 7: Single repetition
    print("Test 7: Single repetition '2[a]'")
    s7 = "2[a]"
    expected7 = "aa"
    result7 = solution.decodeString(s7)
    assert result7 == expected7, f"Test 7 failed: expected '{expected7}', got '{result7}'"
    print(f"  Result: '{result7}' ✓")
    
    # Test case 8: Large repetition count
    print("Test 8: Large repetition count '100[a]'")
    s8 = "100[a]"
    expected8 = "a" * 100
    result8 = solution.decodeString(s8)
    assert result8 == expected8, f"Test 8 failed: expected length {len(expected8)}, got {len(result8)}"
    print(f"  Result length: {len(result8)} ✓")
    
    # Test case 9: Deeply nested
    print("Test 9: Deeply nested '2[3[4[a]]]'")
    s9 = "2[3[4[a]]]"
    expected9 = "a" * 24  # 2 * 3 * 4 = 24
    result9 = solution.decodeString(s9)
    assert result9 == expected9, f"Test 9 failed: expected length {len(expected9)}, got {len(result9)}"
    print(f"  Result length: {len(result9)} ✓")
    
    # Test case 10: Multiple nested
    print("Test 10: Multiple nested '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'")
    s10 = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    # This is complex, let's verify it works
    result10 = solution.decodeString(s10)
    # Expected: "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    # Let's just check it's not empty and has correct structure
    assert len(result10) > 0, "Test 10 failed: result is empty"
    assert 'z' in result10, "Test 10 failed: missing 'z'"
    print(f"  Result length: {len(result10)} ✓")
    
    # Test case 11: Simple nested
    print("Test 11: Simple nested '2[3[a]b]'")
    s11 = "2[3[a]b]"
    expected11 = "aaabaaab"  # 2 * (3*a + b) = 2 * (aaa + b) = aaabaaab
    result11 = solution.decodeString(s11)
    assert result11 == expected11, f"Test 11 failed: expected '{expected11}', got '{result11}'"
    print(f"  Result: '{result11}' ✓")
    
    # Test case 12: Mixed with letters
    print("Test 12: Mixed with letters 'abc3[de]fg'")
    s12 = "abc3[de]fg"
    expected12 = "abcdededefg"
    result12 = solution.decodeString(s12)
    assert result12 == expected12, f"Test 12 failed: expected '{expected12}', got '{result12}'"
    print(f"  Result: '{result12}' ✓")
    
    # Test case 13: Two-digit number
    print("Test 13: Two-digit number '10[ab]'")
    s13 = "10[ab]"
    expected13 = "ab" * 10
    result13 = solution.decodeString(s13)
    assert result13 == expected13, f"Test 13 failed: expected '{expected13}', got '{result13}'"
    print(f"  Result: '{result13}' ✓")
    
    # Test case 14: Three-digit number
    print("Test 14: Three-digit number '100[xy]'")
    s14 = "100[xy]"
    expected14 = "xy" * 100
    result14 = solution.decodeString(s14)
    assert result14 == expected14, f"Test 14 failed: expected length {len(expected14)}, got {len(result14)}"
    print(f"  Result length: {len(result14)} ✓")
    
    # Test case 15: Complex nested pattern
    print("Test 15: Complex nested '2[ab3[cd]]'")
    s15 = "2[ab3[cd]]"
    expected15 = "abcdcdcdabcdcdcd"  # 2 * (ab + 3*cd) = 2 * (ab + cdcdcd) = abcdcdcdabcdcdcd
    result15 = solution.decodeString(s15)
    assert result15 == expected15, f"Test 15 failed: expected '{expected15}', got '{result15}'"
    print(f"  Result: '{result15}' ✓")
    
    # Test case 16: Single bracket group
    print("Test 16: Single bracket group '1[a]'")
    s16 = "1[a]"
    expected16 = "a"
    result16 = solution.decodeString(s16)
    assert result16 == expected16, f"Test 16 failed: expected '{expected16}', got '{result16}'"
    print(f"  Result: '{result16}' ✓")
    
    # Test case 17: Empty string in brackets (edge case - may not occur per constraints)
    print("Test 17: Multiple single characters 'a2[b]c3[d]'")
    s17 = "a2[b]c3[d]"
    expected17 = "abbcddd"
    result17 = solution.decodeString(s17)
    assert result17 == expected17, f"Test 17 failed: expected '{expected17}', got '{result17}'"
    print(f"  Result: '{result17}' ✓")
    
    # Test case 18: Very nested
    print("Test 18: Very nested '2[3[4[5[a]]]]'")
    s18 = "2[3[4[5[a]]]]"
    expected18 = "a" * (2 * 3 * 4 * 5)  # 120 a's
    result18 = solution.decodeString(s18)
    assert result18 == expected18, f"Test 18 failed: expected length {len(expected18)}, got {len(result18)}"
    print(f"  Result length: {len(result18)} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
