"""
100. Same Tree
Difficulty: Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
"""

from collections import deque
from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    def is_same_tree_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach 1: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Base case: both trees are empty
        if not p and not q:
            return True
        
        # One tree is empty, the other is not
        if not p or not q:
            return False
        
        # Compare current node values and recursively check subtrees
        return (p.val == q.val and 
                self.is_same_tree_recursive(p.left, q.left) and 
                self.is_same_tree_recursive(p.right, q.right))
    
    def is_same_tree_iterative_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach 2: Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        # Use stack to store pairs of nodes to compare
        stack = [(p, q)]
        
        while stack:
            node_p, node_q = stack.pop()
            
            # Both nodes are None - continue
            if not node_p and not node_q:
                continue
            
            # One is None, the other is not
            if not node_p or not node_q:
                return False
            
            # Values don't match
            if node_p.val != node_q.val:
                return False
            
            # Add children pairs to stack for comparison
            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))
        
        return True
    
    def is_same_tree_iterative_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach 3: Iterative BFS
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        # Use queue for level-by-level comparison
        queue = deque([(p, q)])
        
        while queue:
            node_p, node_q = queue.popleft()
            
            # Both nodes are None - continue
            if not node_p and not node_q:
                continue
            
            # One is None, the other is not
            if not node_p or not node_q:
                return False
            
            # Values don't match
            if node_p.val != node_q.val:
                return False
            
            # Add children pairs to queue for next level comparison
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
        
        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: [1,2,3] vs [1,2,3]
    # Tree 1:    1    Tree 2:    1
    #           / \            / \
    #          2   3          2   3
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    
    result1 = solution.is_same_tree_recursive(p1, q1)
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"
    
    # Test case 2: [1,2] vs [1,null,2]
    # Tree 1:    1    Tree 2:    1
    #           /                \
    #          2                  2
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    
    result2 = solution.is_same_tree_recursive(p2, q2)
    assert result2 == False, f"Test 2 failed: expected False, got {result2}"
    
    # Test case 3: [1,2,1] vs [1,1,2]
    # Tree 1:    1    Tree 2:    1
    #           / \            / \
    #          2   1          1   2
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)
    
    result3 = solution.is_same_tree_recursive(p3, q3)
    assert result3 == False, f"Test 3 failed: expected False, got {result3}"
    
    # Test case 4: Both empty trees
    p4 = None
    q4 = None
    result4 = solution.is_same_tree_recursive(p4, q4)
    assert result4 == True, f"Test 4 failed: expected True, got {result4}"
    
    # Test case 5: One empty, one not
    p5 = TreeNode(1)
    q5 = None
    result5 = solution.is_same_tree_recursive(p5, q5)
    assert result5 == False, f"Test 5 failed: expected False, got {result5}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()