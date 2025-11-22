"""
543. Diameter of Binary Tree
Difficulty: Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
Explanation: The diameter is the path [2,1] or [1,2].

Example 3:
Input: root = [1]
Output: 0
Explanation: Single node has diameter 0 (no edges).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

Notes:
- Key insight: The diameter of a tree is the maximum of:
  1. Diameter of left subtree
  2. Diameter of right subtree
  3. Longest path passing through current node (left_height + right_height)
- The longest path through a node = height of left subtree + height of right subtree
- We calculate height recursively and update diameter as we go
- Time complexity: O(n) - visit each node once
- Space complexity: O(h) where h is height of tree (recursion stack)
- Alternative approaches:
  - Iterative DFS: O(n) time, O(n) space - use stack
  - Two-pass: O(n) time - first calculate heights, then calculate diameters
  - Return tuple: O(n) time - return both height and diameter from each call
- Edge cases: Empty tree, single node, skewed tree, balanced tree
"""

from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        """
        Approach 1: Recursive DFS with Instance Variable (Current)
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Calculate height recursively and update diameter as we traverse.
        The diameter at each node is the sum of left and right subtree heights.
        """
        self.diameter = 0

        def height(node):
            # Base case: return 0 for empty node
            if not node:
                return 0

            # Calculate heights of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter: longest path through current node
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height of current subtree
            return max(left_height, right_height) + 1
            
        height(root)
        return self.diameter
    
    def diameter_of_binary_tree_tuple(self, root: Optional[TreeNode]) -> int:
        """
        Approach 2: Recursive DFS Returning Tuple
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Return both height and diameter from each recursive call.
        More functional style, no instance variable needed.
        """
        def dfs(node):
            if not node:
                return 0, 0  # (height, diameter)
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            # Current height
            current_height = max(left_height, right_height) + 1
            
            # Current diameter: max of left, right, or through current node
            current_diameter = max(
                left_diameter,
                right_diameter,
                left_height + right_height
            )
            
            return current_height, current_diameter
        
        _, diameter = dfs(root)
        return diameter
    
    def diameter_of_binary_tree_global(self, root: Optional[TreeNode]) -> int:
        """
        Approach 3: Recursive DFS with Global Variable
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Similar to approach 1 but using a nonlocal variable instead of instance variable.
        """
        diameter = 0

        def height(node):
            nonlocal diameter
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter = max(diameter, left_height + right_height)
            return max(left_height, right_height) + 1
            
        height(root)
        return diameter
    
    def diameter_of_binary_tree_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Approach 4: Iterative DFS (Post-order)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Use iterative post-order traversal with a stack.
        More complex but avoids recursion stack.
        """
        if not root:
            return 0
        
        # Dictionary to store heights of nodes
        heights = {}
        stack = [root]
        diameter = 0
        
        while stack:
            node = stack[-1]
            
            # If both children processed, calculate height and diameter
            if (not node.left or node.left in heights) and \
               (not node.right or node.right in heights):
                stack.pop()
                
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                
                # Update diameter
                diameter = max(diameter, left_height + right_height)
                
                # Store height of current node
                heights[node] = max(left_height, right_height) + 1
            else:
                # Add children to stack for processing
                if node.right and node.right not in heights:
                    stack.append(node.right)
                if node.left and node.left not in heights:
                    stack.append(node.left)
        
        return diameter
    
    def diameter_of_binary_tree_two_pass(self, root: Optional[TreeNode]) -> int:
        """
        Approach 5: Two-Pass (Calculate Heights First)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        First pass: calculate and store heights of all nodes.
        Second pass: calculate diameter using stored heights.
        Less efficient but more explicit.
        """
        if not root:
            return 0
        
        # First pass: calculate heights
        heights = {}
        
        def calculate_heights(node):
            if not node:
                return 0
            heights[node] = max(
                calculate_heights(node.left),
                calculate_heights(node.right)
            ) + 1
            return heights[node]
        
        calculate_heights(root)
        
        # Second pass: calculate diameter
        def calculate_diameter(node):
            if not node:
                return 0
            
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            
            current_diameter = left_height + right_height
            
            return max(
                current_diameter,
                calculate_diameter(node.left),
                calculate_diameter(node.right)
            )
        
        return calculate_diameter(root)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5]
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Diameter: path [4,2,1,3] or [5,2,1,3] = 3 edges
    print("Test 1: [1,2,3,4,5]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    expected1 = 3
    result1 = solution.diameter_of_binary_tree(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: [1,2]
    #   1
    #  /
    # 2
    # Diameter: path [2,1] = 1 edge
    print("Test 2: [1,2]")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    
    expected2 = 1
    result2 = solution.diameter_of_binary_tree(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Single node
    print("Test 3: Single node [1]")
    root3 = TreeNode(1)
    expected3 = 0
    result3 = solution.diameter_of_binary_tree(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Skewed tree (left)
    # 1
    #  \
    #   2
    #    \
    #     3
    # Diameter: path [1,2,3] = 2 edges
    print("Test 4: Skewed tree (right) [1,null,2,null,3]")
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    
    expected4 = 2
    result4 = solution.diameter_of_binary_tree(root4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Skewed tree (right)
    #     1
    #    /
    #   2
    #  /
    # 3
    # Diameter: path [3,2,1] = 2 edges
    print("Test 5: Skewed tree (left) [1,2,null,3]")
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    expected5 = 2
    result5 = solution.diameter_of_binary_tree(root5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Balanced tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    # Diameter: path through root = 4 edges (e.g., [4,2,1,3,7])
    print("Test 6: Balanced tree [1,2,3,4,5,6,7]")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    
    expected6 = 4
    result6 = solution.diameter_of_binary_tree(root6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Diameter not through root
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #  /     \
    # 6       7
    # Diameter: path [6,4,2,5,7] = 4 edges (not through root)
    print("Test 7: Diameter not through root")
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(3)
    root7.left.left = TreeNode(4)
    root7.left.right = TreeNode(5)
    root7.left.left.left = TreeNode(6)
    root7.left.right.right = TreeNode(7)
    
    expected7 = 4
    result7 = solution.diameter_of_binary_tree(root7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Large tree
    print("Test 8: Large tree with deep left subtree")
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    root8.left.left.left = TreeNode(6)
    root8.left.left.left.left = TreeNode(7)
    root8.left.right.right = TreeNode(8)
    
    expected8 = 5  # Path from node 7 to node 8
    result8 = solution.diameter_of_binary_tree(root8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Compare all approaches
    print("\nTest 9: Comparing all approaches")
    test_trees = [
        (root1, 3),
        (root2, 1),
        (root3, 0),
        (root4, 2),
        (root5, 2),
        (root6, 4),
    ]
    
    for root, expected in test_trees:
        result1 = solution.diameter_of_binary_tree(root)
        result2 = solution.diameter_of_binary_tree_tuple(root)
        result3 = solution.diameter_of_binary_tree_global(root)
        result4 = solution.diameter_of_binary_tree_iterative(root)
        result5 = solution.diameter_of_binary_tree_two_pass(root)
        
        assert result1 == expected, f"Approach 1 failed for tree: expected {expected}, got {result1}"
        assert result2 == expected, f"Approach 2 failed for tree: expected {expected}, got {result2}"
        assert result3 == expected, f"Approach 3 failed for tree: expected {expected}, got {result3}"
        assert result4 == expected, f"Approach 4 failed for tree: expected {expected}, got {result4}"
        assert result5 == expected, f"Approach 5 failed for tree: expected {expected}, got {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 10: Edge case - empty tree (should handle gracefully)
    print("\nTest 10: Edge case - empty tree")
    root10 = None
    expected10 = 0
    result10 = solution.diameter_of_binary_tree(root10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Complex tree
    #           1
    #          / \
    #         2   3
    #        /   / \
    #       4   5   6
    #      / \     /
    #     7   8   9
    #    /
    #  10
    print("Test 11: Complex tree")
    root11 = TreeNode(1)
    root11.left = TreeNode(2)
    root11.right = TreeNode(3)
    root11.left.left = TreeNode(4)
    root11.right.left = TreeNode(5)
    root11.right.right = TreeNode(6)
    root11.left.left.left = TreeNode(7)
    root11.left.left.right = TreeNode(8)
    root11.right.right.left = TreeNode(9)
    root11.left.left.left.left = TreeNode(10)
    
    expected11 = 6  # Path from node 10 to node 9
    result11 = solution.diameter_of_binary_tree(root11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()