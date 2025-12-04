class Solution:
    def roman_to_integer(self, s: str) -> int:
        """
        Approach 1: Hash Table (Current)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        return total
