"""
1046. Last Stone Weight
Difficulty: Easy

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Example 3:
Input: stones = [2,2]
Output: 0
Explanation: We combine 2 and 2 to get 0 so the array converts to [] then that's the value of the last stone.

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

Notes:
- Key insight: Use a max heap to efficiently get the two heaviest stones.
- The root of the max heap is always the heaviest stone.
- When smashing two stones, push the difference back into the heap if non-zero.
- Alternative approaches include sorting and simulation.
- This is essentially a greedy algorithm that always processes the heaviest stones first.
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Approach 1: Max Heap (Optimal)
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Use a max heap to efficiently get the two heaviest stones.
        Python's heapq is a min heap, so we negate values for max heap behavior.
        """
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        return -max_heap[0] if max_heap else 0
    
    def lastStoneWeightSorting(self, stones: List[int]) -> int:
        """
        Approach 2: Sorting (Alternative)
        Time Complexity: O(n² log n) - sorting n times
        Space Complexity: O(1) - excluding input array
        
        Sort the array and simulate the process.
        Less efficient than heap approach due to repeated sorting.
        """
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [stones[-1] - stones[-2]]
        
        return stones[0] if stones else 0
    
    def lastStoneWeightSimulation(self, stones: List[int]) -> int:
        """
        Approach 3: Simulation with List Operations
        Time Complexity: O(n² log n) - finding max n times
        Space Complexity: O(1) - excluding input array
        
        Simulate the process by repeatedly finding and removing the two heaviest stones.
        Less efficient due to O(n) max finding operations.
        """
        while len(stones) > 1:
            # Find two heaviest stones
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            
            if first != second:
                stones.append(first - second)
        
        return stones[0] if stones else 0
    
    def lastStoneWeightOptimized(self, stones: List[int]) -> int:
        """
        Approach 4: Optimized Max Heap with Early Termination
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Optimized version that handles edge cases more efficiently.
        """
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        # Create max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        return -max_heap[0] if max_heap else 0


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    stones1 = [2, 7, 4, 1, 8, 1]
    expected1 = 1
    result1 = solution.lastStoneWeight(stones1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Single stone
    print("Test 2: Single stone")
    stones2 = [1]
    expected2 = 1
    result2 = solution.lastStoneWeight(stones2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Two equal stones
    print("Test 3: Two equal stones")
    stones3 = [2, 2]
    expected3 = 0
    result3 = solution.lastStoneWeight(stones3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: All stones equal
    print("Test 4: All stones equal")
    stones4 = [3, 3, 3, 3]
    expected4 = 0
    result4 = solution.lastStoneWeight(stones4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Descending order
    print("Test 5: Descending order")
    stones5 = [5, 4, 3, 2, 1]
    expected5 = 1
    result5 = solution.lastStoneWeight(stones5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Ascending order
    print("Test 6: Ascending order")
    stones6 = [1, 2, 3, 4, 5]
    expected6 = 1
    result6 = solution.lastStoneWeight(stones6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Large numbers
    print("Test 7: Large numbers")
    stones7 = [1000, 999, 998, 997]
    expected7 = 0
    result7 = solution.lastStoneWeight(stones7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: Compare different approaches
    print("Test 8: Compare different approaches")
    test_stones = [2, 7, 4, 1, 8, 1]
    
    result_heap = solution.lastStoneWeight(test_stones)
    result_sort = solution.lastStoneWeightSorting(test_stones.copy())
    result_sim = solution.lastStoneWeightSimulation(test_stones.copy())
    result_opt = solution.lastStoneWeightOptimized(test_stones.copy())
    
    expected = 1
    assert result_heap == expected, f"Test 8.1 heap failed: expected {expected}, got {result_heap}"
    assert result_sort == expected, f"Test 8.2 sorting failed: expected {expected}, got {result_sort}"
    assert result_sim == expected, f"Test 8.3 simulation failed: expected {expected}, got {result_sim}"
    assert result_opt == expected, f"Test 8.4 optimized failed: expected {expected}, got {result_opt}"
    
    # Test case 9: Edge case - empty array
    print("Test 9: Edge case - empty array")
    stones9 = []
    expected9 = 0
    result9 = solution.lastStoneWeight(stones9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Complex scenario
    print("Test 10: Complex scenario")
    stones10 = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    expected10 = 1
    result10 = solution.lastStoneWeight(stones10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()