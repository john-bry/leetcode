"""
56. Merge Intervals
Difficulty: Medium

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[1,4],[0,4]]
Output: [[0,4]]
Explanation: Intervals [1,4] and [0,4] overlap.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

Notes:
- Key insight: Sort intervals by start time, then merge overlapping ones.
- Two intervals overlap if: prev[1] >= curr[0] (previous end >= current start)
- When merging: new interval = [min(prev[0], curr[0]), max(prev[1], curr[1])]
- Time complexity: O(n log n) - dominated by sorting
- Space complexity: O(1) excluding output array, O(n) including output
- Alternative approaches:
  - Sort and merge: O(n log n) time, O(n) space - current approach
  - Sort by end time: O(n log n) time, O(n) space - alternative sorting
  - Without sorting: O(n^2) time - check all pairs (inefficient)
- Edge cases: Empty array, single interval, no overlaps, all overlap, intervals contained within others
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach 1: Sort by Start Time (Current)
        Time Complexity: O(n log n)
        Space Complexity: O(n) for output array
        
        Sort intervals by start time, then merge overlapping intervals.
        Two intervals overlap if previous end >= current start.
        """
        if not intervals:
            return []
        
        intervals.sort()
        merged = [intervals[0]]
        
        for curr in intervals[1:]:
            prev = merged[-1]
        
            if prev[1] >= curr[0]:
                # Overlapping: merge by taking min start and max end
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                # No overlap: add as new interval
                merged.append(curr)

        return merged
    
    def merge_sort_by_end(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach 2: Sort by End Time
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Sort by end time instead of start time. Less intuitive but works.
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[1])
        merged = [intervals[0]]
        
        for curr in intervals[1:]:
            prev = merged[-1]
            
            if prev[1] >= curr[0]:
                # Overlapping: merge
                merged[-1] = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            else:
                merged.append(curr)
        
        return merged
    
    def merge_explicit(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach 3: Explicit Overlap Check
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        More explicit version with clearer variable names and overlap logic.
        """
        if not intervals:
            return []
        
        if len(intervals) == 1:
            return intervals
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current_start, current_end = intervals[0]
        
        for next_start, next_end in intervals[1:]:
            # Check if current and next intervals overlap
            if current_end >= next_start:
                # Merge: extend current interval
                current_end = max(current_end, next_end)
            else:
                # No overlap: save current and start new
                merged.append([current_start, current_end])
                current_start, current_end = next_start, next_end
        
        # Don't forget the last interval
        merged.append([current_start, current_end])
        
        return merged
    
    def merge_alternative(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach 4: Alternative Structure
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Similar to approach 1 but with different loop structure.
        """
        if not intervals:
            return []
        
        intervals.sort()
        result = []
        
        for interval in intervals:
            # If result is empty or no overlap, add interval
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # Overlap: merge with last interval
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result
    
    def merge_with_validation(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach 5: With Input Validation
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Same as approach 1 but with input validation.
        """
        if not intervals:
            return []
        
        # Validate intervals
        for interval in intervals:
            if len(interval) != 2 or interval[0] > interval[1]:
                raise ValueError(f"Invalid interval: {interval}")
        
        intervals.sort()
        merged = [intervals[0][:]]  # Copy first interval
        
        for curr in intervals[1:]:
            prev = merged[-1]
            
            # Check for overlap: prev end >= curr start
            if prev[1] >= curr[0]:
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                merged.append(curr[:])  # Copy interval
        
        return merged


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example [[1,3],[2,6],[8,10],[15,18]]")
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    expected1 = [[1,6],[8,10],[15,18]]
    result1 = solution.merge(intervals1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Adjacent intervals
    print("Test 2: Adjacent intervals [[1,4],[4,5]]")
    intervals2 = [[1,4],[4,5]]
    expected2 = [[1,5]]
    result2 = solution.merge(intervals2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Overlapping with different starts
    print("Test 3: Overlapping [[1,4],[0,4]]")
    intervals3 = [[1,4],[0,4]]
    expected3 = [[0,4]]
    result3 = solution.merge(intervals3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single interval
    print("Test 4: Single interval [[1,4]]")
    intervals4 = [[1,4]]
    expected4 = [[1,4]]
    result4 = solution.merge(intervals4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: All overlap
    print("Test 5: All overlap [[1,4],[2,3],[4,5]]")
    intervals5 = [[1,4],[2,3],[4,5]]
    expected5 = [[1,5]]
    result5 = solution.merge(intervals5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: No overlaps
    print("Test 6: No overlaps [[1,2],[3,4],[5,6]]")
    intervals6 = [[1,2],[3,4],[5,6]]
    expected6 = [[1,2],[3,4],[5,6]]
    result6 = solution.merge(intervals6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Compare all approaches
    print("\nTest 7: Comparing all approaches")
    test_cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[1,4],[0,4]],
        [[1,4]],
        [[1,4],[2,3],[4,5]],
        [[1,2],[3,4],[5,6]],
    ]
    
    for intervals in test_cases:
        result1 = solution.merge(intervals)
        result2 = solution.merge_sort_by_end(intervals)
        result3 = solution.merge_explicit(intervals)
        result4 = solution.merge_alternative(intervals)
        result5 = solution.merge_with_validation(intervals)
        
        assert result1 == result2, f"Sort by end failed for {intervals}: {result1} vs {result2}"
        assert result1 == result3, f"Explicit failed for {intervals}: {result1} vs {result3}"
        assert result1 == result4, f"Alternative failed for {intervals}: {result1} vs {result4}"
        assert result1 == result5, f"With validation failed for {intervals}: {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 8: Empty array
    print("\nTest 8: Empty array []")
    intervals8 = []
    expected8 = []
    result8 = solution.merge(intervals8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: One interval contained in another
    print("Test 9: Contained interval [[1,10],[2,3]]")
    intervals9 = [[1,10],[2,3]]
    expected9 = [[1,10]]
    result9 = solution.merge(intervals9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Multiple merges needed
    print("Test 10: Multiple merges [[1,3],[2,4],[5,7],[6,8]]")
    intervals10 = [[1,3],[2,4],[5,7],[6,8]]
    expected10 = [[1,4],[5,8]]
    result10 = solution.merge(intervals10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Unsorted input
    print("Test 11: Unsorted input [[8,10],[1,3],[15,18],[2,6]]")
    intervals11 = [[8,10],[1,3],[15,18],[2,6]]
    expected11 = [[1,6],[8,10],[15,18]]
    result11 = solution.merge(intervals11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: All merge into one
    print("Test 12: All merge into one [[1,2],[2,3],[3,4],[4,5]]")
    intervals12 = [[1,2],[2,3],[3,4],[4,5]]
    expected12 = [[1,5]]
    result12 = solution.merge(intervals12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Zero values
    print("Test 13: Zero values [[0,0],[0,0]]")
    intervals13 = [[0,0],[0,0]]
    expected13 = [[0,0]]
    result13 = solution.merge(intervals13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Large intervals
    print("Test 14: Large intervals [[1,100],[2,50],[51,200]]")
    intervals14 = [[1,100],[2,50],[51,200]]
    expected14 = [[1,200]]
    result14 = solution.merge(intervals14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex case
    print("Test 15: Complex case [[2,3],[4,5],[6,7],[8,9],[1,10]]")
    intervals15 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    expected15 = [[1,10]]
    result15 = solution.merge(intervals15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()