class Solution:
    def reverse(self, x: int) -> int:
        """
        Approach 1: String Conversion
        Time Complexity: O(log(x))
        Space Complexity: O(log(x))
        """
        sign = -1 if x < 0 else 1
        x = str(abs(x))

        result = sign * int(x[::-1])

        return result if -2**31 <= result <= 2**31 - 1 else 0