"""
460. LFU Cache
Difficulty: Hard

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or insert the key if not already present. 
  When the cache reaches its capacity, it should invalidate and remove the least frequently used key before 
  inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), 
  the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with 
the smallest use counter is the least frequently used. When a key is first inserted into the cache, its use 
counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either 
a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3, cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4, cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:
- 1 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to get and put.

Notes:
- Key insight: Need to track both frequency (for LFU) and recency (for tie-breaking).
- LFU = Least Frequently Used - evict the item with the lowest access frequency.
- When frequencies are equal, evict the least recently used (LRU) among them.
- Data structures:
  - cache: {key: value} - stores key-value pairs
  - count: {key: frequency} - tracks access frequency for each key
  - freq_to_keys: {frequency: OrderedDict{key: None}} - groups keys by frequency, maintains LRU order within each frequency
  - min_freq: tracks the minimum frequency for O(1) eviction
- Operations:
  - get(key): Increment frequency, move to higher frequency bucket
  - put(key, value): Update frequency if exists, else add with freq=1, evict from min_freq if at capacity
- Time complexity: O(1) for both get and put operations
- Space complexity: O(capacity) - store at most capacity items
- Edge cases: Capacity 0, capacity 1, get non-existent key, update existing key, tie-breaking on same frequency
"""

from collections import OrderedDict, defaultdict


