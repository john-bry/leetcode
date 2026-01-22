"""
146. LRU Cache
Difficulty: Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
  add the key-value pair to the cache. If the number of keys exceeds the capacity from this 
  operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Notes:
- Key insight: Need O(1) access (hash map) and O(1) insertion/deletion with ordering (doubly linked list).
- LRU = Least Recently Used - evict the item that hasn't been used for the longest time.
- Operations:
  - get(key): Move to front (most recently used)
  - put(key, value): Add/update and move to front, evict from back if at capacity
- Time complexity: O(1) for both get and put operations
- Space complexity: O(capacity) - store at most capacity items
- Alternative approaches:
  - OrderedDict: O(1) time, O(capacity) space - Python's built-in, simplest
  - Doubly Linked List + Hash Map: O(1) time, O(capacity) space - explicit implementation
  - Alternative structure: O(1) time, O(capacity) space - different node organization
- Edge cases: Capacity 1, get non-existent key, put when at capacity, update existing key
"""

from collections import OrderedDict


class LRUCache:
    """
    Approach 1: Using OrderedDict (Current)
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    OrderedDict maintains insertion order and provides O(1) operations.
    Most recently used items are at the end, least recently used at the beginning.
    """
    def __init__(self, capacity: int):
        """Initialize cache with fixed capacity"""
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """Get value and mark as recently used"""
        if key not in self.cache:
            return -1

        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """Add/update key-value pair and mark as recently used"""
        if key in self.cache:
            # Update existing key - move to end
            self.cache.move_to_end(key)

        # Add or update value
        self.cache[key] = value

        # Evict least recently used if over capacity
        if len(self.cache) > self.capacity:
            # Remove from beginning (least recently used)
            self.cache.popitem(last=False)


class LRUCacheDoublyLinkedList:
    """
    Approach 2: Doubly Linked List + Hash Map
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    Explicit implementation using doubly linked list for ordering
    and hash map for O(1) access. More educational but more code.
    """
    class Node:
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node mapping
        
        # Dummy head and tail for easier operations
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: Node) -> None:
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: Node) -> None:
        """Remove node from list"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node: Node) -> None:
        """Move node to head (most recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self) -> Node:
        """Remove and return tail node (least recently used)"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        """Get value and mark as recently used"""
        node = self.cache.get(key)
        
        if not node:
            return -1
        
        # Move to head (most recently used)
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Add/update key-value pair and mark as recently used"""
        node = self.cache.get(key)
        
        if not node:
            # New key
            new_node = self.Node(key, value)
            
            # Add to cache and list
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Evict if over capacity
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update existing key
            node.value = value
            self._move_to_head(node)


