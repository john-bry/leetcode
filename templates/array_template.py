"""
Template for Array/String problems
"""

from typing import List, Optional


class Solution:
    """
    Problem: [Problem Name]
    Difficulty: Easy/Medium/Hard
    
    Problem Statement:
    [Describe the problem here]
    
    Example:
    Input: [example input]
    Output: [example output]
    Explanation: [explanation]
    """
    
    def method1(self, nums: List[int]) -> int:
        """
        Approach 1: [Describe approach]
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Implementation here
        pass
    
    def method2(self, nums: List[int]) -> int:
        """
        Approach 2: [Describe approach]
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Implementation here
        pass


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4, 5]
    expected1 = [expected result]
    result1 = solution.method1(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [5, 4, 3, 2, 1]
    expected2 = [expected result]
    result2 = solution.method1(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
