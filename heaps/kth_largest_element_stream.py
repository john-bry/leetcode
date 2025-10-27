"""
703. Kth Largest Element in a Stream
Difficulty: Easy

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input: ["KthLargest", "add", "add", "add", "add", "add"]
       [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth element.

Notes:
- Key insight: Use a min heap of size k to maintain the k largest elements.
- The root of the min heap is always the kth largest element.
- When adding new elements, maintain heap size by removing smallest if needed.
- Alternative: Use max heap with size n-k+1, but less efficient for this problem.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Approach 1: Min Heap (Optimal)
        Time Complexity: O(n log k) for initialization, O(log k) for add
        Space Complexity: O(k)
        
        Use a min heap of size k to maintain the k largest elements.
        The root is always the kth largest element.
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Keep only k largest elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        # Maintain heap size of k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # Root is kth largest
        return self.min_heap[0]


class KthLargestMaxHeap:
    def __init__(self, k: int, nums: List[int]):
        """
        Approach 2: Max Heap (Alternative)
        Time Complexity: O(n log n) for initialization, O(log n) for add
        Space Complexity: O(n)
        
        Use a max heap to store all elements, then pop n-k+1 elements to get kth largest.
        Less efficient than min heap approach.
        """
        self.k = k
        self.max_heap = [-x for x in nums]  # Negate for max heap behavior
        heapq.heapify(self.max_heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        
        # Create a temporary list to find kth largest
        temp = []
        for _ in range(self.k):
            if self.max_heap:
                temp.append(-heapq.heappop(self.max_heap))
        
        # The last element in temp is the kth largest
        result = temp[-1]
        
        # Restore the heap
        for num in temp:
            heapq.heappush(self.max_heap, -num)
        
        return result


class KthLargestSorting:
    def __init__(self, k: int, nums: List[int]):
        """
        Approach 3: Sorting (Naive)
        Time Complexity: O(n log n) for initialization, O(n log n) for add
        Space Complexity: O(n)
        
        Sort the array and return the kth largest element.
        Inefficient for frequent add operations.
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        
        # Keep only k largest elements for efficiency
        if len(self.nums) > self.k * 2:  # Arbitrary threshold
            self.nums = self.nums[:self.k * 2]
        
        return self.nums[self.k - 1]


