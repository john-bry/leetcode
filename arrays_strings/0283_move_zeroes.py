class Solution:
    def move_zeroes(self, digits: List[int]) -> List[int]:
        """
        Approach 1: Iterative
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums