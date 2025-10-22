"""
230. Kth Smallest Element in a BST
Difficulty: Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow-up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize the kthSmallest function?

Notes:
- Key insight: Inorder traversal of BST gives sorted sequence.
- Can optimize with augmented BST (store subtree sizes).
- For frequent queries, consider caching or lazy evaluation.
"""

from collections import deque
from typing import Optional

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_structures import TreeNode


class Solution:
    def kth_smallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach 1: Iterative Inorder Traversal
        Time Complexity: O(h + k) where h is height of tree
        Space Complexity: O(h) where h is height of tree
        """
        current = root
        stack = []
        count = 0

        while current or stack:
            # Go to leftmost node (smallest element)
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node (inorder)
            current = stack.pop()
            count += 1
            
            # Check if this is the kth smallest
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        return -1  # Should not reach here if k is valid
    
    def kth_smallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach 2: Recursive Inorder Traversal with Early Termination
        Time Complexity: O(h + k) where h is height of tree
        Space Complexity: O(h) where h is height of tree
        """
        # Use instance variables for early termination
        self.count = 0
        self.result = None
        
        def inorder(node):
            # Base case: empty node or already found result
            if not node or self.result is not None:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node and check if kth element
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return self.result
    
    def kth_smallest_optimized(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach 3: Optimized with Early Termination
        Time Complexity: O(h + k) where h is height of tree
        Space Complexity: O(h) where h is height of tree
        """
        current = root
        stack = []
        count = 0

        while current or stack:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            count += 1
            
            # Early termination when we find kth element
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        return -1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [3,1,4,null,2], k=1
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    
    # Test all approaches with the same test cases
    result1_iter = solution.kth_smallest_iterative(root1, 1)
    result1_rec = solution.kth_smallest_recursive(root1, 1)
    result1_opt = solution.kth_smallest_optimized(root1, 1)
    assert result1_iter == 1, f"Test 1 iterative failed: expected 1, got {result1_iter}"
    assert result1_rec == 1, f"Test 1 recursive failed: expected 1, got {result1_rec}"
    assert result1_opt == 1, f"Test 1 optimized failed: expected 1, got {result1_opt}"
    
    # Test case 2: [5,3,6,2,4,null,null,1], k=3
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    
    result2_iter = solution.kth_smallest_iterative(root2, 3)
    result2_rec = solution.kth_smallest_recursive(root2, 3)
    result2_opt = solution.kth_smallest_optimized(root2, 3)
    assert result2_iter == 3, f"Test 2 iterative failed: expected 3, got {result2_iter}"
    assert result2_rec == 3, f"Test 2 recursive failed: expected 3, got {result2_rec}"
    assert result2_opt == 3, f"Test 2 optimized failed: expected 3, got {result2_opt}"
    
    # Test case 3: [1], k=1
    #   1
    root3 = TreeNode(1)
    result3_iter = solution.kth_smallest_iterative(root3, 1)
    result3_rec = solution.kth_smallest_recursive(root3, 1)
    result3_opt = solution.kth_smallest_optimized(root3, 1)
    assert result3_iter == 1, f"Test 3 iterative failed: expected 1, got {result3_iter}"
    assert result3_rec == 1, f"Test 3 recursive failed: expected 1, got {result3_rec}"
    assert result3_opt == 1, f"Test 3 optimized failed: expected 1, got {result3_opt}"
    
    # Test case 4: [3,1,4,null,2], k=4
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root4 = TreeNode(3)
    root4.left = TreeNode(1)
    root4.right = TreeNode(4)
    root4.left.right = TreeNode(2)
    
    result4_iter = solution.kth_smallest_iterative(root4, 4)
    result4_rec = solution.kth_smallest_recursive(root4, 4)
    result4_opt = solution.kth_smallest_optimized(root4, 4)
    assert result4_iter == 4, f"Test 4 iterative failed: expected 4, got {result4_iter}"
    assert result4_rec == 4, f"Test 4 recursive failed: expected 4, got {result4_rec}"
    assert result4_opt == 4, f"Test 4 optimized failed: expected 4, got {result4_opt}"
    
    # Test case 5: [5,3,6,2,4,null,null,1], k=1
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root5 = TreeNode(5)
    root5.left = TreeNode(3)
    root5.right = TreeNode(6)
    root5.left.left = TreeNode(2)
    root5.left.right = TreeNode(4)
    root5.left.left.left = TreeNode(1)
    
    result5_iter = solution.kth_smallest_iterative(root5, 1)
    result5_rec = solution.kth_smallest_recursive(root5, 1)
    result5_opt = solution.kth_smallest_optimized(root5, 1)
    assert result5_iter == 1, f"Test 5 iterative failed: expected 1, got {result5_iter}"
    assert result5_rec == 1, f"Test 5 recursive failed: expected 1, got {result5_rec}"
    assert result5_opt == 1, f"Test 5 optimized failed: expected 1, got {result5_opt}"
    
    # Test case 6: [5,3,6,2,4,null,null,1], k=6
    result6_iter = solution.kth_smallest_iterative(root5, 6)
    result6_rec = solution.kth_smallest_recursive(root5, 6)
    result6_opt = solution.kth_smallest_optimized(root5, 6)
    assert result6_iter == 6, f"Test 6 iterative failed: expected 6, got {result6_iter}"
    assert result6_rec == 6, f"Test 6 recursive failed: expected 6, got {result6_rec}"
    assert result6_opt == 6, f"Test 6 optimized failed: expected 6, got {result6_opt}"
    
    # Test case 7: Test early termination with larger tree
    # Create a larger tree to test early termination
    #       10
    #      /  \
    #     5   15
    #    / \    \
    #   3   7   20
    #  /   /
    # 1   6
    # Inorder traversal: [1, 3, 5, 6, 7, 10, 15, 20]
    # So 3rd smallest is 5
    root7 = TreeNode(10)
    root7.left = TreeNode(5)
    root7.right = TreeNode(15)
    root7.left.left = TreeNode(3)
    root7.left.right = TreeNode(7)
    root7.right.right = TreeNode(20)
    root7.left.left.left = TreeNode(1)
    root7.left.right.left = TreeNode(6)
    
    # Test that all approaches return the same result
    result7_iter = solution.kth_smallest_iterative(root7, 3)
    result7_rec = solution.kth_smallest_recursive(root7, 3)
    result7_opt = solution.kth_smallest_optimized(root7, 3)
    assert result7_iter == 5, f"Test 7 iterative failed: expected 5, got {result7_iter}"
    assert result7_rec == 5, f"Test 7 recursive failed: expected 5, got {result7_rec}"
    assert result7_opt == 5, f"Test 7 optimized failed: expected 5, got {result7_opt}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()