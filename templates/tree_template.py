"""
Template for Tree problems
"""

from typing import List, Optional

from utils.data_structures import TreeNode


class Solution:
    """
    Problem: [Problem Name]
    Difficulty: Easy/Medium/Hard
    
    Problem Statement:
    [Describe the problem here]
    
    Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [expected output]
    Explanation: [explanation]
    """
    
    def recursive_solution(self, root: Optional[TreeNode]) -> int:
        """
        Approach 1: Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        if not root:
            return 0
        
        # Base case
        if not root.left and not root.right:
            return 1
        
        # Recursive case
        left_result = self.recursive_solution(root.left)
        right_result = self.recursive_solution(root.right)
        
        return left_result + right_result
    
    def iterative_solution(self, root: Optional[TreeNode]) -> int:
        """
        Approach 2: Iterative BFS
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        if not root:
            return 0
        
        from collections import deque
        queue = deque([root])
        result = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                # Process current node
                result += 1
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
    
    def dfs_solution(self, root: Optional[TreeNode]) -> int:
        """
        Approach 3: Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        if not root:
            return 0
        
        stack = [root]
        result = 0
        
        while stack:
            node = stack.pop()
            
            # Process current node
            result += 1
            
            # Add children to stack (right first for preorder)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Simple tree
    #    1
    #   / \
    #  2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    
    expected1 = 3
    result1 = solution.recursive_solution(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    expected2 = 1
    result2 = solution.recursive_solution(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Empty tree
    root3 = None
    expected3 = 0
    result3 = solution.recursive_solution(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
