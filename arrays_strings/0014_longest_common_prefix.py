"""
14. Longest Common Prefix
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Explanation: The longest common prefix is "fl".

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Example 3:
Input: strs = ["ab", "a"]
Output: "a"
Explanation: The longest common prefix is "a".

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

Notes:
- Key insight: The longest common prefix must be a prefix of all strings.
- The common prefix cannot be longer than the shortest string.
- Time complexity varies by approach:
  - Sorting: O(n log n + m) where n is number of strings, m is length of shortest string
  - Horizontal scanning: O(S) where S is sum of all characters
  - Vertical scanning: O(n * m) where m is length of shortest string
  - Divide and conquer: O(S) where S is sum of all characters
  - Binary search: O(n * m * log m) where m is length of shortest string
- Space complexity: O(1) for most approaches (excluding recursion stack)
- Edge cases: Empty array, single string, strings with different lengths, no common prefix
- Alternative approaches:
  - Horizontal scanning: Compare first string with all others
  - Vertical scanning: Compare character by character across all strings
  - Divide and conquer: Split array in half, find LCP recursively
  - Binary search: Binary search on the length of common prefix
  - Trie: Build a trie and find the longest common path (overkill for this problem)
"""

from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Approach 1: Sorting (Current)
        Time Complexity: O(n log n + m) where n=len(strs), m=len(shortest string)
        Space Complexity: O(1)
        
        Sort the array and compare the first and last strings.
        The common prefix of the entire array must be the common prefix
        of the lexicographically smallest and largest strings.
        """
        if not strs:
            return ""

        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
    
    def longest_common_prefix_horizontal(self, strs: List[str]) -> str:
        """
        Approach 2: Horizontal Scanning
        Time Complexity: O(S) where S is sum of all characters
        Space Complexity: O(1)
        
        Compare the first string with all other strings one by one.
        Update the common prefix as we go.
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # Find common prefix between current prefix and current string
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
    def longest_common_prefix_vertical(self, strs: List[str]) -> str:
        """
        Approach 3: Vertical Scanning
        Time Complexity: O(n * m) where n=len(strs), m=len(shortest string)
        Space Complexity: O(1)
        
        Compare characters at the same position across all strings.
        Stop when we find a mismatch or reach the end of shortest string.
        """
        if not strs:
            return ""
        
        # Find the shortest string to avoid index out of bounds
        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            char = strs[0][i]
            # Check if all strings have the same character at position i
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return strs[0][:i]
        
        return shortest
    
    def longest_common_prefix_divide_conquer(self, strs: List[str]) -> str:
        """
        Approach 4: Divide and Conquer
        Time Complexity: O(S) where S is sum of all characters
        Space Complexity: O(m * log n) for recursion stack where m is length of prefix
        
        Divide the array into two halves, find LCP of each half recursively,
        then find LCP of the two results.
        """
        if not strs:
            return ""
        
        def lcp_two_strings(s1: str, s2: str) -> str:
            """Find longest common prefix of two strings"""
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return s1[:i]
        
        def lcp_recursive(left: int, right: int) -> str:
            if left == right:
                return strs[left]
            
            mid = (left + right) // 2
            left_lcp = lcp_recursive(left, mid)
            right_lcp = lcp_recursive(mid + 1, right)
            
            return lcp_two_strings(left_lcp, right_lcp)
        
        return lcp_recursive(0, len(strs) - 1)
    
    def longest_common_prefix_binary_search(self, strs: List[str]) -> str:
        """
        Approach 5: Binary Search on Length
        Time Complexity: O(n * m * log m) where m is length of shortest string
        Space Complexity: O(1)
        
        Binary search on the length of the common prefix.
        Check if a prefix of given length is common to all strings.
        """
        if not strs:
            return ""
        
        def is_common_prefix(length: int) -> bool:
            """Check if prefix of given length is common to all strings"""
            prefix = strs[0][:length]
            for i in range(1, len(strs)):
                if not strs[i].startswith(prefix):
                    return False
            return True
        
        # Find minimum length
        min_len = min(len(s) for s in strs)
        
        left, right = 0, min_len
        
        while left < right:
            mid = (left + right + 1) // 2
            if is_common_prefix(mid):
                left = mid
            else:
                right = mid - 1
        
        return strs[0][:left]
    
    def longest_common_prefix_optimized(self, strs: List[str]) -> str:
        """
        Approach 6: Optimized Vertical Scanning
        Time Complexity: O(n * m) where m is length of shortest string
        Space Complexity: O(1)
        
        Similar to vertical scanning but with early termination optimization.
        """
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = []
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return ''.join(prefix)
            prefix.append(char)
        
        return ''.join(prefix)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example ['flower','flow','flight']")
    strs1 = ["flower", "flow", "flight"]
    expected1 = "fl"
    result1 = solution.longest_common_prefix(strs1)
    assert result1 == expected1, f"Test 1 failed: expected '{expected1}', got '{result1}'"
    print(f"  Result: '{result1}' ✓")
    
    # Test case 2: No common prefix
    print("Test 2: No common prefix ['dog','racecar','car']")
    strs2 = ["dog", "racecar", "car"]
    expected2 = ""
    result2 = solution.longest_common_prefix(strs2)
    assert result2 == expected2, f"Test 2 failed: expected '{expected2}', got '{result2}'"
    print(f"  Result: '{result2}' ✓")
    
    # Test case 3: Single character prefix
    print("Test 3: Single character prefix ['ab','a']")
    strs3 = ["ab", "a"]
    expected3 = "a"
    result3 = solution.longest_common_prefix(strs3)
    assert result3 == expected3, f"Test 3 failed: expected '{expected3}', got '{result3}'"
    print(f"  Result: '{result3}' ✓")
    
    # Test case 4: All strings identical
    print("Test 4: All strings identical ['abc','abc','abc']")
    strs4 = ["abc", "abc", "abc"]
    expected4 = "abc"
    result4 = solution.longest_common_prefix(strs4)
    assert result4 == expected4, f"Test 4 failed: expected '{expected4}', got '{result4}'"
    print(f"  Result: '{result4}' ✓")
    
    # Test case 5: Single string
    print("Test 5: Single string ['abc']")
    strs5 = ["abc"]
    expected5 = "abc"
    result5 = solution.longest_common_prefix(strs5)
    assert result5 == expected5, f"Test 5 failed: expected '{expected5}', got '{result5}'"
    print(f"  Result: '{result5}' ✓")
    
    # Test case 6: Empty strings
    print("Test 6: Empty strings ['','']")
    strs6 = ["", ""]
    expected6 = ""
    result6 = solution.longest_common_prefix(strs6)
    assert result6 == expected6, f"Test 6 failed: expected '{expected6}', got '{result6}'"
    print(f"  Result: '{result6}' ✓")
    
    # Test case 7: One empty string
    print("Test 7: One empty string ['abc','']")
    strs7 = ["abc", ""]
    expected7 = ""
    result7 = solution.longest_common_prefix(strs7)
    assert result7 == expected7, f"Test 7 failed: expected '{expected7}', got '{result7}'"
    print(f"  Result: '{result7}' ✓")
    
    # Test case 8: Different lengths
    print("Test 8: Different lengths ['a','ab','abc']")
    strs8 = ["a", "ab", "abc"]
    expected8 = "a"
    result8 = solution.longest_common_prefix(strs8)
    assert result8 == expected8, f"Test 8 failed: expected '{expected8}', got '{result8}'"
    print(f"  Result: '{result8}' ✓")
    
    # Test case 9: Long common prefix
    print("Test 9: Long common prefix ['preview','prefix','prefer']")
    strs9 = ["preview", "prefix", "prefer"]
    expected9 = "pre"
    result9 = solution.longest_common_prefix(strs9)
    assert result9 == expected9, f"Test 9 failed: expected '{expected9}', got '{result9}'"
    print(f"  Result: '{result9}' ✓")
    
    # Test case 10: Compare all approaches
    print("\nTest 10: Comparing all approaches")
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["ab", "a"],
        ["abc", "abc", "abc"],
        ["a", "ab", "abc"],
        ["preview", "prefix", "prefer"],
    ]
    
    for strs in test_cases:
        result1 = solution.longest_common_prefix(strs)
        result2 = solution.longest_common_prefix_horizontal(strs)
        result3 = solution.longest_common_prefix_vertical(strs)
        result4 = solution.longest_common_prefix_divide_conquer(strs)
        result5 = solution.longest_common_prefix_binary_search(strs)
        result6 = solution.longest_common_prefix_optimized(strs)
        
        assert result1 == result2, f"Horizontal mismatch for {strs}: {result1} vs {result2}"
        assert result1 == result3, f"Vertical mismatch for {strs}: {result1} vs {result3}"
        assert result1 == result4, f"Divide & conquer mismatch for {strs}: {result1} vs {result4}"
        assert result1 == result5, f"Binary search mismatch for {strs}: {result1} vs {result5}"
        assert result1 == result6, f"Optimized mismatch for {strs}: {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 11: Edge case - empty array
    print("\nTest 11: Edge case - empty array")
    strs11 = []
    expected11 = ""
    result11 = solution.longest_common_prefix(strs11)
    assert result11 == expected11, f"Test 11 failed: expected '{expected11}', got '{result11}'"
    print(f"  Result: '{result11}' ✓")
    
    # Test case 12: Large array
    print("Test 12: Large array with common prefix")
    strs12 = ["prefix" + str(i) for i in range(100)]
    # All strings start with "prefix"
    expected12 = "prefix"
    result12 = solution.longest_common_prefix(strs12)
    assert result12 == expected12, f"Test 12 failed: expected '{expected12}', got '{result12}'"
    print(f"  Result: '{result12}' ✓")
    
    # Test case 13: Very short strings
    print("Test 13: Very short strings ['a','aa','aaa']")
    strs13 = ["a", "aa", "aaa"]
    expected13 = "a"
    result13 = solution.longest_common_prefix(strs13)
    assert result13 == expected13, f"Test 13 failed: expected '{expected13}', got '{result13}'"
    print(f"  Result: '{result13}' ✓")
    
    # Test case 14: Common prefix in middle (should not match)
    print("Test 14: Common substring (not prefix) ['abc','def','bcd']")
    strs14 = ["abc", "def", "bcd"]
    expected14 = ""
    result14 = solution.longest_common_prefix(strs14)
    assert result14 == expected14, f"Test 14 failed: expected '{expected14}', got '{result14}'"
    print(f"  Result: '{result14}' ✓")
    
    # Test case 15: Single character strings
    print("Test 15: Single character strings ['a','a','a']")
    strs15 = ["a", "a", "a"]
    expected15 = "a"
    result15 = solution.longest_common_prefix(strs15)
    assert result15 == expected15, f"Test 15 failed: expected '{expected15}', got '{result15}'"
    print(f"  Result: '{result15}' ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()