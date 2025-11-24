class Solution:
    def find_idx_first_occurence_in_str(self, haystack: str, needle: str) -> int:
        """
        Approach 1: Brute Force
        Time Complexity: O(n * m)
        Space Complexity: O(1)
        """
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1