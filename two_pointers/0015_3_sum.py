"""
15. 3Sum
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(n²)
        Space Complexity: O(1) excluding output array
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip duplicates for r, l
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.three_sum(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    # Sort both for comparison since order doesn't matter
    result1_sorted = sorted([sorted(triplet) for triplet in result1])
    expected1_sorted = sorted([sorted(triplet) for triplet in expected1])
    assert result1_sorted == expected1_sorted, f"Test 1 failed: expected {expected1_sorted}, got {result1_sorted}"
    
    # Test case 2
    nums2 = [0, 1, 1]
    result2 = solution.three_sum(nums2)
    expected2 = []
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [0, 0, 0]
    result3 = solution.three_sum(nums3)
    expected3 = [[0, 0, 0]]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()