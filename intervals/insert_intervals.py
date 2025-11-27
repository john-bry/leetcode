"""
57. Insert Interval
Difficulty: Medium

You are given an array of non-overlapping intervals where intervals[i] = [start_i, end_i] 
represent the start and the end of the i-th interval and intervals is sorted in ascending 
order by start_i. You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by 
start_i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Explanation: Intervals [1,3] and [2,5] overlap, so merge them into [1,5].

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^5
- intervals is sorted by start_i in ascending order.
- 0 <= start <= end <= 10^5

Notes:
- Key insight: Three phases - before, merge overlapping, after.
- Phase 1: Add all intervals that end before newInterval starts (no overlap)
- Phase 2: Merge all intervals that overlap with newInterval
- Phase 3: Add all remaining intervals
- Time complexity: O(n) - single pass through intervals
- Space complexity: O(n) for output array
- Alternative approaches:
  - Three-phase approach: O(n) time, O(n) space - current approach
  - Merge and sort: O(n log n) time, O(n) space - add and re-merge all
  - Binary search: O(log n) time to find insertion point, O(n) overall
- Edge cases: Empty intervals, newInterval at start, newInterval at end, no overlaps, all overlap
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach 1: Three-Phase Approach (Current)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Three phases:
        1. Add intervals before newInterval (no overlap)
        2. Merge overlapping intervals with newInterval
        3. Add remaining intervals after merged interval
        """
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals that come before newInterval (no overlap)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Phase 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # Phase 3: Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
    
    def insert_merge_all(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach 2: Merge All Approach
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Add newInterval to intervals, then merge all overlapping intervals.
        Less efficient but simpler conceptually.
        """
        # Add new interval
        intervals.append(newInterval)
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Merge overlapping intervals
        merged = [intervals[0]]
        for curr in intervals[1:]:
            prev = merged[-1]
            if prev[1] >= curr[0]:
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                merged.append(curr)
        
        return merged
    
    def insert_binary_search(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach 3: Binary Search for Insertion Point
        Time Complexity: O(n) - still need to merge
        Space Complexity: O(n)
        
        Use binary search to find insertion point, but still need O(n) to merge.
        More complex without significant benefit for this problem.
        """
        if not intervals:
            return [newInterval]
        
        result = []
        n = len(intervals)
        
        # Find insertion point using binary search
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
        
        # Insert at position left
        # Phase 1: Before insertion point
        result.extend(intervals[:left])
        
        # Phase 2: Merge overlapping
        i = left
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # Phase 3: After merged interval
        result.extend(intervals[i:])
        
        return result
    
    def insert_explicit(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach 4: Explicit Phase-by-Phase
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        More explicit version with clearer phase separation.
        """
        result = []
        n = len(intervals)
        new_start, new_end = newInterval
        
        # Phase 1: Add intervals before newInterval
        i = 0
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
        
        # Phase 2: Merge overlapping intervals
        # Update newInterval to include all overlapping intervals
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        result.append([new_start, new_end])
        
        # Phase 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
    
    def insert_alternative(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach 5: Alternative Structure
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Same logic but with different loop structure.
        """
        result = []
        inserted = False
        
        for interval in intervals:
            # If newInterval comes before current interval and not inserted yet
            if newInterval[1] < interval[0] and not inserted:
                result.append(newInterval)
                inserted = True
                result.append(interval)
            # If newInterval overlaps with current interval
            elif newInterval[0] <= interval[1] and interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            # Current interval comes before newInterval
            else:
                result.append(interval)
        
        # If newInterval wasn't inserted, add it at the end
        if not inserted:
            result.append(newInterval)
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example [[1,3],[6,9]] with [2,5]")
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    expected1 = [[1,5],[6,9]]
    result1 = solution.insert(intervals1, newInterval1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Multiple overlaps
    print("Test 2: Multiple overlaps [[1,2],[3,5],[6,7],[8,10],[12,16]] with [4,8]")
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    expected2 = [[1,2],[3,10],[12,16]]
    result2 = solution.insert(intervals2, newInterval2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Empty intervals
    print("Test 3: Empty intervals [] with [5,7]")
    intervals3 = []
    newInterval3 = [5,7]
    expected3 = [[5,7]]
    result3 = solution.insert(intervals3, newInterval3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: No overlap at start
    print("Test 4: No overlap at start [[1,5]] with [0,0]")
    intervals4 = [[1,5]]
    newInterval4 = [0,0]
    expected4 = [[0,0],[1,5]]
    result4 = solution.insert(intervals4, newInterval4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: No overlap at end
    print("Test 5: No overlap at end [[1,5]] with [6,8]")
    intervals5 = [[1,5]]
    newInterval5 = [6,8]
    expected5 = [[1,5],[6,8]]
    result5 = solution.insert(intervals5, newInterval5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Complete overlap
    print("Test 6: Complete overlap [[1,5]] with [2,3]")
    intervals6 = [[1,5]]
    newInterval6 = [2,3]
    expected6 = [[1,5]]
    result6 = solution.insert(intervals6, newInterval6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Compare all approaches
    print("\nTest 7: Comparing all approaches")
    test_cases = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
        ([], [5,7]),
        ([[1,5]], [0,0]),
        ([[1,5]], [6,8]),
    ]
    
    for intervals, newInterval in test_cases:
        result1 = solution.insert(intervals, newInterval)
        result2 = solution.insert_merge_all([row[:] for row in intervals], newInterval[:])
        result3 = solution.insert_binary_search([row[:] for row in intervals], newInterval[:])
        result4 = solution.insert_explicit([row[:] for row in intervals], newInterval[:])
        result5 = solution.insert_alternative([row[:] for row in intervals], newInterval[:])
        
        assert result1 == result2, f"Merge all failed: {result1} vs {result2}"
        assert result1 == result3, f"Binary search failed: {result1} vs {result3}"
        assert result1 == result4, f"Explicit failed: {result1} vs {result4}"
        assert result1 == result5, f"Alternative failed: {result1} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 8: Single interval
    print("\nTest 8: Single interval [[1,3]] with [2,4]")
    intervals8 = [[1,3]]
    newInterval8 = [2,4]
    expected8 = [[1,4]]
    result8 = solution.insert(intervals8, newInterval8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Adjacent intervals
    print("Test 9: Adjacent intervals [[1,2],[3,5]] with [2,3]")
    intervals9 = [[1,2],[3,5]]
    newInterval9 = [2,3]
    expected9 = [[1,5]]
    result9 = solution.insert(intervals9, newInterval9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: New interval extends existing
    print("Test 10: New interval extends [[1,2],[5,6]] with [0,4]")
    intervals10 = [[1,2],[5,6]]
    newInterval10 = [0,4]
    expected10 = [[0,4],[5,6]]
    result10 = solution.insert(intervals10, newInterval10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: New interval in middle
    print("Test 11: New interval in middle [[1,2],[5,6],[9,10]] with [3,4]")
    intervals11 = [[1,2],[5,6],[9,10]]
    newInterval11 = [3,4]
    expected11 = [[1,2],[3,4],[5,6],[9,10]]
    result11 = solution.insert(intervals11, newInterval11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: New interval overlaps all
    print("Test 12: New interval overlaps all [[1,2],[3,4],[5,6]] with [0,7]")
    intervals12 = [[1,2],[3,4],[5,6]]
    newInterval12 = [0,7]
    expected12 = [[0,7]]
    result12 = solution.insert(intervals12, newInterval12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Zero values
    print("Test 13: Zero values [[0,0]] with [0,0]")
    intervals13 = [[0,0]]
    newInterval13 = [0,0]
    expected13 = [[0,0]]
    result13 = solution.insert(intervals13, newInterval13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Large intervals
    print("Test 14: Large intervals [[1,10],[20,30]] with [5,25]")
    intervals14 = [[1,10],[20,30]]
    newInterval14 = [5,25]
    expected14 = [[1,30]]
    result14 = solution.insert(intervals14, newInterval14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex case
    print("Test 15: Complex case [[1,2],[3,5],[6,7],[8,10],[12,16]] with [4,8]")
    intervals15 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval15 = [4,8]
    expected15 = [[1,2],[3,10],[12,16]]
    result15 = solution.insert(intervals15, newInterval15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()