"""
353. Design Snake Game
Difficulty: Medium

Design a Snake game that is played on a device with screen size width x height.
The snake initially occupies 1x1 space at position (0, 0) on the screen.

Implement the SnakeGame class:
- SnakeGame(int width, int height, int[][] food) Initializes the object with a screen
  of size width x height and the food positions given in array food where
  food[i] = [row_i, col_i].
- int move(String direction) Returns the score for the game after applying one direction
  move by the snake. If the game is over, return -1.

The food is eaten when the snake's head coincides with the food's position. When the
snake eats a piece of food, its length grows by 1 and the score increases by 1. If the
next food position is already occupied by the snake's body, it will appear after the
snake moves away, so the snake cannot eat it.

Rules:
- The snake starts at position (0, 0) and moves in the given direction.
- The snake can move Up (U), Down (D), Left (L), or Right (R).
- If the snake moves out of bounds or collides with its body, return -1 (game over).
- When the snake eats food, its score increases by 1 and its length grows by 1.
- The tail is removed before checking for self-collision (so moving into where the tail
  was is valid).

Example 1:
Input
["SnakeGame", "move", "move", "move", "move", "move", "move"]
[[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
Output
[null, 0, 0, 1, 1, 2, -1]

Explanation
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move("R"); // return 0
snakeGame.move("D"); // return 0
snakeGame.move("R"); // return 1, eats food at (1,2)
snakeGame.move("U"); // return 1
snakeGame.move("L"); // return 2, eats food at (0,1)
snakeGame.move("U"); // return -1, snake collides with itself

Constraints:
- 1 <= width, height <= 10^4
- 1 <= food.length <= 50
- 0 <= food[i][0] < height
- 0 <= food[i][1] < width
- direction is one of ['U', 'D', 'L', 'R']
- At most 10^4 calls will be made to move

Notes:
- Key insight: Use a deque to represent the snake body (O(1) head/tail operations)
  and a set for O(1) self-collision detection.
- The tail is conceptually removed BEFORE checking self-collision because the tail
  will vacate its cell as part of this move (unless food is eaten).
- Time complexity: O(1) per move
- Space complexity: O(width * height) for snake body in worst case
- Approaches:
  - Deque + Set: O(1) per move — deque for ordered body, set for fast collision check
  - Deque only: O(n) per move — iterate deque to check collision (simpler, slower)
- Edge cases:
  - Snake moving into the cell just vacated by its own tail (valid move)
  - Food position occupied by snake body when snake arrives (still eat it)
  - Grid of size 1x1
  - Snake fills entire grid
"""

from collections import deque
from typing import List


