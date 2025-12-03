"""
269. Alien Dictionary
Difficulty: Hard

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
- From "wrt" and "wrf", we get 't' < 'f'
- From "wrf" and "er", we get 'w' < 'e'
- From "er" and "ett", we get 'r' < 't'
- From "ett" and "rftt", we get 'e' < 'r'
- So the order is "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"
Explanation: The order is "z" < "x", so return "zx".

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.

Notes:
- Key insight: This is a topological sorting problem. Build a directed graph where edges represent ordering relationships.
- Compare adjacent words to find the first differing character, which gives us an edge in the graph.
- Edge case: If word1 is a prefix of word2 and word1 comes before word2, it's invalid (e.g., ["abc", "ab"]).
- Use Kahn's algorithm (BFS) or DFS for topological sort.
- If there's a cycle, return "" (invalid ordering).
- Time complexity: O(C) where C is total characters across all words
- Space complexity: O(1) for alphabet size (26 letters), but O(V + E) for graph
- Alternative approaches:
  - Kahn's algorithm (BFS): O(V + E) time, O(V + E) space - current approach
  - DFS topological sort: O(V + E) time, O(V + E) space - alternative
  - DFS with cycle detection: O(V + E) time, O(V + E) space - explicit cycle detection
  - Build graph differently: O(C) time, O(1) space for graph - different graph construction
- Edge cases: Empty words, single word, invalid prefix, cycles, disconnected components
"""

