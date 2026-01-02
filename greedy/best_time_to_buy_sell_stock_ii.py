"""
122. Best Time to Buy and Sell Stock II
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of 
the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging 
multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never engage the transaction 
to achieve the maximum profit of 0.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4

Notes:
- Key insight: Since we can buy and sell multiple times, we can capture ALL positive price differences.
- Greedy approach: Whenever price increases from day i-1 to day i, we can buy on day i-1 and sell on day i.
- This is optimal because:
  - If prices are [a, b, c] where a < b < c, buying at a and selling at c gives profit (c - a)
  - But buying at a, selling at b, then buying at b, selling at c also gives (b - a) + (c - b) = (c - a)
  - So we can capture all positive differences without losing any profit
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using a few variables
- Alternative approaches:
  - Greedy (current): Capture all positive differences, O(n) time, O(1) space
  - Valley-Peak: Find valleys and peaks, buy at valleys and sell at peaks
  - Dynamic Programming: Track state of holding/not holding stock, O(n) time, O(1) space
  - Recursive with memoization: O(n) time, O(n) space (overkill for this problem)
- Edge cases: All prices decreasing, all prices same, single price, two prices
"""

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Approach 1: Greedy (Current)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Capture all positive price differences. Whenever price increases,
        we can buy the previous day and sell the current day.
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
    
    def max_profit_valley_peak(self, prices: List[int]) -> int:
        """
        Approach 2: Valley-Peak
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Find valleys (local minima) and peaks (local maxima).
        Buy at valleys and sell at peaks.
        """
        if not prices or len(prices) < 2:
            return 0
        
        max_profit = 0
        i = 0
        n = len(prices)
        
        while i < n - 1:
            # Find valley (local minimum)
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            # Find peak (local maximum)
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            max_profit += peak - valley
            i += 1
        
        return max_profit
    
    def max_profit_dp(self, prices: List[int]) -> int:
        """
        Approach 3: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Track two states:
        - hold: maximum profit when holding a stock
        - not_hold: maximum profit when not holding a stock
        
        At each day, we can either:
        - Hold: keep holding or buy today
        - Not hold: keep not holding or sell today
        """
        if not prices:
            return 0
        
        hold = -prices[0]  # Buy on first day
        not_hold = 0  # Don't buy on first day
        
        for i in range(1, len(prices)):
            # Either keep holding or buy today (from not_hold state)
            new_hold = max(hold, not_hold - prices[i])
            # Either keep not holding or sell today (from hold state)
            new_not_hold = max(not_hold, hold + prices[i])
            
            hold = new_hold
            not_hold = new_not_hold
        
        return not_hold  # Maximum profit when not holding stock
    
    def max_profit_dp_optimized(self, prices: List[int]) -> int:
        """
        Approach 4: DP with State Variables (Optimized)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Same as DP but with clearer variable names.
        """
        if not prices:
            return 0
        
        cash = 0  # Maximum profit with no stock
        hold = -prices[0]  # Maximum profit with stock
        
        for i in range(1, len(prices)):
            # Either keep cash or sell stock today
            cash = max(cash, hold + prices[i])
            # Either keep holding or buy stock today
            hold = max(hold, cash - prices[i])
        
        return cash
    
    def max_profit_recursive(self, prices: List[int]) -> int:
        """
        Approach 5: Recursive with Memoization
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Recursive solution with memoization (for educational purposes).
        Not recommended for production due to recursion overhead.
        """
        if not prices:
            return 0
        
        memo = {}
        
        def dfs(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # Skip today
            skip = dfs(i + 1, holding)
            
            if holding:
                # Sell today
                sell = dfs(i + 1, False) + prices[i]
                result = max(skip, sell)
            else:
                # Buy today
                buy = dfs(i + 1, True) - prices[i]
                result = max(skip, buy)
            
            memo[(i, holding)] = result
            return result
        
        return dfs(0, False)
    
    def max_profit_brute_force(self, prices: List[int]) -> int:
        """
        Approach 6: Brute Force (For Comparison)
        Time Complexity: O(2^n) - exponential
        Space Complexity: O(n) - recursion stack
        
        Try all possible buy/sell combinations.
        Only for educational purposes - too slow for large inputs.
        """
        def calculate(prices: List[int], start: int) -> int:
            if start >= len(prices):
                return 0
            
            max_profit = 0
            for i in range(start, len(prices)):
                max_profit_local = 0
                for j in range(i + 1, len(prices)):
                    if prices[j] > prices[i]:
                        profit = prices[j] - prices[i] + calculate(prices, j + 1)
                        max_profit_local = max(max_profit_local, profit)
                max_profit = max(max_profit, max_profit_local)
            return max_profit
        
        return calculate(prices, 0)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example with multiple transactions
    print("Test 1: Basic example - [7,1,5,3,6,4]")
    prices1 = [7, 1, 5, 3, 6, 4]
    expected1 = 7
    result1 = solution.max_profit(prices1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Continuously increasing
    print("Test 2: Continuously increasing - [1,2,3,4,5]")
    prices2 = [1, 2, 3, 4, 5]
    expected2 = 4
    result2 = solution.max_profit(prices2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Continuously decreasing
    print("Test 3: Continuously decreasing - [7,6,4,3,1]")
    prices3 = [7, 6, 4, 3, 1]
    expected3 = 0
    result3 = solution.max_profit(prices3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single element
    print("Test 4: Single element - [1]")
    prices4 = [1]
    expected4 = 0
    result4 = solution.max_profit(prices4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Two elements, profit
    print("Test 5: Two elements, profit - [1,2]")
    prices5 = [1, 2]
    expected5 = 1
    result5 = solution.max_profit(prices5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two elements, no profit
    print("Test 6: Two elements, no profit - [2,1]")
    prices6 = [2, 1]
    expected6 = 0
    result6 = solution.max_profit(prices6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: All same price
    print("Test 7: All same price - [5,5,5,5,5]")
    prices7 = [5, 5, 5, 5, 5]
    expected7 = 0
    result7 = solution.max_profit(prices7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Multiple peaks and valleys
    print("Test 8: Multiple peaks and valleys - [1,2,1,2,1,2]")
    prices8 = [1, 2, 1, 2, 1, 2]
    expected8 = 3  # Buy at 1, sell at 2 (three times)
    result8 = solution.max_profit(prices8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Large profit opportunity
    print("Test 9: Large profit - [1,5,2,8,3,10]")
    prices9 = [1, 5, 2, 8, 3, 10]
    expected9 = 17  # (5-1) + (8-2) + (10-3) = 4 + 6 + 7 = 17
    result9 = solution.max_profit(prices9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Compare all approaches
    print("\nTest 10: Comparing all approaches")
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [1],
        [1, 2],
        [2, 1],
        [5, 5, 5, 5, 5],
        [1, 2, 1, 2, 1, 2],
        [1, 5, 2, 8, 3, 10],
        [3, 3, 5, 0, 0, 3, 1, 4],
        [2, 1, 2, 0, 1],
    ]
    
    for prices in test_cases:
        result1 = solution.max_profit(prices)
        result2 = solution.max_profit_valley_peak(prices)
        result3 = solution.max_profit_dp(prices)
        result4 = solution.max_profit_dp_optimized(prices)
        result5 = solution.max_profit_recursive(prices)
        
        assert result1 == result2, f"Valley-peak mismatch for {prices}: {result1} vs {result2}"
        assert result1 == result3, f"DP mismatch for {prices}: {result1} vs {result3}"
        assert result1 == result4, f"DP optimized mismatch for {prices}: {result1} vs {result4}"
        assert result1 == result5, f"Recursive mismatch for {prices}: {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 11: Edge case - empty array
    print("\nTest 11: Empty array")
    prices11 = []
    expected11 = 0
    result11 = solution.max_profit(prices11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Single transaction is best
    print("Test 12: Single transaction best - [3,2,6,5,0,3]")
    prices12 = [3, 2, 6, 5, 0, 3]
    expected12 = 7  # (6-2) + (3-0) = 4 + 3 = 7
    result12 = solution.max_profit(prices12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Alternating pattern
    print("Test 13: Alternating pattern - [1,3,2,4,3,5]")
    prices13 = [1, 3, 2, 4, 3, 5]
    expected13 = 6  # (3-1) + (4-2) + (5-3) = 2 + 2 + 2 = 6
    result13 = solution.max_profit(prices13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Large array
    print("Test 14: Large array with increasing trend")
    prices14 = list(range(1000))
    expected14 = 999  # Buy at 0, sell at 999, or capture all differences = 999
    result14 = solution.max_profit(prices14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex pattern
    print("Test 15: Complex pattern - [6,1,3,2,4,7]")
    prices15 = [6, 1, 3, 2, 4, 7]
    expected15 = 7  # (3-1) + (4-2) + (7-4) = 2 + 2 + 3 = 7
    result15 = solution.max_profit(prices15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()