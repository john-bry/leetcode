"""
346. Moving Average from Data Stream
Difficulty: Easy

Given a stream of integers and a window size, calculate the moving average of all integers 
in the sliding window.

Implement the MovingAverage class:
- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:
- 1 <= size <= 1000
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next.

Notes:
- Key insight: Use a queue (deque) to maintain the sliding window and track the sum.
- When window is not full: sum all elements in queue.
- When window is full: remove oldest element and add new one, update sum incrementally.
- Time complexity: O(1) for next() - amortized constant time
- Space complexity: O(size) for storing the window
- Alternative approaches:
  - Queue with sum tracking: O(1) time, O(size) space - current approach (optimal)
  - Array with circular buffer: O(1) time, O(size) space - similar efficiency
  - List with slicing: O(size) time, O(size) space - less efficient
  - Running sum array: O(1) time, O(n) space - more space but simpler
- Edge cases: Window size 1, single element, all same values, negative numbers
"""

from collections import deque
from typing import List


class MovingAverage:
    """
    Approach 1: Queue with Sum Tracking (Current - Optimal)
    Time Complexity: O(1) for next()
    Space Complexity: O(size)
    
    Use a deque to maintain the sliding window and track the running sum.
    When window exceeds size, remove oldest element and subtract from sum.
    """
    
    def __init__(self, size: int):
        """
        Initialize the MovingAverage with a window size.
        
        Args:
            size: Size of the sliding window
        """
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        """
        Add a new value and return the moving average of the last size values.
        
        Args:
            val: New integer value to add
            
        Returns:
            Moving average of the last size values
        """
        self.queue.append(val)
        self.sum += val

        # If window exceeds size, remove oldest element
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()

        return self.sum / len(self.queue)


class MovingAverageCircular:
    """
    Approach 2: Circular Buffer with Array
    Time Complexity: O(1) for next()
    Space Complexity: O(size)
    
    Use a circular buffer (array) to store the window.
    More memory efficient but slightly more complex indexing.
    """
    
    def __init__(self, size: int):
        self.size = size
        self.window = [0] * size
        self.count = 0  # Total number of elements seen
        self.sum = 0

    def next(self, val: int) -> float:
        # Calculate index in circular buffer
        idx = self.count % self.size
        
        # If overwriting an old value, subtract it from sum
        if self.count >= self.size:
            self.sum -= self.window[idx]
        
        # Add new value
        self.window[idx] = val
        self.sum += val
        self.count += 1
        
        # Return average
        window_size = min(self.count, self.size)
        return self.sum / window_size


class MovingAverageList:
    """
    Approach 3: List with Slicing (Less Efficient)
    Time Complexity: O(size) for next()
    Space Complexity: O(size)
    
    Simpler approach but less efficient due to list slicing.
    """
    
    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        self.window.append(val)
        
        # Keep only last size elements
        if len(self.window) > self.size:
            self.window = self.window[-self.size:]
        
        return sum(self.window) / len(self.window)


