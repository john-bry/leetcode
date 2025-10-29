"""
40. Combination Sum II
Difficulty: Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

Notes:
- Key insight: Use backtracking with duplicate skipping.
- Sort candidates first to group duplicates together.
- Skip duplicates at the same level to avoid duplicate combinations.
- Each element can only be used once, so pass i+1 in recursion.
- This is similar to Combination Sum I but with no reuse and duplicates.
"""

from typing import List


class Solution:
    def combination_sum_ii(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 1: Backtracking with Duplicate Skipping (Optimal)
        Time Complexity: O(2^n) - exponential due to all combinations
        Space Complexity: O(target) - recursion stack depth
        
        Use backtracking to explore all possible combinations.
        Sort candidates first to group duplicates together.
        Skip duplicates at the same level to avoid duplicate combinations.
        """
        candidates.sort()  # MUST sort for duplicate detection
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found valid combination
            if remaining == 0:
                result.append(current[:])
                return
            
            # Try each candidate from start onwards
            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Optimization: early termination
                if candidates[i] > remaining:
                    break
                
                # Choose
                current.append(candidates[i])
                # Explore (i+1 because can't reuse)
                backtrack(i + 1, current, remaining - candidates[i])
                # Unchoose
                current.pop()
        
        backtrack(0, [], target)
        return result
    
    def combination_sum_ii_optimized(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 2: Optimized Backtracking with Frequency Count
        Time Complexity: O(2^n)
        Space Complexity: O(target)
        
        Use frequency counting to handle duplicates more efficiently.
        """
        from collections import Counter
        
        candidates.sort()
        freq = Counter(candidates)
        unique_candidates = list(freq.keys())
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                result.append(current[:])
                return
            
            for i in range(start, len(unique_candidates)):
                candidate = unique_candidates[i]
                if candidate > remaining:
                    break
                
                # Try different frequencies of this candidate
                for count in range(1, freq[candidate] + 1):
                    if candidate * count > remaining:
                        break
                    
                    # Add count copies of candidate
                    for _ in range(count):
                        current.append(candidate)
                    
                    backtrack(i + 1, current, remaining - candidate * count)
                    
                    # Remove count copies of candidate
                    for _ in range(count):
                        current.pop()
        
        backtrack(0, [], target)
        return result
    
    def combination_sum_ii_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 3: Iterative with Stack
        Time Complexity: O(2^n)
        Space Complexity: O(target)
        
        Use iterative approach with explicit stack instead of recursion.
        """
        candidates.sort()
        result = []
        stack = [(0, [], target)]  # (start_index, current_combination, remaining)
        
        while stack:
            start, current, remaining = stack.pop()
            
            if remaining == 0:
                result.append(current)
                continue
            
            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                new_current = current + [candidates[i]]
                new_remaining = remaining - candidates[i]
                stack.append((i + 1, new_current, new_remaining))
        
        return result
    
    def combination_sum_ii_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 4: Dynamic Programming (Alternative)
        Time Complexity: O(target * candidates.length * combinations)
        Space Complexity: O(target * combinations)
        
        Use DP to build combinations bottom-up.
        Less efficient than backtracking for this problem.
        """
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        
        for candidate in candidates:
            for t in range(target, candidate - 1, -1):
                for combination in dp[t - candidate]:
                    new_combination = combination + [candidate]
                    if new_combination not in dp[t]:
                        dp[t].append(new_combination)
        
        return dp[target]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    expected1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    result1 = solution.combination_sum_ii(candidates1, target1)
    # Sort both for comparison since order doesn't matter
    result1.sort()
    expected1.sort()
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Multiple duplicates
    print("Test 2: Multiple duplicates")
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    expected2 = [[1, 2, 2], [5]]
    result2 = solution.combination_sum_ii(candidates2, target2)
    result2.sort()
    expected2.sort()
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: No solution
    print("Test 3: No solution")
    candidates3 = [2, 5, 2, 1, 2]
    target3 = 1
    expected3 = [[1]]
    result3 = solution.combination_sum_ii(candidates3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single element
    print("Test 4: Single element")
    candidates4 = [1]
    target4 = 1
    expected4 = [[1]]
    result4 = solution.combination_sum_ii(candidates4, target4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single element - no solution
    print("Test 5: Single element - no solution")
    candidates5 = [2]
    target5 = 1
    expected5 = []
    result5 = solution.combination_sum_ii(candidates5, target5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: All same elements
    print("Test 6: All same elements")
    candidates6 = [1, 1, 1, 1]
    target6 = 2
    expected6 = [[1, 1]]
    result6 = solution.combination_sum_ii(candidates6, target6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_candidates = [10, 1, 2, 7, 6, 1, 5]
    test_target = 8
    
    result_backtrack = solution.combination_sum_ii(test_candidates, test_target)
    result_opt = solution.combination_sum_ii_optimized(test_candidates, test_target)
    result_iter = solution.combination_sum_ii_iterative(test_candidates, test_target)
    result_dp = solution.combination_sum_ii_dp(test_candidates, test_target)
    
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    for result in [result_backtrack, result_opt, result_iter, result_dp]:
        result.sort()
        expected.sort()
        assert result == expected, f"Approach comparison failed: expected {expected}, got {result}"
    
    # Test case 8: Edge case - target equals smallest candidate
    print("Test 8: Edge case - target equals smallest candidate")
    candidates8 = [1, 2, 3]
    target8 = 1
    expected8 = [[1]]
    result8 = solution.combination_sum_ii(candidates8, target8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Edge case - all candidates larger than target
    print("Test 9: Edge case - all candidates larger than target")
    candidates9 = [5, 6, 7]
    target9 = 3
    expected9 = []
    result9 = solution.combination_sum_ii(candidates9, target9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Complex scenario with many duplicates
    print("Test 10: Complex scenario with many duplicates")
    candidates10 = [1, 1, 1, 2, 2, 3, 3, 3]
    target10 = 6
    expected10 = [[1, 1, 1, 3], [1, 1, 2, 2], [1, 2, 3], [3, 3]]
    result10 = solution.combination_sum_ii(candidates10, target10)
    result10.sort()
    expected10.sort()
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    # Test case 11: Large target
    print("Test 11: Large target")
    candidates11 = [1, 2, 3, 4, 5]
    target11 = 8
    expected11 = [[1, 2, 5], [1, 3, 4], [3, 5]]
    result11 = solution.combination_sum_ii(candidates11, target11)
    result11.sort()
    expected11.sort()
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    
    # Test case 12: Negative numbers (if allowed)
    print("Test 12: Edge case - single element equals target")
    candidates12 = [5]
    target12 = 5
    expected12 = [[5]]
    result12 = solution.combination_sum_ii(candidates12, target12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()