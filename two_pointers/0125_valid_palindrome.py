"""
125. Valid Palindrome
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Notes:
- Key insight: Use two pointers from both ends, skip non-alphanumeric characters, compare.
- Convert to lowercase before comparing characters.
- Only alphanumeric characters (letters and digits) matter for palindrome check.
- Time complexity: O(n) where n is the length of the string
- Space complexity: O(1) for two-pointer approach, O(n) for string filtering approach
- Alternative approaches:
  - Two pointers: O(n) time, O(1) space - current approach (optimal)
  - Filter and reverse: O(n) time, O(n) space - filter string, reverse and compare
  - Filter and two pointers: O(n) time, O(n) space - filter first, then use two pointers
  - Recursive: O(n) time, O(n) space - recursive comparison
- Edge cases: Empty string, single character, all non-alphanumeric, all same character,
  mixed case, numbers only, special characters only
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Approach 1: Two Pointers (Current - Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use two pointers from both ends. Skip non-alphanumeric characters,
        convert to lowercase, and compare.
        """
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
    
    def is_palindrome_filter_reverse(self, s: str) -> bool:
        """
        Approach 2: Filter and Reverse
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Filter out non-alphanumeric characters, convert to lowercase,
        then check if it equals its reverse.
        """
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]
    
    def is_palindrome_filter_two_pointers(self, s: str) -> bool:
        """
        Approach 3: Filter Then Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        First filter the string, then use two pointers on the filtered string.
        """
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(filtered) - 1
        
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
    def is_palindrome_alternative(self, s: str) -> bool:
        """
        Approach 4: Alternative Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Same logic as Approach 1 but with helper function for clarity.
        """
        def is_alphanumeric(c: str) -> bool:
            return c.isalnum()
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not is_alphanumeric(s[left]):
                left += 1
            while left < right and not is_alphanumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def is_palindrome_manual(self, s: str) -> bool:
        """
        Approach 5: Manual Character Check
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Manually check if character is alphanumeric instead of using isalnum().
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def is_palindrome_recursive(self, s: str) -> bool:
        """
        Approach 6: Recursive
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack
        
        Recursive version of palindrome check.
        """
        def clean_and_check(left: int, right: int) -> bool:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            if left >= right:
                return True
            
            if s[left].lower() != s[right].lower():
                return False
            
            return clean_and_check(left + 1, right - 1)
        
        return clean_and_check(0, len(s) - 1)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example 'A man, a plan, a canal: Panama'")
    s1 = "A man, a plan, a canal: Panama"
    expected1 = True
    result1 = solution.is_palindrome(s1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Example 2 from problem
    print("\nTest 2: Example 2 'race a car'")
    s2 = "race a car"
    expected2 = False
    result2 = solution.is_palindrome(s2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Example 3 from problem
    print("\nTest 3: Example 3 ' '")
    s3 = " "
    expected3 = True
    result3 = solution.is_palindrome(s3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Compare all approaches
    print("\nTest 4: Comparing all approaches")
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "Madam",
        "No 'x' in Nixon",
    ]
    
    for s in test_cases:
        result1 = solution.is_palindrome(s)
        result2 = solution.is_palindrome_filter_reverse(s)
        result3 = solution.is_palindrome_filter_two_pointers(s)
        result4 = solution.is_palindrome_alternative(s)
        result5 = solution.is_palindrome_manual(s)
        result6 = solution.is_palindrome_recursive(s)
        
        assert result1 == result2 == result3 == result4 == result5 == result6, \
            f"Mismatch for s='{s}': {result1} vs {result2} vs {result3} vs {result4} vs {result5} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 5: Empty string
    print("\nTest 5: Empty string ''")
    s5 = ""
    expected5 = True
    result5 = solution.is_palindrome(s5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Single character
    print("Test 6: Single character 'a'")
    s6 = "a"
    expected6 = True
    result6 = solution.is_palindrome(s6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Simple palindrome
    print("Test 7: Simple palindrome 'aba'")
    s7 = "aba"
    expected7 = True
    result7 = solution.is_palindrome(s7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Not a palindrome
    print("Test 8: Not a palindrome 'abc'")
    s8 = "abc"
    expected8 = False
    result8 = solution.is_palindrome(s8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: All non-alphanumeric
    print("Test 9: All non-alphanumeric '!@#$%'")
    s9 = "!@#$%"
    expected9 = True  # Empty string after filtering is a palindrome
    result9 = solution.is_palindrome(s9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Mixed case palindrome
    print("Test 10: Mixed case palindrome 'MaDaM'")
    s10 = "MaDaM"
    expected10 = True
    result10 = solution.is_palindrome(s10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Palindrome with numbers
    print("Test 11: Palindrome with numbers 'a1b2b1a'")
    s11 = "a1b2b1a"
    expected11 = True
    result11 = solution.is_palindrome(s11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Not palindrome with numbers
    print("Test 12: Not palindrome with numbers 'a1b2c3'")
    s12 = "a1b2c3"
    expected12 = False
    result12 = solution.is_palindrome(s12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Palindrome with spaces and punctuation
    print("Test 13: Palindrome with spaces and punctuation 'Was it a car or a cat I saw?'")
    s13 = "Was it a car or a cat I saw?"
    expected13 = True
    result13 = solution.is_palindrome(s13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Numbers only - palindrome
    print("Test 14: Numbers only - palindrome '12321'")
    s14 = "12321"
    expected14 = True
    result14 = solution.is_palindrome(s14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Numbers only - not palindrome
    print("Test 15: Numbers only - not palindrome '12345'")
    s15 = "12345"
    expected15 = False
    result15 = solution.is_palindrome(s15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Single alphanumeric with spaces
    print("Test 16: Single alphanumeric with spaces '   a   '")
    s16 = "   a   "
    expected16 = True
    result16 = solution.is_palindrome(s16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    # Test case 17: Palindrome with special characters
    print("Test 17: Palindrome with special characters 'a.b.a'")
    s17 = "a.b.a"
    expected17 = True
    result17 = solution.is_palindrome(s17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    print(f"  Result: {result17} ✓")
    
    # Test case 18: Long palindrome
    print("Test 18: Long palindrome")
    s18 = "A" + "b" * 1000 + "A"
    expected18 = True
    result18 = solution.is_palindrome(s18)
    assert result18 == expected18, f"Test 18 failed: expected {expected18}, got {result18}"
    print(f"  Result: {result18} ✓")
    
    # Test case 19: Palindrome with mixed alphanumeric
    print("Test 19: Palindrome with mixed alphanumeric 'a1b2c3c2b1a'")
    s19 = "a1b2c3c2b1a"
    expected19 = True
    result19 = solution.is_palindrome(s19)
    assert result19 == expected19, f"Test 19 failed: expected {expected19}, got {result19}"
    print(f"  Result: {result19} ✓")
    
    # Test case 20: Not palindrome - one character difference
    print("Test 20: Not palindrome - one character difference 'abca'")
    s20 = "abca"
    expected20 = False
    result20 = solution.is_palindrome(s20)
    assert result20 == expected20, f"Test 20 failed: expected {expected20}, got {result20}"
    print(f"  Result: {result20} ✓")
    
    # Test case 21: Palindrome with underscores
    print("Test 21: Palindrome with underscores 'a_b_a'")
    s21 = "a_b_a"
    expected21 = True
    result21 = solution.is_palindrome(s21)
    assert result21 == expected21, f"Test 21 failed: expected {expected21}, got {result21}"
    print(f"  Result: {result21} ✓")
    
    # Test case 22: Complex example
    print("Test 22: Complex example 'Mr. Owl ate my metal worm'")
    s22 = "Mr. Owl ate my metal worm"
    expected22 = True
    result22 = solution.is_palindrome(s22)
    assert result22 == expected22, f"Test 22 failed: expected {expected22}, got {result22}"
    print(f"  Result: {result22} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
