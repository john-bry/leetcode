"""
39. Combination Sum
Difficulty: Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

Notes:
- Key insight: Use backtracking to explore all possible combinations.
- Sort candidates first to enable pruning and avoid duplicates.
- Use start index to avoid duplicate combinations (e.g., [2,3] and [3,2]).
- Same element can be used multiple times, so pass same index in recursion.
- Prune branches where remaining target < current candidate.
"""

from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 1: Backtracking (Optimal)
        Time Complexity: O(2^target) - exponential due to unlimited reuse
        Space Complexity: O(target) - recursion stack depth
        
        Use backtracking to explore all possible combinations.
        Sort candidates first to enable pruning and avoid duplicates.
        """
        result = []
        candidates.sort()  # Sort to enable pruning
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found valid combination
            if remaining == 0:
                result.append(current[:])  # Must copy!
                return
            
            # Try each candidate from start onwards
            for i in range(start, len(candidates)):
                # Pruning: if current candidate > remaining, skip rest
                if candidates[i] > remaining:
                    break
                
                # Choose: add candidate
                current.append(candidates[i])
                
                # Explore: same index allows reuse
                backtrack(i, current, remaining - candidates[i])
                
                # Unchoose: backtrack
                current.pop()
        
        backtrack(0, [], target)
        return result
    
    def combination_sum_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 2: Dynamic Programming
        Time Complexity: O(target * candidates.length * combinations)
        Space Complexity: O(target * combinations)
        
        Use DP to build combinations bottom-up.
        Less efficient than backtracking for this problem.
        """
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # Base case: empty combination for target 0
        
        for candidate in candidates:
            for t in range(candidate, target + 1):
                for combination in dp[t - candidate]:
                    dp[t].append(combination + [candidate])
        
        return dp[target]
    
    def combination_sum_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 3: Iterative with Stack
        Time Complexity: O(2^target)
        Space Complexity: O(target)
        
        Use iterative approach with explicit stack instead of recursion.
        """
        result = []
        candidates.sort()
        stack = [(0, [], target)]  # (start_index, current_combination, remaining)
        
        while stack:
            start, current, remaining = stack.pop()
            
            if remaining == 0:
                result.append(current)
                continue
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                new_current = current + [candidates[i]]
                new_remaining = remaining - candidates[i]
                stack.append((i, new_current, new_remaining))
        
        return result
    
    def combination_sum_optimized(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 4: Optimized Backtracking with Early Pruning
        Time Complexity: O(2^target)
        Space Complexity: O(target)
        
        Optimized version with better pruning and early termination.
        """
        result = []
        candidates.sort()
        
        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                # Early pruning
                if candidates[i] > remaining:
                    break
                
                # Skip duplicates (if candidates had duplicates)
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    result1 = solution.combination_sum(candidates1, target1)
    # Sort both for comparison since order doesn't matter
    result1.sort()
    expected1.sort()
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Multiple combinations
    print("Test 2: Multiple combinations")
    candidates2 = [2, 3, 5]
    target2 = 8
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result2 = solution.combination_sum(candidates2, target2)
    result2.sort()
    expected2.sort()
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: No solution
    print("Test 3: No solution")
    candidates3 = [2]
    target3 = 1
    expected3 = []
    result3 = solution.combination_sum(candidates3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single element solution
    print("Test 4: Single element solution")
    candidates4 = [1]
    target4 = 1
    expected4 = [[1]]
    result4 = solution.combination_sum(candidates4, target4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Large target
    print("Test 5: Large target")
    candidates5 = [2, 3, 5]
    target5 = 8
    expected5 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result5 = solution.combination_sum(candidates5, target5)
    result5.sort()
    expected5.sort()
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Compare different approaches
    print("Test 6: Compare different approaches")
    test_candidates = [2, 3, 6, 7]
    test_target = 7
    
    result_backtrack = solution.combination_sum(test_candidates, test_target)
    result_dp = solution.combination_sumDP(test_candidates, test_target)
    result_iter = solution.combination_sumIterative(test_candidates, test_target)
    result_opt = solution.combination_sumOptimized(test_candidates, test_target)
    
    expected = [[2, 2, 3], [7]]
    for result in [result_backtrack, result_dp, result_iter, result_opt]:
        result.sort()
        expected.sort()
        assert result == expected, f"Approach comparison failed: expected {expected}, got {result}"
    
    # Test case 7: Edge case - target equals smallest candidate
    print("Test 7: Edge case - target equals smallest candidate")
    candidates7 = [2, 3, 4]
    target7 = 2
    expected7 = [[2]]
    result7 = solution.combination_sum(candidates7, target7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: Edge case - all candidates larger than target
    print("Test 8: Edge case - all candidates larger than target")
    candidates8 = [5, 6, 7]
    target8 = 3
    expected8 = []
    result8 = solution.combination_sum(candidates8, target8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Single candidate used multiple times
    print("Test 9: Single candidate used multiple times")
    candidates9 = [3]
    target9 = 9
    expected9 = [[3, 3, 3]]
    result9 = solution.combination_sum(candidates9, target9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Complex scenario
    print("Test 10: Complex scenario")
    candidates10 = [2, 3, 4, 5]
    target10 = 10
    expected10 = [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 3, 3], [2, 3, 5], [2, 4, 4], [3, 3, 4], [5, 5]]
    result10 = solution.combination_sum(candidates10, target10)
    result10.sort()
    expected10.sort()
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
