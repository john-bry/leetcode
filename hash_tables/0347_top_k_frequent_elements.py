"""
347. Top K Frequent Elements
Difficulty: Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: The two most frequent elements are 1 (appears 3 times) and 2 (appears 2 times).

Example 2:
Input: nums = [1], k = 1
Output: [1]
Explanation: The only element appears once.

Example 3:
Input: nums = [1,2], k = 2
Output: [1,2]
Explanation: Both elements appear once, so both are in the top 2.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Notes:
- Key insight: We need to find the k elements with highest frequency.
- Hash map + sorting approach: Count frequencies, then sort by frequency - O(n log n) time, O(n) space.
- Heap approach: Use min heap of size k to maintain top k elements - O(n log k) time, O(n) space.
- Bucket sort approach: Use frequency as index in array - O(n) time, O(n) space (optimal).
- The heap approach is better when k << n (much smaller than total unique elements).
- The bucket sort approach is optimal for time complexity but requires knowing max frequency.
- For this problem, heap or bucket sort are preferred over sorting all elements.
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Hash Map with Counter + Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # Count the frequency of each number
        count = Counter(nums)

        # Sort the numbers by frequency
        sorted_list = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Return the top k numbers
        return [num for num, _ in sorted_list[:k]]
    
    def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Hash Map + Min Heap
        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        
        # Use min heap of size k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove smallest frequency
        
        # Extract numbers from heap
        return [num for _, num in heap]
    
    def top_k_frequent_bucket(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Bucket Sort
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        max_freq = max(count.values())
        
        # Create buckets: index = frequency, value = list of numbers
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Extract top k from buckets (from highest frequency to lowest)
        result = []
        for i in range(max_freq, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    break
        
        return result[:k]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.top_k_frequent(nums1, k1)
    result1_sorted = sorted(result1)
    expected1 = [1, 2]
    expected1_sorted = sorted(expected1)
    assert result1_sorted == expected1_sorted, f"Test 1 failed: expected {expected1_sorted}, got {result1_sorted}"
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    result2 = solution.top_k_frequent(nums2, k2)
    expected2 = [1]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [1, 2]
    k3 = 2
    result3 = solution.top_k_frequent(nums3, k3)
    result3_sorted = sorted(result3)
    expected3 = [1, 2]
    expected3_sorted = sorted(expected3)
    assert result3_sorted == expected3_sorted, f"Test 3 failed: expected {expected3_sorted}, got {result3_sorted}"
    
    # Test case 4 - all same frequency
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    result4 = solution.top_k_frequent(nums4, k4)
    result4_sorted = sorted(result4)
    expected4 = [1, 2, 3]  # Any 3 elements since all have frequency 1
    assert len(result4) == k4, f"Test 4 failed: expected length {k4}, got {len(result4)}"
    
    # Test case 5 - one element appears many times
    nums5 = [1, 1, 1, 1, 2, 2, 3]
    k5 = 2
    result5 = solution.top_k_frequent(nums5, k5)
    result5_sorted = sorted(result5)
    expected5 = [1, 2]
    expected5_sorted = sorted(expected5)
    assert result5_sorted == expected5_sorted, f"Test 5 failed: expected {expected5_sorted}, got {result5_sorted}"
    
    # Test case 6 - negative numbers
    nums6 = [-1, -1, -2, -2, -3]
    k6 = 2
    result6 = solution.top_k_frequent(nums6, k6)
    result6_sorted = sorted(result6)
    expected6 = [-1, -2]
    expected6_sorted = sorted(expected6)
    assert result6_sorted == expected6_sorted, f"Test 6 failed: expected {expected6_sorted}, got {result6_sorted}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()