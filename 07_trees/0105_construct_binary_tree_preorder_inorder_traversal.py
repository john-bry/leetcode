"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.

Notes:
- Key insight: First element in preorder is always the root.
- In inorder, elements to the left of root form left subtree, right form right subtree.
- Use hash map for O(1) lookup of inorder positions.
- Recursive approach naturally handles the tree construction.
"""

import os
import sys
from typing import List, Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_structures import TreeNode


class Solution:
    def build_tree_recursive(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach 1: Recursive with Hash Map
        Time Complexity: O(n)
        Space Complexity: O(n) for hash map + O(h) for recursion stack
        """
        # Create hash map for O(1) lookup of inorder positions
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            # Base case: no elements in current range
            if left > right:
                return None
            
            # Pick current root from preorder (first element is always root)
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1  # Move to next element in preorder
            
            # Find where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Build left subtree first, then right subtree
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        
        return build(0, len(inorder) - 1)
    
    def build_tree_iterative(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach 2: Iterative with Stack
        Time Complexity: O(n)
        Space Complexity: O(n) for stack
        """
        if not preorder:
            return None
        
        # Create hash map for O(1) lookup of inorder positions
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Initialize with root node
        root = TreeNode(preorder[0])
        stack = [root]
        pre_idx = 1
        
        for i in range(1, len(inorder)):
            # Current node from inorder
            current = TreeNode(preorder[pre_idx])
            pre_idx += 1
            
            # Find parent in stack
            parent = None
            while stack and inorder_map[stack[-1].val] < inorder_map[current.val]:
                parent = stack.pop()
            
            if parent:
                # Current is right child of parent
                parent.right = current
            else:
                # Current is left child of top of stack
                stack[-1].left = current
            
            stack.append(current)
        
        return root
    
    def build_tree_optimized(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach 3: Optimized Recursive with Slicing
        Time Complexity: O(n^2) due to slicing
        Space Complexity: O(n) for recursion stack
        """
        if not preorder or not inorder:
            return None
        
        # First element in preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find root position in inorder
        root_idx = inorder.index(root_val)
        
        # Split inorder array around root
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]
        
        # Split preorder array (skip first element, take lengths from inorder)
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        
        # Recursively build left and right subtrees
        root.left = self.build_tree_optimized(left_preorder, left_inorder)
        root.right = self.build_tree_optimized(right_preorder, right_inorder)
        
        return root


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Expected tree:
    #     3
    #    / \
    #   9   20
    #      /  \
    #     15   7
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    
    result1_rec = solution.build_tree_recursive(preorder1, inorder1)
    result1_iter = solution.build_tree_iterative(preorder1, inorder1)
    result1_opt = solution.build_tree_optimized(preorder1, inorder1)
    
    # Verify the tree structure by checking key nodes
    assert result1_rec.val == 3, f"Test 1 recursive root failed: expected 3, got {result1_rec.val}"
    assert result1_iter.val == 3, f"Test 1 iterative root failed: expected 3, got {result1_iter.val}"
    assert result1_opt.val == 3, f"Test 1 optimized root failed: expected 3, got {result1_opt.val}"
    
    # Test case 2: [-1], inorder = [-1]
    # Expected tree:
    #   -1
    preorder2 = [-1]
    inorder2 = [-1]
    
    result2_rec = solution.build_tree_recursive(preorder2, inorder2)
    result2_iter = solution.build_tree_iterative(preorder2, inorder2)
    result2_opt = solution.build_tree_optimized(preorder2, inorder2)
    
    assert result2_rec.val == -1, f"Test 2 recursive failed: expected -1, got {result2_rec.val}"
    assert result2_iter.val == -1, f"Test 2 iterative failed: expected -1, got {result2_iter.val}"
    assert result2_opt.val == -1, f"Test 2 optimized failed: expected -1, got {result2_opt.val}"
    
    # Test case 3: [1,2,3], inorder = [2,1,3]
    # Expected tree:
    #   1
    #  / \
    # 2   3
    preorder3 = [1, 2, 3]
    inorder3 = [2, 1, 3]
    
    result3_rec = solution.build_tree_recursive(preorder3, inorder3)
    result3_iter = solution.build_tree_iterative(preorder3, inorder3)
    result3_opt = solution.build_tree_optimized(preorder3, inorder3)
    
    assert result3_rec.val == 1, f"Test 3 recursive failed: expected 1, got {result3_rec.val}"
    assert result3_iter.val == 1, f"Test 3 iterative failed: expected 1, got {result3_iter.val}"
    assert result3_opt.val == 1, f"Test 3 optimized failed: expected 1, got {result3_opt.val}"
    
    # Test case 4: [1,2,4,5,3,6,7], inorder = [4,2,5,1,6,3,7]
    # Expected tree:
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    preorder4 = [1, 2, 4, 5, 3, 6, 7]
    inorder4 = [4, 2, 5, 1, 6, 3, 7]
    
    result4_rec = solution.build_tree_recursive(preorder4, inorder4)
    result4_iter = solution.build_tree_iterative(preorder4, inorder4)
    result4_opt = solution.build_tree_optimized(preorder4, inorder4)
    
    assert result4_rec.val == 1, f"Test 4 recursive failed: expected 1, got {result4_rec.val}"
    assert result4_iter.val == 1, f"Test 4 iterative failed: expected 1, got {result4_iter.val}"
    assert result4_opt.val == 1, f"Test 4 optimized failed: expected 1, got {result4_opt.val}"
    
    # Test case 5: Empty arrays
    preorder5 = []
    inorder5 = []
    
    result5_rec = solution.build_tree_recursive(preorder5, inorder5)
    result5_iter = solution.build_tree_iterative(preorder5, inorder5)
    result5_opt = solution.build_tree_optimized(preorder5, inorder5)
    
    assert result5_rec is None, f"Test 5 recursive failed: expected None, got {result5_rec}"
    assert result5_iter is None, f"Test 5 iterative failed: expected None, got {result5_iter}"
    assert result5_opt is None, f"Test 5 optimized failed: expected None, got {result5_opt}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()