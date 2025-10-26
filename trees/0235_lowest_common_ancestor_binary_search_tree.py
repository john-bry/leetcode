"""
235. Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
"""

from collections import deque
from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def lowest_common_ancestor_recursive(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Approach 1: Recursive DFS
        Time Complexity: O(h) where h is height of tree
        Space Complexity: O(h) where h is height of tree
        """
        # Base case: empty tree
        if not root:
            return None
        
        # Both nodes are smaller - LCA is in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor_recursive(root.left, p, q)
        
        # Both nodes are larger - LCA is in right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor_recursive(root.right, p, q)
        
        # Current node is the LCA (split point or one equals root)
        else:
            return root
    
    def lowest_common_ancestor_iterative(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Approach 2: Iterative DFS
        Time Complexity: O(h) where h is height of tree
        Space Complexity: O(1)
        """
        # Handle empty tree
        if not root:
            return None
        
        current = root
        while current:
            # Both nodes are smaller - go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            
            # Both nodes are larger - go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            
            # Found the LCA (split point or one equals current)
            else:
                return current
        
        return None
    
    def lowest_common_ancestor_path_based(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Approach 3: Path-based approach
        Time Complexity: O(h) where h is height of tree
        Space Complexity: O(h) where h is height of tree
        """
        # Handle empty tree
        if not root:
            return None
        
        # Find path to p
        def find_path(node, target, path):
            if not node:
                return False
            
            path.append(node)
            
            if node.val == target.val:
                return True
            
            if target.val < node.val:
                if find_path(node.left, target, path):
                    return True
            else:
                if find_path(node.right, target, path):
                    return True
            
            path.pop()
            return False
        
        path_p = []
        path_q = []
        
        # Find paths to both nodes
        find_path(root, p, path_p)
        find_path(root, q, path_q)
        
        # Find the last common node in both paths
        lca = None
        min_length = min(len(path_p), len(path_q))
        
        for i in range(min_length):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
        
        return lca


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [6,2,8,0,4,7,9,null,null,3,5], p=2, q=8
    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7  9
    #     / \
    #    3   5
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    
    p1 = root1.left  # node with val 2
    q1 = root1.right  # node with val 8
    expected1 = root1  # node with val 6
    
    result1 = solution.lowest_common_ancestor_recursive(root1, p1, q1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1.val}, got {result1.val if result1 else None}"
    
    # Test case 2: [6,2,8,0,4,7,9,null,null,3,5], p=2, q=4
    p2 = root1.left  # node with val 2
    q2 = root1.left.right  # node with val 4
    expected2 = root1.left  # node with val 2
    
    result2 = solution.lowest_common_ancestor_recursive(root1, p2, q2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2.val}, got {result2.val if result2 else None}"
    
    # Test case 3: [2,1], p=2, q=1
    #   2
    #  /
    # 1
    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    
    p3 = root3  # node with val 2
    q3 = root3.left  # node with val 1
    expected3 = root3  # node with val 2
    
    result3 = solution.lowest_common_ancestor_recursive(root3, p3, q3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3.val}, got {result3.val if result3 else None}"
    
    # Test case 4: Edge case - p and q are the same
    root4 = TreeNode(5)
    root4.left = TreeNode(3)
    root4.right = TreeNode(7)
    
    p4 = root4.left  # node with val 3
    q4 = root4.left  # same node
    expected4 = root4.left  # node with val 3
    
    result4 = solution.lowest_common_ancestor_recursive(root4, p4, q4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4.val}, got {result4.val if result4 else None}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()