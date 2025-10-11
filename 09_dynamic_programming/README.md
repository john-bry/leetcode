# Dynamic Programming

## Overview

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It's particularly useful for optimization problems where we need to find the best solution.

## Core Concepts

### 1. Overlapping Subproblems

- The same subproblems are solved multiple times
- DP stores solutions to avoid recomputation

### 2. Optimal Substructure

- Optimal solution contains optimal solutions to subproblems
- Can build optimal solution from optimal subproblem solutions

### 3. Memoization vs Tabulation

- **Memoization**: Top-down approach, recursive with caching
- **Tabulation**: Bottom-up approach, iterative with table

## Common DP Patterns

### 1. Fibonacci Sequence

```python
# Memoization
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Tabulation
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

### 2. Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1
```

### 3. House Robber

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current

    return prev1
```

## 2D DP Problems

### 1. Unique Paths

```python
def unique_paths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
```

### 2. Longest Common Subsequence

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

## Knapsack Problems

### 0/1 Knapsack

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

## Common DP Categories

### 1. Linear DP

- **Fibonacci**: F(n) = F(n-1) + F(n-2)
- **Climbing Stairs**: Ways to reach top
- **House Robber**: Maximum money without adjacent

### 2. Grid DP

- **Unique Paths**: Count paths in grid
- **Minimum Path Sum**: Minimum cost path
- **Robot Paths**: With obstacles

### 3. String DP

- **Longest Common Subsequence**: LCS
- **Edit Distance**: Minimum operations
- **Longest Palindromic Subsequence**: LPS

### 4. Tree DP

- **House Robber III**: Tree version
- **Binary Tree Maximum Path Sum**: Tree paths
- **Diameter of Binary Tree**: Tree properties

## Optimization Techniques

### Space Optimization

```python
# Instead of 2D array, use 1D array
def optimized_dp(n):
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            curr[j] = prev[j-1] + curr[j-1]
        prev, curr = curr, prev

    return prev[n]
```

### Rolling Array

```python
# Use only necessary previous states
def rolling_array_dp(n):
    prev2, prev1 = 0, 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1
```

## Time Complexity Patterns

- **O(n)**: Linear DP, single dimension
- **O(n²)**: 2D DP, nested loops
- **O(n \* m)**: Two sequences of length n, m
- **O(n \* capacity)**: Knapsack problems

## Space Complexity Patterns

- **O(n)**: 1D DP array
- **O(n²)**: 2D DP array
- **O(1)**: Space-optimized with rolling variables
- **O(n \* m)**: Two-dimensional problems