class LRUCacheAlternative:
    """
    Approach 3: Alternative OrderedDict Implementation
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    Same as Approach 1 but with more explicit comments and structure.
    """
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end to mark as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        # If key exists, update and move to end
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new key
            self.cache[key] = value
            # Evict least recently used if at capacity
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)  # Remove oldest (first) item


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    cache1 = LRUCache(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    assert cache1.get(1) == 1, "Test 1a failed"
    cache1.put(3, 3)  # evicts key 2
    assert cache1.get(2) == -1, "Test 1b failed"
    cache1.put(4, 4)  # evicts key 1
    assert cache1.get(1) == -1, "Test 1c failed"
    assert cache1.get(3) == 3, "Test 1d failed"
    assert cache1.get(4) == 4, "Test 1e failed"
    print("  Result: All operations correct ✓")
    
    # Test case 2: Capacity 1
    print("Test 2: Capacity 1")
    cache2 = LRUCache(1)
    cache2.put(1, 1)
    assert cache2.get(1) == 1, "Test 2a failed"
    cache2.put(2, 2)  # evicts key 1
    assert cache2.get(1) == -1, "Test 2b failed"
    assert cache2.get(2) == 2, "Test 2c failed"
    print("  Result: All operations correct ✓")
    
    # Test case 3: Get non-existent key
    print("Test 3: Get non-existent key")
    cache3 = LRUCache(2)
    assert cache3.get(1) == -1, "Test 3 failed"
    print("  Result: Returns -1 ✓")
    
    # Test case 4: Update existing key
    print("Test 4: Update existing key")
    cache4 = LRUCache(2)
    cache4.put(1, 1)
    cache4.put(2, 2)
    cache4.put(1, 10)  # Update key 1
    assert cache4.get(1) == 10, "Test 4 failed"
    print("  Result: Update works correctly ✓")
    
    # Test case 5: Multiple evictions
    print("Test 5: Multiple evictions")
    cache5 = LRUCache(3)
    cache5.put(1, 1)
    cache5.put(2, 2)
    cache5.put(3, 3)
    cache5.put(4, 4)  # evicts key 1
    assert cache5.get(1) == -1, "Test 5a failed"
    assert cache5.get(4) == 4, "Test 5b failed"
    cache5.put(5, 5)  # evicts key 2
    assert cache5.get(2) == -1, "Test 5c failed"
    print("  Result: Multiple evictions work correctly ✓")
    
    # Test case 6: Get operations update LRU order
    print("Test 6: Get operations update LRU order")
    cache6 = LRUCache(2)
    cache6.put(1, 1)
    cache6.put(2, 2)
    cache6.get(1)  # Make 1 most recently used
    cache6.put(3, 3)  # Should evict 2, not 1
    assert cache6.get(1) == 1, "Test 6a failed"
    assert cache6.get(2) == -1, "Test 6b failed"
    assert cache6.get(3) == 3, "Test 6c failed"
    print("  Result: Get updates LRU order correctly ✓")
    
    # Test case 7: Compare all approaches
    print("\nTest 7: Comparing all approaches")
    operations = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1, None),
        ("put", 3, 3),
        ("get", 2, None),
        ("put", 4, 4),
        ("get", 1, None),
        ("get", 3, None),
        ("get", 4, None),
    ]
    
    cache_ordered = LRUCache(2)
    cache_dll = LRUCacheDoublyLinkedList(2)
    cache_alt = LRUCacheAlternative(2)
    
    for op, key, value in operations:
        if op == "get":
            result1 = cache_ordered.get(key)
            result2 = cache_dll.get(key)
            result3 = cache_alt.get(key)
            assert result1 == result2 == result3, f"Mismatch for get({key}): {result1} vs {result2} vs {result3}"
        else:
            cache_ordered.put(key, value)
            cache_dll.put(key, value)
            cache_alt.put(key, value)
    
    print("  All approaches match! ✓")
    
    # Test case 8: Large capacity
    print("\nTest 8: Large capacity")
    cache8 = LRUCache(100)
    for i in range(100):
        cache8.put(i, i)
    assert cache8.get(0) == 0, "Test 8a failed"
    cache8.put(100, 100)  # Should evict key 1 (least recently used after 0)
    assert cache8.get(1) == -1, "Test 8b failed"
    assert cache8.get(100) == 100, "Test 8c failed"
    print("  Result: Large capacity works correctly ✓")
    
    # Test case 9: Sequential gets
    print("Test 9: Sequential gets")
    cache9 = LRUCache(3)
    cache9.put(1, 1)
    cache9.put(2, 2)
    cache9.put(3, 3)
    cache9.get(1)
    cache9.get(2)
    cache9.get(3)
    cache9.put(4, 4)  # Should evict key 1 (least recently used)
    assert cache9.get(1) == -1, "Test 9 failed"
    print("  Result: Sequential gets work correctly ✓")
    
    # Test case 10: Zero values
    print("Test 10: Zero values")
    cache10 = LRUCache(2)
    cache10.put(0, 0)
    cache10.put(1, 0)
    assert cache10.get(0) == 0, "Test 10a failed"
    assert cache10.get(1) == 0, "Test 10b failed"
    print("  Result: Zero values work correctly ✓")
    
    # Test case 11: Negative keys (if allowed)
    print("Test 11: Edge case - same key multiple times")
    cache11 = LRUCache(2)
    cache11.put(1, 1)
    cache11.put(1, 2)
    cache11.put(1, 3)
    assert cache11.get(1) == 3, "Test 11 failed"
    print("  Result: Multiple puts of same key work correctly ✓")
    
    # Test case 12: Complex sequence
    print("Test 12: Complex sequence")
    cache12 = LRUCache(3)
    cache12.put(1, 1)
    cache12.put(2, 2)
    cache12.put(3, 3)
    cache12.get(2)
    cache12.put(4, 4)  # evicts 1 (least recently used)
    assert cache12.get(1) == -1, "Test 12a failed"
    cache12.get(3)
    cache12.put(5, 5)  # evicts 4 (least recently used)
    assert cache12.get(4) == -1, "Test 12b failed"
    assert cache12.get(2) == 2, "Test 12c failed"
    print("  Result: Complex sequence works correctly ✓")
    
    # Test case 13: Get after eviction
    print("Test 13: Get after eviction")
    cache13 = LRUCache(2)
    cache13.put(1, 1)
    cache13.put(2, 2)
    cache13.put(3, 3)  # evicts 1
    assert cache13.get(1) == -1, "Test 13 failed"
    print("  Result: Get after eviction returns -1 ✓")
    
    # Test case 14: All operations on same key
    print("Test 14: All operations on same key")
    cache14 = LRUCache(2)
    cache14.put(1, 1)
    cache14.get(1)
    cache14.put(1, 2)
    cache14.get(1)
    cache14.put(2, 2)
    cache14.put(3, 3)  # Should evict 2, not 1
    assert cache14.get(1) == 2, "Test 14 failed"
    print("  Result: Same key operations work correctly ✓")
    
    # Test case 15: Capacity equals number of operations
    print("Test 15: Capacity equals number of operations")
    cache15 = LRUCache(5)
    for i in range(5):
        cache15.put(i, i)
    for i in range(5):
        assert cache15.get(i) == i, f"Test 15 failed for key {i}"
    print("  Result: All keys accessible ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()