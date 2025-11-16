class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        """
        Approach: Expand Around Center
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """

        def expand_substring(l, r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count

        for i in range(len(s)):
            palindromes += expand_substring(i, i)
            palindromes += expand_substring(i, i + 1)

        return palindromes

        
