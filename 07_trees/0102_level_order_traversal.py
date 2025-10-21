"""
102. Binary Tree Level Order Traversal
Difficulty: Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Notes:
- Great problem to learn level by level BFS traversal.
- Queue vs Stack: O(1) vs O(n) time complexity.
"""

from collections import deque
from typing import List, Optional

from utils.data_structures import TreeNode


class Solution:
    def level_order_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach 1: BFS with Queue
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        # Handle empty tree
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            # Get number of nodes at current level
            level_size = len(queue)
            level_vals = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level to result
            result.append(level_vals)
        
        return result
    
    def level_order_dfs_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach 2: DFS Recursive
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return []
        
        result = []
        
        def dfs(node, level):
            # Base case: empty node
            if not node:
                return
            
            # Create new level if needed
            if level >= len(result):
                result.append([])
            
            # Add current node to its level
            result[level].append(node.val)
            
            # Recursively process children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result
    
    def level_order_dfs_iterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach 3: DFS Iterative with Stack
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return []
        
        result = []
        # Stack stores (node, level) pairs
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            
            # Create new level if needed
            if level >= len(result):
                result.append([])
            
            # Add current node to its level
            result[level].append(node.val)
            
            # Add children to stack (right first for left-to-right order)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    #     3
    #    / \
    #   9   20
    #      /  \
    #     15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    expected1 = [[3], [9, 20], [15, 7]]
    result1 = solution.level_order_bfs(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: [1]
    #   1
    root2 = TreeNode(1)
    expected2 = [[1]]
    result2 = solution.level_order_bfs(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Empty tree
    root3 = None
    expected3 = []
    result3 = solution.level_order_bfs(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: [1,2,3,4,5,6,7]
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    
    expected4 = [[1], [2, 3], [4, 5, 6, 7]]
    result4 = solution.level_order_bfs(root4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single path tree [1,2,null,3]
    #   1
    #  /
    # 2
    #  \
    #   3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.right = TreeNode(3)
    
    expected5 = [[1], [2], [3]]
    result5 = solution.level_order_bfs(root5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()