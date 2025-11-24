from typing import List

class Solution:
    def valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Approach 1: Hash Table
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(rows)):
            for c in range(len(cols)):
                if board[r][c] == '.':
                    continue

                num = board[r][c]

                box_idx = (r // 3) * 3 + (c // 3)

                if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

        return True