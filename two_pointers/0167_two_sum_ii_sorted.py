"""
167. Two Sum II - Input Array Is Sorted
Difficulty: Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

Notes:
- Key insight: Use two pointers since the array is sorted.
- Start with left pointer at beginning and right pointer at end.
- If sum is too large, move right pointer left; if too small, move left pointer right.
- Alternative approaches include binary search and hash map, but two pointers is optimal.
- This is a classic two-pointer technique for sorted arrays.
"""

from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach 1: Two Pointers (Optimal)
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Use two pointers starting from both ends of the sorted array.
        Move pointers based on whether the current sum is too large or too small.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        
        return []  # Should never reach here given problem constraints
    
    def two_sum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach 2: Binary Search
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        For each element, binary search for the complement.
        Less efficient than two pointers but demonstrates binary search technique.
        """
        for i in range(len(numbers)):
            complement = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]  # 1-indexed
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return []
    
    def two_sum_hash_map(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach 3: Hash Map (Not optimal for this problem)
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Use hash map to store complements. Works but doesn't utilize sorted property.
        Not recommended for this problem due to O(n) space requirement.
        """
        num_map = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_map:
                return [num_map[complement] + 1, i + 1]  # 1-indexed
            num_map[num] = i
        
        return []
    
    def two_sum_optimized(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach 4: Optimized Two Pointers with Early Termination
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Optimized version with early termination conditions.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
                # Skip duplicates for slight optimization
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            else:
                left += 1
                # Skip duplicates for slight optimization
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
        
        return []


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality")
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [1, 2]
    result1 = solution.two_sum(numbers1, target1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Different target
    print("Test 2: Different target")
    numbers2 = [2, 3, 4]
    target2 = 6
    expected2 = [1, 3]
    result2 = solution.two_sum(numbers2, target2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Negative numbers
    print("Test 3: Negative numbers")
    numbers3 = [-1, 0]
    target3 = -1
    expected3 = [1, 2]
    result3 = solution.two_sum(numbers3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Large numbers
    print("Test 4: Large numbers")
    numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target4 = 19
    expected4 = [9, 10]
    result4 = solution.two_sum(numbers4, target4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Duplicate numbers
    print("Test 5: Duplicate numbers")
    numbers5 = [1, 1, 2, 2, 3, 3]
    target5 = 4
    expected5 = [1, 6]
    result5 = solution.two_sum(numbers5, target5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Small array
    print("Test 6: Small array")
    numbers6 = [1, 2]
    target6 = 3
    expected6 = [1, 2]
    result6 = solution.two_sum(numbers6, target6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_numbers = [2, 7, 11, 15]
    test_target = 9
    
    result_two_pointers = solution.two_sum(test_numbers, test_target)
    result_binary = solution.two_sumBinarySearch(test_numbers, test_target)
    result_hash = solution.two_sumHashMap(test_numbers, test_target)
    result_opt = solution.two_sumOptimized(test_numbers, test_target)
    
    expected = [1, 2]
    assert result_two_pointers == expected, f"Test 7.1 two pointers failed: expected {expected}, got {result_two_pointers}"
    assert result_binary == expected, f"Test 7.2 binary search failed: expected {expected}, got {result_binary}"
    assert result_hash == expected, f"Test 7.3 hash map failed: expected {expected}, got {result_hash}"
    assert result_opt == expected, f"Test 7.4 optimized failed: expected {expected}, got {result_opt}"
    
    # Test case 8: Edge case - minimum length
    print("Test 8: Edge case - minimum length")
    numbers8 = [1, 2]
    target8 = 3
    expected8 = [1, 2]
    result8 = solution.two_sum(numbers8, target8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Negative target
    print("Test 9: Negative target")
    numbers9 = [-3, -2, -1, 0, 1, 2, 3]
    target9 = -5
    expected9 = [1, 2]
    result9 = solution.two_sum(numbers9, target9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    # Test case 10: Large array
    print("Test 10: Large array")
    numbers10 = list(range(1, 1001))
    target10 = 1999
    expected10 = [999, 1000]
    result10 = solution.two_sum(numbers10, target10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()