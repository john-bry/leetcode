class Solution:
    def find_all_duplicates_in_array(self, nums: List[int]) -> List[int]:
        """
        Approach 1: Hash Table (Current)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1

                if seen[num] == 2:
                    result.append(num)

            else:
                seen[num] = 1

        return result

    def find_all_duplicates_in_array_optimized(self, nums: List[int]) -> List[int]:
        """
        Approach 2: Hash Table (Optimized)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1

                if seen[num] == 2:
                    result.append(num)

            else:
                seen[num] = 1

        return result