class MovingAverageSimple:
    """
    Approach 4: Simple List with Sum Calculation
    Time Complexity: O(size) for next()
    Space Complexity: O(size)
    
    Simplest approach - recalculate sum each time.
    Less efficient but very straightforward.
    """
    
    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        self.window.append(val)
        
        # Keep only last size elements
        if len(self.window) > self.size:
            self.window.pop(0)
        
        return sum(self.window) / len(self.window)


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example [1, 10, 3, 5] with size=3")
    ma1 = MovingAverage(3)
    result1a = ma1.next(1)
    expected1a = 1.0
    assert abs(result1a - expected1a) < 0.0001, f"Test 1a failed: expected {expected1a}, got {result1a}"
    print(f"  next(1): {result1a} ✓")
    
    result1b = ma1.next(10)
    expected1b = 5.5
    assert abs(result1b - expected1b) < 0.0001, f"Test 1b failed: expected {expected1b}, got {result1b}"
    print(f"  next(10): {result1b} ✓")
    
    result1c = ma1.next(3)
    expected1c = 4.66667
    assert abs(result1c - expected1c) < 0.01, f"Test 1c failed: expected {expected1c}, got {result1c}"
    print(f"  next(3): {result1c} ✓")
    
    result1d = ma1.next(5)
    expected1d = 6.0
    assert abs(result1d - expected1d) < 0.0001, f"Test 1d failed: expected {expected1d}, got {result1d}"
    print(f"  next(5): {result1d} ✓")
    
    # Test case 2: Window size 1
    print("\nTest 2: Window size 1")
    ma2 = MovingAverage(1)
    result2a = ma2.next(5)
    assert abs(result2a - 5.0) < 0.0001, f"Test 2a failed: expected 5.0, got {result2a}"
    print(f"  next(5): {result2a} ✓")
    
    result2b = ma2.next(10)
    assert abs(result2b - 10.0) < 0.0001, f"Test 2b failed: expected 10.0, got {result2b}"
    print(f"  next(10): {result2b} ✓")
    
    # Test case 3: Compare all approaches
    print("\nTest 3: Comparing all approaches")
    test_sequence = [1, 10, 3, 5, 7, 2]
    size = 3
    
    ma_a = MovingAverage(size)
    ma_b = MovingAverageCircular(size)
    ma_c = MovingAverageList(size)
    ma_d = MovingAverageSimple(size)
    
    for val in test_sequence:
        result_a = ma_a.next(val)
        result_b = ma_b.next(val)
        result_c = ma_c.next(val)
        result_d = ma_d.next(val)
        
        assert abs(result_a - result_b) < 0.0001, f"Mismatch: {result_a} vs {result_b}"
        assert abs(result_a - result_c) < 0.0001, f"Mismatch: {result_a} vs {result_c}"
        assert abs(result_a - result_d) < 0.0001, f"Mismatch: {result_a} vs {result_d}"
    
    print("  All approaches match! ✓")
    
    # Test case 4: All same values
    print("\nTest 4: All same values [5, 5, 5, 5] with size=3")
    ma4 = MovingAverage(3)
    for val in [5, 5, 5, 5]:
        result = ma4.next(val)
    expected4 = 5.0
    assert abs(result - expected4) < 0.0001, f"Test 4 failed: expected {expected4}, got {result}"
    print(f"  Result: {result} ✓")
    
    # Test case 5: Negative numbers
    print("Test 5: Negative numbers [-1, -2, -3, -4] with size=2")
    ma5 = MovingAverage(2)
    ma5.next(-1)
    ma5.next(-2)
    result5a = ma5.next(-3)
    expected5a = -2.5  # (-2 + -3) / 2
    assert abs(result5a - expected5a) < 0.0001, f"Test 5a failed: expected {expected5a}, got {result5a}"
    print(f"  next(-3): {result5a} ✓")
    
    result5b = ma5.next(-4)
    expected5b = -3.5  # (-3 + -4) / 2
    assert abs(result5b - expected5b) < 0.0001, f"Test 5b failed: expected {expected5b}, got {result5b}"
    print(f"  next(-4): {result5b} ✓")
    
    # Test case 6: Mixed positive and negative
    print("Test 6: Mixed positive and negative [1, -1, 2, -2] with size=3")
    ma6 = MovingAverage(3)
    ma6.next(1)
    ma6.next(-1)
    result6a = ma6.next(2)
    expected6a = (1 + -1 + 2) / 3  # 0.66667
    assert abs(result6a - expected6a) < 0.0001, f"Test 6a failed: expected {expected6a}, got {result6a}"
    print(f"  next(2): {result6a} ✓")
    
    result6b = ma6.next(-2)
    expected6b = (-1 + 2 + -2) / 3  # -0.33333
    assert abs(result6b - expected6b) < 0.0001, f"Test 6b failed: expected {expected6b}, got {result6b}"
    print(f"  next(-2): {result6b} ✓")
    
    # Test case 7: Large window size
    print("Test 7: Large window size (size=10)")
    ma7 = MovingAverage(10)
    for i in range(1, 16):
        result = ma7.next(i)
    expected7 = (6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15) / 10  # 10.5
    assert abs(result - expected7) < 0.0001, f"Test 7 failed: expected {expected7}, got {result}"
    print(f"  Result: {result} ✓")
    
    # Test case 8: Sequential numbers
    print("Test 8: Sequential numbers [1, 2, 3, 4, 5] with size=3")
    ma8 = MovingAverage(3)
    results = []
    for val in [1, 2, 3, 4, 5]:
        results.append(ma8.next(val))
    expected8 = [1.0, 1.5, 2.0, 3.0, 4.0]
    for i, (result, expected) in enumerate(zip(results, expected8)):
        assert abs(result - expected) < 0.0001, f"Test 8.{i} failed: expected {expected}, got {result}"
    print(f"  Results: {results} ✓")
    
    # Test case 9: Single element before window fills
    print("Test 9: Single element before window fills")
    ma9 = MovingAverage(5)
    result9 = ma9.next(100)
    expected9 = 100.0
    assert abs(result9 - expected9) < 0.0001, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Zero values
    print("Test 10: Zero values [0, 0, 0, 0] with size=2")
    ma10 = MovingAverage(2)
    for val in [0, 0, 0, 0]:
        result = ma10.next(val)
    expected10 = 0.0
    assert abs(result - expected10) < 0.0001, f"Test 10 failed: expected {expected10}, got {result}"
    print(f"  Result: {result} ✓")
    
    # Test case 11: Large numbers
    print("Test 11: Large numbers [100000, 200000, 300000] with size=2")
    ma11 = MovingAverage(2)
    ma11.next(100000)
    result11a = ma11.next(200000)
    expected11a = 150000.0
    assert abs(result11a - expected11a) < 0.0001, f"Test 11a failed: expected {expected11a}, got {result11a}"
    print(f"  next(200000): {result11a} ✓")
    
    result11b = ma11.next(300000)
    expected11b = 250000.0
    assert abs(result11b - expected11b) < 0.0001, f"Test 11b failed: expected {expected11b}, got {result11b}"
    print(f"  next(300000): {result11b} ✓")
    
    # Test case 12: Alternating pattern
    print("Test 12: Alternating pattern [1, 10, 1, 10, 1] with size=3")
    ma12 = MovingAverage(3)
    ma12.next(1)
    ma12.next(10)
    result12a = ma12.next(1)
    expected12a = (1 + 10 + 1) / 3  # 4.0
    assert abs(result12a - expected12a) < 0.0001, f"Test 12a failed: expected {expected12a}, got {result12a}"
    print(f"  next(1): {result12a} ✓")
    
    result12b = ma12.next(10)
    expected12b = (10 + 1 + 10) / 3  # 7.0
    assert abs(result12b - expected12b) < 0.0001, f"Test 12b failed: expected {expected12b}, got {result12b}"
    print(f"  next(10): {result12b} ✓")
    
    # Test case 13: Window size equals number of elements
    print("Test 13: Window size equals number of elements")
    ma13 = MovingAverage(3)
    ma13.next(1)
    ma13.next(2)
    result13 = ma13.next(3)
    expected13 = (1 + 2 + 3) / 3  # 2.0
    assert abs(result13 - expected13) < 0.0001, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Many operations
    print("Test 14: Many operations (100 values)")
    ma14 = MovingAverage(10)
    for i in range(100):
        result = ma14.next(i)
    # Last 10 values: 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
    expected14 = sum(range(90, 100)) / 10  # 94.5
    assert abs(result - expected14) < 0.0001, f"Test 14 failed: expected {expected14}, got {result}"
    print(f"  Result: {result} ✓")
    
    # Test case 15: Decreasing sequence
    print("Test 15: Decreasing sequence [5, 4, 3, 2, 1] with size=3")
    ma15 = MovingAverage(3)
    ma15.next(5)
    ma15.next(4)
    result15a = ma15.next(3)
    expected15a = (5 + 4 + 3) / 3  # 4.0
    assert abs(result15a - expected15a) < 0.0001, f"Test 15a failed: expected {expected15a}, got {result15a}"
    print(f"  next(3): {result15a} ✓")
    
    result15b = ma15.next(2)
    expected15b = (4 + 3 + 2) / 3  # 3.0
    assert abs(result15b - expected15b) < 0.0001, f"Test 15b failed: expected {expected15b}, got {result15b}"
    print(f"  next(2): {result15b} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
