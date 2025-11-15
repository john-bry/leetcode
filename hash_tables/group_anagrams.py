"""
49. Group Anagrams
Difficulty: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: 
- "bat" has no anagrams, so it's in its own group.
- "nat" and "tan" are anagrams of each other.
- "ate", "eat", and "tea" are anagrams of each other.

Example 2:
Input: strs = [""]
Output: [[""]]
Explanation: Empty string is grouped with itself.

Example 3:
Input: strs = ["a"]
Output: [["a"]]
Explanation: Single character string is grouped with itself.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Notes:
- Key insight: Two strings are anagrams if they have the same sorted character sequence.
- Hash map approach: Use sorted string as key to group anagrams together.
- Time complexity: O(n * k log k) where n is number of strings and k is average length of strings.
  - Sorting each string: O(k log k)
  - Processing n strings: O(n)
- Space complexity: O(n * k) to store all strings in the result.
- Alternative approaches:
  - Character frequency counting: Count characters in each string and use tuple of counts as key - O(n * k) time, O(n * k) space.
  - This avoids sorting but requires building frequency arrays.
- The sorted string approach is simpler and more intuitive.
- Using tuple(sorted(s)) as key because lists are not hashable (cannot be dictionary keys).
"""

from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hash Map with Sorted String as Key
        Time Complexity: O(n * k log k) where n is number of strings, k is average length
        Space Complexity: O(n * k)
        """
        anagrams = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())
    
    def group_anagrams_frequency(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Hash Map with Character Frequency as Key
        Time Complexity: O(n * k) where n is number of strings, k is average length
        Space Complexity: O(n * k)
        """
        anagrams = defaultdict(list)
        for s in strs:
            # Create frequency count tuple (26 characters for lowercase English)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(s)
        
        return list(anagrams.values())


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.group_anagrams(strs1)
    # Sort each group and the overall result for comparison
    result1_sorted = sorted([sorted(group) for group in result1])
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected1_sorted = sorted([sorted(group) for group in expected1])
    assert result1_sorted == expected1_sorted, f"Test 1 failed: expected {expected1_sorted}, got {result1_sorted}"
    
    # Test case 2
    strs2 = [""]
    result2 = solution.group_anagrams(strs2)
    expected2 = [[""]]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    strs3 = ["a"]
    result3 = solution.group_anagrams(strs3)
    expected3 = [["a"]]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - no anagrams
    strs4 = ["abc", "def", "ghi"]
    result4 = solution.group_anagrams(strs4)
    result4_sorted = sorted([sorted(group) for group in result4])
    expected4 = [["abc"], ["def"], ["ghi"]]
    expected4_sorted = sorted([sorted(group) for group in expected4])
    assert result4_sorted == expected4_sorted, f"Test 4 failed: expected {expected4_sorted}, got {result4_sorted}"
    
    # Test case 5 - all anagrams
    strs5 = ["abc", "bca", "cab"]
    result5 = solution.group_anagrams(strs5)
    result5_sorted = sorted([sorted(group) for group in result5])
    expected5 = [["abc", "bca", "cab"]]
    expected5_sorted = sorted([sorted(group) for group in expected5])
    assert result5_sorted == expected5_sorted, f"Test 5 failed: expected {expected5_sorted}, got {result5_sorted}"
    
    # Test case 6 - multiple groups
    strs6 = ["listen", "silent", "enlist", "hello", "world"]
    result6 = solution.group_anagrams(strs6)
    result6_sorted = sorted([sorted(group) for group in result6])
    expected6 = [["listen", "silent", "enlist"], ["hello"], ["world"]]
    expected6_sorted = sorted([sorted(group) for group in expected6])
    assert result6_sorted == expected6_sorted, f"Test 6 failed: expected {expected6_sorted}, got {result6_sorted}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()