class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Approach: Two Pointers (Optimal)
        Time Complexity: O(n) where n is length of s
        Space Complexity: O(1)
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