class SnakeGame:
    """
    Approach 1: Deque + Set (Current)
    Time Complexity: O(1) per move
    Space Complexity: O(width * height) — snake body at most fills the grid

    Use a deque to track body positions in order (head at left, tail at right).
    Use a set for O(1) self-collision detection. On each move:
    1. Compute the new head position.
    2. Check bounds — return -1 if out of bounds.
    3. Remove the tail (speculatively) from set and deque.
    4. Check self-collision — return -1 if new head is in body set.
    5. If food is at new head position, restore tail (snake grows) and advance food.
    6. Add new head to deque and set. Return current score.
    """

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize the snake game.

        Args:
            width: Number of columns in the grid.
            height: Number of rows in the grid.
            food: List of [row, col] food positions in order they appear.
        """
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.score = 0

        # Deque stores (row, col) tuples; head is at the left (index 0)
        self.body = deque([(0, 0)])
        # Set for O(1) collision detection
        self.body_set = {(0, 0)}

        self._directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }

    def move(self, direction: str) -> int:
        """
        Move the snake one step in the given direction.

        Args:
            direction: One of 'U', 'D', 'L', 'R'.

        Returns:
            Current score, or -1 if the game is over.
        """
        dr, dc = self._directions[direction]
        head_r, head_c = self.body[0]
        new_r, new_c = head_r + dr, head_c + dc

        # Check out of bounds
        if not (0 <= new_r < self.height and 0 <= new_c < self.width):
            return -1

        # Speculatively remove tail (it will move unless food is eaten)
        tail = self.body[-1]
        self.body.pop()
        self.body_set.discard(tail)

        # Check self-collision (after tail removal — tail cell is now free)
        if (new_r, new_c) in self.body_set:
            return -1

        # Check if food is eaten
        if (self.food_idx < len(self.food) and
                new_r == self.food[self.food_idx][0] and
                new_c == self.food[self.food_idx][1]):
            # Restore tail — snake grows
            self.body.append(tail)
            self.body_set.add(tail)
            self.food_idx += 1
            self.score += 1

        # Add new head
        self.body.appendleft((new_r, new_c))
        self.body_set.add((new_r, new_c))

        return self.score


class SnakeGameDequeOnly:
    """
    Approach 2: Deque Only (No Set)
    Time Complexity: O(n) per move — n is current snake length
    Space Complexity: O(width * height)

    Simpler but slower. Uses only a deque; self-collision is checked by
    scanning the deque. Fine for small grids / short snakes.
    """

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.score = 0
        self.body = deque([(0, 0)])

        self._directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }

    def move(self, direction: str) -> int:
        dr, dc = self._directions[direction]
        head_r, head_c = self.body[0]
        new_r, new_c = head_r + dr, head_c + dc

        if not (0 <= new_r < self.height and 0 <= new_c < self.width):
            return -1

        # Remove tail speculatively
        tail = self.body[-1]
        self.body.pop()

        # Self-collision check (O(n))
        if (new_r, new_c) in self.body:
            return -1

        # Eat food?
        if (self.food_idx < len(self.food) and
                new_r == self.food[self.food_idx][0] and
                new_c == self.food[self.food_idx][1]):
            self.body.append(tail)
            self.food_idx += 1
            self.score += 1

        self.body.appendleft((new_r, new_c))
        return self.score


def test_solution():
    """Test cases for the SnakeGame solution."""

    # Test 1: Example from problem statement
    print("Test 1: Problem example")
    game = SnakeGame(3, 2, [[1, 2], [0, 1]])
    assert game.move("R") == 0, "Test 1a failed"
    assert game.move("D") == 0, "Test 1b failed"
    assert game.move("R") == 1, "Test 1c failed"  # eats (1,2)
    assert game.move("U") == 1, "Test 1d failed"
    assert game.move("L") == 2, "Test 1e failed"  # eats (0,1)
    assert game.move("U") == -1, "Test 1f failed"  # self collision
    print("  Result: All moves correct ✓")

    # Test 2: Out of bounds — left wall
    print("Test 2: Out of bounds left")
    game2 = SnakeGame(3, 3, [])
    assert game2.move("L") == -1, "Test 2 failed"
    print("  Result: Returns -1 ✓")

    # Test 3: Out of bounds — top wall
    print("Test 3: Out of bounds top")
    game3 = SnakeGame(3, 3, [])
    assert game3.move("U") == -1, "Test 3 failed"
    print("  Result: Returns -1 ✓")

    # Test 4: Out of bounds — right wall
    print("Test 4: Out of bounds right")
    game4 = SnakeGame(1, 3, [])
    assert game4.move("R") == -1, "Test 4 failed"
    print("  Result: Returns -1 ✓")

    # Test 5: Out of bounds — bottom wall
    print("Test 5: Out of bounds bottom")
    game5 = SnakeGame(3, 1, [])
    assert game5.move("D") == -1, "Test 5 failed"
    print("  Result: Returns -1 ✓")

    # Test 6: No food, snake stays length 1
    print("Test 6: No food, no collision")
    game6 = SnakeGame(5, 5, [])
    assert game6.move("R") == 0
    assert game6.move("R") == 0
    assert game6.move("D") == 0
    assert game6.move("L") == 0
    print("  Result: Score stays 0 ✓")

    # Test 7: Move into tail's previous position (valid)
    print("Test 7: Move into vacated tail cell (valid)")
    # Snake at (0,0), grows right to (0,0)-(0,1)-(0,2), then turns back
    game7 = SnakeGame(5, 5, [[0, 1], [0, 2]])
    game7.move("R")  # head=(0,1), eats food → body=(0,1),(0,0), score=1
    game7.move("R")  # head=(0,2), eats food → body=(0,2),(0,1),(0,0), score=2
    # Now turn back: (0,1) is occupied but (0,0) will be vacated
    result = game7.move("L")  # head=(0,1) — occupied by body! → -1
    assert result == -1, f"Test 7 failed, got {result}"
    print("  Result: Self-collision detected ✓")

    # Test 8: Snake can move into cell just vacated by tail
    print("Test 8: Move into just-vacated tail (valid)")
    game8 = SnakeGame(4, 1, [[0, 1]])
    # Snake at (0,0), food at (0,1)
    assert game8.move("R") == 1  # eats food → body: (0,1),(0,0)
    # Now the tail is at (0,0). Moving left → new head at (0,0) = tail's current pos
    # Tail is removed first, so (0,0) is free → valid
    assert game8.move("L") == 1, "Test 8 failed"
    print("  Result: Tail vacate rule works ✓")

    # Test 9: Score accumulates correctly
    print("Test 9: Score accumulation")
    game9 = SnakeGame(10, 10, [[0, 1], [0, 2], [0, 3], [0, 4]])
    for _ in range(4):
        game9.move("R")
    assert game9.score == 4, f"Test 9 failed, score={game9.score}"
    print("  Result: Score = 4 ✓")

    # Test 10: 1x1 grid, no food — any move is out of bounds
    print("Test 10: 1x1 grid")
    game10 = SnakeGame(1, 1, [])
    assert game10.move("U") == -1
    assert game10.move("D") == -1
    assert game10.move("L") == -1
    assert game10.move("R") == -1
    print("  Result: All moves out of bounds ✓")

    # Test 11: Both approaches agree on the example
    print("Test 11: Both approaches agree")
    moves = ["R", "D", "R", "U", "L", "U"]
    food = [[1, 2], [0, 1]]

    g1 = SnakeGame(3, 2, food)
    g2 = SnakeGameDequeOnly(3, 2, food)

    for m in moves:
        r1 = g1.move(m)
        r2 = g2.move(m)
        assert r1 == r2, f"Mismatch on move {m}: {r1} vs {r2}"
    print("  Result: Both approaches match ✓")

    # Test 12: Long snake, no self-collision until forced
    print("Test 12: Long snake traversal")
    game12 = SnakeGame(5, 1, [[0, 1], [0, 2], [0, 3], [0, 4]])
    assert game12.move("R") == 1
    assert game12.move("R") == 2
    assert game12.move("R") == 3
    assert game12.move("R") == 4  # snake fills entire row
    # Any move now hits boundary
    assert game12.move("R") == -1
    print("  Result: Long snake works correctly ✓")

    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
