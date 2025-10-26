"""
226. Invert Binary Tree
Difficulty: Easy

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def invert_tree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach 1: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Base case: empty tree
        if not root:
            return None
        
        # Recursively invert left and right subtrees
        left = self.invert_tree_recursive(root.left)
        right = self.invert_tree_recursive(root.right)
        
        # Swap the children at current node
        root.left = right
        root.right = left
        
        return root
    
    def invert_tree_iterative_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach 2: Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return None
        
        # Use stack for DFS traversal
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # Swap children at current node
                node.left, node.right = node.right, node.left
                # Add children to stack for processing
                stack.append(node.left)
                stack.append(node.right)
        
        return root
    
    def invert_tree_iterative_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach 3: Iterative BFS
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        # Handle empty tree
        if not root:
            return None
        
        # Use queue for BFS traversal (level by level)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                # Swap children at current node
                node.left, node.right = node.right, node.left
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9]
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    
    # Expected after inversion:
    #     4
    #    / \
    #   7   2
    #  / \ / \
    # 9  6 3  1
    
    # Test recursive approach
    result1 = solution.invert_tree_recursive(root1)
    assert result1.val == 4
    assert result1.left.val == 7
    assert result1.right.val == 2
    assert result1.left.left.val == 9
    assert result1.left.right.val == 6
    assert result1.right.left.val == 3
    assert result1.right.right.val == 1
    
    # Test case 2: [2,1,3]
    #   2
    #  / \
    # 1   3
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    
    # Expected after inversion:
    #   2
    #  / \
    # 3   1
    
    result2 = solution.invert_tree_recursive(root2)
    assert result2.val == 2
    assert result2.left.val == 3
    assert result2.right.val == 1
    
    # Test case 3: Empty tree
    root3 = None
    result3 = solution.invert_tree_recursive(root3)
    assert result3 is None
    
    # Test case 4: Single node
    root4 = TreeNode(1)
    result4 = solution.invert_tree_recursive(root4)
    assert result4.val == 1
    assert result4.left is None
    assert result4.right is None
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()