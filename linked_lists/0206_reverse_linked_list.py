"""
206. Reverse Linked List
Difficulty: Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Notes:
- Key insight: Reverse the links between nodes while traversing the list.
- At each node, we need to:
  1. Save the next node (to continue traversal)
  2. Point current node's next to previous node
  3. Move previous to current, current to next
- Time complexity: O(n) - single pass through the list
- Space complexity: O(1) for iterative, O(n) for recursive (call stack)
- Alternative approaches:
  - Iterative: O(n) time, O(1) space - use three pointers
  - Recursive: O(n) time, O(n) space - reverse rest, then connect
  - Stack: O(n) time, O(n) space - push all nodes, pop to reverse
- Edge cases: Empty list, single node, two nodes
"""

import os
import sys
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import ListNode


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Iterative (Current)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use three pointers: prev, curr, and next (temp).
        Reverse links as we traverse the list.
        """
        curr = head
        prev = None

        while curr:
            temp = curr.next  # Save next node
            curr.next = prev  # Reverse the link
            prev = curr       # Move prev forward
            curr = temp       # Move curr forward

        return prev
    
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2: Recursive
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack
        
        Recursively reverse the rest of the list, then connect current node.
        Base case: empty list or single node returns itself.
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        reversed_rest = self.reverse_list_recursive(head.next)
        
        # Connect current node to reversed list
        head.next.next = head
        head.next = None
        
        return reversed_rest
    
    def reverse_list_stack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 3: Using Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Push all nodes onto a stack, then pop to build reversed list.
        Less efficient but demonstrates stack usage.
        """
        if not head:
            return None
        
        stack = []
        curr = head
        
        # Push all nodes onto stack
        while curr:
            stack.append(curr)
            curr = curr.next
        
        # Pop nodes to build reversed list
        new_head = stack.pop()
        curr = new_head
        
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        
        curr.next = None  # Set last node's next to None
        return new_head
    
    def reverse_list_iterative_alt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 4: Alternative Iterative (More Explicit)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Same as approach 1 but with more explicit variable names.
        """
        if not head:
            return None
        
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save next node
            current.next = prev        # Reverse link
            prev = current             # Move prev forward
            current = next_node        # Move current forward
        
        return prev
    
    def reverse_list_recursive_tail(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 5: Tail Recursive (Helper Function)
        Time Complexity: O(n)
        Space Complexity: O(n) - Python doesn't optimize tail recursion
        
        Tail-recursive version with helper function.
        More functional style.
        """
        def reverse_helper(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not curr:
                return prev
            
            next_node = curr.next
            curr.next = prev
            return reverse_helper(next_node, curr)
        
        return reverse_helper(head, None)


def list_to_array(head: Optional[ListNode]) -> list:
    """Helper function to convert linked list to array for testing"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example [1,2,3,4,5]
    print("Test 1: Basic example [1,2,3,4,5]")
    head1 = ListNode.from_list([1, 2, 3, 4, 5])
    expected1 = [5, 4, 3, 2, 1]
    result1 = solution.reverse_list(head1)
    result_array1 = list_to_array(result1)
    assert result_array1 == expected1, f"Test 1 failed: expected {expected1}, got {result_array1}"
    print(f"  Result: {result_array1} ✓")
    
    # Test case 2: Two nodes [1,2]
    print("Test 2: Two nodes [1,2]")
    head2 = ListNode.from_list([1, 2])
    expected2 = [2, 1]
    result2 = solution.reverse_list(head2)
    result_array2 = list_to_array(result2)
    assert result_array2 == expected2, f"Test 2 failed: expected {expected2}, got {result_array2}"
    print(f"  Result: {result_array2} ✓")
    
    # Test case 3: Empty list
    print("Test 3: Empty list []")
    head3 = None
    expected3 = []
    result3 = solution.reverse_list(head3)
    result_array3 = list_to_array(result3) if result3 else []
    assert result_array3 == expected3, f"Test 3 failed: expected {expected3}, got {result_array3}"
    print(f"  Result: {result_array3} ✓")
    
    # Test case 4: Single node
    print("Test 4: Single node [1]")
    head4 = ListNode.from_list([1])
    expected4 = [1]
    result4 = solution.reverse_list(head4)
    result_array4 = list_to_array(result4)
    assert result_array4 == expected4, f"Test 4 failed: expected {expected4}, got {result_array4}"
    print(f"  Result: {result_array4} ✓")
    
    # Test case 5: Large list
    print("Test 5: Large list [1,2,3,...,10]")
    head5 = ListNode.from_list(list(range(1, 11)))
    expected5 = list(range(10, 0, -1))
    result5 = solution.reverse_list(head5)
    result_array5 = list_to_array(result5)
    assert result_array5 == expected5, f"Test 5 failed: expected {expected5}, got {result_array5}"
    print(f"  Result: {result_array5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [1, 2, 3],
        list(range(1, 6)),
    ]
    
    for test_input in test_cases:
        head = ListNode.from_list(test_input)
        expected = list(reversed(test_input))
        
        result1 = list_to_array(solution.reverse_list(ListNode.from_list(test_input)))
        result2 = list_to_array(solution.reverse_list_recursive(ListNode.from_list(test_input)))
        result3 = list_to_array(solution.reverse_list_stack(ListNode.from_list(test_input)))
        result4 = list_to_array(solution.reverse_list_iterative_alt(ListNode.from_list(test_input)))
        result5 = list_to_array(solution.reverse_list_recursive_tail(ListNode.from_list(test_input)))
        
        assert result1 == expected, f"Iterative failed for {test_input}: {result1} vs {expected}"
        assert result2 == expected, f"Recursive failed for {test_input}: {result2} vs {expected}"
        assert result3 == expected, f"Stack failed for {test_input}: {result3} vs {expected}"
        assert result4 == expected, f"Iterative alt failed for {test_input}: {result4} vs {expected}"
        assert result5 == expected, f"Tail recursive failed for {test_input}: {result5} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: Negative values
    print("\nTest 7: Negative values [-1,-2,-3]")
    head7 = ListNode.from_list([-1, -2, -3])
    expected7 = [-3, -2, -1]
    result7 = solution.reverse_list(head7)
    result_array7 = list_to_array(result7)
    assert result_array7 == expected7, f"Test 7 failed: expected {expected7}, got {result_array7}"
    print(f"  Result: {result_array7} ✓")
    
    # Test case 8: Mixed positive and negative
    print("Test 8: Mixed values [1,-2,3,-4,5]")
    head8 = ListNode.from_list([1, -2, 3, -4, 5])
    expected8 = [5, -4, 3, -2, 1]
    result8 = solution.reverse_list(head8)
    result_array8 = list_to_array(result8)
    assert result_array8 == expected8, f"Test 8 failed: expected {expected8}, got {result_array8}"
    print(f"  Result: {result_array8} ✓")
    
    # Test case 9: All same values
    print("Test 9: All same values [5,5,5,5]")
    head9 = ListNode.from_list([5, 5, 5, 5])
    expected9 = [5, 5, 5, 5]
    result9 = solution.reverse_list(head9)
    result_array9 = list_to_array(result9)
    assert result_array9 == expected9, f"Test 9 failed: expected {expected9}, got {result_array9}"
    print(f"  Result: {result_array9} ✓")
    
    # Test case 10: Zero values
    print("Test 10: Zero values [0,0,0]")
    head10 = ListNode.from_list([0, 0, 0])
    expected10 = [0, 0, 0]
    result10 = solution.reverse_list(head10)
    result_array10 = list_to_array(result10)
    assert result_array10 == expected10, f"Test 10 failed: expected {expected10}, got {result_array10}"
    print(f"  Result: {result_array10} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()