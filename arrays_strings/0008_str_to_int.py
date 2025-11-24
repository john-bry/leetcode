class Solution:
    def str_to_int(self, s: str) -> int:
        """
        Approach 1: String Conversion
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        s = s.lstrip()
        
        if not s:
            return 0

        sign = 1
        result = 0
        i = 0

        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i +=1

        result = sign * result

        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        
        return result