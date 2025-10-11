"""
Common data structures for LeetCode problems
"""

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"
    
    def to_list(self):
        """Convert linked list to Python list for debugging."""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    @classmethod
    def from_list(cls, values):
        """Create linked list from Python list."""
        if not values:
            return None
        
        head = cls(values[0])
        current = head
        for val in values[1:]:
            current.next = cls(val)
            current = current.next
        return head


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
    
    def to_list(self):
        """Convert binary tree to list representation (level order)."""
        if not self:
            return []
        
        result = []
        queue = [self]
        
        while queue:
            node = queue.pop(0)
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
    
    @classmethod
    def from_list(cls, values):
        """Create binary tree from list representation."""
        if not values or values[0] is None:
            return None
        
        root = cls(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = cls(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = cls(values[i])
                queue.append(node.right)
            i += 1
        
        return root


class Node:
    """Definition for a node with children (N-ary tree)."""
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class TrieNode:
    """Trie node for prefix tree implementation."""
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
