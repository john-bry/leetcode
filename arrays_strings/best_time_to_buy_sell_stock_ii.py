from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Approach 1: Greedy
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit