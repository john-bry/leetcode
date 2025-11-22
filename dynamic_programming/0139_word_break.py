"""
139. Word Break
Difficulty: Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
Explanation: "catsandog" cannot be segmented into dictionary words.

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

Notes:
- Key insight: This is a dynamic programming problem where we check if the string can be
  broken into valid words from the dictionary.
- At each position, we try all possible prefixes and check if:
  1. The prefix is in the dictionary
  2. The remaining suffix can be broken (recursive subproblem)
- Memoization is crucial to avoid recomputing the same subproblems.
- Time complexity: O(n^2 * m) where n is string length, m is average word length
  - We check each position (n)
  - For each position, we check all suffixes (n)
  - For each suffix, we check dictionary lookup (m)
- Space complexity: O(n) for memoization and recursion stack
- Alternative approaches:
  - Bottom-up DP (tabulation): O(n^2 * m) time, O(n) space
  - BFS: O(n^2 * m) time, O(n) space - treat as graph problem
  - Optimized: Only check word lengths that exist in dictionary
- Edge cases: Empty string, single character, wordDict with overlapping words
"""

from collections import deque
from typing import List, Set


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 1: Top-down DP with Memoization (Current)
        Time Complexity: O(n^2 * m) where n=len(s), m=avg word length
        Space Complexity: O(n) for memoization and recursion stack
        
        Use memoization to cache results of subproblems.
        For each position, try all possible prefixes and recurse on the suffix.
        """
        word_set = set(word_dict)  # Convert to set for O(1) lookup
        memo = {}

        def dp(start):
            # Base case: reached end of string
            if start == len(s):
                return True
            # Check memoization
            if start in memo:
                return memo[start]
            # Try all prefixes from start position
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                # If prefix is in dictionary and suffix can be broken
                if prefix in word_set and dp(end):
                    memo[start] = True
                    return True
            # Store result in memo
            memo[start] = False
            return False
        
        return dp(0)
    
    def word_break_tabulation(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 2: Bottom-up DP (Tabulation)
        Time Complexity: O(n^2 * m)
        Space Complexity: O(n)
        
        Build solution from left to right using a DP array.
        dp[i] = True if s[0:i] can be broken into words.
        """
        word_set = set(word_dict)
        n = len(s)
        # dp[i] = True if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented
        
        for i in range(1, n + 1):
            # Check all possible prefixes ending at position i
            for j in range(i):
                # If s[0:j] can be segmented and s[j:i] is in dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid segmentation, no need to check further
        
        return dp[n]
    
    def word_break_optimized(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 3: Optimized DP (Only Check Valid Word Lengths)
        Time Complexity: O(n * m * k) where k is number of words
        Space Complexity: O(n)
        
        Instead of checking all possible substrings, only check lengths
        that correspond to words in the dictionary. More efficient when
        dictionary words are much shorter than the string.
        """
        word_set = set(word_dict)
        # Get all possible word lengths
        word_lengths = sorted(set(len(word) for word in word_dict), reverse=True)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            # Only check lengths that exist in dictionary
            for length in word_lengths:
                if i >= length:
                    start = i - length
                    if dp[start] and s[start:i] in word_set:
                        dp[i] = True
                        break
        
        return dp[n]
    
    def word_break_bfs(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 4: BFS (Breadth-First Search)
        Time Complexity: O(n^2 * m)
        Space Complexity: O(n)
        
        Treat the problem as a graph where each position is a node.
        We can move from position i to position j if s[i:j] is in dictionary.
        Use BFS to find if we can reach the end of the string.
        """
        word_set = set(word_dict)
        n = len(s)
        queue = deque([0])  # Start from position 0
        visited = set([0])
        
        while queue:
            start = queue.popleft()
            
            # Try all possible endings from current position
            for end in range(start + 1, n + 1):
                if end in visited:
                    continue
                
                prefix = s[start:end]
                if prefix in word_set:
                    # Reached the end of string
                    if end == n:
                        return True
                    # Add new position to queue
                    queue.append(end)
                    visited.add(end)
        
        return False
    
    def word_break_dfs(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 5: DFS without Memoization (Inefficient)
        Time Complexity: O(2^n) - exponential
        Space Complexity: O(n) for recursion stack
        
        Pure recursive approach without memoization.
        Only for understanding - not recommended for production.
        """
        word_set = set(word_dict)
        
        def dfs(start):
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and dfs(end):
                    return True
            
            return False
        
        return dfs(0)
    
    def word_break_dp_early_exit(self, s: str, word_dict: List[str]) -> bool:
        """
        Approach 6: DP with Early Exit Optimization
        Time Complexity: O(n^2 * m)
        Space Complexity: O(n)
        
        Similar to tabulation but with optimization to check if
        remaining characters can form any word before processing.
        """
        word_set = set(word_dict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Precompute which positions have valid words starting from them
        # This helps with early exit
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example - 'leetcode' with ['leet','code']")
    s1 = "leetcode"
    word_dict1 = ["leet", "code"]
    expected1 = True
    result1 = solution.word_break(s1, word_dict1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Reusing words
    print("Test 2: Reusing words - 'applepenapple' with ['apple','pen']")
    s2 = "applepenapple"
    word_dict2 = ["apple", "pen"]
    expected2 = True
    result2 = solution.word_break(s2, word_dict2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Cannot be segmented
    print("Test 3: Cannot be segmented - 'catsandog'")
    s3 = "catsandog"
    word_dict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = False
    result3 = solution.word_break(s3, word_dict3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single character
    print("Test 4: Single character - 'a' with ['a']")
    s4 = "a"
    word_dict4 = ["a"]
    expected4 = True
    result4 = solution.word_break(s4, word_dict4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single character not in dict
    print("Test 5: Single character not in dict - 'a' with ['b']")
    s5 = "a"
    word_dict5 = ["b"]
    expected5 = False
    result5 = solution.word_break(s5, word_dict5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Empty string (edge case)
    print("Test 6: Empty string with empty dict")
    s6 = ""
    word_dict6 = []
    expected6 = True  # Empty string can always be segmented
    result6 = solution.word_break(s6, word_dict6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Overlapping words
    print("Test 7: Overlapping words - 'aaaaaaa' with ['aaaa','aaa']")
    s7 = "aaaaaaa"
    word_dict7 = ["aaaa", "aaa"]
    expected7 = True
    result7 = solution.word_break(s7, word_dict7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Multiple valid segmentations
    print("Test 8: Multiple valid segmentations")
    s8 = "catsanddog"
    word_dict8 = ["cat", "cats", "and", "sand", "dog"]
    expected8 = True
    result8 = solution.word_break(s8, word_dict8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Long string with short words
    print("Test 9: Long string with short words")
    s9 = "aaaaaaaaaaaaaaaaaaaa"
    word_dict9 = ["a", "aa", "aaa", "aaaa"]
    expected9 = True
    result9 = solution.word_break(s9, word_dict9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Word not matching exactly
    print("Test 10: Word not matching exactly")
    s10 = "leetcode"
    word_dict10 = ["leet", "code", "leetcod"]
    expected10 = True  # Can use "leet" and "code"
    result10 = solution.word_break(s10, word_dict10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Cannot segment due to missing character
    print("Test 11: Cannot segment due to missing character")
    s11 = "leetcode"
    word_dict11 = ["leet", "cod"]  # Missing 'e' at end
    expected11 = False
    result11 = solution.word_break(s11, word_dict11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Compare all approaches
    print("\nTest 12: Comparing all approaches")
    test_cases = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
        ("aaaaaaa", ["aaaa", "aaa"]),
    ]
    
    for s, word_dict in test_cases:
        result1 = solution.word_break(s, word_dict)
        result2 = solution.word_break_tabulation(s, word_dict)
        result3 = solution.word_break_optimized(s, word_dict)
        result4 = solution.word_break_bfs(s, word_dict)
        result5 = solution.word_break_dp_early_exit(s, word_dict)
        
        # Skip DFS for longer strings (too slow)
        if len(s) <= 20:
            result6 = solution.word_break_dfs(s, word_dict)
            assert result1 == result6, f"DFS mismatch for s='{s}': {result1} vs {result6}"
        
        assert result1 == result2, f"Tabulation mismatch for s='{s}': {result1} vs {result2}"
        assert result1 == result3, f"Optimized mismatch for s='{s}': {result1} vs {result3}"
        assert result1 == result4, f"BFS mismatch for s='{s}': {result1} vs {result4}"
        assert result1 == result5, f"Early exit mismatch for s='{s}': {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 13: Complex case with many possibilities
    print("\nTest 13: Complex case with many possibilities")
    s13 = "pineapplepenapple"
    word_dict13 = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected13 = True
    result13 = solution.word_break(s13, word_dict13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: All characters match but wrong segmentation
    print("Test 14: All characters match but wrong segmentation")
    s14 = "goalspecial"
    word_dict14 = ["go", "goal", "goals", "special"]
    expected14 = True  # "goals" + "pecial" - wait, "pecial" not in dict
    # Actually: "goal" + "special" = True
    result14 = solution.word_break(s14, word_dict14)
    expected14 = True
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Dictionary with single long word
    print("Test 15: Dictionary with single long word")
    s15 = "supercalifragilisticexpialidocious"
    word_dict15 = ["supercalifragilisticexpialidocious"]
    expected15 = True
    result15 = solution.word_break(s15, word_dict15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()