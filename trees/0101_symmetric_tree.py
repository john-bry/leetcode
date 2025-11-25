"""
101. Symmetric Tree
Difficulty: Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
Explanation: The tree is symmetric around the center.

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
Explanation: The tree is not symmetric.

Example 3:
Input: root = [1]
Output: true
Explanation: Single node is symmetric.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

Notes:
- Key insight: A tree is symmetric if the left subtree is a mirror of the right subtree.
- Compare nodes in mirror positions: left.left with right.right, and left.right with right.left.
- Time complexity: O(n) - visit each node once
- Space complexity: 
  - Recursive: O(h) where h is height (recursion stack)
  - Iterative BFS: O(w) where w is maximum width
  - Iterative DFS: O(h) where h is height (stack)
- Alternative approaches:
  - Recursive: O(n) time, O(h) space - most intuitive, compare mirror subtrees
  - Iterative BFS: O(n) time, O(w) space - level-by-level comparison (current)
  - Iterative DFS: O(n) time, O(h) space - use stack instead of queue
- Edge cases: Empty tree, single node, asymmetric values, asymmetric structure
"""

import os
import sys
from collections import deque
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import TreeNode


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 1: Iterative BFS (Current)
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        
        Use a queue to compare nodes level by level in mirror positions.
        """
        # Handle empty tree
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            # Both null - symmetric, continue
            if not left and not right:
                continue
            
            # One null or values don't match - not symmetric
            if not left or not right or left.val != right.val:
                return False
            
            # Add children in mirror order
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True
    
    def is_symmetric_recursive(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 2: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Recursively compare mirror subtrees.
        Most intuitive and commonly used approach.
        """
        if not root:
            return True
        
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both are None - symmetric
            if not left and not right:
                return True
            
            # One is None, the other is not - not symmetric
            if not left or not right:
                return False
            
            # Values must match, and subtrees must be mirrors
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)
    
    def is_symmetric_iterative_dfs(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 3: Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Use a stack instead of queue for depth-first comparison.
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            # Both null - symmetric, continue
            if not left and not right:
                continue
            
            # One null or values don't match - not symmetric
            if not left or not right or left.val != right.val:
                return False
            
            # Add children in mirror order (right first for DFS)
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        
        return True
    
    def is_symmetric_alternative(self, root: Optional[TreeNode]) -> bool:
        """
        Approach 4: Alternative Recursive (Helper as Method)
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Same as recursive but with helper as a method instead of nested function.
        """
        if not root:
            return True
        
        return self._check_symmetric(root.left, root.right)
    
    def _check_symmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """Helper method to check if two subtrees are symmetric"""
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                self._check_symmetric(left.left, right.right) and
                self._check_symmetric(left.right, right.left))


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Symmetric tree [1,2,2,3,4,4,3]
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    print("Test 1: Symmetric tree [1,2,2,3,4,4,3]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    
    expected1 = True
    result1 = solution.is_symmetric(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Not symmetric [1,2,2,null,3,null,3]
    #       1
    #      / \
    #     2   2
    #      \   \
    #       3   3
    print("Test 2: Not symmetric [1,2,2,null,3,null,3]")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    
    expected2 = False
    result2 = solution.is_symmetric(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Single node [1]
    print("Test 3: Single node [1]")
    root3 = TreeNode(1)
    expected3 = True
    result3 = solution.is_symmetric(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Empty tree
    print("Test 4: Empty tree []")
    root4 = None
    expected4 = True
    result4 = solution.is_symmetric(root4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Two nodes symmetric [1,2,2]
    #       1
    #      / \
    #     2   2
    print("Test 5: Two nodes symmetric [1,2,2]")
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(2)
    
    expected5 = True
    result5 = solution.is_symmetric(root5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two nodes not symmetric [1,2,3]
    #       1
    #      / \
    #     2   3
    print("Test 6: Two nodes not symmetric [1,2,3]")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    
    expected6 = False
    result6 = solution.is_symmetric(root6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Asymmetric structure [1,2,2,2,null,2]
    #       1
    #      / \
    #     2   2
    #    /     \
    #   2       2
    print("Test 7: Asymmetric structure [1,2,2,2,null,2]")
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(2)
    root7.left.left = TreeNode(2)
    root7.right.right = TreeNode(2)
    
    expected7 = False
    result7 = solution.is_symmetric(root7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Large symmetric tree
    print("Test 8: Large symmetric tree")
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(2)
    root8.left.left = TreeNode(3)
    root8.left.right = TreeNode(4)
    root8.right.left = TreeNode(4)
    root8.right.right = TreeNode(3)
    root8.left.left.left = TreeNode(5)
    root8.left.left.right = TreeNode(6)
    root8.left.right.left = TreeNode(7)
    root8.left.right.right = TreeNode(8)
    root8.right.left.left = TreeNode(8)
    root8.right.left.right = TreeNode(7)
    root8.right.right.left = TreeNode(6)
    root8.right.right.right = TreeNode(5)
    
    expected8 = True
    result8 = solution.is_symmetric(root8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Compare all approaches
    print("\nTest 9: Comparing all approaches")
    test_cases = [
        (root1, True),
        (root2, False),
        (root3, True),
        (root5, True),
        (root6, False),
    ]
    
    for root, expected in test_cases:
        # Recreate trees for each approach since they may modify the tree
        def recreate_tree(vals, idx=0):
            if idx >= len(vals) or vals[idx] is None:
                return None
            node = TreeNode(vals[idx])
            node.left = recreate_tree(vals, 2*idx + 1) if 2*idx + 1 < len(vals) else None
            node.right = recreate_tree(vals, 2*idx + 2) if 2*idx + 2 < len(vals) else None
            return node
        
        # For simplicity, test with manually created trees
        if root == root1:
            test_root1 = TreeNode(1)
            test_root1.left = TreeNode(2)
            test_root1.right = TreeNode(2)
            test_root1.left.left = TreeNode(3)
            test_root1.left.right = TreeNode(4)
            test_root1.right.left = TreeNode(4)
            test_root1.right.right = TreeNode(3)
            result1 = solution.is_symmetric(test_root1)
            result2 = solution.is_symmetric_recursive(test_root1)
            result3 = solution.is_symmetric_iterative_dfs(test_root1)
            result4 = solution.is_symmetric_alternative(test_root1)
            assert result1 == expected, f"BFS failed: {result1} vs {expected}"
            assert result2 == expected, f"Recursive failed: {result2} vs {expected}"
            assert result3 == expected, f"DFS failed: {result3} vs {expected}"
            assert result4 == expected, f"Alternative failed: {result4} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 10: All same values symmetric [1,1,1,1,1,1,1]
    print("\nTest 10: All same values symmetric")
    root10 = TreeNode(1)
    root10.left = TreeNode(1)
    root10.right = TreeNode(1)
    root10.left.left = TreeNode(1)
    root10.left.right = TreeNode(1)
    root10.right.left = TreeNode(1)
    root10.right.right = TreeNode(1)
    
    expected10 = True
    result10 = solution.is_symmetric(root10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Negative values
    print("Test 11: Negative values [-1,-2,-2]")
    root11 = TreeNode(-1)
    root11.left = TreeNode(-2)
    root11.right = TreeNode(-2)
    
    expected11 = True
    result11 = solution.is_symmetric(root11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Zero values
    print("Test 12: Zero values [0,0,0]")
    root12 = TreeNode(0)
    root12.left = TreeNode(0)
    root12.right = TreeNode(0)
    
    expected12 = True
    result12 = solution.is_symmetric(root12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Mixed positive and negative
    print("Test 13: Mixed values [1,-2,-2]")
    root13 = TreeNode(1)
    root13.left = TreeNode(-2)
    root13.right = TreeNode(-2)
    
    expected13 = True
    result13 = solution.is_symmetric(root13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Skewed tree (not symmetric)
    print("Test 14: Skewed tree [1,2,null]")
    root14 = TreeNode(1)
    root14.left = TreeNode(2)
    
    expected14 = False
    result14 = solution.is_symmetric(root14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex asymmetric
    print("Test 15: Complex asymmetric tree")
    root15 = TreeNode(1)
    root15.left = TreeNode(2)
    root15.right = TreeNode(2)
    root15.left.left = TreeNode(3)
    root15.left.right = TreeNode(4)
    root15.right.left = TreeNode(4)
    root15.right.right = TreeNode(3)
    root15.left.left.left = TreeNode(5)
    root15.right.right.right = TreeNode(6)  # Different value
    
    expected15 = False
    result15 = solution.is_symmetric(root15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()