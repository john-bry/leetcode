"""
704. Binary Search
Difficulty: Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i] < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
- -10^4 < target < 10^4

Notes:
- Key insight: Classic binary search on a sorted array.
- Use two pointers (left and right) and repeatedly narrow down the search space.
- Calculate mid index using `left + (right - left) // 2` to avoid integer overflow.
- Time complexity: O(log n) where n is the length of the array
- Space complexity: O(1) - only using a few variables
- Alternative approaches:
  - Iterative binary search: O(log n) time, O(1) space - current approach (optimal)
  - Recursive binary search: O(log n) time, O(log n) space - uses recursion stack
  - Linear search: O(n) time, O(1) space - too slow for large arrays
- Edge cases: Empty array, single element, target at first/last position, 
  target not in array, target smaller than all, target larger than all
- Important: The while condition should be `left <= right` to check the last position.
  Using `left < right` will miss the case when left == right.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach: Iterative Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Use two pointers to narrow down the search space by half at each step.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Avoid integer overflow
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    
    def search_recursive(self, nums: List[int], target: int) -> int:
        """
        Approach 2: Recursive Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        
        Recursive version of binary search.
        """
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return binary_search(mid + 1, right)
        
        return binary_search(0, len(nums) - 1)
    
    def search_alternative(self, nums: List[int], target: int) -> int:
        """
        Approach 3: Alternative Iterative Implementation
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Same logic but with slightly different variable names.
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            center = (lo + hi) // 2
            
            if nums[center] == target:
                return center
            elif nums[center] < target:
                lo = center + 1
            else:
                hi = center - 1
        
        return -1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example [-1,0,3,5,9,12], target=9")
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    expected1 = 4
    result1 = solution.search(nums1, target1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Target not in array
    print("\nTest 2: Target not in array [-1,0,3,5,9,12], target=2")
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    expected2 = -1
    result2 = solution.search(nums2, target2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Compare all approaches
    print("\nTest 3: Comparing all approaches")
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 6),
    ]
    
    for nums, target in test_cases:
        result1 = solution.search(nums, target)
        result2 = solution.search_recursive(nums, target)
        result3 = solution.search_alternative(nums, target)
        
        assert result1 == result2 == result3, \
            f"Mismatch for nums={nums}, target={target}: {result1} vs {result2} vs {result3}"
    
    print("  All approaches match! ✓")
    
    # Test case 4: Single element - target found
    print("\nTest 4: Single element - target found [5], target=5")
    nums4 = [5]
    target4 = 5
    expected4 = 0
    result4 = solution.search(nums4, target4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single element - target not found
    print("Test 5: Single element - target not found [5], target=3")
    nums5 = [5]
    target5 = 3
    expected5 = -1
    result5 = solution.search(nums5, target5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Target at first position
    print("Test 6: Target at first position [1,2,3,4,5], target=1")
    nums6 = [1, 2, 3, 4, 5]
    target6 = 1
    expected6 = 0
    result6 = solution.search(nums6, target6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Target at last position
    print("Test 7: Target at last position [1,2,3,4,5], target=5")
    nums7 = [1, 2, 3, 4, 5]
    target7 = 5
    expected7 = 4
    result7 = solution.search(nums7, target7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Target smaller than all elements
    print("Test 8: Target smaller than all [1,2,3,4,5], target=0")
    nums8 = [1, 2, 3, 4, 5]
    target8 = 0
    expected8 = -1
    result8 = solution.search(nums8, target8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Target larger than all elements
    print("Test 9: Target larger than all [1,2,3,4,5], target=10")
    nums9 = [1, 2, 3, 4, 5]
    target9 = 10
    expected9 = -1
    result9 = solution.search(nums9, target9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Two elements - target found
    print("Test 10: Two elements - target found [1,3], target=1")
    nums10 = [1, 3]
    target10 = 1
    expected10 = 0
    result10 = solution.search(nums10, target10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Two elements - target found at second
    print("Test 11: Two elements - target found at second [1,3], target=3")
    nums11 = [1, 3]
    target11 = 3
    expected11 = 1
    result11 = solution.search(nums11, target11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Two elements - target not found
    print("Test 12: Two elements - target not found [1,3], target=2")
    nums12 = [1, 3]
    target12 = 2
    expected12 = -1
    result12 = solution.search(nums12, target12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Negative numbers
    print("Test 13: Negative numbers [-5,-3,-1,0,2,4], target=-3")
    nums13 = [-5, -3, -1, 0, 2, 4]
    target13 = -3
    expected13 = 1
    result13 = solution.search(nums13, target13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Large array
    print("Test 14: Large array (1000 elements)")
    nums14 = list(range(1, 1001))
    target14 = 500
    expected14 = 499  # Index of 500 in 1-indexed array
    result14 = solution.search(nums14, target14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Target at middle
    print("Test 15: Target at middle [1,2,3,4,5], target=3")
    nums15 = [1, 2, 3, 4, 5]
    target15 = 3
    expected15 = 2
    result15 = solution.search(nums15, target15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Odd length array
    print("Test 16: Odd length array [1,2,3,4,5,6,7], target=4")
    nums16 = [1, 2, 3, 4, 5, 6, 7]
    target16 = 4
    expected16 = 3
    result16 = solution.search(nums16, target16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    # Test case 17: Even length array
    print("Test 17: Even length array [1,2,3,4,5,6], target=3")
    nums17 = [1, 2, 3, 4, 5, 6]
    target17 = 3
    expected17 = 2
    result17 = solution.search(nums17, target17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    print(f"  Result: {result17} ✓")
    
    # Test case 18: Duplicate values (though problem says unique, test edge case)
    print("Test 18: All same values [5,5,5,5,5], target=5")
    nums18 = [5, 5, 5, 5, 5]
    target18 = 5
    # Should return one of the indices (implementation may vary)
    result18 = solution.search(nums18, target18)
    assert 0 <= result18 < len(nums18), f"Test 18 failed: invalid index {result18}"
    assert nums18[result18] == target18, f"Test 18 failed: wrong value at index {result18}"
    print(f"  Result: {result18} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