from collections import defaultdict, deque
from typing import List, Set


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Approach 1: Kahn's Algorithm (BFS Topological Sort - Current)
        Time Complexity: O(C) where C is total characters
        Space Complexity: O(1) for alphabet (26 letters), O(V + E) for graph
        
        Build a directed graph from adjacent word comparisons, then use BFS
        to perform topological sort.
        """
        # Step 1: Initialize graph and in-degree
        graph = defaultdict(set)
        in_degree = {}
        
        # Initialize all characters that appear in words
        for word in words:
            for char in word:
                in_degree[char] = 0
        
        # Step 2: Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Edge case: word1 is prefix of word2 but comes after
            # e.g., ["abc", "ab"] is invalid
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Find first differing character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # Add edge: word1[j] → word2[j]
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break  # Only need first difference
        
        # Step 3: Topological sort using BFS (Kahn's algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            # Reduce in-degree of neighbors
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we didn't process all characters, there's a cycle
        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)
    
    def alienOrderDFS(self, words: List[str]) -> str:
        """
        Approach 2: DFS Topological Sort
        Time Complexity: O(C) where C is total characters
        Space Complexity: O(1) for alphabet, O(V + E) for graph
        
        Use DFS to perform topological sort. Mark nodes as visiting, visited, or unvisited.
        """
        # Build graph
        graph = defaultdict(set)
        
        # Initialize all characters
        all_chars = set()
        for word in words:
            for char in word:
                all_chars.add(char)
        
        # Build graph from adjacent word comparisons
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Invalid: word1 is prefix of word2
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Find first differing character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        
        # DFS topological sort
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {char: WHITE for char in all_chars}
        result = []
        
        def dfs(char: str) -> bool:
            """Returns True if cycle detected"""
            if color[char] == GRAY:  # Cycle detected
                return True
            if color[char] == BLACK:  # Already processed
                return False
            
            color[char] = GRAY  # Mark as visiting
            
            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True
            
            color[char] = BLACK  # Mark as visited
            result.append(char)
            return False
        
        # Process all characters
        for char in all_chars:
            if color[char] == WHITE:
                if dfs(char):
                    return ""  # Cycle detected
        
        return "".join(reversed(result))  # Reverse because DFS adds in reverse order
    
    def alienOrderDFSCycle(self, words: List[str]) -> str:
        """
        Approach 3: DFS with Explicit Cycle Detection
        Time Complexity: O(C)
        Space Complexity: O(1) for alphabet, O(V + E) for graph
        
        Similar to Approach 2 but with more explicit cycle detection.
        """
        graph = defaultdict(set)
        all_chars = set()
        
        for word in words:
            for char in word:
                all_chars.add(char)
        
        # Build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        
        # DFS with cycle detection
        visited = set()
        visiting = set()
        result = []
        
        def has_cycle(char: str) -> bool:
            """Returns True if cycle detected"""
            if char in visiting:
                return True
            if char in visited:
                return False
            
            visiting.add(char)
            
            for neighbor in graph[char]:
                if has_cycle(neighbor):
                    return True
            
            visiting.remove(char)
            visited.add(char)
            result.append(char)
            return False
        
        for char in all_chars:
            if char not in visited:
                if has_cycle(char):
                    return ""
        
        return "".join(reversed(result))
    
    def alienOrderAlternative(self, words: List[str]) -> str:
        """
        Approach 4: Alternative Graph Building
        Time Complexity: O(C)
        Space Complexity: O(1) for alphabet, O(V + E) for graph
        
        Same logic but with different graph building structure.
        """
        if not words:
            return ""
        
        # Initialize
        graph = defaultdict(set)
        in_degree = {}
        
        # Collect all unique characters
        for word in words:
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0
        
        # Build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check for invalid prefix
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            # Compare characters
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Topological sort
        queue = deque([char for char, degree in in_degree.items() if degree == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return "".join(order) if len(order) == len(in_degree) else ""
    
    def alienOrderOriginal(self, words: List[str]) -> str:
        """
        Approach 5: Original Implementation
        Time Complexity: O(C)
        Space Complexity: O(1) for alphabet, O(V + E) for graph
        
        Original implementation with same logic as Approach 1.
        """
        graph = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example [\"wrt\",\"wrf\",\"er\",\"ett\",\"rftt\"]")
    words1 = ["wrt","wrf","er","ett","rftt"]
    result1 = solution.alienOrder(words1)
    # Valid outputs: "wertf" or any valid topological ordering
    assert len(result1) == 5, f"Test 1 failed: expected length 5, got {len(result1)}"
    assert set(result1) == {'w', 'e', 'r', 't', 'f'}, f"Test 1 failed: wrong characters"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Simple two words
    print("Test 2: Simple two words [\"z\",\"x\"]")
    words2 = ["z","x"]
    expected2 = "zx"
    result2 = solution.alienOrder(words2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Invalid ordering (cycle)
    print("Test 3: Invalid ordering [\"z\",\"x\",\"z\"]")
    words3 = ["z","x","z"]
    expected3 = ""
    result3 = solution.alienOrder(words3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single word
    print("Test 4: Single word [\"abc\"]")
    words4 = ["abc"]
    result4 = solution.alienOrder(words4)
    # Should return all unique characters in any order
    assert len(result4) == 3, f"Test 4 failed: expected length 3, got {len(result4)}"
    assert set(result4) == {'a', 'b', 'c'}, f"Test 4 failed: wrong characters"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Invalid prefix
    print("Test 5: Invalid prefix [\"abc\",\"ab\"]")
    words5 = ["abc","ab"]
    expected5 = ""
    result5 = solution.alienOrder(words5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        ["wrt","wrf","er","ett","rftt"],
        ["z","x"],
        ["abc"],
        ["ab","abc"],
    ]
    
    for words in test_cases:
        result1 = solution.alienOrder(words)
        result2 = solution.alienOrderDFS(words)
        result3 = solution.alienOrderDFSCycle(words)
        result4 = solution.alienOrderAlternative(words)
        result5 = solution.alienOrderOriginal(words)
        
        # For valid cases, check that all results have same characters
        if result1 != "":
            assert set(result1) == set(result2), f"DFS failed for {words}: {result1} vs {result2}"
            assert set(result1) == set(result3), f"DFS Cycle failed for {words}: {result1} vs {result3}"
            assert set(result1) == set(result4), f"Alternative failed for {words}: {result1} vs {result4}"
            assert set(result1) == set(result5), f"Original failed for {words}: {result1} vs {result5}"
        else:
            assert result2 == "", f"DFS should also return empty for {words}"
            assert result3 == "", f"DFS Cycle should also return empty for {words}"
            assert result4 == "", f"Alternative should also return empty for {words}"
            assert result5 == "", f"Original should also return empty for {words}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: Empty words
    print("\nTest 7: Empty words []")
    words7 = []
    result7 = solution.alienOrder(words7)
    assert result7 == "", f"Test 7 failed: expected empty string, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Single character words
    print("Test 8: Single character words [\"a\",\"b\",\"c\"]")
    words8 = ["a","b","c"]
    result8 = solution.alienOrder(words8)
    assert len(result8) == 3, f"Test 8 failed: expected length 3, got {len(result8)}"
    assert set(result8) == {'a', 'b', 'c'}, f"Test 8 failed: wrong characters"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: All same words
    print("Test 9: All same words [\"abc\",\"abc\",\"abc\"]")
    words9 = ["abc","abc","abc"]
    result9 = solution.alienOrder(words9)
    assert len(result9) == 3, f"Test 9 failed: expected length 3, got {len(result9)}"
    assert set(result9) == {'a', 'b', 'c'}, f"Test 9 failed: wrong characters"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Disconnected components
    print("Test 10: Disconnected components [\"ab\",\"cd\"]")
    words10 = ["ab","cd"]
    result10 = solution.alienOrder(words10)
    assert len(result10) == 4, f"Test 10 failed: expected length 4, got {len(result10)}"
    assert set(result10) == {'a', 'b', 'c', 'd'}, f"Test 10 failed: wrong characters"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Complex ordering
    print("Test 11: Complex ordering [\"baa\",\"abcd\",\"abca\",\"cab\",\"cad\"]")
    words11 = ["baa","abcd","abca","cab","cad"]
    result11 = solution.alienOrder(words11)
    # Valid orderings exist, check characters match
    assert len(result11) > 0, f"Test 11 failed: should have valid ordering"
    all_chars = set(''.join(words11))
    assert set(result11) == all_chars, f"Test 11 failed: wrong characters"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Cycle detection
    print("Test 12: Cycle detection [\"a\",\"b\",\"a\"]")
    words12 = ["a","b","a"]
    expected12 = ""
    result12 = solution.alienOrder(words12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Multiple valid orderings
    print("Test 13: Multiple valid orderings [\"a\",\"b\",\"c\",\"d\"]")
    words13 = ["a","b","c","d"]
    result13 = solution.alienOrder(words13)
    assert len(result13) == 4, f"Test 13 failed: expected length 4, got {len(result13)}"
    assert set(result13) == {'a', 'b', 'c', 'd'}, f"Test 13 failed: wrong characters"
    # Should be in order: a < b < c < d
    assert result13.index('a') < result13.index('b') < result13.index('c') < result13.index('d'), \
        f"Test 13 failed: wrong ordering"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Long words
    print("Test 14: Long words [\"abcdef\",\"abcdeg\",\"abcdeh\"]")
    words14 = ["abcdef","abcdeg","abcdeh"]
    result14 = solution.alienOrder(words14)
    assert len(result14) >= 6, f"Test 14 failed: expected at least 6 characters"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Invalid prefix case 2
    print("Test 15: Invalid prefix [\"ab\",\"a\"]")
    words15 = ["ab","a"]
    expected15 = ""
    result15 = solution.alienOrder(words15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Complex cycle
    print("Test 16: Complex cycle [\"a\",\"b\",\"c\",\"a\"]")
    words16 = ["a","b","c","a"]
    expected16 = ""
    result16 = solution.alienOrder(words16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
