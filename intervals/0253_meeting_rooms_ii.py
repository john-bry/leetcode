"""
253. Meeting Rooms II
Difficulty: Medium

Given an array of meeting time intervals where intervals[i] = [start_i, end_i], return the minimum 
number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: We need two meeting rooms:
- Room 1: [0,30]
- Room 2: [5,10], [15,20]

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
Explanation: The meetings can be scheduled in one room since they don't overlap.

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6

Notes:
- Key insight: Use a min-heap to track end times of ongoing meetings. When a new meeting starts, 
  if the earliest ending meeting has finished, reuse that room; otherwise, allocate a new room.
- Alternative: Chronological events approach - track all start and end events, count concurrent meetings.
- Time complexity: O(n log n) - sorting + heap operations
- Space complexity: O(n) - heap can contain at most n end times
- Alternative approaches:
  - Heap-based: O(n log n) time, O(n) space - current approach
  - Chronological events: O(n log n) time, O(n) space - track all events
  - Line sweep: O(n log n) time, O(n) space - similar to events
  - Brute force: O(n^2) time - check all pairs
- Edge cases: Empty array (0 rooms), single meeting (1 room), no overlaps (1 room), all overlap (n rooms)
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Approach 1: Heap-Based (Current)
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Sort intervals by start time. Use a min-heap to track end times of ongoing meetings.
        When a new meeting starts, if the earliest ending meeting has finished, reuse that room.
        """
        if not intervals:
            return 0
        
        intervals.sort()
        rooms = []  # Min-heap of end times
        
        for start, end in intervals:
            # If earliest ending meeting is done, reuse that room
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            
            # Add current meeting's end time
            heapq.heappush(rooms, end)
        
        return len(rooms)
    
    def minMeetingRoomsChronological(self, intervals: List[List[int]]) -> int:
        """
        Approach 2: Chronological Events
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Create events for all start and end times. Sort events chronologically.
        For start events, increment room count; for end events, decrement.
        Track maximum concurrent rooms needed.
        """
        if not intervals:
            return 0
        
        events = []
        for start, end in intervals:
            events.append((start, 1))   # Start event: +1 room
            events.append((end, -1))     # End event: -1 room
        
        # Sort by time, if tie, end events come before start events
        events.sort(key=lambda x: (x[0], x[1]))
        
        max_rooms = 0
        current_rooms = 0
        
        for time, delta in events:
            current_rooms += delta
            max_rooms = max(max_rooms, current_rooms)
        
        return max_rooms
    
    def minMeetingRoomsLineSweep(self, intervals: List[List[int]]) -> int:
        """
        Approach 3: Line Sweep
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Similar to chronological events but with explicit start/end tracking.
        """
        if not intervals:
            return 0
        
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        
        rooms = 0
        max_rooms = 0
        start_ptr = 0
        end_ptr = 0
        
        while start_ptr < len(intervals):
            if starts[start_ptr] < ends[end_ptr]:
                # New meeting starts before one ends
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_ptr += 1
            else:
                # A meeting ends
                rooms -= 1
                end_ptr += 1
        
        return max_rooms
    
    def minMeetingRoomsBruteForce(self, intervals: List[List[int]]) -> int:
        """
        Approach 4: Brute Force
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        For each interval's start time, count how many intervals are active at that time.
        The maximum count is the minimum number of rooms needed.
        """
        if not intervals:
            return 0
        
        max_rooms = 0
        
        for i in range(len(intervals)):
            # Check how many intervals are active at the start time of interval i
            active_count = 0
            check_time = intervals[i][0]
            
            for j in range(len(intervals)):
                start, end = intervals[j]
                # Interval is active if check_time is within [start, end)
                if start <= check_time < end:
                    active_count += 1
            
            max_rooms = max(max_rooms, active_count)
        
        return max_rooms
    
    def minMeetingRoomsAlternative(self, intervals: List[List[int]]) -> int:
        """
        Approach 5: Alternative Heap Structure
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Same heap approach but with slightly different structure.
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        heap = []
        
        for interval in intervals:
            start, end = interval
            
            # If earliest ending meeting has ended, reuse that room (pop once)
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)
    
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        """
        Approach 6: Original Implementation
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Original implementation with same logic as Approach 1.
        """
        if not intervals:
            return 0
        # sort intervals
        intervals.sort()
        # track end-times of ongoing meetings
        rooms = []
        # iterate through intervals
        for start, end in intervals:
            # if earliest meeting is done, reuse that room
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # add current meeting's end time
            heapq.heappush(rooms, end)

        return len(rooms)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example [[0,30],[5,10],[15,20]]")
    intervals1 = [[0,30],[5,10],[15,20]]
    expected1 = 2
    result1 = solution.minMeetingRooms(intervals1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: No overlaps
    print("Test 2: No overlaps [[7,10],[2,4]]")
    intervals2 = [[7,10],[2,4]]
    expected2 = 1
    result2 = solution.minMeetingRooms(intervals2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Empty array
    print("Test 3: Empty array []")
    intervals3 = []
    expected3 = 0
    result3 = solution.minMeetingRooms(intervals3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single meeting
    print("Test 4: Single meeting [[1,2]]")
    intervals4 = [[1,2]]
    expected4 = 1
    result4 = solution.minMeetingRooms(intervals4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All overlap
    print("Test 5: All overlap [[1,5],[2,6],[3,7]]")
    intervals5 = [[1,5],[2,6],[3,7]]
    expected5 = 3
    result5 = solution.minMeetingRooms(intervals5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        [[0,30],[5,10],[15,20]],
        [[7,10],[2,4]],
        [],
        [[1,2]],
        [[1,5],[2,6],[3,7]],
        [[1,3],[2,4],[4,6]],
    ]
    
    for intervals in test_cases:
        result1 = solution.minMeetingRooms([row[:] for row in intervals])
        result2 = solution.minMeetingRoomsChronological([row[:] for row in intervals])
        result3 = solution.minMeetingRoomsLineSweep([row[:] for row in intervals])
        result4 = solution.minMeetingRoomsBruteForce([row[:] for row in intervals])
        result5 = solution.minMeetingRoomsAlternative([row[:] for row in intervals])
        result6 = solution.min_meeting_rooms([row[:] for row in intervals])
        
        assert result1 == result2, f"Chronological failed for {intervals}: {result1} vs {result2}"
        assert result1 == result3, f"Line sweep failed for {intervals}: {result1} vs {result3}"
        assert result1 == result4, f"Brute force failed for {intervals}: {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed for {intervals}: {result1} vs {result5}"
        assert result1 == result6, f"Original failed for {intervals}: {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: Adjacent meetings (no overlap)
    print("\nTest 7: Adjacent meetings [[1,2],[2,3],[3,4]]")
    intervals7 = [[1,2],[2,3],[3,4]]
    expected7 = 1
    result7 = solution.minMeetingRooms(intervals7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: One contained in another
    print("Test 8: Contained interval [[1,10],[2,3]]")
    intervals8 = [[1,10],[2,3]]
    expected8 = 2
    result8 = solution.minMeetingRooms(intervals8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Unsorted input
    print("Test 9: Unsorted input [[15,20],[0,30],[5,10]]")
    intervals9 = [[15,20],[0,30],[5,10]]
    expected9 = 2
    result9 = solution.minMeetingRooms(intervals9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Many non-overlapping
    print("Test 10: Many non-overlapping [[1,2],[3,4],[5,6],[7,8]]")
    intervals10 = [[1,2],[3,4],[5,6],[7,8]]
    expected10 = 1
    result10 = solution.minMeetingRooms(intervals10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Duplicate intervals
    print("Test 11: Duplicate intervals [[1,2],[1,2],[1,2]]")
    intervals11 = [[1,2],[1,2],[1,2]]
    expected11 = 3  # All overlap, need 3 rooms
    result11 = solution.minMeetingRooms(intervals11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Large intervals
    print("Test 12: Large intervals [[0,1000000],[500000,1500000]]")
    intervals12 = [[0,1000000],[500000,1500000]]
    expected12 = 2
    result12 = solution.minMeetingRooms(intervals12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Complex case
    print("Test 13: Complex case [[1,3],[4,6],[8,10],[2,5]]")
    intervals13 = [[1,3],[4,6],[8,10],[2,5]]
    expected13 = 2  # [1,3] and [2,5] overlap, [4,6] and [8,10] don't
    result13 = solution.minMeetingRooms(intervals13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Many meetings, all non-overlapping
    print("Test 14: Many meetings, all non-overlapping")
    intervals14 = [[i*2, i*2+1] for i in range(100)]
    expected14 = 1
    result14 = solution.minMeetingRooms(intervals14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: All meetings start at same time
    print("Test 15: All meetings start at same time [[0,1],[0,2],[0,3]]")
    intervals15 = [[0,1],[0,2],[0,3]]
    expected15 = 3
    result15 = solution.minMeetingRooms(intervals15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Optimal room reuse
    print("Test 16: Optimal room reuse [[0,5],[1,3],[2,4],[4,6]]")
    intervals16 = [[0,5],[1,3],[2,4],[4,6]]
    expected16 = 3  # [0,5], [1,3], [2,4] need 3 rooms, [4,6] can reuse room from [1,3]
    result16 = solution.minMeetingRooms(intervals16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    # Test case 17: Chain of meetings
    print("Test 17: Chain of meetings [[1,2],[2,3],[3,4],[4,5]]")
    intervals17 = [[1,2],[2,3],[3,4],[4,5]]
    expected17 = 1
    result17 = solution.minMeetingRooms(intervals17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    print(f"  Result: {result17} ✓")
    
    # Test case 18: Mixed overlaps
    print("Test 18: Mixed overlaps [[1,4],[2,5],[3,6],[7,8]]")
    intervals18 = [[1,4],[2,5],[3,6],[7,8]]
    expected18 = 3  # First three overlap, last is separate
    result18 = solution.minMeetingRooms(intervals18)
    assert result18 == expected18, f"Test 18 failed: expected {expected18}, got {result18}"
    print(f"  Result: {result18} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
