"""
238. Product of Array Except Self
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- For index 0: product of all elements except nums[0] = 2 * 3 * 4 = 24
- For index 1: product of all elements except nums[1] = 1 * 3 * 4 = 12
- For index 2: product of all elements except nums[2] = 1 * 2 * 4 = 8
- For index 3: product of all elements except nums[3] = 1 * 2 * 3 = 6

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation: 
- For index 0: product = 1 * 0 * -3 * 3 = 0
- For index 1: product = -1 * 0 * -3 * 3 = 0
- For index 2: product = -1 * 1 * -3 * 3 = 9
- For index 3: product = -1 * 1 * 0 * 3 = 0
- For index 4: product = -1 * 1 * 0 * -3 = 0

Example 3:
Input: nums = [2,3,4,5]
Output: [60,40,30,24]
Explanation: 
- For index 0: product = 3 * 4 * 5 = 60
- For index 1: product = 2 * 4 * 5 = 40
- For index 2: product = 2 * 3 * 5 = 30
- For index 3: product = 2 * 3 * 4 = 24

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Notes:
- Key insight: For each index i, we need the product of all elements before i and all elements after i.
- Two-pass approach: 
  - First pass: Calculate left products (product of all elements to the left of each index)
  - Second pass: Calculate right products and multiply with left products
- Time complexity: O(n) - two passes through the array
- Space complexity: O(1) - output array doesn't count as extra space, only using a few variables
- Cannot use division operator, so we can't calculate total product and divide by each element.
- The two-pass approach is optimal and avoids division.
- Alternative approach: Use two arrays (left and right products), but that uses O(n) extra space.
"""

from typing import List


class Solution:
    def product_array_except_self(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pass (Left and Right Products)
        Time Complexity: O(n)
        Space Complexity: O(1) excluding output array
        """
        res, prod = [], 1

        for i in range(len(nums)):
            res.append(prod)
            prod *= nums[i]

        prod = 1

        for j in range(len(nums) - 1, -1, -1):
            res[j] *= prod
            prod *= nums[j]

        return res
    
    def product_except_self_extra_space(self, nums: List[int]) -> List[int]:
        """
        Approach: Using Left and Right Arrays
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n
        
        # Calculate left products
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Calculate right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Multiply left and right products
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    result1 = solution.product_array_except_self(nums1)
    expected1 = [24, 12, 8, 6]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.product_array_except_self(nums2)
    expected2 = [0, 0, 9, 0, 0]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [2, 3, 4, 5]
    result3 = solution.product_array_except_self(nums3)
    expected3 = [60, 40, 30, 24]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - two elements
    nums4 = [2, 3]
    result4 = solution.product_array_except_self(nums4)
    expected4 = [3, 2]
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - negative numbers
    nums5 = [-1, -2, -3]
    result5 = solution.product_array_except_self(nums5)
    expected5 = [6, 3, 2]
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - contains zero
    nums6 = [1, 0, 2, 3]
    result6 = solution.product_array_except_self(nums6)
    expected6 = [0, 6, 0, 0]
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()