class KthLargestOptimized:
    def __init__(self, k: int, nums: List[int]):
        """
        Approach 4: Optimized Min Heap with Early Termination
        Time Complexity: O(n log k) for initialization, O(log k) for add
        Space Complexity: O(k)
        
        Optimized version that handles edge cases better.
        """
        self.k = k
        self.min_heap = []
        
        # Add all elements and maintain heap size
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            # Heap not full yet, just add
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            # New value is larger than current kth largest
            heapq.heapreplace(self.min_heap, val)
        
        # Return kth largest (root of min heap)
        return self.min_heap[0]


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    
    assert kth_largest.add(3) == 4, f"Test 1.1 failed: expected 4, got {kth_largest.add(3)}"
    assert kth_largest.add(5) == 5, f"Test 1.2 failed: expected 5, got {kth_largest.add(5)}"
    assert kth_largest.add(10) == 5, f"Test 1.3 failed: expected 5, got {kth_largest.add(10)}"
    assert kth_largest.add(9) == 8, f"Test 1.4 failed: expected 8, got {kth_largest.add(9)}"
    assert kth_largest.add(4) == 8, f"Test 1.5 failed: expected 8, got {kth_largest.add(4)}"
    
    # Test case 2: Empty initial array
    print("Test 2: Empty initial array")
    kth_largest2 = KthLargest(1, [])
    assert kth_largest2.add(-3) == -3, f"Test 2.1 failed: expected -3, got {kth_largest2.add(-3)}"
    assert kth_largest2.add(-2) == -2, f"Test 2.2 failed: expected -2, got {kth_largest2.add(-2)}"
    assert kth_largest2.add(-4) == -2, f"Test 2.3 failed: expected -2, got {kth_largest2.add(-4)}"
    assert kth_largest2.add(0) == 0, f"Test 2.4 failed: expected 0, got {kth_largest2.add(0)}"
    assert kth_largest2.add(4) == 4, f"Test 2.5 failed: expected 4, got {kth_largest2.add(4)}"
    
    # Test case 3: k = 1 (largest element)
    print("Test 3: k = 1")
    kth_largest3 = KthLargest(1, [])
    assert kth_largest3.add(-3) == -3, f"Test 3.1 failed: expected -3, got {kth_largest3.add(-3)}"
    assert kth_largest3.add(-2) == -2, f"Test 3.2 failed: expected -2, got {kth_largest3.add(-2)}"
    assert kth_largest3.add(-4) == -2, f"Test 3.3 failed: expected -2, got {kth_largest3.add(-4)}"
    assert kth_largest3.add(0) == 0, f"Test 3.4 failed: expected 0, got {kth_largest3.add(0)}"
    assert kth_largest3.add(4) == 4, f"Test 3.5 failed: expected 4, got {kth_largest3.add(4)}"
    
    # Test case 4: Large k
    print("Test 4: Large k")
    kth_largest4 = KthLargest(3, [1, 1])
    assert kth_largest4.add(1) == 1, f"Test 4.1 failed: expected 1, got {kth_largest4.add(1)}"
    assert kth_largest4.add(1) == 1, f"Test 4.2 failed: expected 1, got {kth_largest4.add(1)}"
    assert kth_largest4.add(3) == 1, f"Test 4.3 failed: expected 1, got {kth_largest4.add(3)}"
    assert kth_largest4.add(3) == 1, f"Test 4.4 failed: expected 1, got {kth_largest4.add(3)}"
    assert kth_largest4.add(3) == 3, f"Test 4.5 failed: expected 3, got {kth_largest4.add(3)}"
    
    # Test case 5: Negative numbers
    print("Test 5: Negative numbers")
    kth_largest5 = KthLargest(2, [-1, 0, -2])
    assert kth_largest5.add(-3) == -1, f"Test 5.1 failed: expected -1, got {kth_largest5.add(-3)}"
    assert kth_largest5.add(1) == 0, f"Test 5.2 failed: expected 0, got {kth_largest5.add(1)}"
    assert kth_largest5.add(-2) == 0, f"Test 5.3 failed: expected 0, got {kth_largest5.add(-2)}"
    assert kth_largest5.add(-4) == -1, f"Test 5.4 failed: expected -1, got {kth_largest5.add(-4)}"
    assert kth_largest5.add(3) == 0, f"Test 5.5 failed: expected 0, got {kth_largest5.add(3)}"
    
    # Test case 6: Compare different approaches
    print("Test 6: Compare different approaches")
    nums = [4, 5, 8, 2]
    k = 3
    
    kth_min_heap = KthLargest(k, nums)
    kth_max_heap = KthLargestMaxHeap(k, nums)
    kth_sorting = KthLargestSorting(k, nums)
    kth_optimized = KthLargestOptimized(k, nums)
    
    test_values = [3, 5, 10, 9, 4]
    expected_results = [4, 5, 5, 8, 8]
    
    for i, val in enumerate(test_values):
        result_min = kth_min_heap.add(val)
        result_max = kth_max_heap.add(val)
        result_sort = kth_sorting.add(val)
        result_opt = kth_optimized.add(val)
        expected = expected_results[i]
        
        assert result_min == expected, f"Test 6.{i+1} min heap failed: expected {expected}, got {result_min}"
        assert result_max == expected, f"Test 6.{i+1} max heap failed: expected {expected}, got {result_max}"
        assert result_sort == expected, f"Test 6.{i+1} sorting failed: expected {expected}, got {result_sort}"
        assert result_opt == expected, f"Test 6.{i+1} optimized failed: expected {expected}, got {result_opt}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()