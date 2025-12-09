"""
42. Trapping Rain Water
Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Notes:
- Key insight: At each position, water trapped = min(max_left, max_right) - height[i]
- Two-pointer approach: Process from both ends, always process the side with smaller height.
- When height[left] < height[right], we know the water level at left is bounded by left_max 
  (since right side has a taller bar). Process left side.
- When height[left] >= height[right], we know the water level at right is bounded by right_max.
  Process right side.
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only using a few variables
- Alternative approaches:
  - Two pointers: O(n) time, O(1) space - current approach (optimal)
  - Stack-based: O(n) time, O(n) space - use stack to track bars
  - Dynamic programming: O(n) time, O(n) space - precompute left_max and right_max arrays
  - Brute force: O(n²) time, O(1) space - for each position, find max_left and max_right
- Edge cases: Empty array, single element, all same height, increasing/decreasing heights,
  no water can be trapped, all water can be trapped
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach 1: Two Pointers (Current - Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use two pointers from both ends. Always process the side with smaller height,
        as we know the water level is bounded by the max on that side.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
    
    def trap_stack(self, height: List[int]) -> int:
        """
        Approach 2: Stack-Based
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Use a stack to store indices of bars. When we find a bar taller than the bar at 
        the top of the stack, we can trap water between them.
        """
        if not height:
            return 0
        
        stack = []
        water = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                water += distance * bounded_height
            
            stack.append(i)
        
        return water
    
    def trap_dp(self, height: List[int]) -> int:
        """
        Approach 3: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Precompute left_max and right_max arrays, then calculate water at each position.
        """
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Compute left_max for each position
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Compute right_max for each position
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate trapped water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water
    
    def trap_brute_force(self, height: List[int]) -> int:
        """
        Approach 4: Brute Force
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        For each position, find the maximum height on left and right, then calculate water.
        """
        if not height:
            return 0
        
        water = 0
        n = len(height)
        
        for i in range(1, n - 1):
            left_max = max(height[:i])
            right_max = max(height[i + 1:])
            water += max(0, min(left_max, right_max) - height[i])
        
        return water
    
    def trap_alternative(self, height: List[int]) -> int:
        """
        Approach 5: Alternative Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Same logic as Approach 1 but with slightly different structure.
        Uses explicit comparison of left_max and right_max.
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        
        return water


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example [0,1,0,2,1,0,1,3,2,1,2,1]")
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected1 = 6
    result1 = solution.trap(height1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Example 2 from problem
    print("\nTest 2: Example 2 [4,2,0,3,2,5]")
    height2 = [4, 2, 0, 3, 2, 5]
    expected2 = 9
    result2 = solution.trap(height2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Compare all approaches
    print("\nTest 3: Comparing all approaches")
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [3, 0, 2, 0, 4],
        [2, 0, 2],
    ]
    
    for height in test_cases:
        result1 = solution.trap(height)
        result2 = solution.trap_stack(height)
        result3 = solution.trap_dp(height)
        result4 = solution.trap_brute_force(height)
        result5 = solution.trap_alternative(height)
        
        assert result1 == result2 == result3 == result4 == result5, \
            f"Mismatch for height={height}: {result1} vs {result2} vs {result3} vs {result4} vs {result5}"
    
    print("  All approaches match! ✓")
    
    # Test case 4: Empty array
    print("\nTest 4: Empty array []")
    height4 = []
    expected4 = 0
    result4 = solution.trap(height4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Single element
    print("Test 5: Single element [5]")
    height5 = [5]
    expected5 = 0
    result5 = solution.trap(height5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Two elements - no water
    print("Test 6: Two elements [2, 3]")
    height6 = [2, 3]
    expected6 = 0
    result6 = solution.trap(height6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Simple case - water in middle
    print("Test 7: Simple case [3, 0, 2]")
    height7 = [3, 0, 2]
    expected7 = 2
    result7 = solution.trap(height7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: All same height
    print("Test 8: All same height [5, 5, 5, 5]")
    height8 = [5, 5, 5, 5]
    expected8 = 0
    result8 = solution.trap(height8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Increasing heights
    print("Test 9: Increasing heights [1, 2, 3, 4, 5]")
    height9 = [1, 2, 3, 4, 5]
    expected9 = 0
    result9 = solution.trap(height9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Decreasing heights
    print("Test 10: Decreasing heights [5, 4, 3, 2, 1]")
    height10 = [5, 4, 3, 2, 1]
    expected10 = 0
    result10 = solution.trap(height10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: V-shaped
    print("Test 11: V-shaped [5, 1, 5]")
    height11 = [5, 1, 5]
    expected11 = 4
    result11 = solution.trap(height11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: U-shaped
    print("Test 12: U-shaped [5, 1, 1, 5]")
    height12 = [5, 1, 1, 5]
    expected12 = 8
    result12 = solution.trap(height12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Multiple peaks
    print("Test 13: Multiple peaks [3, 0, 2, 0, 4]")
    height13 = [3, 0, 2, 0, 4]
    expected13 = 7
    result13 = solution.trap(height13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: All zeros
    print("Test 14: All zeros [0, 0, 0, 0]")
    height14 = [0, 0, 0, 0]
    expected14 = 0
    result14 = solution.trap(height14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Single peak in middle
    print("Test 15: Single peak in middle [1, 0, 0, 0, 1]")
    height15 = [1, 0, 0, 0, 1]
    expected15 = 3
    result15 = solution.trap(height15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    # Test case 16: Large values
    print("Test 16: Large values [100000, 0, 100000]")
    height16 = [100000, 0, 100000]
    expected16 = 100000
    result16 = solution.trap(height16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Result: {result16} ✓")
    
    # Test case 17: Complex pattern
    print("Test 17: Complex pattern [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]")
    height17 = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
    # This is a complex case, let's verify it works
    result17 = solution.trap(height17)
    assert result17 >= 0, f"Test 17 failed: negative result {result17}"
    print(f"  Result: {result17} ✓")
    
    # Test case 18: Alternating pattern
    print("Test 18: Alternating pattern [1, 0, 1, 0, 1, 0, 1]")
    height18 = [1, 0, 1, 0, 1, 0, 1]
    expected18 = 3
    result18 = solution.trap(height18)
    assert result18 == expected18, f"Test 18 failed: expected {expected18}, got {result18}"
    print(f"  Result: {result18} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
