class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def partition_string(self, s: str) -> List[str]:
        seen = set()
        partition = ''
        partitions = []

        for char in s:
            partition += char

            if partition not in seen:
                seen.add(partition)
                partitions.append(partition)
                partition = ''

        return partitions



            

            