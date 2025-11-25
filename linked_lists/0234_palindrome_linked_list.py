"""
234. Palindrome Linked List
Difficulty: Easy

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
Explanation: The list [1,2,2,1] is a palindrome.

Example 2:
Input: head = [1,2]
Output: false
Explanation: The list [1,2] is not a palindrome.

Example 3:
Input: head = [1]
Output: true
Explanation: Single node is a palindrome.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Notes:
- Key insight: A palindrome reads the same forwards and backwards.
- For linked lists, we can't directly access elements from the end.
- Optimal approach: Find middle, reverse second half, compare with first half.
- Time complexity: O(n) for all approaches
- Space complexity: 
  - Convert to list: O(n)
  - Reverse half: O(1) - optimal
  - Stack: O(n)
  - Recursive: O(n) for call stack
- Alternative approaches:
  - Convert to list: O(n) time, O(n) space - simple but uses extra space
  - Reverse half: O(n) time, O(1) space - optimal, modifies list temporarily
  - Stack: O(n) time, O(n) space - push first half, compare with second half
  - Recursive: O(n) time, O(n) space - use recursion to compare from both ends
- Edge cases: Empty list (not possible per constraints), single node, two nodes, odd/even length
"""

import os
import sys
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import ListNode


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach 1: Convert to List and Check (Current)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Convert the linked list to a list and check if it is a palindrome.
        Simple but uses O(n) extra space.
        """
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]
    
    def is_palindrome_reverse_half(self, head: Optional[ListNode]) -> bool:
        """
        Approach 2: Reverse Second Half (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Find the middle, reverse the second half, then compare with first half.
        Most space-efficient approach.
        """
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare first half with reversed second half
        first = head
        second = prev
        while second:  # Second half might be shorter for odd-length lists
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
    def is_palindrome_stack(self, head: Optional[ListNode]) -> bool:
        """
        Approach 3: Using Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Push first half onto stack, then compare with second half.
        """
        if not head or not head.next:
            return True
        
        # Find the middle and length
        slow = fast = head
        stack = []
        
        # Push first half onto stack
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        # If odd length, skip middle node
        if fast:
            slow = slow.next
        
        # Compare second half with stack
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        
        return True
    
    def is_palindrome_recursive(self, head: Optional[ListNode]) -> bool:
        """
        Approach 4: Recursive with Global Variable
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack
        
        Use recursion to compare nodes from both ends.
        More elegant but uses O(n) space for call stack.
        """
        self.front = head
        
        def check_recursive(curr: Optional[ListNode]) -> bool:
            if curr:
                # Recurse to the end
                if not check_recursive(curr.next):
                    return False
                # Compare current node with front
                if self.front.val != curr.val:
                    return False
                self.front = self.front.next
            return True
        
        return check_recursive(head)
    
    def is_palindrome_two_pointers(self, head: Optional[ListNode]) -> bool:
        """
        Approach 5: Two Pointers with List Conversion (Alternative)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Convert to list and use two pointers from both ends.
        More explicit than list reversal.
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        left, right = 0, len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        
        return True


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
    
    # Test case 1: Basic palindrome [1,2,2,1]
    print("Test 1: Basic palindrome [1,2,2,1]")
    head1 = ListNode.from_list([1, 2, 2, 1])
    expected1 = True
    result1 = solution.is_palindrome(head1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Not a palindrome [1,2]
    print("Test 2: Not a palindrome [1,2]")
    head2 = ListNode.from_list([1, 2])
    expected2 = False
    result2 = solution.is_palindrome(head2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Single node
    print("Test 3: Single node [1]")
    head3 = ListNode.from_list([1])
    expected3 = True
    result3 = solution.is_palindrome(head3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Odd length palindrome [1,2,3,2,1]
    print("Test 4: Odd length palindrome [1,2,3,2,1]")
    head4 = ListNode.from_list([1, 2, 3, 2, 1])
    expected4 = True
    result4 = solution.is_palindrome(head4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Even length palindrome [1,2,3,3,2,1]
    print("Test 5: Even length palindrome [1,2,3,3,2,1]")
    head5 = ListNode.from_list([1, 2, 3, 3, 2, 1])
    expected5 = True
    result5 = solution.is_palindrome(head5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Not palindrome [1,2,3,4]
    print("Test 6: Not palindrome [1,2,3,4]")
    head6 = ListNode.from_list([1, 2, 3, 4])
    expected6 = False
    result6 = solution.is_palindrome(head6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: All same values [1,1,1,1]
    print("Test 7: All same values [1,1,1,1]")
    head7 = ListNode.from_list([1, 1, 1, 1])
    expected7 = True
    result7 = solution.is_palindrome(head7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Two nodes palindrome [1,1]
    print("Test 8: Two nodes palindrome [1,1]")
    head8 = ListNode.from_list([1, 1])
    expected8 = True
    result8 = solution.is_palindrome(head8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Two nodes not palindrome [1,2]
    print("Test 9: Two nodes not palindrome [1,2]")
    head9 = ListNode.from_list([1, 2])
    expected9 = False
    result9 = solution.is_palindrome(head9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Compare all approaches
    print("\nTest 10: Comparing all approaches")
    test_cases = [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 1], True),
        ([1, 1], True),
        ([1, 2, 3, 3, 2, 1], True),
    ]
    
    for test_input, expected in test_cases:
        head = ListNode.from_list(test_input)
        
        result1 = solution.is_palindrome(ListNode.from_list(test_input))
        result2 = solution.is_palindrome_reverse_half(ListNode.from_list(test_input))
        result3 = solution.is_palindrome_stack(ListNode.from_list(test_input))
        result4 = solution.is_palindrome_recursive(ListNode.from_list(test_input))
        result5 = solution.is_palindrome_two_pointers(ListNode.from_list(test_input))
        
        assert result1 == expected, f"List conversion failed for {test_input}: {result1} vs {expected}"
        assert result2 == expected, f"Reverse half failed for {test_input}: {result2} vs {expected}"
        assert result3 == expected, f"Stack failed for {test_input}: {result3} vs {expected}"
        assert result4 == expected, f"Recursive failed for {test_input}: {result4} vs {expected}"
        assert result5 == expected, f"Two pointers failed for {test_input}: {result5} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 11: Long palindrome
    print("\nTest 11: Long palindrome")
    head11 = ListNode.from_list([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    expected11 = True
    result11 = solution.is_palindrome(head11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Long not palindrome
    print("Test 12: Long not palindrome")
    head12 = ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected12 = False
    result12 = solution.is_palindrome(head12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Single different character [1,2,1]
    print("Test 13: Single different character [1,2,1]")
    head13 = ListNode.from_list([1, 2, 1])
    expected13 = True
    result13 = solution.is_palindrome(head13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Zero values [0,0]
    print("Test 14: Zero values [0,0]")
    head14 = ListNode.from_list([0, 0])
    expected14 = True
    result14 = solution.is_palindrome(head14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Mixed values [1,2,3,2,1]
    print("Test 15: Mixed values [1,2,3,2,1]")
    head15 = ListNode.from_list([1, 2, 3, 2, 1])
    expected15 = True
    result15 = solution.is_palindrome(head15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()