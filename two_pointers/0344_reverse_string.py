class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Approach 1: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1