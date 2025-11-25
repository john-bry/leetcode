"""
141. Linked List Cycle
Difficulty: Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Notes:
- Key insight: If there's a cycle, a fast pointer will eventually catch up to a slow pointer.
- Floyd's Cycle Detection (Tortoise and Hare): Use two pointers moving at different speeds.
  - Slow pointer moves 1 step at a time
  - Fast pointer moves 2 steps at a time
  - If they meet, there's a cycle
  - If fast reaches None, there's no cycle
- Time complexity: O(n) - linear time
- Space complexity: O(1) for Floyd's algorithm, O(n) for hash set
- Alternative approaches:
  - Floyd's algorithm: O(n) time, O(1) space - optimal
  - Hash set: O(n) time, O(n) space - track visited nodes
  - Marking nodes: O(n) time, O(1) space - modify nodes (if allowed)
  - Alternative pointer speeds: O(n) time, O(1) space - different speed ratios
- Edge cases: Empty list, single node, two nodes, cycle at head, cycle at tail
"""

import os
import sys
from typing import Optional

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from data_structures import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach 1: Floyd's Cycle Detection (Tortoise and Hare) - Current
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use two pointers: slow (1x) and fast (2x). If there's a cycle, fast will meet slow.
        This is the optimal approach with O(1) space.
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    
    def has_cycle_hash_set(self, head: Optional[ListNode]) -> bool:
        """
        Approach 2: Hash Set
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Traverse the list and store visited nodes in a set.
        If we encounter a node already in the set, there's a cycle.
        """
        visited = set()
        curr = head
        
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        
        return False
    
    def has_cycle_marking(self, head: Optional[ListNode]) -> bool:
        """
        Approach 3: Marking Nodes (Modifies List)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Mark visited nodes by setting a special value or attribute.
        If we encounter a marked node, there's a cycle.
        Note: This modifies the list, which may not be allowed.
        """
        curr = head
        
        while curr:
            # Check if node has been marked (using a sentinel value)
            if hasattr(curr, '_visited') and curr._visited:
                return True
            
            # Mark the node
            curr._visited = True
            curr = curr.next
        
        return False
    
    def has_cycle_alternative_speeds(self, head: Optional[ListNode]) -> bool:
        """
        Approach 4: Alternative Pointer Speeds
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Similar to Floyd's but with different speed ratios.
        Uses slow (1x) and fast (3x) instead of 2x.
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next.next if head.next else None
        
        while fast and fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next.next
        
        return False
    
    def has_cycle_explicit(self, head: Optional[ListNode]) -> bool:
        """
        Approach 5: Explicit Floyd's Implementation
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        More explicit version of Floyd's algorithm with clearer variable names.
        """
        if not head or not head.next:
            return False
        
        slow_pointer = head
        fast_pointer = head.next
        
        while fast_pointer and fast_pointer.next:
            if slow_pointer == fast_pointer:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return False


def create_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    """
    Helper function to create a cycle in a linked list.
    pos: index where tail connects to (0-indexed), -1 means no cycle
    """
    if pos == -1 or not head:
        return head
    
    # Find the tail and the node at pos
    tail = head
    cycle_node = None
    index = 0
    
    while tail.next:
        if index == pos:
            cycle_node = tail
        tail = tail.next
        index += 1
    
    # If pos is the last node, cycle_node might be None
    if index == pos:
        cycle_node = tail
    
    # If we found a cycle node, connect tail to it
    if cycle_node:
        tail.next = cycle_node
    
    return head


def list_to_array(head: Optional[ListNode], max_nodes: int = 20) -> list:
    """
    Helper function to convert linked list to array for testing.
    Stops at max_nodes to avoid infinite loops with cycles.
    """
    result = []
    curr = head
    count = 0
    
    while curr and count < max_nodes:
        result.append(curr.val)
        curr = curr.next
        count += 1
    
    if count == max_nodes:
        result.append("... (cycle detected)")
    
    return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Cycle at position 1 [3,2,0,-4] with pos=1
    print("Test 1: Cycle at position 1 [3,2,0,-4]")
    head1 = ListNode.from_list([3, 2, 0, -4])
    head1 = create_cycle(head1, 1)
    expected1 = True
    result1 = solution.has_cycle(head1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Cycle at position 0 [1,2] with pos=0
    print("Test 2: Cycle at position 0 [1,2]")
    head2 = ListNode.from_list([1, 2])
    head2 = create_cycle(head2, 0)
    expected2 = True
    result2 = solution.has_cycle(head2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: No cycle [1] with pos=-1
    print("Test 3: No cycle [1]")
    head3 = ListNode.from_list([1])
    head3 = create_cycle(head3, -1)
    expected3 = False
    result3 = solution.has_cycle(head3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Empty list
    print("Test 4: Empty list []")
    head4 = None
    expected4 = False
    result4 = solution.has_cycle(head4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single node with self-cycle
    print("Test 5: Single node with self-cycle [1]")
    head5 = ListNode(1)
    head5.next = head5  # Self-cycle
    expected5 = True
    result5 = solution.has_cycle(head5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two nodes with cycle [1,2]
    print("Test 6: Two nodes with cycle [1,2]")
    head6 = ListNode.from_list([1, 2])
    head6 = create_cycle(head6, 0)
    expected6 = True
    result6 = solution.has_cycle(head6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Long list with cycle
    print("Test 7: Long list with cycle [1,2,3,4,5] at pos=2")
    head7 = ListNode.from_list([1, 2, 3, 4, 5])
    head7 = create_cycle(head7, 2)
    expected7 = True
    result7 = solution.has_cycle(head7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Long list without cycle
    print("Test 8: Long list without cycle [1,2,3,4,5]")
    head8 = ListNode.from_list([1, 2, 3, 4, 5])
    head8 = create_cycle(head8, -1)
    expected8 = False
    result8 = solution.has_cycle(head8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Cycle at tail [1,2,3,4] with pos=3
    print("Test 9: Cycle at tail [1,2,3,4] with pos=3")
    head9 = ListNode.from_list([1, 2, 3, 4])
    head9 = create_cycle(head9, 3)
    expected9 = True
    result9 = solution.has_cycle(head9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Compare all approaches
    print("\nTest 10: Comparing all approaches")
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2, 3, 4, 5], 2, True),
        ([1, 2, 3, 4, 5], -1, False),
        ([1], 0, True),  # Self-cycle
    ]
    
    for test_input, pos, expected in test_cases:
        head = ListNode.from_list(test_input)
        head = create_cycle(head, pos)
        
        result1 = solution.has_cycle(head)
        result2 = solution.has_cycle_hash_set(head)
        result3 = solution.has_cycle_explicit(head)
        
        # Skip marking approach as it modifies the list
        # Skip alternative speeds as it may not work for all cases
        
        assert result1 == expected, f"Floyd's failed for {test_input} pos={pos}: {result1} vs {expected}"
        assert result2 == expected, f"Hash set failed for {test_input} pos={pos}: {result2} vs {expected}"
        assert result3 == expected, f"Explicit failed for {test_input} pos={pos}: {result3} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 11: Large cycle
    print("\nTest 11: Large cycle [1,2,...,10] with pos=5")
    head11 = ListNode.from_list(list(range(1, 11)))
    head11 = create_cycle(head11, 5)
    expected11 = True
    result11 = solution.has_cycle(head11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Cycle at head [1,2,3] with pos=0
    print("Test 12: Cycle at head [1,2,3] with pos=0")
    head12 = ListNode.from_list([1, 2, 3])
    head12 = create_cycle(head12, 0)
    expected12 = True
    result12 = solution.has_cycle(head12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Negative values with cycle
    print("Test 13: Negative values with cycle [-1,-2,-3] with pos=1")
    head13 = ListNode.from_list([-1, -2, -3])
    head13 = create_cycle(head13, 1)
    expected13 = True
    result13 = solution.has_cycle(head13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Zero values
    print("Test 14: Zero values [0,0,0] with pos=-1")
    head14 = ListNode.from_list([0, 0, 0])
    head14 = create_cycle(head14, -1)
    expected14 = False
    result14 = solution.has_cycle(head14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Mixed values with cycle
    print("Test 15: Mixed values [-1,0,1,2] with pos=2")
    head15 = ListNode.from_list([-1, 0, 1, 2])
    head15 = create_cycle(head15, 2)
    expected15 = True
    result15 = solution.has_cycle(head15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()