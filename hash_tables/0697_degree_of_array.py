class Solution:
    def find_shortest_subarray(self, nums: List[int]) -> int:
        """
        Approach 1: Hash Table (Current)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        first, last, count = {}, {}, {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())

        min_len = len(nums)

        for num, count in count.items():
            if count == degree:
                cur_len = last[num] - first[num] + 1
                min_len = min(min_len, cur_len)
            
        return min_len