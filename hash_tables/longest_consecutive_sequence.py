"""
128. Longest Consecutive Sequence
Difficulty: Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.

Example 3:
Input: nums = [1,0,1,2]
Output: 3
Explanation: The longest consecutive elements sequence is [0, 1, 2]. Therefore its length is 3.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Notes:
- Key insight: Use a hash set to check if consecutive numbers exist in O(1) time.
- Only start counting from the beginning of a sequence (when num - 1 is not in the set).
- This ensures each number is visited at most twice (once when checking if it's a start, once when counting), giving O(n) time.
- Time complexity: O(n) - each number is visited at most twice.
- Space complexity: O(n) - hash set to store all numbers.
- Alternative approach: Sort the array first, then find longest consecutive sequence - O(n log n) time, O(1) space.
- The hash set approach is optimal for time complexity.
"""

from typing import List


class Solution:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        """
        Approach: Hash Set (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        num_set = set(nums)
        longest = 1

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                cur = num
                cur_len = 1
                # Count consecutive numbers forward
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                    
                longest = max(longest, cur_len)

        return longest
    
    def longest_consecutive_sort(self, nums: List[int]) -> int:
        """
        Approach: Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        current = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i - 1]:
                continue
            # Check if consecutive
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        
        return max(longest, current)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longest_consecutive_sequence(nums1)
    expected1 = 4
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longest_consecutive_sequence(nums2)
    expected2 = 9
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [1, 0, 1, 2]
    result3 = solution.longest_consecutive_sequence(nums3)
    expected3 = 3
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - empty array
    nums4 = []
    result4 = solution.longest_consecutive_sequence(nums4)
    expected4 = 0
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - single element
    nums5 = [1]
    result5 = solution.longest_consecutive_sequence(nums5)
    expected5 = 1
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - no consecutive sequence
    nums6 = [1, 3, 5, 7, 9]
    result6 = solution.longest_consecutive_sequence(nums6)
    expected6 = 1
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - negative numbers
    nums7 = [-1, -2, -3, 0, 1]
    result7 = solution.longest_consecutive_sequence(nums7)
    expected7 = 5
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    # Test case 8 - duplicates
    nums8 = [1, 2, 0, 1]
    result8 = solution.longest_consecutive_sequence(nums8)
    expected8 = 3
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()