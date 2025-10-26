"""
LeetCode 143: Reorder List

Problem:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

Algorithm:
1. Find the middle of the linked list using slow and fast pointers
2. Split the list into two halves at the middle
3. Reverse the second half of the list
4. Merge the two halves by alternating nodes from each half

Time Complexity: O(n) - we traverse the list a constant number of times
Space Complexity: O(1) - we only use a constant amount of extra space

Dependencies:
- ListNode from utils.data_structures
- typing.Optional for type hints
"""

import os
import sys
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import ListNode
from helpers import print_linked_list


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Reorder the linked list by alternating nodes from the first half 
        with reversed nodes from the second half.
        
        Args:
            head: The head of the linked list to reorder
            
        Returns:
            None (modifies the list in-place)
        """
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the list using slow and fast pointers
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split the list into two halves at the middle
        second = slow.next
        slow.next = None  # Break the connection

        # Step 3: Reverse the second half
        prev = None
        while second: 
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Step 4: Merge the two halves by alternating nodes
        first, second = head, prev
        while second:
            # Save the next nodes of each list
            first_next = first.next
            second_next = second.next
            
            # Connect first to second, second to first's next
            first.next = second
            second.next = first_next
            
            # Move to the next pair
            first = first_next
            second = second_next


def create_test_cases():
    """Create comprehensive test cases for the reorder list problem."""
    return [
        {
            "name": "Example 1: Even length list",
            "input": [1, 2, 3, 4],
            "expected": [1, 4, 2, 3]
        },
        {
            "name": "Example 2: Odd length list", 
            "input": [1, 2, 3, 4, 5],
            "expected": [1, 5, 2, 4, 3]
        },
        {
            "name": "Single node",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Two nodes",
            "input": [1, 2],
            "expected": [1, 2]
        },
        {
            "name": "Three nodes",
            "input": [1, 2, 3],
            "expected": [1, 3, 2]
        },
        {
            "name": "Longer list",
            "input": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": [1, 8, 2, 7, 3, 6, 4, 5]
        },
        {
            "name": "All same values",
            "input": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1]
        }
    ]


def run_test_case(test_case, solution):
    """Run a single test case and return the result."""
    # Create linked list from input
    head = ListNode.from_list(test_case["input"])
    
    # Print original list
    print(f"\nTest: {test_case['name']}")
    print(f"Input: {test_case['input']}")
    print("Original list: ", end="")
    print_linked_list(head)
    
    # Apply the solution
    solution.reorder_list(head)
    
    # Convert result back to list
    result = head.to_list() if head else []
    
    # Print result
    print("Reordered list: ", end="")
    print_linked_list(head)
    print(f"Result: {result}")
    print(f"Expected: {test_case['expected']}")
    
    # Check if result matches expected
    passed = result == test_case["expected"]
    print(f"Status: {'✅ PASSED' if passed else '❌ FAILED'}")
    
    return passed


def run_all_tests():
    """Run all test cases and report results."""
    print("=" * 60)
    print("LeetCode 143: Reorder List - Test Suite")
    print("=" * 60)
    
    solution = Solution()
    test_cases = create_test_cases()
    
    passed = 0
    total = len(test_cases)
    
    for test_case in test_cases:
        if run_test_case(test_case, solution):
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    print("=" * 60)
    
    return passed == total


def demonstrate_algorithm():
    """Demonstrate the algorithm step by step with a simple example."""
    print("\n" + "=" * 60)
    print("Algorithm Demonstration")
    print("=" * 60)
    
    # Create a simple list for demonstration
    head = ListNode.from_list([1, 2, 3, 4, 5])
    print("Original list: ", end="")
    print_linked_list(head)
    
    # Step 1: Find middle
    fast = slow = head
    print(f"\nStep 1: Finding middle...")
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    print(f"Middle node: {slow.val}")
    
    # Step 2: Split list
    second = slow.next
    slow.next = None
    print(f"First half: ", end="")
    print_linked_list(head)
    print(f"Second half: ", end="")
    print_linked_list(second)
    
    # Step 3: Reverse second half
    prev = None
    current = second
    print(f"\nStep 3: Reversing second half...")
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    print(f"Reversed second half: ", end="")
    print_linked_list(prev)
    
    # Step 4: Merge
    print(f"\nStep 4: Merging halves...")
    first, second = head, prev
    while second:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next
    
    print("Final result: ", end="")
    print_linked_list(head)


if __name__ == "__main__":
    # Run all tests
    all_passed = run_all_tests()
    
    # Demonstrate the algorithm
    demonstrate_algorithm()
    
    # Exit with appropriate code
    exit(0 if all_passed else 1)