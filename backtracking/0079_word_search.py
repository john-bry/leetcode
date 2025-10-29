"""
79. Word Search
Difficulty: Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

Notes:
- Key insight: Use backtracking/DFS to explore all possible paths.
- Mark visited cells to avoid revisiting the same cell in one path.
- Try starting from every cell in the board.
- Use in-place marking for space efficiency.
- Early termination when word is found.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Approach 1: Backtracking with In-place Marking (Optimal)
        Time Complexity: O(m * n * 4^L) where L is word length
        Space Complexity: O(L) - recursion stack depth
        
        Use backtracking to explore all possible paths from each starting cell.
        Mark visited cells in-place to avoid revisiting in the same path.
        """
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(row: int, col: int, idx: int) -> bool:
            # Base case: found complete word
            if idx == len(word):
                return True
            
            # Check boundaries and character match
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                board[row][col] != word[idx]):
                return False
            
            # Mark as visited (in-place)
            temp = board[row][col]
            board[row][col] = "#"
            
            # Explore all 4 directions
            found = (backtrack(row + 1, col, idx + 1) or  # Down
                     backtrack(row - 1, col, idx + 1) or  # Up
                     backtrack(row, col + 1, idx + 1) or  # Right
                     backtrack(row, col - 1, idx + 1))    # Left
            
            # Restore cell value (backtrack)
            board[row][col] = temp
            
            return found
        
        # Try starting from every cell
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
    
    def existWithVisitedSet(self, board: List[List[str]], word: str) -> bool:
        """
        Approach 2: DFS with Visited Set
        Time Complexity: O(m * n * 4^L)
        Space Complexity: O(L) - recursion stack + visited set
        
        Use a separate visited set instead of in-place marking.
        Less space efficient but doesn't modify the original board.
        """
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(row: int, col: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                (row, col) in visited or
                board[row][col] != word[idx]):
                return False
            
            visited.add((row, col))
            
            found = (dfs(row + 1, col, idx + 1) or
                     dfs(row - 1, col, idx + 1) or
                     dfs(row, col + 1, idx + 1) or
                     dfs(row, col - 1, idx + 1))
            
            visited.remove((row, col))
            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
    
    def existOptimized(self, board: List[List[str]], word: str) -> bool:
        """
        Approach 3: Optimized with Early Pruning
        Time Complexity: O(m * n * 4^L)
        Space Complexity: O(L)
        
        Optimized version with character frequency check and early pruning.
        """
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        # Early pruning: check if all characters in word exist in board
        board_chars = set()
        for row in board:
            board_chars.update(row)
        
        for char in word:
            if char not in board_chars:
                return False
        
        def backtrack(row: int, col: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                board[row][col] != word[idx]):
                return False
            
            # Mark as visited
            temp = board[row][col]
            board[row][col] = "#"
            
            # Explore all 4 directions
            found = (backtrack(row + 1, col, idx + 1) or
                     backtrack(row - 1, col, idx + 1) or
                     backtrack(row, col + 1, idx + 1) or
                     backtrack(row, col - 1, idx + 1))
            
            # Restore cell value
            board[row][col] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
    
    def existIterative(self, board: List[List[str]], word: str) -> bool:
        """
        Approach 4: Iterative with Stack
        Time Complexity: O(m * n * 4^L)
        Space Complexity: O(L)
        
        Iterative implementation using explicit stack instead of recursion.
        """
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    stack = [(i, j, 0, set())]  # (row, col, word_idx, visited)
                    
                    while stack:
                        row, col, idx, visited = stack.pop()
                        
                        if idx == len(word) - 1:
                            return True
                        
                        if (row, col) in visited:
                            continue
                        
                        visited.add((row, col))
                        
                        for dr, dc in directions:
                            new_row, new_col = row + dr, col + dc
                            if (0 <= new_row < rows and 
                                0 <= new_col < cols and
                                (new_row, new_col) not in visited and
                                board[new_row][new_col] == word[idx + 1]):
                                stack.append((new_row, new_col, idx + 1, visited.copy()))
        
        return False


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality - word exists
    print("Test 1: Basic functionality - word exists")
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    expected1 = True
    result1 = solution.exist(board1, word1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Word exists - different path
    print("Test 2: Word exists - different path")
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    expected2 = True
    result2 = solution.exist(board2, word2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Word doesn't exist
    print("Test 3: Word doesn't exist")
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    expected3 = False
    result3 = solution.exist(board3, word3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single character word
    print("Test 4: Single character word")
    board4 = [["A","B"],["C","D"]]
    word4 = "A"
    expected4 = True
    result4 = solution.exist(board4, word4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single character word - not found
    print("Test 5: Single character word - not found")
    board5 = [["A","B"],["C","D"]]
    word5 = "E"
    expected5 = False
    result5 = solution.exist(board5, word5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Single cell board
    print("Test 6: Single cell board")
    board6 = [["A"]]
    word6 = "A"
    expected6 = True
    result6 = solution.exist(board6, word6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Single cell board - word too long
    print("Test 7: Single cell board - word too long")
    board7 = [["A"]]
    word7 = "AB"
    expected7 = False
    result7 = solution.exist(board7, word7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8: Compare different approaches
    print("Test 8: Compare different approaches")
    test_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    test_word = "ABCCED"
    
    result_backtrack = solution.exist(test_board, test_word)
    result_visited = solution.existWithVisitedSet(test_board, test_word)
    result_opt = solution.existOptimized(test_board, test_word)
    result_iter = solution.existIterative(test_board, test_word)
    
    expected = True
    assert result_backtrack == expected, f"Test 8.1 backtrack failed: expected {expected}, got {result_backtrack}"
    assert result_visited == expected, f"Test 8.2 visited set failed: expected {expected}, got {result_visited}"
    assert result_opt == expected, f"Test 8.3 optimized failed: expected {expected}, got {result_opt}"
    assert result_iter == expected, f"Test 8.4 iterative failed: expected {expected}, got {result_iter}"
    
    # Test case 9: Edge case - empty word
    print("Test 9: Edge case - empty word")
    board9 = [["A","B"],["C","D"]]
    word9 = ""
    expected9 = True  # Empty word is considered to exist
    result9 = solution.exist(board9, word9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Complex path
    print("Test 10: Complex path")
    board10 = [["A","B","C"],["D","E","F"],["G","H","I"]]
    word10 = "ABCFIHGDE"
    expected10 = True
    result10 = solution.exist(board10, word10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    # Test case 11: Reusing cells (should fail)
    print("Test 11: Reusing cells (should fail)")
    board11 = [["A","B"],["C","D"]]
    word11 = "ABA"  # Would need to reuse A
    expected11 = False
    result11 = solution.exist(board11, word11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    
    # Test case 12: Large word
    print("Test 12: Large word")
    board12 = [["A","B","C","D"],["E","F","G","H"],["I","J","K","L"],["M","N","O","P"]]
    word12 = "ABCDHLPONMIEFG"
    expected12 = True
    result12 = solution.exist(board12, word12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()