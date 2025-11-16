"""
121. Best Time to Buy and Sell Stock
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Example 3:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Notes:
- Key insight: Track the minimum price seen so far and calculate profit for each day.
- Sliding window/two pointers approach:
  - Use buy pointer to track the minimum price (best day to buy)
  - Use sell pointer to iterate through all days
  - If current price is lower than buy price, update buy pointer
  - Otherwise, calculate profit and update max profit
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using a few variables
- Alternative approach: Track minimum price and calculate max profit in one pass.
- The sliding window approach is optimal and intuitive.
"""

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: Sliding Window / Two Pointers (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, profit)
            else:
                buy = sell

            sell += 1

        return max_profit
    
    def max_profit_min_price(self, prices: List[int]) -> int:
        """
        Approach: Track Minimum Price
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.max_profit(prices1)
    expected1 = 5
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.max_profit(prices2)
    expected2 = 0
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    prices3 = [1, 2, 3, 4, 5]
    result3 = solution.max_profit(prices3)
    expected3 = 4
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - single element
    prices4 = [1]
    result4 = solution.max_profit(prices4)
    expected4 = 0
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - two elements, profit
    prices5 = [1, 2]
    result5 = solution.max_profit(prices5)
    expected5 = 1
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - two elements, no profit
    prices6 = [2, 1]
    result6 = solution.max_profit(prices6)
    expected6 = 0
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - all same price
    prices7 = [5, 5, 5, 5, 5]
    result7 = solution.max_profit(prices7)
    expected7 = 0
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - best profit not at end
    prices8 = [3, 2, 6, 5, 0, 3]
    result8 = solution.max_profit(prices8)
    expected8 = 4  # Buy at 2, sell at 6
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()