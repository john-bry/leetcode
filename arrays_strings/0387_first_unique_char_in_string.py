from collections import Counter

class Solution:
    def first_unique_char(self, s: str) -> int:
        """
        Approach 1: Counter
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = Counter(s)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
            
        return -1