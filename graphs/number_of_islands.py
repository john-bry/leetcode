"""
200. Number of Islands
Difficulty: Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

Notes:
- Key insight: Use DFS or BFS to mark all connected land cells as visited.
- In-place marking by changing '1' to '0' is space efficient.
- Alternative: Use Union-Find to count connected components.
"""

from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        Approach 1: DFS with In-place Marking (Optimal)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) - recursion stack in worst case
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(row, col):
            # Boundary checks and water check
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                grid[row][col] == '0'):
                return
            
            # Mark as visited
            grid[row][col] = '0'
            
            # Explore 4 directions
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left
        
        # Scan entire grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1  # Found new island
                    dfs(i, j)     # Mark entire island
        
        return islands
    
    def num_islands_bfs(self, grid: List[List[str]]) -> int:
        """
        Approach 2: BFS
        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n)) - queue size
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        from collections import deque
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '0'
                    
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            r, c = row + dr, col + dc
                            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                                grid[r][c] = '0'
                                queue.append((r, c))
        
        return islands


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Single island
    print("Test 1: Single island")
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected1 = 1
    result1 = solution.num_islands([row[:] for row in grid1])
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Multiple islands
    print("Test 2: Multiple islands")
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected2 = 3
    result2 = solution.num_islands([row[:] for row in grid2])
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: No islands
    print("Test 3: No islands")
    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    expected3 = 0
    result3 = solution.num_islands([row[:] for row in grid3])
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: All land
    print("Test 4: All land")
    grid4 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    expected4 = 1
    result4 = solution.num_islands([row[:] for row in grid4])
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single cell
    print("Test 5: Single cell")
    grid5 = [["1"]]
    expected5 = 1
    result5 = solution.num_islands([row[:] for row in grid5])
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Single cell water
    print("Test 6: Single cell water")
    grid6 = [["0"]]
    expected6 = 0
    result6 = solution.num_islands([row[:] for row in grid6])
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected = 3
    result_dfs = solution.num_islands([row[:] for row in test_grid])
    result_bfs = solution.num_islands_bfs([row[:] for row in test_grid])
    assert result_dfs == expected, f"Test 7.1 DFS failed: expected {expected}, got {result_dfs}"
    assert result_bfs == expected, f"Test 7.2 BFS failed: expected {expected}, got {result_bfs}"
    
    # Test case 8: L-shaped island
    print("Test 8: L-shaped island")
    grid8 = [
        ["1","1","0"],
        ["1","0","0"],
        ["1","0","0"]
    ]
    expected8 = 1
    result8 = solution.num_islands([row[:] for row in grid8])
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
