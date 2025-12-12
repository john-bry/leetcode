"""
28. Find the Index of the First Occurrence in a String
Difficulty: Easy

Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, 
so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Example 3:
Input: haystack = "hello", needle = "ll"
Output: 2
Explanation: "ll" occurs at index 2.

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English letters.

Notes:
- This is a classic string matching problem (substring search).
- Key insight: We need to check every possible starting position in haystack.
- Edge cases: Empty needle (should return 0), needle longer than haystack (return -1),
  needle at the end of haystack, multiple occurrences (return first).
- Time complexity varies by approach:
  - Brute force: O(n * m) where n=len(haystack), m=len(needle)
  - Built-in find: O(n * m) in worst case, but optimized in Python
  - KMP algorithm: O(n + m) - optimal for repeated patterns
  - Boyer-Moore: O(n * m) worst case, O(n/m) best case
  - Rabin-Karp (rolling hash): O(n + m) average, O(n * m) worst case
- Space complexity:
  - Brute force: O(1)
  - KMP: O(m) for the prefix table
  - Boyer-Moore: O(m) for the bad character table
  - Rabin-Karp: O(1)
- For interview purposes, brute force is acceptable for small inputs.
- KMP is the most efficient for large inputs or when needle has repeated patterns.
- Python's built-in str.find() uses optimized algorithms internally.
"""


