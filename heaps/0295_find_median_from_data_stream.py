"""
295. Find Median from Data Stream
Difficulty: Hard

The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5 of the 
  actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Example 2:
Input
["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"]
[[], [2], [], [3], []]
Output
[null, null, 2.0, null, 2.5]

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Notes:
- Key insight: Use two heaps to maintain the two halves of the sorted data.
- Small heap (max heap): Stores the smaller half, use negative values to simulate max heap.
- Large heap (min heap): Stores the larger half.
- Invariants:
  1. |size(small) - size(large)| <= 1 (heaps are balanced)
  2. max(small) <= min(large) (all elements in small <= all elements in large)
- Time complexity: O(log n) for addNum, O(1) for findMedian
- Space complexity: O(n) for storing all numbers
- Alternative approaches:
  - Two heaps: O(log n) add, O(1) find - current approach (optimal)
  - Sorted list with insertion: O(n) add, O(1) find - less efficient
  - Balanced BST: O(log n) add, O(1) find - more complex
  - Quick select: O(n) average add, O(1) find - not suitable for streaming
- Edge cases: Single element, two elements, all same values, alternating pattern
"""

import heapq
from typing import List


class MedianFinder:
    """
    Approach 1: Two Heaps (Current - Optimal)
    Time Complexity: O(log n) for addNum, O(1) for findMedian
    Space Complexity: O(n)
    
    Maintain two heaps:
    - small: max heap (using negative values) for smaller half
    - large: min heap for larger half
    """
    
    def __init__(self):
        """
        Initialize the MedianFinder.
        small: max heap (stored as negative values) for smaller half
        large: min heap for larger half
        """
        self.small = []  # max heap (use negative vals)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        
        Algorithm:
        1. Always add to small heap first
        2. Move largest from small to large (maintain invariant: max(small) <= min(large))
        3. Balance sizes (maintain invariant: |size(small) - size(large)| <= 1)
        """
        # 1 - always add to small first
        heapq.heappush(self.small, -num)
        # 2 - move largest from small to large (maintain invariant 2)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 3 - balance sizes (maintain invariant 1)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        """
        Find the median of all numbers added so far.
        
        Returns:
            Median value (float)
        """
        if len(self.small) > len(self.large):
            return -self.small[0]  # odd count - return middle element
        
        return (-self.small[0] + self.large[0]) / 2  # even count - return average of two middle elements


class MedianFinderAlternative:
    """
    Approach 2: Alternative Two Heaps Structure
    Time Complexity: O(log n) for addNum, O(1) for findMedian
    Space Complexity: O(n)
    
    Same logic but with slightly different structure and clearer variable names.
    """
    
    def __init__(self):
        self.max_heap = []  # Smaller half (using negative values)
        self.min_heap = []  # Larger half

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.max_heap, -num)
        
        # Ensure max of max_heap <= min of min_heap
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            max_val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_val)
        
        # Balance sizes
        if len(self.max_heap) > len(self.min_heap) + 1:
            max_val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class MedianFinderSortedList:
    """
    Approach 3: Sorted List (Less Efficient)
    Time Complexity: O(n) for addNum, O(1) for findMedian
    Space Complexity: O(n)
    
    Maintain a sorted list. Less efficient but simpler conceptually.
    """
    
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # Insert in sorted order (O(n))
        import bisect
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example [1, 2, 3]")
    mf1 = MedianFinder()
    mf1.addNum(1)
    mf1.addNum(2)
    result1 = mf1.findMedian()
    expected1 = 1.5
    assert abs(result1 - expected1) < 0.0001, f"Test 1a failed: expected {expected1}, got {result1}"
    print(f"  After [1, 2]: {result1} ✓")
    
    mf1.addNum(3)
    result1b = mf1.findMedian()
    expected1b = 2.0
    assert abs(result1b - expected1b) < 0.0001, f"Test 1b failed: expected {expected1b}, got {result1b}"
    print(f"  After [1, 2, 3]: {result1b} ✓")
    
    # Test case 2: Example 2 from problem
    print("\nTest 2: Example 2 [2, 3]")
    mf2 = MedianFinder()
    mf2.addNum(2)
    result2a = mf2.findMedian()
    expected2a = 2.0
    assert abs(result2a - expected2a) < 0.0001, f"Test 2a failed: expected {expected2a}, got {result2a}"
    print(f"  After [2]: {result2a} ✓")
    
    mf2.addNum(3)
    result2b = mf2.findMedian()
    expected2b = 2.5
    assert abs(result2b - expected2b) < 0.0001, f"Test 2b failed: expected {expected2b}, got {result2b}"
    print(f"  After [2, 3]: {result2b} ✓")
    
    # Test case 3: Single element
    print("\nTest 3: Single element [5]")
    mf3 = MedianFinder()
    mf3.addNum(5)
    result3 = mf3.findMedian()
    expected3 = 5.0
    assert abs(result3 - expected3) < 0.0001, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Compare all approaches
    print("\nTest 4: Comparing all approaches")
    test_sequence = [1, 2, 3, 4, 5]
    
    mf_a = MedianFinder()
    mf_b = MedianFinderAlternative()
    mf_c = MedianFinderSortedList()
    
    for num in test_sequence:
        mf_a.addNum(num)
        mf_b.addNum(num)
        mf_c.addNum(num)
    
    result_a = mf_a.findMedian()
    result_b = mf_b.findMedian()
    result_c = mf_c.findMedian()
    
    expected = 3.0
    assert abs(result_a - expected) < 0.0001, f"Approach 1 failed: {result_a}"
    assert abs(result_b - expected) < 0.0001, f"Approach 2 failed: {result_b}"
    assert abs(result_c - expected) < 0.0001, f"Approach 3 failed: {result_c}"
    print(f"  All approaches match: {result_a} ✓")
    
    # Test case 5: All same values
    print("\nTest 5: All same values [3, 3, 3, 3]")
    mf5 = MedianFinder()
    for num in [3, 3, 3, 3]:
        mf5.addNum(num)
    result5 = mf5.findMedian()
    expected5 = 3.0
    assert abs(result5 - expected5) < 0.0001, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Alternating pattern
    print("Test 6: Alternating pattern [1, 5, 2, 4, 3]")
    mf6 = MedianFinder()
    for num in [1, 5, 2, 4, 3]:
        mf6.addNum(num)
    result6 = mf6.findMedian()
    expected6 = 3.0  # Sorted: [1, 2, 3, 4, 5], median = 3
    assert abs(result6 - expected6) < 0.0001, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Decreasing order
    print("Test 7: Decreasing order [5, 4, 3, 2, 1]")
    mf7 = MedianFinder()
    for num in [5, 4, 3, 2, 1]:
        mf7.addNum(num)
    result7 = mf7.findMedian()
    expected7 = 3.0
    assert abs(result7 - expected7) < 0.0001, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Negative numbers
    print("Test 8: Negative numbers [-1, -2, -3, -4]")
    mf8 = MedianFinder()
    for num in [-1, -2, -3, -4]:
        mf8.addNum(num)
    result8 = mf8.findMedian()
    expected8 = -2.5  # Sorted: [-4, -3, -2, -1], median = (-3 + -2) / 2 = -2.5
    assert abs(result8 - expected8) < 0.0001, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Mixed positive and negative
    print("Test 9: Mixed positive and negative [-1, 2, -3, 4, 0]")
    mf9 = MedianFinder()
    for num in [-1, 2, -3, 4, 0]:
        mf9.addNum(num)
    result9 = mf9.findMedian()
    expected9 = 0.0  # Sorted: [-3, -1, 0, 2, 4], median = 0
    assert abs(result9 - expected9) < 0.0001, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Large numbers
    print("Test 10: Large numbers [100000, 200000, 300000]")
    mf10 = MedianFinder()
    for num in [100000, 200000, 300000]:
        mf10.addNum(num)
    result10 = mf10.findMedian()
    expected10 = 200000.0
    assert abs(result10 - expected10) < 0.0001, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Even number of elements
    print("Test 11: Even number [1, 2, 3, 4]")
    mf11 = MedianFinder()
    for num in [1, 2, 3, 4]:
        mf11.addNum(num)
    result11 = mf11.findMedian()
    expected11 = 2.5  # (2 + 3) / 2
    assert abs(result11 - expected11) < 0.0001, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Odd number of elements
    print("Test 12: Odd number [1, 2, 3, 4, 5]")
    mf12 = MedianFinder()
    for num in [1, 2, 3, 4, 5]:
        mf12.addNum(num)
    result12 = mf12.findMedian()
    expected12 = 3.0
    assert abs(result12 - expected12) < 0.0001, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Sequential operations
    print("\nTest 13: Sequential operations")
    mf13 = MedianFinder()
    operations = [
        (1, 1.0),
        (2, 1.5),
        (3, 2.0),
        (4, 2.5),
        (5, 3.0),
    ]
    for num, expected_median in operations:
        mf13.addNum(num)
        result = mf13.findMedian()
        assert abs(result - expected_median) < 0.0001, \
            f"Test 13 failed at {num}: expected {expected_median}, got {result}"
    print("  All sequential operations correct ✓")
    
    # Test case 14: Large dataset
    print("Test 14: Large dataset (1000 elements)")
    mf14 = MedianFinder()
    for i in range(1, 1001):
        mf14.addNum(i)
    result14 = mf14.findMedian()
    expected14 = 500.5  # (500 + 501) / 2
    assert abs(result14 - expected14) < 0.0001, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Duplicate values
    print("Test 15: Duplicate values [1, 1, 2, 2, 3, 3]")
    mf15 = MedianFinder()
    for num in [1, 1, 2, 2, 3, 3]:
        mf15.addNum(num)
    result15 = mf15.findMedian()
    expected15 = 2.0  # (2 + 2) / 2
    assert abs(result15 - expected15) < 0.0001, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
