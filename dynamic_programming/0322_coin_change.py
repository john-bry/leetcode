from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Find the minimum number of coins needed to make up the given amount.
        If it's not possible, return -1.
        
        Approach: Top-down dynamic programming with memoization
        Time Complexity: O(n * m) where n is amount, m is number of coin types
        Space Complexity: O(n) for memoization
        
        Edge cases handled:
        - Empty coins list: Returns -1
        - Amount = 0: Returns 0 (no coins needed)
        - Negative amount: Returns -1
        - Invalid coins (negative or zero): Filtered out
        - Impossible to make amount: Returns -1
        """
        # Edge case: Invalid amount
        if amount < 0:
            return -1
        
        # Edge case: Amount is 0
        if amount == 0:
            return 0
        
        # Edge case: Empty or invalid coins
        if not coins:
            return -1
        
        # Filter out invalid coins (negative or zero)
        valid_coins = [coin for coin in coins if coin > 0]
        if not valid_coins:
            return -1
        
        memo = {}

        def dp(amount: int) -> int:
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            min_coins = float('inf')

            for coin in valid_coins:
                if amount - coin >= 0:
                    result = dp(amount - coin)
                    if result != -1:  # Only consider valid subproblems
                        min_coins = min(min_coins, 1 + result)

            memo[amount] = min_coins if min_coins != float('inf') else -1
            return memo[amount]

        result = dp(amount)
        return result if result != float('inf') else -1
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach 2: Bottom-Up DP (Tabulation) - Simpler and More Intuitive
        Time Complexity: O(n * m) where n is amount, m is number of coin types
        Space Complexity: O(n) for DP array
        
        Build solution from bottom up. For each amount from 0 to target,
        find minimum coins needed using previously computed values.
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        # dp[i] = minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # For each amount from 1 to target
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin > 0 and i >= coin:
                    # If we can use this coin, update minimum
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def coinChangeSimplified(self, coins: List[int], amount: int) -> int:
        """
        Approach 3: Simplified Bottom-Up DP
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Cleaner version with less edge case handling upfront.
        """
        # Initialize DP array: dp[i] = min coins for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Build solution bottom-up
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def coinChangeClean(self, coins: List[int], amount: int) -> int:
        """
        Approach 4: Clean Top-Down with Simpler Logic
        Time Complexity: O(n * m)
        Space Complexity: O(n)
        
        Simpler version of memoization approach.
        """
        memo = {}
        
        def dp(remaining: int) -> int:
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            
            min_coins = float('inf')
            for coin in coins:
                res = dp(remaining - coin)
                if res != -1:
                    min_coins = min(min_coins, res + 1)
            
            memo[remaining] = min_coins if min_coins != float('inf') else -1
            return memo[remaining]
        
        return dp(amount)


# Test cases and examples

if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 60)
    print("Coin Change Test Cases")
    print("=" * 60)
    
    # Example 1: Standard case - can make change
    # coins = [1, 2, 5], amount = 11
    # Optimal: 5 + 5 + 1 = 3 coins
    print("\nExample 1: coins = [1, 2, 5], amount = 11")
    print("Expected: 3 (5 + 5 + 1)")
    result = solution.coin_change([1, 2, 5], 11)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 3 else '✗'}")
    
    # Example 2: Standard case - different coins
    # coins = [2], amount = 3
    # Cannot make 3 with only 2s
    print("\nExample 2: coins = [2], amount = 3")
    print("Expected: -1 (impossible)")
    result = solution.coin_change([2], 3)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == -1 else '✗'}")
    
    # Example 3: Edge case - amount = 0
    print("\nExample 3: coins = [1, 2, 5], amount = 0")
    print("Expected: 0 (no coins needed)")
    result = solution.coin_change([1, 2, 5], 0)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 0 else '✗'}")
    
    # Example 4: Edge case - empty coins list
    print("\nExample 4: coins = [], amount = 5")
    print("Expected: -1 (no coins available)")
    result = solution.coin_change([], 5)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == -1 else '✗'}")
    
    # Example 5: Edge case - negative amount
    print("\nExample 5: coins = [1, 2, 5], amount = -5")
    print("Expected: -1 (invalid amount)")
    result = solution.coin_change([1, 2, 5], -5)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == -1 else '✗'}")
    
    # Example 6: Edge case - coins with invalid values (negative or zero)
    print("\nExample 6: coins = [1, 0, -2, 5], amount = 6")
    print("Expected: 2 (5 + 1, ignoring invalid coins)")
    result = solution.coin_change([1, 0, -2, 5], 6)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 2 else '✗'}")
    
    # Example 7: Edge case - all coins invalid
    print("\nExample 7: coins = [0, -1, -5], amount = 10")
    print("Expected: -1 (no valid coins)")
    result = solution.coin_change([0, -1, -5], 10)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == -1 else '✗'}")
    
    # Example 8: Large amount with small coins
    # coins = [1], amount = 100
    # Need 100 coins of 1
    print("\nExample 8: coins = [1], amount = 100")
    print("Expected: 100 (100 coins of 1)")
    result = solution.coin_change([1], 100)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 100 else '✗'}")
    
    # Example 9: Greedy approach fails - need DP
    # coins = [1, 3, 4], amount = 6
    # Greedy: 4 + 1 + 1 = 3 coins
    # Optimal: 3 + 3 = 2 coins
    print("\nExample 9: coins = [1, 3, 4], amount = 6")
    print("Expected: 2 (3 + 3, not 4 + 1 + 1)")
    result = solution.coin_change([1, 3, 4], 6)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 2 else '✗'}")
    
    # Example 10: Single coin type that works
    print("\nExample 10: coins = [5], amount = 15")
    print("Expected: 3 (three 5s)")
    result = solution.coin_change([5], 15)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == 3 else '✗'}")
    
    # Example 11: Single coin type that doesn't work
    print("\nExample 11: coins = [5], amount = 12")
    print("Expected: -1 (cannot make 12 with 5s)")
    result = solution.coin_change([5], 12)
    print(f"Result: {result}")
    print(f"Verification: {'✓' if result == -1 else '✗'}")
    
    print("\n" + "=" * 60)
    print("Testing All Approaches")
    print("=" * 60)
    
    # Test all approaches return same results
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1, 2, 5], 0),
        ([1, 3, 4], 6),
        ([5], 15),
        ([5], 12),
    ]
    
    for coins, amt in test_cases:
        result1 = solution.coin_change(coins, amt)
        result2 = solution.coinChange(coins, amt)
        result3 = solution.coinChangeSimplified(coins, amt)
        result4 = solution.coinChangeClean(coins, amt)
        
        assert result1 == result2 == result3 == result4, \
            f"Mismatch for coins={coins}, amount={amt}: {result1} vs {result2} vs {result3} vs {result4}"
    
    print("✓ All approaches produce same results!")
    
    print("\n" + "=" * 60)
    print("All test cases completed!")
    print("=" * 60)
