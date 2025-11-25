"""
21. Merge Two Sorted Lists
Difficulty: Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together 
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

Notes:
- Key insight: Compare nodes from both lists and link the smaller one.
- Use a dummy node to simplify edge cases (empty lists, starting point).
- After the loop, attach remaining nodes from the non-empty list.
- Time complexity: O(n + m) where n and m are lengths of the two lists
- Space complexity: O(1) for iterative, O(n + m) for recursive (call stack)
- Alternative approaches:
  - Iterative with dummy node: O(n + m) time, O(1) space (current)
  - Recursive: O(n + m) time, O(n + m) space - more elegant but uses stack
  - In-place iterative: O(n + m) time, O(1) space - without dummy node
  - Alternative iterative: O(n + m) time, O(1) space - different structure
- Edge cases: Empty lists, one empty list, all elements from one list
"""

import os
import sys
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import ListNode


class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Iterative with Dummy Node (Current)
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        
        Use a dummy node to simplify the merging process.
        Compare nodes from both lists and link the smaller one.
        """
        tail = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2

        return head.next
    
    def merge_two_lists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2: Recursive
        Time Complexity: O(n + m)
        Space Complexity: O(n + m) for recursion stack
        
        Recursively merge the lists by choosing the smaller head and
        recursively merging the rest.
        """
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Choose the smaller head and recursively merge the rest
        if list1.val <= list2.val:
            list1.next = self.merge_two_lists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists_recursive(list1, list2.next)
            return list2
    
    def merge_two_lists_inplace(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 3: In-place Iterative (No Dummy Node)
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        
        Merge without using a dummy node by handling the first node separately.
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Determine the head
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        current = head
        
        # Merge the rest
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        current.next = list1 or list2
        
        return head
    
    def merge_two_lists_alternative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 4: Alternative Iterative Structure
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        
        Similar to approach 1 but with a slightly different structure.
        """
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next
    
    def merge_two_lists_while_loop(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 5: While Loop with Explicit Conditions
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        
        More explicit version that handles each case separately.
        """
        dummy = ListNode(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Attach remaining nodes
        while list1 is not None:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        
        while list2 is not None:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        
        return dummy.next


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
    
    # Test case 1: Basic example
    print("Test 1: Basic example [1,2,4] and [1,3,4]")
    list1_1 = ListNode.from_list([1, 2, 4])
    list2_1 = ListNode.from_list([1, 3, 4])
    expected1 = [1, 1, 2, 3, 4, 4]
    result1 = solution.merge_two_lists(list1_1, list2_1)
    result_array1 = list_to_array(result1)
    assert result_array1 == expected1, f"Test 1 failed: expected {expected1}, got {result_array1}"
    print(f"  Result: {result_array1} ✓")
    
    # Test case 2: Both empty
    print("Test 2: Both empty [] and []")
    list1_2 = None
    list2_2 = None
    expected2 = []
    result2 = solution.merge_two_lists(list1_2, list2_2)
    result_array2 = list_to_array(result2) if result2 else []
    assert result_array2 == expected2, f"Test 2 failed: expected {expected2}, got {result_array2}"
    print(f"  Result: {result_array2} ✓")
    
    # Test case 3: One empty
    print("Test 3: One empty [] and [0]")
    list1_3 = None
    list2_3 = ListNode.from_list([0])
    expected3 = [0]
    result3 = solution.merge_two_lists(list1_3, list2_3)
    result_array3 = list_to_array(result3)
    assert result_array3 == expected3, f"Test 3 failed: expected {expected3}, got {result_array3}"
    print(f"  Result: {result_array3} ✓")
    
    # Test case 4: Single nodes
    print("Test 4: Single nodes [1] and [2]")
    list1_4 = ListNode.from_list([1])
    list2_4 = ListNode.from_list([2])
    expected4 = [1, 2]
    result4 = solution.merge_two_lists(list1_4, list2_4)
    result_array4 = list_to_array(result4)
    assert result_array4 == expected4, f"Test 4 failed: expected {expected4}, got {result_array4}"
    print(f"  Result: {result_array4} ✓")
    
    # Test case 5: All from list1
    print("Test 5: All from list1 [1,2,3] and []")
    list1_5 = ListNode.from_list([1, 2, 3])
    list2_5 = None
    expected5 = [1, 2, 3]
    result5 = solution.merge_two_lists(list1_5, list2_5)
    result_array5 = list_to_array(result5)
    assert result_array5 == expected5, f"Test 5 failed: expected {expected5}, got {result_array5}"
    print(f"  Result: {result_array5} ✓")
    
    # Test case 6: All from list2
    print("Test 6: All from list2 [] and [1,2,3]")
    list1_6 = None
    list2_6 = ListNode.from_list([1, 2, 3])
    expected6 = [1, 2, 3]
    result6 = solution.merge_two_lists(list1_6, list2_6)
    result_array6 = list_to_array(result6)
    assert result_array6 == expected6, f"Test 6 failed: expected {expected6}, got {result_array6}"
    print(f"  Result: {result_array6} ✓")
    
    # Test case 7: Different lengths
    print("Test 7: Different lengths [1,3,5] and [2,4]")
    list1_7 = ListNode.from_list([1, 3, 5])
    list2_7 = ListNode.from_list([2, 4])
    expected7 = [1, 2, 3, 4, 5]
    result7 = solution.merge_two_lists(list1_7, list2_7)
    result_array7 = list_to_array(result7)
    assert result_array7 == expected7, f"Test 7 failed: expected {expected7}, got {result_array7}"
    print(f"  Result: {result_array7} ✓")
    
    # Test case 8: Duplicate values
    print("Test 8: Duplicate values [1,1,2] and [1,2,2]")
    list1_8 = ListNode.from_list([1, 1, 2])
    list2_8 = ListNode.from_list([1, 2, 2])
    expected8 = [1, 1, 1, 2, 2, 2]
    result8 = solution.merge_two_lists(list1_8, list2_8)
    result_array8 = list_to_array(result8)
    assert result_array8 == expected8, f"Test 8 failed: expected {expected8}, got {result_array8}"
    print(f"  Result: {result_array8} ✓")
    
    # Test case 9: Negative values
    print("Test 9: Negative values [-1,0,1] and [-2,-1,2]")
    list1_9 = ListNode.from_list([-1, 0, 1])
    list2_9 = ListNode.from_list([-2, -1, 2])
    expected9 = [-2, -1, -1, 0, 1, 2]
    result9 = solution.merge_two_lists(list1_9, list2_9)
    result_array9 = list_to_array(result9)
    assert result_array9 == expected9, f"Test 9 failed: expected {expected9}, got {result_array9}"
    print(f"  Result: {result_array9} ✓")
    
    # Test case 10: Compare all approaches
    print("\nTest 10: Comparing all approaches")
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([1, 2, 3], []),
        ([], [1, 2, 3]),
        ([1], [2]),
        ([1, 3, 5], [2, 4]),
        ([1, 1, 2], [1, 2, 2]),
    ]
    
    for list1_vals, list2_vals in test_cases:
        list1 = ListNode.from_list(list1_vals)
        list2 = ListNode.from_list(list2_vals)
        expected = sorted(list1_vals + list2_vals)
        
        result1 = list_to_array(solution.merge_two_lists(ListNode.from_list(list1_vals), ListNode.from_list(list2_vals)))
        result2 = list_to_array(solution.merge_two_lists_recursive(ListNode.from_list(list1_vals), ListNode.from_list(list2_vals)))
        result3 = list_to_array(solution.merge_two_lists_inplace(ListNode.from_list(list1_vals), ListNode.from_list(list2_vals)))
        result4 = list_to_array(solution.merge_two_lists_alternative(ListNode.from_list(list1_vals), ListNode.from_list(list2_vals)))
        result5 = list_to_array(solution.merge_two_lists_while_loop(ListNode.from_list(list1_vals), ListNode.from_list(list2_vals)))
        
        assert result1 == expected, f"Iterative failed for {list1_vals} and {list2_vals}: {result1} vs {expected}"
        assert result2 == expected, f"Recursive failed for {list1_vals} and {list2_vals}: {result2} vs {expected}"
        assert result3 == expected, f"In-place failed for {list1_vals} and {list2_vals}: {result3} vs {expected}"
        assert result4 == expected, f"Alternative failed for {list1_vals} and {list2_vals}: {result4} vs {expected}"
        assert result5 == expected, f"While loop failed for {list1_vals} and {list2_vals}: {result5} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 11: Large lists
    print("\nTest 11: Large lists")
    list1_11 = ListNode.from_list(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
    list2_11 = ListNode.from_list(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
    expected11 = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result11 = solution.merge_two_lists(list1_11, list2_11)
    result_array11 = list_to_array(result11)
    assert result_array11 == expected11, f"Test 11 failed: expected {expected11}, got {result_array11}"
    print(f"  Result: {result_array11} ✓")
    
    # Test case 12: One much longer
    print("Test 12: One much longer [1] and [2,3,4,5,6]")
    list1_12 = ListNode.from_list([1])
    list2_12 = ListNode.from_list([2, 3, 4, 5, 6])
    expected12 = [1, 2, 3, 4, 5, 6]
    result12 = solution.merge_two_lists(list1_12, list2_12)
    result_array12 = list_to_array(result12)
    assert result_array12 == expected12, f"Test 12 failed: expected {expected12}, got {result_array12}"
    print(f"  Result: {result_array12} ✓")
    
    # Test case 13: All same values
    print("Test 13: All same values [5,5,5] and [5,5]")
    list1_13 = ListNode.from_list([5, 5, 5])
    list2_13 = ListNode.from_list([5, 5])
    expected13 = [5, 5, 5, 5, 5]
    result13 = solution.merge_two_lists(list1_13, list2_13)
    result_array13 = list_to_array(result13)
    assert result_array13 == expected13, f"Test 13 failed: expected {expected13}, got {result_array13}"
    print(f"  Result: {result_array13} ✓")
    
    # Test case 14: Non-overlapping ranges
    print("Test 14: Non-overlapping ranges [1,2,3] and [4,5,6]")
    list1_14 = ListNode.from_list([1, 2, 3])
    list2_14 = ListNode.from_list([4, 5, 6])
    expected14 = [1, 2, 3, 4, 5, 6]
    result14 = solution.merge_two_lists(list1_14, list2_14)
    result_array14 = list_to_array(result14)
    assert result_array14 == expected14, f"Test 14 failed: expected {expected14}, got {result_array14}"
    print(f"  Result: {result_array14} ✓")
    
    # Test case 15: Zero values
    print("Test 15: Zero values [0,0,0] and [0,1]")
    list1_15 = ListNode.from_list([0, 0, 0])
    list2_15 = ListNode.from_list([0, 1])
    expected15 = [0, 0, 0, 0, 1]
    result15 = solution.merge_two_lists(list1_15, list2_15)
    result_array15 = list_to_array(result15)
    assert result_array15 == expected15, f"Test 15 failed: expected {expected15}, got {result_array15}"
    print(f"  Result: {result_array15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()