"""
108. Convert Sorted Array to Binary Search Tree
Difficulty: Easy

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in a strictly increasing order.

Notes:
- Key insight: For a sorted array, the middle element should be the root to maintain balance.
- Recursively build left and right subtrees from left and right halves of the array.
- Time complexity: O(n) - visit each element once
- Space complexity: 
  - With slicing: O(n log n) - creates new arrays at each level
  - With indices: O(log n) - only recursion stack for balanced tree
- Alternative approaches:
  - Recursive with slicing: O(n) time, O(n log n) space - simple but inefficient
  - Recursive with indices: O(n) time, O(log n) space - optimal, avoids array copying
  - Iterative: O(n) time, O(log n) space - use stack to simulate recursion
- Edge cases: Empty array, single element, two elements, odd/even length
"""

import os
import sys
from typing import List, Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import TreeNode


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach 1: Recursive with Slicing (Current)
        Time Complexity: O(n)
        Space Complexity: O(n log n) due to array slicing
        
        Simple approach but creates new arrays at each recursive call.
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid+1:])

        return root
    
    def sorted_array_to_bst_optimized(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach 2: Recursive with Indices (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(log n) for balanced tree
        
        Use indices instead of slicing to avoid creating new arrays.
        More space-efficient approach.
        """
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
        
        return build_bst(0, len(nums) - 1)
    
    def sorted_array_to_bst_iterative(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach 3: Iterative with Stack
        Time Complexity: O(n)
        Space Complexity: O(log n)
        
        Use a stack to simulate recursion.
        Less intuitive but avoids recursion stack.
        """
        if not nums:
            return None
        
        # Stack stores (left, right, parent, is_left) tuples
        root = TreeNode(0)  # Dummy root
        stack = [(0, len(nums) - 1, root, True)]
        
        while stack:
            left, right, parent, is_left = stack.pop()
            
            if left > right:
                continue
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            # Add right subtree first (stack is LIFO)
            stack.append((mid + 1, right, node, False))
            stack.append((left, mid - 1, node, True))
        
        return root.left
    
    def sorted_array_to_bst_alternative(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach 4: Alternative Recursive Structure
        Time Complexity: O(n)
        Space Complexity: O(n log n) with slicing
        
        Similar to approach 1 but with helper method.
        """
        if not nums:
            return None
        
        return self._build_bst(nums, 0, len(nums) - 1)
    
    def _build_bst(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        """Helper method to build BST from array segment"""
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        root.left = self._build_bst(nums, left, mid - 1)
        root.right = self._build_bst(nums, mid + 1, right)
        
        return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Helper function to convert tree to list representation for testing"""
    if not root:
        return []
    
    result = []
    from collections import deque
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Helper function to validate if tree is a valid BST"""
    def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def get_height(root: Optional[TreeNode]) -> int:
    """Helper function to get tree height"""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Helper function to check if tree is height-balanced"""
    def check_balance(node: Optional[TreeNode]) -> tuple[bool, int]:
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)
        
        balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
        height = 1 + max(left_height, right_height)
        
        return balanced, height
    
    balanced, _ = check_balance(root)
    return balanced


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example [-10,-3,0,5,9]
    print("Test 1: Basic example [-10,-3,0,5,9]")
    nums1 = [-10, -3, 0, 5, 9]
    result1 = solution.sorted_array_to_bst(nums1)
    # Should create a balanced BST
    assert is_valid_bst(result1), "Test 1 failed: Not a valid BST"
    assert is_balanced(result1), "Test 1 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 2: Two elements [1,3]
    print("Test 2: Two elements [1,3]")
    nums2 = [1, 3]
    result2 = solution.sorted_array_to_bst(nums2)
    assert is_valid_bst(result2), "Test 2 failed: Not a valid BST"
    assert is_balanced(result2), "Test 2 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 3: Single element [0]
    print("Test 3: Single element [0]")
    nums3 = [0]
    result3 = solution.sorted_array_to_bst(nums3)
    assert result3 is not None, "Test 3 failed: Root is None"
    assert result3.val == 0, "Test 3 failed: Wrong root value"
    assert result3.left is None and result3.right is None, "Test 3 failed: Should be single node"
    print(f"  Result: Single node with value 0 ✓")
    
    # Test case 4: Empty array
    print("Test 4: Empty array []")
    nums4 = []
    result4 = solution.sorted_array_to_bst(nums4)
    assert result4 is None, "Test 4 failed: Should return None for empty array"
    print(f"  Result: None ✓")
    
    # Test case 5: Odd length [1,2,3,4,5]
    print("Test 5: Odd length [1,2,3,4,5]")
    nums5 = [1, 2, 3, 4, 5]
    result5 = solution.sorted_array_to_bst(nums5)
    assert is_valid_bst(result5), "Test 5 failed: Not a valid BST"
    assert is_balanced(result5), "Test 5 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 6: Even length [1,2,3,4]
    print("Test 6: Even length [1,2,3,4]")
    nums6 = [1, 2, 3, 4]
    result6 = solution.sorted_array_to_bst(nums6)
    assert is_valid_bst(result6), "Test 6 failed: Not a valid BST"
    assert is_balanced(result6), "Test 6 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 7: Negative values
    print("Test 7: Negative values [-5,-4,-3,-2,-1]")
    nums7 = [-5, -4, -3, -2, -1]
    result7 = solution.sorted_array_to_bst(nums7)
    assert is_valid_bst(result7), "Test 7 failed: Not a valid BST"
    assert is_balanced(result7), "Test 7 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 8: Compare all approaches
    print("\nTest 8: Comparing all approaches")
    test_cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [-5, -4, -3, -2, -1],
    ]
    
    for nums in test_cases:
        result1 = solution.sorted_array_to_bst(nums)
        result2 = solution.sorted_array_to_bst_optimized(nums)
        result3 = solution.sorted_array_to_bst_iterative(nums)
        result4 = solution.sorted_array_to_bst_alternative(nums)
        
        # All should produce valid and balanced BSTs
        assert is_valid_bst(result1), f"Slicing failed for {nums}"
        assert is_valid_bst(result2), f"Optimized failed for {nums}"
        assert is_valid_bst(result3), f"Iterative failed for {nums}"
        assert is_valid_bst(result4), f"Alternative failed for {nums}"
        
        assert is_balanced(result1), f"Slicing not balanced for {nums}"
        assert is_balanced(result2), f"Optimized not balanced for {nums}"
        assert is_balanced(result3), f"Iterative not balanced for {nums}"
        assert is_balanced(result4), f"Alternative not balanced for {nums}"
    
    print("  All approaches produce valid and balanced BSTs! ✓")
    
    # Test case 9: Large array
    print("\nTest 9: Large array [0..99]")
    nums9 = list(range(100))
    result9 = solution.sorted_array_to_bst(nums9)
    assert is_valid_bst(result9), "Test 9 failed: Not a valid BST"
    assert is_balanced(result9), "Test 9 failed: Not height-balanced"
    height9 = get_height(result9)
    # For 100 elements, height should be around log2(100) ≈ 7
    assert height9 <= 8, f"Test 9 failed: Height {height9} too large for balanced tree"
    print(f"  Result: Valid and balanced BST with height {height9} ✓")
    
    # Test case 10: Zero values
    print("Test 10: Zero values [0,0,0]")
    nums10 = [0, 0, 0]
    result10 = solution.sorted_array_to_bst(nums10)
    # Note: This violates BST property (duplicates), but the problem states strictly increasing
    # So this test case might not be valid per constraints
    print(f"  Result: Tree created (note: duplicates violate BST property) ✓")
    
    # Test case 11: Three elements
    print("Test 11: Three elements [1,2,3]")
    nums11 = [1, 2, 3]
    result11 = solution.sorted_array_to_bst(nums11)
    assert is_valid_bst(result11), "Test 11 failed: Not a valid BST"
    assert is_balanced(result11), "Test 11 failed: Not height-balanced"
    assert result11.val == 2, "Test 11 failed: Root should be middle element"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 12: Mixed positive and negative
    print("Test 12: Mixed values [-3,-1,0,2,4]")
    nums12 = [-3, -1, 0, 2, 4]
    result12 = solution.sorted_array_to_bst(nums12)
    assert is_valid_bst(result12), "Test 12 failed: Not a valid BST"
    assert is_balanced(result12), "Test 12 failed: Not height-balanced"
    print(f"  Result: Valid and balanced BST ✓")
    
    # Test case 13: Verify inorder traversal gives sorted array
    print("Test 13: Verify inorder traversal")
    nums13 = [1, 2, 3, 4, 5, 6, 7]
    result13 = solution.sorted_array_to_bst(nums13)
    
    def inorder(node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    inorder_result = inorder(result13)
    assert inorder_result == nums13, f"Test 13 failed: Inorder {inorder_result} != original {nums13}"
    print(f"  Result: Inorder traversal matches original array ✓")
    
    # Test case 14: Height verification
    print("Test 14: Height verification for balanced tree")
    nums14 = list(range(15))  # 15 elements
    result14 = solution.sorted_array_to_bst(nums14)
    height14 = get_height(result14)
    # For 15 elements, balanced tree height should be around 4
    assert 4 <= height14 <= 5, f"Test 14 failed: Height {height14} not balanced for 15 elements"
    print(f"  Result: Height {height14} is balanced ✓")
    
    # Test case 15: Edge case - two elements with different structures
    print("Test 15: Two elements structure check")
    nums15 = [1, 2]
    result15 = solution.sorted_array_to_bst(nums15)
    # Should have root = 1 or 2 (depending on implementation)
    # Both are valid balanced BSTs
    assert result15 is not None, "Test 15 failed: Root is None"
    assert result15.val in [1, 2], "Test 15 failed: Root value incorrect"
    assert is_balanced(result15), "Test 15 failed: Not balanced"
    print(f"  Result: Valid balanced BST ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()