class LFUCache:
    """
    Approach 1: Using defaultdict(OrderedDict) (Current)
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    Uses a frequency-to-keys mapping where each frequency level maintains an OrderedDict
    for LRU ordering within that frequency level. This allows O(1) access to the minimum
    frequency and O(1) eviction of the least recently used key at that frequency.
    """
    def __init__(self, capacity: int):
        """Initialize cache with fixed capacity"""
        self.cache = {}  # {key: value}
        self.count = {}  # {key: frequency}
        self.freq_to_keys = defaultdict(OrderedDict)  # {frequency: OrderedDict{key: None}}
        self.capacity = capacity
        self.min_freq = 0  # Track minimum frequency for O(1) eviction

    def _update_freq(self, key):
        """
        Update frequency of a key:
        1. Remove from current frequency bucket
        2. Increment frequency
        3. Add to new frequency bucket
        4. Update min_freq if necessary
        """
        freq = self.count[key]
        self.count[key] += 1

        # Remove from current frequency bucket
        del self.freq_to_keys[freq][key]
        
        # If this frequency bucket is now empty, clean it up
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            # If this was the minimum frequency, increment min_freq
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Add to new frequency bucket (at the end for LRU ordering)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        """
        Get value and increment frequency.
        Returns -1 if key doesn't exist.
        """
        if key not in self.cache:
            return -1

        self._update_freq(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Add/update key-value pair.
        If key exists, update value and frequency.
        If key doesn't exist and at capacity, evict LFU key (LRU if tie).
        New keys start with frequency 1.
        """
        if self.capacity == 0:
            return

        # Update existing key
        if key in self.cache:
            self.cache[key] = value
            self._update_freq(key)
            return

        # Evict if at capacity
        if len(self.cache) >= self.capacity:
            # Evict least recently used key from minimum frequency bucket
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.cache[evict_key]
            del self.count[evict_key]

        # Add new key with frequency 1
        self.cache[key] = value
        self.count[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1  # New keys always have frequency 1


class LFUCacheDoublyLinkedList:
    """
    Approach 2: Using Doubly Linked List for each frequency level
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    Alternative implementation using explicit doubly linked lists instead of OrderedDict.
    More complex but gives explicit control over the data structure.
    """
    class Node:
        def __init__(self, key, value, freq=1):
            self.key = key
            self.value = value
            self.freq = freq
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: Node}
        self.freq_to_dll = defaultdict(self._create_dll)  # {freq: (head, tail)}
        self.min_freq = 0

    def _create_dll(self):
        """Create a dummy head and tail for a doubly linked list"""
        head = self.Node(0, 0)
        tail = self.Node(0, 0)
        head.next = tail
        tail.prev = head
        return (head, tail)

    def _add_node(self, node, head, tail):
        """Add node at the end (most recently used)"""
        node.prev = tail.prev
        node.next = tail
        tail.prev.next = node
        tail.prev = node

    def _remove_node(self, node):
        """Remove node from its current position"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _update_freq(self, node):
        """Move node to higher frequency bucket"""
        # Remove from current frequency bucket
        head, tail = self.freq_to_dll[node.freq]
        self._remove_node(node)
        
        # Clean up empty frequency bucket
        if head.next == tail:
            del self.freq_to_dll[node.freq]
            if self.min_freq == node.freq:
                self.min_freq += 1
        
        # Add to new frequency bucket
        node.freq += 1
        head, tail = self.freq_to_dll[node.freq]
        self._add_node(node, head, tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
            return

        # Evict if at capacity
        if len(self.cache) >= self.capacity:
            head, tail = self.freq_to_dll[self.min_freq]
            lru_node = head.next
            self._remove_node(lru_node)
            del self.cache[lru_node.key]
            
            # Clean up empty frequency bucket
            if head.next == tail:
                del self.freq_to_dll[self.min_freq]

        # Add new node
        node = self.Node(key, value, 1)
        self.cache[key] = node
        head, tail = self.freq_to_dll[1]
        self._add_node(node, head, tail)
        self.min_freq = 1


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    cache1 = LFUCache(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    assert cache1.get(1) == 1, "Test 1a failed"
    cache1.put(3, 3)  # evicts key 2 (freq=1, LRU)
    assert cache1.get(2) == -1, "Test 1b failed"
    assert cache1.get(3) == 3, "Test 1c failed"
    cache1.put(4, 4)  # evicts key 1 (freq=2, but 3 also freq=2, 1 is LRU)
    assert cache1.get(1) == -1, "Test 1d failed"
    assert cache1.get(3) == 3, "Test 1e failed"
    assert cache1.get(4) == 4, "Test 1f failed"
    print("  Result: All operations correct ✓")
    
    # Test case 2: Capacity 1
    print("Test 2: Capacity 1")
    cache2 = LFUCache(1)
    cache2.put(1, 1)
    assert cache2.get(1) == 1, "Test 2a failed"
    cache2.put(2, 2)  # evicts key 1
    assert cache2.get(1) == -1, "Test 2b failed"
    assert cache2.get(2) == 2, "Test 2c failed"
    print("  Result: All operations correct ✓")
    
    # Test case 3: Get non-existent key
    print("Test 3: Get non-existent key")
    cache3 = LFUCache(2)
    assert cache3.get(1) == -1, "Test 3 failed"
    print("  Result: Returns -1 ✓")
    
    # Test case 4: Update existing key
    print("Test 4: Update existing key")
    cache4 = LFUCache(2)
    cache4.put(1, 1)
    cache4.put(2, 2)
    cache4.put(1, 10)  # Update key 1, increases frequency
    assert cache4.get(1) == 10, "Test 4a failed"
    assert cache4.get(1) == 10, "Test 4b failed"  # Frequency now 3
    cache4.put(3, 3)  # Should evict key 2 (freq=1), not key 1 (freq=3)
    assert cache4.get(2) == -1, "Test 4c failed"
    assert cache4.get(1) == 10, "Test 4d failed"
    print("  Result: Update works correctly ✓")
    
    # Test case 5: Capacity 0
    print("Test 5: Capacity 0")
    cache5 = LFUCache(0)
    cache5.put(1, 1)
    assert cache5.get(1) == -1, "Test 5 failed"
    print("  Result: Capacity 0 works correctly ✓")
    
    # Test case 6: Tie-breaking (same frequency, LRU wins)
    print("Test 6: Tie-breaking (same frequency, LRU wins)")
    cache6 = LFUCache(2)
    cache6.put(1, 1)
    cache6.put(2, 2)
    cache6.get(1)  # Both now have freq=2
    cache6.get(2)  # Both now have freq=2
    cache6.put(3, 3)  # Should evict key 1 (LRU among freq=2)
    assert cache6.get(1) == -1, "Test 6a failed"
    assert cache6.get(2) == 2, "Test 6b failed"
    assert cache6.get(3) == 3, "Test 6c failed"
    print("  Result: Tie-breaking works correctly ✓")
    
    # Test case 7: Multiple evictions
    print("Test 7: Multiple evictions")
    cache7 = LFUCache(3)
    cache7.put(1, 1)
    cache7.put(2, 2)
    cache7.put(3, 3)
    cache7.get(1)  # freq=2
    cache7.get(2)  # freq=2
    cache7.put(4, 4)  # evicts key 3 (freq=1)
    assert cache7.get(3) == -1, "Test 7a failed"
    assert cache7.get(4) == 4, "Test 7b failed"  # key 4 now has freq=2
    # After get(4), all keys have freq=2, so LRU is evicted
    cache7.put(5, 5)  # evicts LRU among freq=2 keys (key 1, 2, or 4)
    # Since all have same freq, one of them should be evicted
    evicted_count = sum(1 for k in [1, 2, 4] if cache7.get(k) == -1)
    assert evicted_count == 1, "Test 7c failed: Should evict exactly one key"
    assert cache7.get(5) == 5, "Test 7d failed"
    print("  Result: Multiple evictions work correctly ✓")
    
    # Test case 8: Sequential gets increase frequency
    print("Test 8: Sequential gets increase frequency")
    cache8 = LFUCache(2)
    cache8.put(1, 1)
    cache8.put(2, 2)
    cache8.get(1)  # freq=2
    cache8.get(1)  # freq=3
    cache8.get(1)  # freq=4
    cache8.put(3, 3)  # Should evict key 2 (freq=1), not key 1 (freq=4)
    assert cache8.get(1) == 1, "Test 8a failed"
    assert cache8.get(2) == -1, "Test 8b failed"
    print("  Result: Sequential gets work correctly ✓")
    
    # Test case 9: Complex sequence
    print("Test 9: Complex sequence")
    cache9 = LFUCache(3)
    cache9.put(1, 1)
    cache9.put(2, 2)
    cache9.put(3, 3)
    cache9.get(2)  # freq=2
    cache9.get(3)  # freq=2
    cache9.put(4, 4)  # evicts key 1 (freq=1)
    assert cache9.get(1) == -1, "Test 9a failed"
    cache9.get(3)  # freq=3
    cache9.get(4)  # freq=2 (moves from freq=1 to freq=2, making min_freq=2)
    # After get(4): key 2 and key 4 both have freq=2, key 2 is LRU (moved to freq=2 first)
    cache9.put(5, 5)  # evicts key 2 (freq=2, LRU among keys with freq=2)
    assert cache9.get(2) == -1, "Test 9b failed"
    assert cache9.get(4) == 4, "Test 9c failed"
    assert cache9.get(3) == 3, "Test 9d failed"
    assert cache9.get(5) == 5, "Test 9e failed"
    print("  Result: Complex sequence works correctly ✓")
    
    # Test case 10: Zero values
    print("Test 10: Zero values")
    cache10 = LFUCache(2)
    cache10.put(0, 0)
    cache10.put(1, 0)
    assert cache10.get(0) == 0, "Test 10a failed"
    assert cache10.get(1) == 0, "Test 10b failed"
    print("  Result: Zero values work correctly ✓")
    
    # Test case 11: Same key multiple puts
    print("Test 11: Same key multiple puts")
    cache11 = LFUCache(2)
    cache11.put(1, 1)
    cache11.put(1, 2)
    cache11.put(1, 3)  # Each put increases frequency
    assert cache11.get(1) == 3, "Test 11a failed"
    cache11.put(2, 2)
    cache11.put(3, 3)  # Should evict key 2 (freq=1), not key 1 (freq=4)
    assert cache11.get(1) == 3, "Test 11b failed"
    assert cache11.get(2) == -1, "Test 11c failed"
    print("  Result: Multiple puts of same key work correctly ✓")
    
    # Test case 12: Get after eviction
    print("Test 12: Get after eviction")
    cache12 = LFUCache(2)
    cache12.put(1, 1)
    cache12.put(2, 2)
    cache12.put(3, 3)  # evicts 1 or 2 (whichever is LFU)
    assert cache12.get(1) == -1 or cache12.get(2) == -1, "Test 12 failed"
    print("  Result: Get after eviction returns -1 ✓")
    
    # Test case 13: All operations on same key
    print("Test 13: All operations on same key")
    cache13 = LFUCache(2)
    cache13.put(1, 1)
    cache13.get(1)
    cache13.put(1, 2)
    cache13.get(1)
    cache13.put(2, 2)
    cache13.put(3, 3)  # Should evict key 2 (freq=1), not key 1 (freq=4)
    assert cache13.get(1) == 2, "Test 13 failed"
    print("  Result: Same key operations work correctly ✓")
    
    # Test case 14: Frequency distribution
    print("Test 14: Frequency distribution")
    cache14 = LFUCache(3)
    cache14.put(1, 1)
    cache14.put(2, 2)
    cache14.put(3, 3)
    # Make frequencies: 1->freq=1, 2->freq=3, 3->freq=2
    cache14.get(2)
    cache14.get(2)
    cache14.get(3)
    cache14.put(4, 4)  # Should evict key 1 (freq=1)
    assert cache14.get(1) == -1, "Test 14a failed"
    assert cache14.get(2) == 2, "Test 14b failed"
    assert cache14.get(3) == 3, "Test 14c failed"
    print("  Result: Frequency distribution works correctly ✓")
    
    # Test case 15: Large capacity
    print("Test 15: Large capacity")
    cache15 = LFUCache(100)
    for i in range(100):
        cache15.put(i, i)
    for i in range(100):
        assert cache15.get(i) == i, f"Test 15 failed for key {i}"
    print("  Result: Large capacity works correctly ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()