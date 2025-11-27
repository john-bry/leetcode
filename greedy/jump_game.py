"""
55. Jump Game
Difficulty: Medium

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
which makes it impossible to reach the last index.

Example 3:
Input: nums = [0]
Output: true
Explanation: Already at the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Notes:
- Key insight: We don't need to know the exact path, just whether we can reach the end.
- Greedy approach: Track the farthest position we can reach from current position.
- If at any point we can't reach the current index, we can't reach the end.
- Time complexity: O(n) for greedy, O(n^2) for DP
- Space complexity: O(1) for greedy, O(n) for DP
- Alternative approaches:
  - Greedy backward: O(n) time, O(1) space - work backwards from goal (current)
  - Greedy forward: O(n) time, O(1) space - track max reachable position
  - DP tabulation: O(n^2) time, O(n) space - bottom-up DP
  - DP memoization: O(n^2) time, O(n) space - top-down DP
  - BFS: O(n^2) time, O(n) space - treat as graph problem
- Edge cases: Single element, all zeros, can't reach end, can reach in one jump
"""

from collections import deque
from typing import Dict, List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        """
        Approach 1: Greedy Backward (Current)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Work backwards from the goal. If we can reach the goal from position i,
        then the goal becomes i. Check if we can reach position 0.
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0
    
    def can_jump_greedy_forward(self, nums: List[int]) -> bool:
        """
        Approach 2: Greedy Forward (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Track the farthest position we can reach. If we can't reach current index,
        we can't reach the end.
        """
        max_reach = 0
        
        for i in range(len(nums)):
            # If we can't reach current index, return False
            if i > max_reach:
                return False
            
            # Update farthest position we can reach
            max_reach = max(max_reach, i + nums[i])
            
            # Early exit: already reached the end
            if max_reach >= len(nums) - 1:
                return True
        
        return True
    
    def can_jump_tabulation(self, nums: List[int]) -> bool:
        """
        Approach 3: Dynamic Programming Tabulation
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        dp[i] = True if we can reach index i from index 0.
        For each position, check if any previous reachable position can jump to it.
        """
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]
    
    def can_jump_memoization(self, nums: List[int]) -> bool:
        """
        Approach 4: Dynamic Programming with Memoization
        Time Complexity: O(n^2)
        Space Complexity: O(n) for memoization and recursion stack
        
        Top-down approach with memoization.
        Check if we can reach the end from current position.
        """
        memo: Dict[int, bool] = {}
        
        def dp(position: int) -> bool:
            # Base case: reached the end
            if position >= len(nums) - 1:
                return True
            
            # Check memoization
            if position in memo:
                return memo[position]
            
            # Try all possible jumps from current position
            max_jump = nums[position]
            for jump in range(1, max_jump + 1):
                if dp(position + jump):
                    memo[position] = True
                    return True
            
            memo[position] = False
            return False
        
        return dp(0)
    
    def can_jump_bfs(self, nums: List[int]) -> bool:
        """
        Approach 5: BFS (Breadth-First Search)
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Treat as a graph problem. Each index is a node, and we can jump to
        indices within jump range. Use BFS to find if we can reach the end.
        """
        if len(nums) == 1:
            return True
        
        queue = deque([0])
        visited = set([0])
        target = len(nums) - 1
        
        while queue:
            current = queue.popleft()
            max_jump = nums[current]
            
            # Try all possible jumps
            for jump in range(1, max_jump + 1):
                next_pos = current + jump
                
                if next_pos >= target:
                    return True
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append(next_pos)
        
        return False
    
    def can_jump_dfs(self, nums: List[int]) -> bool:
        """
        Approach 6: DFS (Depth-First Search) with Memoization
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Similar to memoization but using DFS terminology.
        """
        memo: Dict[int, bool] = {}
        
        def dfs(position: int) -> bool:
            if position >= len(nums) - 1:
                return True
            
            if position in memo:
                return memo[position]
            
            max_jump = nums[position]
            for jump in range(max_jump, 0, -1):  # Try larger jumps first
                if dfs(position + jump):
                    memo[position] = True
                    return True
            
            memo[position] = False
            return False
        
        return dfs(0)
    
    def can_jump_optimized_dp(self, nums: List[int]) -> bool:
        """
        Approach 7: Optimized DP (Early Exit)
        Time Complexity: O(n^2) worst case, O(n) best case
        Space Complexity: O(n)
        
        Same as tabulation but with early exit optimization.
        """
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):  # Check backwards for early exit
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
            # Early exit: if we can't reach current position, can't reach end
            if not dp[i]:
                return False
        
        return dp[-1]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example [2,3,1,1,4]
    print("Test 1: Basic example [2,3,1,1,4]")
    nums1 = [2, 3, 1, 1, 4]
    expected1 = True
    result1 = solution.can_jump(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Cannot reach end [3,2,1,0,4]
    print("Test 2: Cannot reach end [3,2,1,0,4]")
    nums2 = [3, 2, 1, 0, 4]
    expected2 = False
    result2 = solution.can_jump(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Single element [0]
    print("Test 3: Single element [0]")
    nums3 = [0]
    expected3 = True
    result3 = solution.can_jump(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Can reach in one jump [4,0,0,0,0]
    print("Test 4: Can reach in one jump [4,0,0,0,0]")
    nums4 = [4, 0, 0, 0, 0]
    expected4 = True
    result4 = solution.can_jump(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All zeros except start [1,0,0,0,0]
    print("Test 5: All zeros except start [1,0,0,0,0]")
    nums5 = [1, 0, 0, 0, 0]
    expected5 = False
    result5 = solution.can_jump(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two elements [1,0]
    print("Test 6: Two elements [1,0]")
    nums6 = [1, 0]
    expected6 = True
    result6 = solution.can_jump(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Two elements cannot reach [0,1]
    print("Test 7: Two elements cannot reach [0,1]")
    nums7 = [0, 1]
    expected7 = False
    result7 = solution.can_jump(nums7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Compare all approaches
    print("\nTest 8: Comparing all approaches")
    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [1, 0],
        [2, 0, 0],
        [1, 1, 1, 1],
        [1, 2, 3, 4, 5],
    ]
    
    for nums in test_cases:
        result1 = solution.can_jump(nums)
        result2 = solution.can_jump_greedy_forward(nums)
        result3 = solution.can_jump_tabulation(nums)
        result4 = solution.can_jump_memoization(nums)
        result5 = solution.can_jump_bfs(nums)
        result6 = solution.can_jump_dfs(nums)
        result7 = solution.can_jump_optimized_dp(nums)
        
        assert result1 == result2, f"Greedy forward mismatch for {nums}: {result1} vs {result2}"
        assert result1 == result3, f"Tabulation mismatch for {nums}: {result1} vs {result3}"
        assert result1 == result4, f"Memoization mismatch for {nums}: {result1} vs {result4}"
        assert result1 == result5, f"BFS mismatch for {nums}: {result1} vs {result5}"
        assert result1 == result6, f"DFS mismatch for {nums}: {result1} vs {result6}"
        assert result1 == result7, f"Optimized DP mismatch for {nums}: {result1} vs {result7}"
    
    print("  All approaches match! ✓")
    
    # Test case 9: Large jump at start [5,0,0,0,0,0,0]
    print("\nTest 9: Large jump at start [5,0,0,0,0,0,0]")
    nums9 = [5, 0, 0, 0, 0, 0, 0]
    expected9 = True
    result9 = solution.can_jump(nums9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Alternating pattern [1,0,1,0,1]
    print("Test 10: Alternating pattern [1,0,1,0,1]")
    nums10 = [1, 0, 1, 0, 1]
    expected10 = True
    result10 = solution.can_jump(nums10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Cannot jump past zero [1,0,2]
    print("Test 11: Cannot jump past zero [1,0,2]")
    nums11 = [1, 0, 2]
    expected11 = False
    result11 = solution.can_jump(nums11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: All ones [1,1,1,1,1]
    print("Test 12: All ones [1,1,1,1,1]")
    nums12 = [1, 1, 1, 1, 1]
    expected12 = True
    result12 = solution.can_jump(nums12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Large numbers [10,9,8,7,6,5,4,3,2,1,0,0]
    print("Test 13: Large numbers [10,9,8,7,6,5,4,3,2,1,0,0]")
    nums13 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
    expected13 = True
    result13 = solution.can_jump(nums13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Zero at end [2,0,0]
    print("Test 14: Zero at end [2,0,0]")
    nums14 = [2, 0, 0]
    expected14 = True
    result14 = solution.can_jump(nums14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex case [2,5,0,0]
    print("Test 15: Complex case [2,5,0,0]")
    nums15 = [2, 5, 0, 0]
    expected15 = True
    result15 = solution.can_jump(nums15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()