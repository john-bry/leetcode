class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        """
        Approach 1: Iterative
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0  
            
        return [1] + digits