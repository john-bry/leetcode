"""
98. Validate Binary Search Tree
Difficulty: Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Example 3:
Input: root = [5,4,6,null,null,3,7]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Notes:
- Key insight: BST property must hold for every node, not just immediate children.
- Use bounds (min, max) to validate each node's value.
- Inorder traversal of valid BST gives sorted sequence.
"""

from collections import deque
from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def is_valid_bst_recursive(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 1: Recursive DFS with Bounds
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        def valid(node, min_val, max_val):
            # Base case: empty node is valid
            if not node:
                return True
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively check left and right subtrees with updated bounds
            return (
                valid(node.left, min_val, node.val) and
                valid(node.right, node.val, max_val)
            )
        
        return valid(root, float('-inf'), float('inf'))
    
    def is_valid_bst_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 2: Iterative DFS with Bounds
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return True
        
        # Stack stores (node, min_val, max_val) tuples
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, min_val, max_val = stack.pop()
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Add children to stack with updated bounds
            if node.left:
                stack.append((node.left, min_val, node.val))
            if node.right:
                stack.append((node.right, node.val, max_val))
        
        return True
    
    def is_valid_bst_inorder(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 3: Inorder Traversal
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return True
        
        stack = []
        current = root
        prev_val = None
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            
            # Check if values are in ascending order
            if prev_val is not None and current.val <= prev_val:
                return False
            
            prev_val = current.val
            current = current.right
        
        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [2,1,3] - Valid BST
    #   2
    #  / \
    # 1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    
    result1 = solution.is_valid_bst_recursive(root1)
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"
    
    # Test case 2: [5,1,4,null,null,3,6] - Invalid BST
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    
    result2 = solution.is_valid_bst_recursive(root2)
    assert result2 == False, f"Test 2 failed: expected False, got {result2}"
    
    # Test case 3: [5,4,6,null,null,3,7] - Invalid BST
    #     5
    #    / \
    #   4   6
    #      / \
    #     3   7
    root3 = TreeNode(5)
    root3.left = TreeNode(4)
    root3.right = TreeNode(6)
    root3.right.left = TreeNode(3)
    root3.right.right = TreeNode(7)
    
    result3 = solution.is_valid_bst_recursive(root3)
    assert result3 == False, f"Test 3 failed: expected False, got {result3}"
    
    # Test case 4: [1] - Single node (valid BST)
    root4 = TreeNode(1)
    result4 = solution.is_valid_bst_recursive(root4)
    assert result4 == True, f"Test 4 failed: expected True, got {result4}"
    
    # Test case 5: [10,5,15,null,null,6,20] - Invalid BST
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      6   20
    root5 = TreeNode(10)
    root5.left = TreeNode(5)
    root5.right = TreeNode(15)
    root5.right.left = TreeNode(6)
    root5.right.right = TreeNode(20)
    
    result5 = solution.is_valid_bst_recursive(root5)
    assert result5 == False, f"Test 5 failed: expected False, got {result5}"
    
    # Test case 6: [2,2,2] - Invalid BST (duplicate values)
    #   2
    #  / \
    # 2   2
    root6 = TreeNode(2)
    root6.left = TreeNode(2)
    root6.right = TreeNode(2)
    
    result6 = solution.is_valid_bst_recursive(root6)
    assert result6 == False, f"Test 6 failed: expected False, got {result6}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()