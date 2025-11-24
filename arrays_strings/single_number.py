from collections import Counter
from typing import List

class Solution:
    def single_number(self, nums: List[int]) -> int:
        """
        Approach 1: Counter
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        return count.most_common()[-1][0]   