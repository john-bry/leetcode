
"""
LeetCode 19: Remove Nth Node From End of List

Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Algorithm:
1. Use two pointers (fast and slow) with a dummy node
2. Move fast pointer n steps ahead of slow pointer
3. Move both pointers until fast reaches the end
4. Remove the nth node by updating slow.next to skip it
5. Return the actual head (dummy.next)

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only using constant extra space

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
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list.
        
        Args:
            head: The head of the linked list
            n: The position from the end to remove (1-indexed)
            
        Returns:
            The head of the modified linked list
        """
        # Assign a "dummy" node and prepend it to the list 
        # to handle the edge case where nth node is head
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Move fast n steps ahead of slow
        for i in range(n):
            fast = fast.next
            
        # Move fast to next to end of list, slow to nth - 1
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Skip/remove nth node
        slow.next = slow.next.next
        
        # Return actual head 
        return dummy.next


def create_test_cases():
    """Create comprehensive test cases for the remove nth node problem."""
    return [
        {
            "name": "Example 1: Remove 2nd from end",
            "input": [1, 2, 3, 4, 5],
            "n": 2,
            "expected": [1, 2, 3, 5]
        },
        {
            "name": "Example 2: Single node",
            "input": [1],
            "n": 1,
            "expected": []
        },
        {
            "name": "Example 3: Two nodes, remove last",
            "input": [1, 2],
            "n": 1,
            "expected": [1]
        },
        {
            "name": "Remove first node",
            "input": [1, 2, 3, 4, 5],
            "n": 5,
            "expected": [2, 3, 4, 5]
        },
        {
            "name": "Remove last node",
            "input": [1, 2, 3, 4, 5],
            "n": 1,
            "expected": [1, 2, 3, 4]
        },
        {
            "name": "Remove middle node",
            "input": [1, 2, 3, 4, 5],
            "n": 3,
            "expected": [1, 2, 4, 5]
        },
        {
            "name": "Longer list",
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6, 7, 9, 10]
        },
        {
            "name": "All same values",
            "input": [1, 1, 1, 1],
            "n": 2,
            "expected": [1, 1, 1]
        }
    ]


def run_test_case(test_case, solution):
    """Run a single test case and return the result."""
    # Create linked list from input
    head = ListNode.from_list(test_case["input"])
    
    # Print original list
    print(f"\nTest: {test_case['name']}")
    print(f"Input: {test_case['input']}, n = {test_case['n']}")
    print("Original list: ", end="")
    print_linked_list(head)
    
    # Apply the solution
    result_head = solution.remove_nth_from_end(head, test_case["n"])
    
    # Convert result back to list
    result = result_head.to_list() if result_head else []
    
    # Print result
    print("Modified list: ", end="")
    print_linked_list(result_head)
    print(f"Result: {result}")
    print(f"Expected: {test_case['expected']}")
    
    # Check if result matches expected
    passed = result == test_case["expected"]
    print(f"Status: {'✅ PASSED' if passed else '❌ FAILED'}")
    
    return passed


def run_all_tests():
    """Run all test cases and report results."""
    print("=" * 60)
    print("LeetCode 19: Remove Nth Node From End of List - Test Suite")
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
    n = 2  # Remove 2nd from end (value 4)
    print(f"Original list: ", end="")
    print_linked_list(head)
    print(f"Removing {n}th node from end")
    
    # Step 1: Create dummy node
    dummy = ListNode(0)
    dummy.next = head
    print(f"\nStep 1: Create dummy node")
    print("List with dummy: ", end="")
    print_linked_list(dummy)
    
    # Step 2: Initialize pointers
    fast = slow = dummy
    print(f"\nStep 2: Initialize fast and slow pointers at dummy")
    
    # Step 3: Move fast n steps ahead
    print(f"\nStep 3: Move fast pointer {n} steps ahead")
    for i in range(n):
        fast = fast.next
        print(f"  Fast moved to: {fast.val}")
    
    print(f"Current positions:")
    print(f"  Slow at: {slow.val}")
    print(f"  Fast at: {fast.val}")
    
    # Step 4: Move both pointers until fast reaches end
    print(f"\nStep 4: Move both pointers until fast reaches end")
    step = 1
    while fast.next:
        slow = slow.next
        fast = fast.next
        print(f"  Step {step}: Slow at {slow.val}, Fast at {fast.val}")
        step += 1
    
    print(f"\nFinal positions:")
    print(f"  Slow at: {slow.val} (points to node before target)")
    print(f"  Fast at: {fast.val} (at end)")
    
    # Step 5: Remove the nth node
    print(f"\nStep 5: Remove nth node by skipping it")
    target_node = slow.next
    print(f"  Target node to remove: {target_node.val}")
    slow.next = slow.next.next
    print(f"  After removal: ", end="")
    print_linked_list(dummy.next)


if __name__ == "__main__":
    # Run all tests
    all_passed = run_all_tests()
    
    # Demonstrate the algorithm
    demonstrate_algorithm()
    
    # Exit with appropriate code
    exit(0 if all_passed else 1)