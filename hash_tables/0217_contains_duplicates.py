"""
217. Contains Duplicate
Difficulty: Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The value 1 appears twice in the array.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All values are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Explanation: Multiple values appear more than once.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Notes:
- Key insight: We need to detect if any element appears more than once.
- Hash set approach: Use a set to track seen elements. If we encounter an element already in the set, return true.
- Time complexity: O(n) - single pass through array.
- Space complexity: O(n) - set can contain up to n elements in worst case.
- Alternative approaches:
  - Sorting: Sort array first, then check adjacent elements - O(n log n) time, O(1) space.
  - Using set length: Convert to set and compare lengths - O(n) time, O(n) space, but more Pythonic.
- The hash set approach is optimal for time complexity while maintaining readability.
"""

from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Approach: Hash Set
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        
        for num in nums:
            if num in seen:
                return True
            
            seen[num] = True

        return False
    
    def contains_duplicate_set(self, nums: List[int]) -> bool:
        """
        Approach: Set Length Comparison (More Pythonic)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return len(nums) != len(set(nums))
    
    def contains_duplicate_sort(self, nums: List[int]) -> bool:
        """
        Approach: Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1]
    result1 = solution.contains_duplicate(nums1)
    expected1 = True
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    result2 = solution.contains_duplicate(nums2)
    expected2 = False
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = solution.contains_duplicate(nums3)
    expected3 = True
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - single element
    nums4 = [1]
    result4 = solution.contains_duplicate(nums4)
    expected4 = False
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - two identical elements
    nums5 = [1, 1]
    result5 = solution.contains_duplicate(nums5)
    expected5 = True
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