class Solution:
    def find_idx_first_occurence_in_str(self, haystack: str, needle: str) -> int:
        """
        Approach 1: Brute Force
        Time Complexity: O(n * m) where n=len(haystack), m=len(needle)
        Space Complexity: O(1)
        
        Check every possible starting position in haystack.
        For each position, check if the substring matches needle.
        """
        if len(needle) > len(haystack):
            return -1
        
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
    
    def find_idx_builtin(self, haystack: str, needle: str) -> int:
        """
        Approach 2: Built-in String Method
        Time Complexity: O(n * m) worst case, but optimized in Python
        Space Complexity: O(1)
        
        Uses Python's optimized str.find() method.
        Note: In interviews, you might be asked to implement without built-ins.
        """
        return haystack.find(needle)
    
    def find_idx_optimized_brute_force(self, haystack: str, needle: str) -> int:
        """
        Approach 3: Optimized Brute Force (Character-by-Character)
        Time Complexity: O(n * m) worst case, but can be faster in practice
        Space Complexity: O(1)
        
        Instead of slicing, compare character by character.
        This avoids creating substring objects and can be faster.
        """
        if len(needle) > len(haystack):
            return -1
        
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        
        return -1
    
    def find_idx_kmp(self, haystack: str, needle: str) -> int:
        """
        Approach 4: KMP (Knuth-Morris-Pratt) Algorithm
        Time Complexity: O(n + m)
        Space Complexity: O(m)
        
        Uses a prefix table (LPS - Longest Proper Prefix which is also Suffix)
        to avoid re-checking characters. Optimal for repeated patterns.
        
        Key insight: When a mismatch occurs, we can skip some characters
        based on what we've already matched.
        """
        if len(needle) > len(haystack):
            return -1
        
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        # Build the prefix table (LPS array)
        def build_lps(pattern: str) -> list:
            """Build Longest Proper Prefix which is also Suffix table"""
            lps = [0] * len(pattern)
            length = 0  # Length of previous longest prefix suffix
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = build_lps(needle)
        
        # Search using KMP
        i = 0  # Index for haystack
        j = 0  # Index for needle
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j  # Found match
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]  # Don't match lps[0..lps[j-1]] characters
                else:
                    i += 1
        
        return -1
    
    def find_idx_rabin_karp(self, haystack: str, needle: str) -> int:
        """
        Approach 5: Rabin-Karp (Rolling Hash)
        Time Complexity: O(n + m) average, O(n * m) worst case
        Space Complexity: O(1)
        
        Uses rolling hash to compare substrings.
        If hash matches, verify with actual string comparison.
        Good for multiple pattern searches.
        """
        if len(needle) > len(haystack):
            return -1
        
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        # Base and modulus for hash
        base = 256
        mod = 10**9 + 7
        
        # Calculate hash of needle
        needle_hash = 0
        for char in needle:
            needle_hash = (needle_hash * base + ord(char)) % mod
        
        # Calculate hash of first window in haystack
        window_hash = 0
        for i in range(m):
            window_hash = (window_hash * base + ord(haystack[i])) % mod
        
        # Check first window
        if window_hash == needle_hash and haystack[:m] == needle:
            return 0
        
        # Calculate base^(m-1) for rolling hash
        base_power = pow(base, m - 1, mod)
        
        # Rolling hash for remaining windows
        for i in range(1, n - m + 1):
            # Remove leftmost character and add rightmost character
            window_hash = (window_hash - ord(haystack[i - 1]) * base_power) % mod
            window_hash = (window_hash * base + ord(haystack[i + m - 1])) % mod
            window_hash = (window_hash + mod) % mod  # Handle negative
            
            # Check if hash matches and verify with actual comparison
            if window_hash == needle_hash and haystack[i:i+m] == needle:
                return i
        
        return -1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example - needle at start
    print("Test 1: Basic example - 'sadbutsad' with 'sad'")
    haystack1 = "sadbutsad"
    needle1 = "sad"
    expected1 = 0
    result1 = solution.find_idx_first_occurence_in_str(haystack1, needle1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Needle not found
    print("Test 2: Needle not found - 'leetcode' with 'leeto'")
    haystack2 = "leetcode"
    needle2 = "leeto"
    expected2 = -1
    result2 = solution.find_idx_first_occurence_in_str(haystack2, needle2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Needle in middle
    print("Test 3: Needle in middle - 'hello' with 'll'")
    haystack3 = "hello"
    needle3 = "ll"
    expected3 = 2
    result3 = solution.find_idx_first_occurence_in_str(haystack3, needle3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Needle at end
    print("Test 4: Needle at end - 'abc' with 'c'")
    haystack4 = "abc"
    needle4 = "c"
    expected4 = 2
    result4 = solution.find_idx_first_occurence_in_str(haystack4, needle4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Needle longer than haystack
    print("Test 5: Needle longer than haystack - 'abc' with 'abcd'")
    haystack5 = "abc"
    needle5 = "abcd"
    expected5 = -1
    result5 = solution.find_idx_first_occurence_in_str(haystack5, needle5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Empty needle
    print("Test 6: Empty needle - 'abc' with ''")
    haystack6 = "abc"
    needle6 = ""
    expected6 = 0
    result6 = solution.find_idx_first_occurence_in_str(haystack6, needle6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Single character match
    print("Test 7: Single character match - 'a' with 'a'")
    haystack7 = "a"
    needle7 = "a"
    expected7 = 0
    result7 = solution.find_idx_first_occurence_in_str(haystack7, needle7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Multiple occurrences (return first)
    print("Test 8: Multiple occurrences - 'mississippi' with 'issi'")
    haystack8 = "mississippi"
    needle8 = "issi"
    expected8 = 1
    result8 = solution.find_idx_first_occurence_in_str(haystack8, needle8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Needle equals haystack
    print("Test 9: Needle equals haystack - 'abc' with 'abc'")
    haystack9 = "abc"
    needle9 = "abc"
    expected9 = 0
    result9 = solution.find_idx_first_occurence_in_str(haystack9, needle9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: No match - partial match
    print("Test 10: Partial match - 'abc' with 'abd'")
    haystack10 = "abc"
    needle10 = "abd"
    expected10 = -1
    result10 = solution.find_idx_first_occurence_in_str(haystack10, needle10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Compare all approaches
    print("\nTest 11: Comparing all approaches")
    test_cases = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
        ("hello", "ll"),
        ("abc", "c"),
        ("mississippi", "issi"),
        ("a", "a"),
        ("abc", "abc"),
        ("aaaaa", "bba"),
        ("", "a"),
        ("a", ""),
    ]
    
    for haystack, needle in test_cases:
        # Skip invalid cases for some approaches
        if len(needle) > len(haystack) and haystack:
            continue
        
        result1 = solution.find_idx_first_occurence_in_str(haystack, needle)
        result2 = solution.find_idx_builtin(haystack, needle)
        result3 = solution.find_idx_optimized_brute_force(haystack, needle)
        result4 = solution.find_idx_kmp(haystack, needle)
        result5 = solution.find_idx_rabin_karp(haystack, needle)
        
        assert result1 == result2, f"Built-in mismatch: {haystack}, {needle}: {result1} vs {result2}"
        assert result1 == result3, f"Optimized brute force mismatch: {haystack}, {needle}: {result1} vs {result3}"
        assert result1 == result4, f"KMP mismatch: {haystack}, {needle}: {result1} vs {result4}"
        assert result1 == result5, f"Rabin-Karp mismatch: {haystack}, {needle}: {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 12: Edge case - empty haystack
    print("\nTest 12: Empty haystack - '' with 'a'")
    haystack12 = ""
    needle12 = "a"
    expected12 = -1
    result12 = solution.find_idx_first_occurence_in_str(haystack12, needle12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Edge case - both empty
    print("Test 13: Both empty - '' with ''")
    haystack13 = ""
    needle13 = ""
    expected13 = 0
    result13 = solution.find_idx_first_occurence_in_str(haystack13, needle13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Repeated pattern (good for KMP)
    print("Test 14: Repeated pattern - 'ababcababa' with 'ababa'")
    haystack14 = "ababcababa"
    needle14 = "ababa"
    expected14 = 5
    result14 = solution.find_idx_first_occurence_in_str(haystack14, needle14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Long strings
    print("Test 15: Long strings - haystack with 1000 chars, needle at position 500")
    haystack15 = "a" * 500 + "bcd" + "a" * 500
    needle15 = "bcd"
    expected15 = 500
    result15 = solution.find_idx_first_occurence_in_str(haystack15, needle15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()