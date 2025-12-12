from typing import List

class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def string_string(self, s: str) -> List[str]:
        seen = set()
        result = []
        start = 0

        for i in range(len(s)):
            string = s[start:i+1]

            if string not in seen:
                seen.add(string)
                result.append(string)
                start = i + 1

        return result
