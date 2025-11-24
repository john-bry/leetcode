# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def delete_node(self, node):
        """
        Approach 1: Copy Next Node's Value
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Copy the value of the next node to the current node and delete the next node.
        This effectively removes the current node from the list.
        """
        node.val = node.next.val
        node.next = node.next.next