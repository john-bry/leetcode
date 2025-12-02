"""
435. Non-overlapping Intervals
Difficulty: Medium

Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of 
intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= start_i < end_i <= 5 * 10^4

Notes:
- Key insight: Greedy approach - sort by end time, keep intervals with earliest end times.
- When two intervals overlap, always remove the one with the larger end time (greedy choice).
- This maximizes space for future intervals.
- Alternative: Sort by start time and keep track of last end time.
- Time complexity: O(n log n) - dominated by sorting
- Space complexity: O(1) excluding input, O(n) if we need to store sorted array
- Alternative approaches:
  - Sort by end time (greedy): O(n log n) time, O(1) space - current approach
  - Sort by start time: O(n log n) time, O(1) space - similar logic
  - DP approach: O(n^2) time - find longest non-overlapping subsequence
  - Activity selection problem variant
- Edge cases: Empty array, single interval, no overlaps, all overlap, intervals contained within others
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Approach 1: Sort by End Time (Greedy - Current)
        Time Complexity: O(n log n)
        Space Complexity: O(1) excluding input
        
        Sort intervals by end time. When two intervals overlap, always keep the one 
        with the smaller end time (greedy choice) to maximize space for future intervals.
        """
        if not intervals or len(intervals) <= 1:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If current interval overlaps with last kept interval
            if intervals[i][0] < last_end:
                count += 1  # Remove current interval
            else:
                last_end = intervals[i][1]  # Keep current interval
        
        return count
    
    def eraseOverlapIntervalsSortStart(self, intervals: List[List[int]]) -> int:
        """
        Approach 2: Sort by Start Time
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Sort by start time. When overlapping, keep the interval with smaller end time.
        """
        if not intervals or len(intervals) <= 1:
            return 0
        
        intervals.sort()
        count = 0
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            
            if curr_start < last_end:
                # Overlap: remove the one with larger end time
                count += 1
                last_end = min(last_end, curr_end)  # Keep the one with smaller end
            else:
                last_end = curr_end
        
        return count
    
    def eraseOverlapIntervalsExplicit(self, intervals: List[List[int]]) -> int:
        """
        Approach 3: Explicit Greedy with Tracking
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        More explicit version that tracks which intervals to keep.
        """
        if not intervals or len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        removed = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            
            # Check for overlap
            if curr_start < prev_end:
                # Overlap detected: remove current interval
                removed += 1
            else:
                # No overlap: keep current interval
                prev_end = curr_end
        
        return removed
    
    def eraseOverlapIntervalsDP(self, intervals: List[List[int]]) -> int:
        """
        Approach 4: Dynamic Programming (Less Efficient)
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Find the longest non-overlapping subsequence, then return n - length.
        Less efficient but demonstrates DP approach.
        """
        if not intervals or len(intervals) <= 1:
            return 0
        
        intervals.sort()
        n = len(intervals)
        
        # dp[i] = length of longest non-overlapping subsequence ending at index i
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                # If intervals[j] doesn't overlap with intervals[i]
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_non_overlapping = max(dp)
        return n - max_non_overlapping
    
    def eraseOverlapIntervalsAlternative(self, intervals: List[List[int]]) -> int:
        """
        Approach 5: Alternative Greedy Structure
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Same greedy logic but with different structure.
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        removed = 0
        
        for start, curr_end in intervals:
            if start >= end:
                # No overlap: keep this interval
                end = curr_end
            else:
                # Overlap: remove this interval
                removed += 1
        
        return removed
    
    def non_overlapping_intervals(self, intervals: List[List[int]]) -> int:
        """
        Approach 6: Original Implementation (Sort by Start)
        Time Complexity: O(n log n)
        Space Complexity: O(n) for non_overlapping list
        
        Original implementation that tracks non-overlapping intervals.
        When overlap occurs, keeps the interval with smaller end time.
        """
        if not intervals:
            return 0
        
        intervals.sort()
        non_overlapping = [intervals[0]]
        result = 0

        for curr in intervals[1:]:
            prev = non_overlapping[-1]

            if prev[1] > curr[0]:
                # Overlap: need to remove one
                result += 1
                # Keep the one with smaller end time
                if curr[1] < prev[1]:
                    non_overlapping[-1] = curr
            else:
                # No overlap: add to non-overlapping list
                non_overlapping.append(curr)

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example [[1,2],[2,3],[3,4],[1,3]]")
    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    expected1 = 1
    result1 = solution.eraseOverlapIntervals(intervals1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Multiple duplicates
    print("Test 2: Multiple duplicates [[1,2],[1,2],[1,2]]")
    intervals2 = [[1,2],[1,2],[1,2]]
    expected2 = 2
    result2 = solution.eraseOverlapIntervals(intervals2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: No overlaps
    print("Test 3: No overlaps [[1,2],[2,3]]")
    intervals3 = [[1,2],[2,3]]
    expected3 = 0
    result3 = solution.eraseOverlapIntervals(intervals3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single interval
    print("Test 4: Single interval [[1,2]]")
    intervals4 = [[1,2]]
    expected4 = 0
    result4 = solution.eraseOverlapIntervals(intervals4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All overlap
    print("Test 5: All overlap [[1,10],[2,3],[4,5],[6,7]]")
    intervals5 = [[1,10],[2,3],[4,5],[6,7]]
    expected5 = 1  # Keep [2,3],[4,5],[6,7], remove [1,10]
    result5 = solution.eraseOverlapIntervals(intervals5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Compare all approaches
    print("\nTest 6: Comparing all approaches")
    test_cases = [
        [[1,2],[2,3],[3,4],[1,3]],
        [[1,2],[1,2],[1,2]],
        [[1,2],[2,3]],
        [[1,2]],
        [[1,10],[2,3],[4,5],[6,7]],
        [[1,2],[1,3],[2,3],[3,4]],
    ]
    
    for intervals in test_cases:
        result1 = solution.eraseOverlapIntervals([row[:] for row in intervals])
        result2 = solution.eraseOverlapIntervalsSortStart([row[:] for row in intervals])
        result3 = solution.eraseOverlapIntervalsExplicit([row[:] for row in intervals])
        result4 = solution.eraseOverlapIntervalsDP([row[:] for row in intervals])
        result5 = solution.eraseOverlapIntervalsAlternative([row[:] for row in intervals])
        result6 = solution.non_overlapping_intervals([row[:] for row in intervals])
        
        assert result1 == result2, f"Sort start failed for {intervals}: {result1} vs {result2}"
        assert result1 == result3, f"Explicit failed for {intervals}: {result1} vs {result3}"
        assert result1 == result4, f"DP failed for {intervals}: {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed for {intervals}: {result1} vs {result5}"
        assert result1 == result6, f"Original failed for {intervals}: {result1} vs {result6}"
    
    print("  All approaches match! ✓")
    
    # Test case 7: Empty array
    print("\nTest 7: Empty array []")
    intervals7 = []
    expected7 = 0
    result7 = solution.eraseOverlapIntervals(intervals7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Adjacent intervals (no overlap)
    print("Test 8: Adjacent intervals [[1,2],[2,3],[3,4]]")
    intervals8 = [[1,2],[2,3],[3,4]]
    expected8 = 0
    result8 = solution.eraseOverlapIntervals(intervals8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: One contained in another
    print("Test 9: Contained interval [[1,10],[2,3]]")
    intervals9 = [[1,10],[2,3]]
    expected9 = 1  # Remove [1,10], keep [2,3]
    result9 = solution.eraseOverlapIntervals(intervals9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Complex case
    print("Test 10: Complex case [[1,2],[1,3],[2,3],[3,4]]")
    intervals10 = [[1,2],[1,3],[2,3],[3,4]]
    expected10 = 1  # Remove [1,3], keep others
    result10 = solution.eraseOverlapIntervals(intervals10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Unsorted input
    print("Test 11: Unsorted input [[3,4],[1,2],[2,3],[1,3]]")
    intervals11 = [[3,4],[1,2],[2,3],[1,3]]
    expected11 = 1
    result11 = solution.eraseOverlapIntervals(intervals11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Large intervals
    print("Test 12: Large intervals [[1,100],[2,3],[4,5]]")
    intervals12 = [[1,100],[2,3],[4,5]]
    expected12 = 1  # Remove [1,100], keep others
    result12 = solution.eraseOverlapIntervals(intervals12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Negative values
    print("Test 13: Negative values [[-5,-1],[-3,0],[-2,1]]")
    intervals13 = [[-5,-1],[-3,0],[-2,1]]
    expected13 = 2  # All three overlap, keep one ([-5,-1]), remove two
    result13 = solution.eraseOverlapIntervals(intervals13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Many intervals
    print("Test 14: Many intervals")
    intervals14 = [[1,2],[2,3],[3,4],[4,5],[1,3],[2,4],[3,5]]
    expected14 = 3  # Remove overlapping ones
    result14 = solution.eraseOverlapIntervals(intervals14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Very close intervals
    print("Test 15: Very close intervals [[1,2],[1,2],[2,3]]")
    intervals15 = [[1,2],[1,2],[2,3]]
    expected15 = 1  # Remove one duplicate [1,2], keep [1,2] and [2,3]
    result15 = solution.eraseOverlapIntervals(intervals15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Optimal greedy choice
    print("Test 16: Optimal greedy choice [[1,4],[2,3],[3,4]]")
    intervals16 = [[1,4],[2,3],[3,4]]
    expected16 = 1  # Remove [1,4], keep [2,3] and [3,4]
    result16 = solution.eraseOverlapIntervals(intervals16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
