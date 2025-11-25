"""
278. First Bad Version
Difficulty: Easy

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions 
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number 
of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1

Notes:
- Key insight: Once a version is bad, all subsequent versions are also bad.
- This is a binary search problem to find the leftmost bad version.
- Use binary search with left boundary search pattern.
- Time complexity: O(log n) - binary search
- Space complexity: O(1) - only using variables
- Alternative approaches:
  - Binary search (left boundary): O(log n) time, O(1) space - optimal
  - Linear search: O(n) time, O(1) space - check each version sequentially
  - Alternative binary search: O(log n) time, O(1) space - different boundary handling
- Edge cases: First version is bad, last version is bad, all versions are bad
"""

import os
import sys
from typing import Callable

# Add the utils directory to the path so we can import our data structures
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))


# Mock implementation of isBadVersion API for testing
# In the actual LeetCode problem, this is provided by the platform
def create_is_bad_version(bad_version: int) -> Callable[[int], bool]:
    """Create a mock isBadVersion function for testing"""
    def is_bad_version(version: int) -> bool:
        return version >= bad_version
    return is_bad_version


class Solution:
    def first_bad_version(self, n: int, is_bad_version: Callable[[int], bool]) -> int:
        """
        Approach 1: Binary Search - Left Boundary (Current)
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Use binary search to find the leftmost bad version.
        If mid is bad, search left (including mid).
        If mid is good, search right (excluding mid).
        """
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2  # Avoid overflow
            
            if is_bad_version(mid):
                right = mid  # Search left, including mid
            else:
                left = mid + 1  # Search right, excluding mid
        
        return left
    
    def first_bad_version_alternative(self, n: int, is_bad_version: Callable[[int], bool]) -> int:
        """
        Approach 2: Alternative Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Similar approach but with different boundary conditions.
        """
        left, right = 1, n
        result = n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if is_bad_version(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
    def first_bad_version_linear(self, n: int, is_bad_version: Callable[[int], bool]) -> int:
        """
        Approach 3: Linear Search
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Check each version sequentially until finding the first bad one.
        Not optimal but simple to understand.
        """
        for version in range(1, n + 1):
            if is_bad_version(version):
                return version
        return n  # Should never reach here
    
    def first_bad_version_recursive(self, n: int, is_bad_version: Callable[[int], bool]) -> int:
        """
        Approach 4: Recursive Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(log n) for recursion stack
        
        Recursive version of binary search.
        Less efficient due to recursion overhead.
        """
        def search(left: int, right: int) -> int:
            if left >= right:
                return left
            
            mid = left + (right - left) // 2
            
            if is_bad_version(mid):
                return search(left, mid)
            else:
                return search(mid + 1, right)
        
        return search(1, n)
    
    def first_bad_version_optimized(self, n: int, is_bad_version: Callable[[int], bool]) -> int:
        """
        Approach 5: Optimized Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Same as approach 1 but with explicit comments and variable names.
        """
        first_bad = n
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if is_bad_version(mid):
                first_bad = mid
                right = mid - 1  # Continue searching left
            else:
                left = mid + 1  # Search right
        
        return first_bad


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example n=5, bad=4
    print("Test 1: n=5, bad=4")
    is_bad1 = create_is_bad_version(4)
    expected1 = 4
    result1 = solution.first_bad_version(5, is_bad1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Result: {result1} ✓")
    
    # Test case 2: First version is bad n=1, bad=1
    print("Test 2: n=1, bad=1")
    is_bad2 = create_is_bad_version(1)
    expected2 = 1
    result2 = solution.first_bad_version(1, is_bad2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Last version is bad n=5, bad=5
    print("Test 3: n=5, bad=5")
    is_bad3 = create_is_bad_version(5)
    expected3 = 5
    result3 = solution.first_bad_version(5, is_bad3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Middle version is bad n=10, bad=5
    print("Test 4: n=10, bad=5")
    is_bad4 = create_is_bad_version(5)
    expected4 = 5
    result4 = solution.first_bad_version(10, is_bad4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Large n, early bad version n=100, bad=3
    print("Test 5: n=100, bad=3")
    is_bad5 = create_is_bad_version(3)
    expected5 = 3
    result5 = solution.first_bad_version(100, is_bad5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Result: {result5} ✓")
    
    # Test case 6: Large n, late bad version n=1000, bad=999
    print("Test 6: n=1000, bad=999")
    is_bad6 = create_is_bad_version(999)
    expected6 = 999
    result6 = solution.first_bad_version(1000, is_bad6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Compare all approaches
    print("\nTest 7: Comparing all approaches")
    test_cases = [
        (5, 4),
        (1, 1),
        (10, 5),
        (100, 50),
        (1000, 1),
        (1000, 1000),
    ]
    
    for n, bad in test_cases:
        is_bad = create_is_bad_version(bad)
        expected = bad
        
        result1 = solution.first_bad_version(n, is_bad)
        result2 = solution.first_bad_version_alternative(n, create_is_bad_version(bad))
        result3 = solution.first_bad_version_linear(n, create_is_bad_version(bad))
        result4 = solution.first_bad_version_recursive(n, create_is_bad_version(bad))
        result5 = solution.first_bad_version_optimized(n, create_is_bad_version(bad))
        
        assert result1 == expected, f"Binary search failed for n={n}, bad={bad}: {result1} vs {expected}"
        assert result2 == expected, f"Alternative failed for n={n}, bad={bad}: {result2} vs {expected}"
        assert result3 == expected, f"Linear failed for n={n}, bad={bad}: {result3} vs {expected}"
        assert result4 == expected, f"Recursive failed for n={n}, bad={bad}: {result4} vs {expected}"
        assert result5 == expected, f"Optimized failed for n={n}, bad={bad}: {result5} vs {expected}"
    
    print("  All approaches match! ✓")
    
    # Test case 8: Very large n
    print("\nTest 8: Very large n=10000, bad=5000")
    is_bad8 = create_is_bad_version(5000)
    expected8 = 5000
    result8 = solution.first_bad_version(10000, is_bad8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Two versions, first is bad
    print("Test 9: n=2, bad=1")
    is_bad9 = create_is_bad_version(1)
    expected9 = 1
    result9 = solution.first_bad_version(2, is_bad9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Two versions, second is bad
    print("Test 10: n=2, bad=2")
    is_bad10 = create_is_bad_version(2)
    expected10 = 2
    result10 = solution.first_bad_version(2, is_bad10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Three versions, middle is bad
    print("Test 11: n=3, bad=2")
    is_bad11 = create_is_bad_version(2)
    expected11 = 2
    result11 = solution.first_bad_version(3, is_bad11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: All versions are bad (edge case)
    print("Test 12: n=10, bad=1 (all bad)")
    is_bad12 = create_is_bad_version(1)
    expected12 = 1
    result12 = solution.first_bad_version(10, is_bad12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Odd number of versions
    print("Test 13: n=7, bad=4")
    is_bad13 = create_is_bad_version(4)
    expected13 = 4
    result13 = solution.first_bad_version(7, is_bad13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Even number of versions
    print("Test 14: n=8, bad=5")
    is_bad14 = create_is_bad_version(5)
    expected14 = 5
    result14 = solution.first_bad_version(8, is_bad14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Count API calls (verify efficiency)
    print("Test 15: Count API calls for efficiency")
    call_count = [0]
    
    def counting_is_bad(version: int) -> bool:
        call_count[0] += 1
        return version >= 50
    
    result15 = solution.first_bad_version(100, counting_is_bad)
    assert result15 == 50, f"Test 15 failed: expected 50, got {result15}"
    # Binary search should make at most log2(100) ≈ 7 calls
    assert call_count[0] <= 10, f"Test 15 failed: Too many API calls: {call_count[0]}"
    print(f"  Result: {result15} found in {call_count[0]} API calls ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()