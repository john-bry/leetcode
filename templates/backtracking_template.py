"""
Template for Backtracking problems
"""

from typing import List, Optional


class Solution:
    """
    Problem: [Problem Name]
    Difficulty: Easy/Medium/Hard
    
    Problem Statement:
    [Describe the problem here]
    
    Example:
    Input: [example input]
    Output: [example output]
    Explanation: [explanation]
    """
    
    def permutations(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 1: Generate all permutations
        Time Complexity: O(n! * n)
        Space Complexity: O(n! * n)
        """
        result = []
        
        def backtrack(current_path):
            # Base case: if we have used all numbers
            if len(current_path) == len(nums):
                result.append(current_path[:])
                return
            
            # Try each unused number
            for num in nums:
                if num not in current_path:
                    current_path.append(num)
                    backtrack(current_path)
                    current_path.pop()  # Backtrack
        
        backtrack([])
        return result
    
    def combinations(self, n: int, k: int) -> List[List[int]]:
        """
        Approach 2: Generate combinations
        Time Complexity: O(C(n,k) * k)
        Space Complexity: O(C(n,k) * k)
        """
        result = []
        
        def backtrack(start, current_path):
            # Base case: if we have k numbers
            if len(current_path) == k:
                result.append(current_path[:])
                return
            
            # Try numbers from start to n
            for i in range(start, n + 1):
                current_path.append(i)
                backtrack(i + 1, current_path)
                current_path.pop()  # Backtrack
        
        backtrack(1, [])
        return result
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 3: Generate all subsets
        Time Complexity: O(2^n * n)
        Space Complexity: O(2^n * n)
        """
        result = []
        
        def backtrack(start, current_path):
            # Add current subset to result
            result.append(current_path[:])
            
            # Try adding each remaining number
            for i in range(start, len(nums)):
                current_path.append(nums[i])
                backtrack(i + 1, current_path)
                current_path.pop()  # Backtrack
        
        backtrack(0, [])
        return result
    
    def n_queens(self, n: int) -> List[List[str]]:
        """
        Approach 4: N-Queens problem
        Time Complexity: O(n!)
        Space Complexity: O(n^2)
        """
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def is_safe(row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check diagonal (top-left to bottom-right)
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check diagonal (top-right to bottom-left)
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(row):
            # Base case: all queens placed
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'  # Backtrack
        
        backtrack(0)
        return result
    
    def word_search(self, board: List[List[str]], word: str) -> bool:
        """
        Approach 5: Word search with backtracking
        Time Complexity: O(m * n * 4^L) where L is length of word
        Space Complexity: O(L)
        """
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, index):
            # Base case: found the word
            if index == len(word):
                return True
            
            # Check bounds and if current cell matches
            if (row < 0 or row >= m or col < 0 or col >= n or 
                (row, col) in visited or board[row][col] != word[index]):
                return False
            
            # Mark as visited
            visited.add((row, col))
            
            # Try all four directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                if dfs(row + dr, col + dc, index + 1):
                    return True
            
            # Backtrack
            visited.remove((row, col))
            return False
        
        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Permutations
    nums1 = [1, 2, 3]
    expected1_len = 6  # 3! = 6
    result1 = solution.permutations(nums1)
    assert len(result1) == expected1_len, f"Test 1 failed: expected {expected1_len} permutations, got {len(result1)}"
    
    # Test case 2: Combinations
    n2, k2 = 4, 2
    expected2_len = 6  # C(4,2) = 6
    result2 = solution.combinations(n2, k2)
    assert len(result2) == expected2_len, f"Test 2 failed: expected {expected2_len} combinations, got {len(result2)}"
    
    # Test case 3: Subsets
    nums3 = [1, 2, 3]
    expected3_len = 8  # 2^3 = 8
    result3 = solution.subsets(nums3)
    assert len(result3) == expected3_len, f"Test 3 failed: expected {expected3_len} subsets, got {len(result3)}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
