"""
104. Maximum Depth of Binary Tree
Difficulty: Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def max_depth_recursive(self, root: Optional[TreeNode]) -> int:
        """
        Approach 1: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        if not root:
            return 0
        
        left_depth = self.max_depth_recursive(root.left)
        right_depth = self.max_depth_recursive(root.right)
        
        return max(left_depth, right_depth) + 1
    
    def max_depth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        """
        Approach 2: Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth
    
    def max_depth_iterative_bfs(self, root: Optional[TreeNode]) -> int:
        """
        Approach 3: Iterative BFS
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        if not root:
            return 0
        
        from collections import deque
        queue = deque([root])
        depth = 0
        
        while queue:
            level_size = len(queue)
            depth += 1
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


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
    
    expected1 = 3
    result1 = solution.max_depth_recursive(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: [1,null,2]
    #   1
    #    \
    #     2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    
    expected2 = 2
    result2 = solution.max_depth_recursive(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Empty tree
    root3 = None
    expected3 = 0
    result3 = solution.max_depth_recursive(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single node
    root4 = TreeNode(0)
    expected4 = 1
    result4 = solution.max_depth_recursive(root4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
