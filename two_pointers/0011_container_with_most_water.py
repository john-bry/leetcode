"""
11. Container With Most Water
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
Explanation: The container formed by the two lines has area = 1 * 1 = 1.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Notes:
- Key insight: Use two pointers starting from both ends of the array.
- Two pointers approach:
  - Start with left pointer at 0 and right pointer at n-1
  - Calculate area: width * min(height[left], height[right])
  - Move the pointer with the smaller height inward (greedy approach)
  - This is optimal because moving the larger height pointer can only decrease the area
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using two pointers
- Alternative approach: Brute force checking all pairs - O(n²) time, O(1) space.
- The two pointers approach is optimal for this problem.
"""

from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        """
        Approach: Two Pointers (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area
    
    def max_area_brute_force(self, height: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        
        return max_area


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.max_area(height1)
    expected1 = 49
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    height2 = [1, 1]
    result2 = solution.max_area(height2)
    expected2 = 1
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3 - two elements with different heights
    height3 = [1, 2]
    result3 = solution.max_area(height3)
    expected3 = 1
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4 - increasing heights
    height4 = [1, 2, 3, 4, 5]
    result4 = solution.max_area(height4)
    expected4 = 6  # (4-0) * min(1, 5) = 4 * 1 = 4, or (4-1) * min(2, 5) = 3 * 2 = 6
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5 - decreasing heights
    height5 = [5, 4, 3, 2, 1]
    result5 = solution.max_area(height5)
    expected5 = 6  # (4-0) * min(5, 1) = 4 * 1 = 4, or (4-1) * min(4, 1) = 3 * 1 = 3, or (3-0) * min(5, 2) = 3 * 2 = 6
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6 - all same height
    height6 = [3, 3, 3, 3, 3]
    result6 = solution.max_area(height6)
    expected6 = 12  # (4-0) * 3 = 12
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7 - contains zeros
    height7 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result7 = solution.max_area(height7)
    expected7 = 9  # Various combinations possible
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()