"""
46. Permutations
Difficulty: Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

Notes:
- Key insight: Use backtracking to build permutations by choosing unused elements.
- Variants: Iterative insertion method; Heap's algorithm.
- Ensure no duplicates by using distinct inputs or tracking used positions.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 1: Backtracking (original style)
        Time Complexity: O(n · n!) – there are n! permutations and building each takes O(n)
        Space Complexity: O(n) for recursion and path storage (output excluded)
        """
        if not nums:
            return []

        permutations: List[List[int]] = []

        def backtrack(current: List[int]) -> None:
            if len(current) == len(nums):
                permutations.append(current[:])
                return

            for num in nums:
                # original approach: skip numbers already used in current path
                if num in current:
                    continue
                current.append(num)
                backtrack(current)
                current.pop()

        backtrack([])
        return permutations
    
    def permute_insertion(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 2: Iterative Insertion
        Time Complexity: O(n · n!)
        Space Complexity: O(n · n!) for the list of permutations
        
        Build permutations by inserting each number into all positions of existing permutations.
        """
        permutations: List[List[int]] = [[]]
        for num in nums:
            new_perms: List[List[int]] = []
            for perm in permutations:
                for pos in range(len(perm) + 1):
                    new_perms.append(perm[:pos] + [num] + perm[pos:])
            permutations = new_perms
        return permutations
    
    def permute_heaps(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 3: Heap's Algorithm (in-place generation)
        Time Complexity: O(n · n!)
        Space Complexity: O(n) excluding output (uses recursion depth n)
        """
        result: List[List[int]] = []
        arr = nums[:]
        n = len(arr)
        
        def generate(k: int) -> None:
            if k == 1:
                result.append(arr[:])
                return
            
            generate(k - 1)
            for i in range(k - 1):
                if k % 2 == 0:
                    arr[i], arr[k - 1] = arr[k - 1], arr[i]
                else:
                    arr[0], arr[k - 1] = arr[k - 1], arr[0]
                generate(k - 1)
        
        generate(n)
        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic [1,2,3]
    print("Test 1: Basic [1,2,3]")
    nums1 = [1, 2, 3]
    expected1 = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1],
    ]
    result1 = solution.permute(nums1)
    assert sorted(result1) == sorted(expected1), f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Two elements
    print("Test 2: Two elements")
    nums2 = [0, 1]
    expected2 = [[0, 1], [1, 0]]
    result2 = solution.permute(nums2)
    assert sorted(result2) == sorted(expected2), f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single element
    print("Test 3: Single element")
    nums3 = [1]
    expected3 = [[1]]
    result3 = solution.permute(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Compare approaches
    print("Test 4: Compare approaches")
    nums4 = [1, 2, 3]
    expected4 = expected1
    res_backtrack = solution.permute(nums4)
    res_insertion = solution.permute_insertion(nums4)
    res_heaps = solution.permute_heaps(nums4)
    assert sorted(res_backtrack) == sorted(expected4), "Backtracking mismatch"
    assert sorted(res_insertion) == sorted(expected4), "Insertion mismatch"
    assert sorted(res_heaps) == sorted(expected4), "Heap's algorithm mismatch"
    
    # Test case 5: Larger n within constraints
    print("Test 5: Larger n within constraints")
    nums5 = [1, 2, 3, 4]
    res5 = solution.permute(nums5)
    assert len(res5) == 24, f"Test 5 failed: expected 24 permutations, got {len(res5)}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()