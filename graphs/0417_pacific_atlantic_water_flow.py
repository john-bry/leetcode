"""
417. Pacific Atlantic Water Flow
Difficulty: Medium

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to both Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to both oceans.

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5

Notes:
- Key insight: Start DFS from ocean borders (not from every cell).
- Water flows from higher to lower (or equal) heights.
- Find cells reachable from both Pacific and Atlantic borders.
- Use two sets to track reachability from each ocean.
"""

from typing import List


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach 1: DFS from Ocean Borders (Optimal)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) for sets and recursion stack
        
        Start DFS from all Pacific border cells and Atlantic border cells.
        Find intersection of cells reachable from both oceans.
        """
        if not heights:
            return []
        
        num_rows, num_cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(row, col, reachable_set):
            reachable_set.add((row, col))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for row_offset, col_offset in directions:
                next_row = row + row_offset
                next_col = col + col_offset
                
                # Check ALL conditions with short-circuit evaluation
                if (0 <= next_row < num_rows and 
                    0 <= next_col < num_cols and
                    (next_row, next_col) not in reachable_set and
                    heights[next_row][next_col] >= heights[row][col]):
                    dfs(next_row, next_col, reachable_set)
        
        # Pacific borders
        for col in range(num_cols):
            dfs(0, col, pacific)
        for row in range(num_rows):
            dfs(row, 0, pacific)
        
        # Atlantic borders
        for col in range(num_cols):
            dfs(num_rows - 1, col, atlantic)
        for row in range(num_rows):
            dfs(row, num_cols - 1, atlantic)
        
        return list(pacific & atlantic)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example")
    heights1 = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    result1 = solution.pacific_atlantic(heights1)
    expected1 = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    # Convert to sets for comparison since order doesn't matter
    result1_set = set(tuple(x) for x in result1)
    expected1_set = set(tuple(x) for x in expected1)
    assert result1_set == expected1_set, f"Test 1 failed: expected {expected1_set}, got {result1_set}"
    
    # Test case 2: Single cell
    print("Test 2: Single cell")
    heights2 = [[1]]
    result2 = solution.pacific_atlantic(heights2)
    assert result2 == [[0, 0]], f"Test 2 failed: expected [[0,0]], got {result2}"
    
    # Test case 3: All cells reachable
    print("Test 3: All cells reachable")
    heights3 = [
        [1,1],
        [1,1]
    ]
    result3 = solution.pacific_atlantic(heights3)
    result3_set = set(tuple(x) for x in result3)
    expected3_set = {(0,0), (0,1), (1,0), (1,1)}
    assert result3_set == expected3_set, f"Test 3 failed: expected {expected3_set}, got {result3_set}"
    
    # Test case 4: No cells reachable (descending from corners)
    print("Test 4: Descending from corners")
    heights4 = [
        [5,4,3],
        [4,3,2],
        [3,2,1]
    ]
    result4 = solution.pacific_atlantic(heights4)
    result4_set = set(tuple(x) for x in result4)
    # All border cells should be reachable
    assert len(result4) > 0, "Test 4 failed: should have some reachable cells"
    
    # Test case 5: Single row
    print("Test 5: Single row")
    heights5 = [[1,2,3,4,5]]
    result5 = solution.pacific_atlantic(heights5)
    result5_set = set(tuple(x) for x in result5)
    # All cells in single row should be reachable
    expected5_set = {(0,0), (0,1), (0,2), (0,3), (0,4)}
    assert result5_set == expected5_set, f"Test 5 failed: expected {expected5_set}, got {result5_set}"
    
    # Test case 6: Single column
    print("Test 6: Single column")
    heights6 = [[1],[2],[3],[4],[5]]
    result6 = solution.pacific_atlantic(heights6)
    result6_set = set(tuple(x) for x in result6)
    # All cells in single column should be reachable
    expected6_set = {(0,0), (1,0), (2,0), (3,0), (4,0)}
    assert result6_set == expected6_set, f"Test 6 failed: expected {expected6_set}, got {result6_set}"
    
    # Test case 7: Mountain in center
    print("Test 7: Mountain in center")
    heights7 = [
        [1,2,1],
        [2,3,2],
        [1,2,1]
    ]
    result7 = solution.pacific_atlantic(heights7)
    result7_set = set(tuple(x) for x in result7)
    # Center cell should be reachable
    assert (1, 1) in result7_set, "Test 7 failed: center cell should be reachable"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()