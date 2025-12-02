"""
252. Meeting Rooms
Difficulty: Easy

Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person 
could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: Meeting [5,10] overlaps with [0,30], so the person cannot attend all meetings.

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: No meetings overlap, so the person can attend all meetings.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6

Notes:
- Key insight: Sort intervals by start time, then check if any interval starts before the previous one ends.
- Two intervals overlap if: curr_start < prev_end
- Time complexity: O(n log n) - dominated by sorting
- Space complexity: O(1) excluding input, O(n) if we need to store sorted array
- Alternative approaches:
  - Sort by start time: O(n log n) time, O(1) space - current approach
  - Sort by end time: O(n log n) time, O(1) space - similar logic
  - Brute force: O(n^2) time - check all pairs
  - Using sorted list: O(n log n) time, O(n) space - maintain sorted order
- Edge cases: Empty array (can attend), single meeting (can attend), no overlaps, all overlap
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Approach 1: Sort by Start Time (Current)
        Time Complexity: O(n log n)
        Space Complexity: O(1) excluding input
        
        Sort intervals by start time, then check if any interval starts before 
        the previous one ends.
        """
        if not intervals or len(intervals) <= 1:
            return True
        
        intervals.sort()
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True
    
    def canAttendMeetingsSortEnd(self, intervals: List[List[int]]) -> bool:
        """
        Approach 2: Sort by End Time
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Sort by end time instead. Check if any interval starts before previous ends.
        """
        if not intervals or len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x[1])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True
    
    def canAttendMeetingsExplicit(self, intervals: List[List[int]]) -> bool:
        """
        Approach 3: Explicit Variable Names
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        More explicit version with clearer variable names.
        """
        if not intervals or len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i-1]
            curr_start, curr_end = intervals[i]
            
            # Check if current meeting starts before previous ends
            if curr_start < prev_end:
                return False
        
        return True
    
    def canAttendMeetingsBruteForce(self, intervals: List[List[int]]) -> bool:
        """
        Approach 4: Brute Force
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        Check all pairs of intervals for overlap. Less efficient but simpler.
        """
        if not intervals or len(intervals) <= 1:
            return True
        
        n = len(intervals)
        for i in range(n):
            for j in range(i + 1, n):
                start1, end1 = intervals[i]
                start2, end2 = intervals[j]
                
                # Two intervals overlap if: start1 < end2 AND start2 < end1
                if start1 < end2 and start2 < end1:
                    return False
        
        return True
    
    def canAttendMeetingsAlternative(self, intervals: List[List[int]]) -> bool:
        """
        Approach 5: Alternative Structure
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Same logic but with different loop structure.
        """
        if not intervals:
            return True
        
        intervals.sort()
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start < prev_end:
                return False
            prev_end = curr_end
        
        return True
    
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        """
        Approach 6: Original Implementation
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Original implementation with same logic as Approach 1.
        """
        if not intervals:
            return True

        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Overlapping meetings
    print("Test 1: Overlapping meetings [[0,30],[5,10],[15,20]]")
    intervals1 = [[0,30],[5,10],[15,20]]
    expected1 = False
    result1 = solution.canAttendMeetings(intervals1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: No overlaps
    print("Test 2: No overlaps [[7,10],[2,4]]")
    intervals2 = [[7,10],[2,4]]
    expected2 = True
    result2 = solution.canAttendMeetings(intervals2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Empty array
    print("Test 3: Empty array []")
    intervals3 = []
    expected3 = True
    result3 = solution.canAttendMeetings(intervals3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single meeting
    print("Test 4: Single meeting [[1,2]]")
    intervals4 = [[1,2]]
    expected4 = True
    result4 = solution.canAttendMeetings(intervals4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Adjacent meetings (no overlap)
    print("Test 5: Adjacent meetings [[1,2],[2,3],[3,4]]")
    intervals5 = [[1,2],[2,3],[3,4]]
    expected5 = True
    result5 = solution.canAttendMeetings(intervals5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        [[0,30],[5,10],[15,20]],
        [[7,10],[2,4]],
        [],
        [[1,2]],
        [[1,2],[2,3],[3,4]],
        [[1,3],[2,4]],
    ]
    
    for intervals in test_cases:
        result1 = solution.canAttendMeetings([row[:] for row in intervals])
        result2 = solution.canAttendMeetingsSortEnd([row[:] for row in intervals])
        result3 = solution.canAttendMeetingsExplicit([row[:] for row in intervals])
        result4 = solution.canAttendMeetingsBruteForce([row[:] for row in intervals])
        result5 = solution.canAttendMeetingsAlternative([row[:] for row in intervals])
        result6 = solution.can_attend_meetings([row[:] for row in intervals])
        
        assert result1 == result2, f"Sort end failed for {intervals}: {result1} vs {result2}"
        assert result1 == result3, f"Explicit failed for {intervals}: {result1} vs {result3}"
        assert result1 == result4, f"Brute force failed for {intervals}: {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed for {intervals}: {result1} vs {result5}"
        assert result1 == result6, f"Original failed for {intervals}: {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: All overlap
    print("\nTest 7: All overlap [[1,5],[2,6],[3,7]]")
    intervals7 = [[1,5],[2,6],[3,7]]
    expected7 = False
    result7 = solution.canAttendMeetings(intervals7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: One contained in another
    print("Test 8: Contained interval [[1,10],[2,3]]")
    intervals8 = [[1,10],[2,3]]
    expected8 = False
    result8 = solution.canAttendMeetings(intervals8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Unsorted input
    print("Test 9: Unsorted input [[15,20],[0,30],[5,10]]")
    intervals9 = [[15,20],[0,30],[5,10]]
    expected9 = False
    result9 = solution.canAttendMeetings(intervals9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Many non-overlapping
    print("Test 10: Many non-overlapping [[1,2],[3,4],[5,6],[7,8]]")
    intervals10 = [[1,2],[3,4],[5,6],[7,8]]
    expected10 = True
    result10 = solution.canAttendMeetings(intervals10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Duplicate intervals
    print("Test 11: Duplicate intervals [[1,2],[1,2],[1,2]]")
    intervals11 = [[1,2],[1,2],[1,2]]
    expected11 = False  # All overlap with each other
    result11 = solution.canAttendMeetings(intervals11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Large intervals
    print("Test 12: Large intervals [[0,1000000],[500000,1500000]]")
    intervals12 = [[0,1000000],[500000,1500000]]
    expected12 = False
    result12 = solution.canAttendMeetings(intervals12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Negative values (if allowed)
    print("Test 13: Negative values [[-5,-1],[-3,0]]")
    intervals13 = [[-5,-1],[-3,0]]
    expected13 = False
    result13 = solution.canAttendMeetings(intervals13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Zero start times
    print("Test 14: Zero start times [[0,5],[5,10]]")
    intervals14 = [[0,5],[5,10]]
    expected14 = True  # Adjacent, no overlap
    result14 = solution.canAttendMeetings(intervals14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex case
    print("Test 15: Complex case [[1,3],[4,6],[8,10],[2,5]]")
    intervals15 = [[1,3],[4,6],[8,10],[2,5]]
    expected15 = False  # [2,5] overlaps with [1,3] and [4,6]
    result15 = solution.canAttendMeetings(intervals15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Many meetings, all non-overlapping
    print("Test 16: Many meetings, all non-overlapping")
    intervals16 = [[i*2, i*2+1] for i in range(100)]
    expected16 = True
    result16 = solution.canAttendMeetings(intervals16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
