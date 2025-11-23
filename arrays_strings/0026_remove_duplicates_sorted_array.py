from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Approach 1: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1