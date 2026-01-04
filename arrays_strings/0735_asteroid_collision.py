"""
735. Asteroid Collision
Difficulty: Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one 
will explode. If both are the same size, both will explode. Two asteroids moving in the same 
direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide, but -5 is larger. Then 10 and -5 collide, and 10 wins.

Example 4:
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The asteroids are all moving in the same direction, so no collisions occur.

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

Notes:
- Key insight: Only collisions occur when a positive asteroid (moving right) is followed by a 
  negative asteroid (moving left), i.e., stack[-1] > 0 and asteroid < 0
- Stack-based approach: Use a stack to simulate collisions
- When collision occurs:
  - If right asteroid (stack top) is smaller: pop it and continue checking
  - If both are equal: pop stack and don't add current asteroid
  - If right asteroid is larger: don't add current asteroid (it explodes)
- Time complexity: O(n) where n is number of asteroids
- Space complexity: O(n) for the stack
- Edge cases: All positive, all negative, alternating directions, equal sizes
- Alternative approaches:
  1. Stack-based simulation (current) - O(n) time, O(n) space
  2. Two-pointer approach - O(n) time, O(n) space
  3. Recursive approach - O(n²) worst case, O(n) space
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Approach 1: Stack-based Simulation (Current)
        Time Complexity: O(n) where n is number of asteroids
        Space Complexity: O(n) for the stack
        
        Use a stack to simulate asteroid collisions. When a negative asteroid (moving left)
        encounters a positive asteroid (moving right) on the stack, handle the collision.
        """
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue

                elif stack[-1] == -asteroid: 
                    stack.pop()

                break

            else:
                stack.append(asteroid)

        return stack
    
    def asteroidCollisionExplicit(self, asteroids: List[int]) -> List[int]:
        """
        Approach 2: Stack-based with Explicit Logic
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        More explicit version of the stack approach with clearer collision handling.
        """
        stack = []
        
        for asteroid in asteroids:
            # Keep processing collisions while there's a collision
            while stack and stack[-1] > 0 and asteroid < 0:
                # Collision detected: positive (right) vs negative (left)
                if abs(stack[-1]) < abs(asteroid):
                    # Right asteroid is smaller, remove it and continue
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    # Both are equal, both explode
                    stack.pop()
                    asteroid = None  # Don't add this asteroid
                    break
                else:
                    # Right asteroid is larger, current asteroid explodes
                    asteroid = None  # Don't add this asteroid
                    break
            
            # Add asteroid if it survived
            if asteroid is not None:
                stack.append(asteroid)
        
        return stack
    
    def asteroidCollisionTwoPass(self, asteroids: List[int]) -> List[int]:
        """
        Approach 3: Two-Pass Simulation
        Time Complexity: O(n²) worst case
        Space Complexity: O(n)
        
        Simulate collisions in multiple passes until no more collisions occur.
        Less efficient but more straightforward conceptually.
        """
        result = asteroids[:]
        changed = True
        
        while changed:
            changed = False
            new_result = []
            i = 0
            
            while i < len(result):
                # Check if current and next will collide
                if i < len(result) - 1 and result[i] > 0 and result[i + 1] < 0:
                    # Collision!
                    changed = True
                    if abs(result[i]) > abs(result[i + 1]):
                        # Left asteroid wins
                        new_result.append(result[i])
                    elif abs(result[i]) < abs(result[i + 1]):
                        # Right asteroid wins
                        new_result.append(result[i + 1])
                    # If equal, both explode (don't add either)
                    i += 2
                else:
                    # No collision, keep asteroid
                    new_result.append(result[i])
                    i += 1
            
            result = new_result
        
        return result
    
    def asteroidCollisionRecursive(self, asteroids: List[int]) -> List[int]:
        """
        Approach 4: Recursive Approach
        Time Complexity: O(n²) worst case
        Space Complexity: O(n) for recursion stack
        
        Recursively process collisions. Less efficient but demonstrates recursive thinking.
        """
        if len(asteroids) <= 1:
            return asteroids
        
        # Find first collision
        for i in range(len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i + 1] < 0:
                # Collision at positions i and i+1
                left_size = abs(asteroids[i])
                right_size = abs(asteroids[i + 1])
                
                if left_size > right_size:
                    # Left wins, remove right
                    new_asteroids = asteroids[:i + 1] + asteroids[i + 2:]
                elif left_size < right_size:
                    # Right wins, remove left
                    new_asteroids = asteroids[:i] + asteroids[i + 1:]
                else:
                    # Both explode
                    new_asteroids = asteroids[:i] + asteroids[i + 2:]
                
                # Recursively process the new state
                return self.asteroidCollisionRecursive(new_asteroids)
        
        # No collisions found
        return asteroids


def test_solution():
    """Test cases for asteroid collision solutions"""
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test 1: Basic example - [5,10,-5]")
    asteroids1 = [5, 10, -5]
    expected1 = [5, 10]
    result1 = solution.asteroidCollision(asteroids1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  Input: {asteroids1}")
    print(f"  Output: {result1} ✓")
    
    # Test case 2: Both explode
    print("\nTest 2: Both explode - [8,-8]")
    asteroids2 = [8, -8]
    expected2 = []
    result2 = solution.asteroidCollision(asteroids2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Input: {asteroids2}")
    print(f"  Output: {result2} ✓")
    
    # Test case 3: Chain collision
    print("\nTest 3: Chain collision - [10,2,-5]")
    asteroids3 = [10, 2, -5]
    expected3 = [10]
    result3 = solution.asteroidCollision(asteroids3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Input: {asteroids3}")
    print(f"  Output: {result3} ✓")
    
    # Test case 4: No collisions (all same direction)
    print("\nTest 4: No collisions - [-2,-1,1,2]")
    asteroids4 = [-2, -1, 1, 2]
    expected4 = [-2, -1, 1, 2]
    result4 = solution.asteroidCollision(asteroids4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Input: {asteroids4}")
    print(f"  Output: {result4} ✓")
    
    # Test case 5: All positive
    print("\nTest 5: All positive - [1,2,3,4]")
    asteroids5 = [1, 2, 3, 4]
    expected5 = [1, 2, 3, 4]
    result5 = solution.asteroidCollision(asteroids5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  Input: {asteroids5}")
    print(f"  Output: {result5} ✓")
    
    # Test case 6: All negative
    print("\nTest 6: All negative - [-1,-2,-3,-4]")
    asteroids6 = [-1, -2, -3, -4]
    expected6 = [-1, -2, -3, -4]
    result6 = solution.asteroidCollision(asteroids6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  Input: {asteroids6}")
    print(f"  Output: {result6} ✓")
    
    # Test case 7: Multiple collisions
    print("\nTest 7: Multiple collisions - [5,10,-5,-10]")
    asteroids7 = [5, 10, -5, -10]
    expected7 = []
    result7 = solution.asteroidCollision(asteroids7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Input: {asteroids7}")
    print(f"  Output: {result7} ✓")
    
    # Test case 8: Large negative destroys multiple
    print("\nTest 8: Large negative destroys multiple - [1,2,3,-10]")
    asteroids8 = [1, 2, 3, -10]
    expected8 = [-10]
    result8 = solution.asteroidCollision(asteroids8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Input: {asteroids8}")
    print(f"  Output: {result8} ✓")
    
    # Test case 9: Large positive survives
    print("\nTest 9: Large positive survives - [10,-1,-2,-3]")
    asteroids9 = [10, -1, -2, -3]
    expected9 = [10]
    result9 = solution.asteroidCollision(asteroids9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Input: {asteroids9}")
    print(f"  Output: {result9} ✓")
    
    # Test case 10: Alternating with equal sizes
    print("\nTest 10: Alternating equal sizes - [1,-1,2,-2,3,-3]")
    asteroids10 = [1, -1, 2, -2, 3, -3]
    expected10 = []
    result10 = solution.asteroidCollision(asteroids10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Input: {asteroids10}")
    print(f"  Output: {result10} ✓")
    
    # Test case 11: Compare all approaches
    print("\nTest 11: Comparing all approaches")
    test_cases = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -1, 1, 2],
        [1, 2, 3, 4],
        [-1, -2, -3, -4],
        [5, 10, -5, -10],
        [1, 2, 3, -10],
        [10, -1, -2, -3],
        [1, -1, 2, -2, 3, -3],
        [2, 1, -1],
        [-1, 1, 2],
        [1, -2, -2, -2],
    ]
    
    for asteroids in test_cases:
        result1 = solution.asteroidCollision(asteroids)
        result2 = solution.asteroidCollisionExplicit(asteroids)
        result3 = solution.asteroidCollisionTwoPass(asteroids)
        result4 = solution.asteroidCollisionRecursive(asteroids)
        
        assert result1 == result2, f"Explicit mismatch for {asteroids}: {result1} vs {result2}"
        assert result1 == result3, f"TwoPass mismatch for {asteroids}: {result1} vs {result3}"
        assert result1 == result4, f"Recursive mismatch for {asteroids}: {result1} vs {result4}"
    
    print("  All approaches match! ✓")
    
    # Test case 12: Single asteroid
    print("\nTest 12: Single asteroid - [5]")
    asteroids12 = [5]
    expected12 = [5]
    result12 = solution.asteroidCollision(asteroids12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Input: {asteroids12}")
    print(f"  Output: {result12} ✓")
    
    # Test case 13: Single negative
    print("\nTest 13: Single negative - [-5]")
    asteroids13 = [-5]
    expected13 = [-5]
    result13 = solution.asteroidCollision(asteroids13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Input: {asteroids13}")
    print(f"  Output: {result13} ✓")
    
    # Test case 14: Complex chain
    print("\nTest 14: Complex chain - [1,2,3,4,-5]")
    asteroids14 = [1, 2, 3, 4, -5]
    expected14 = []
    result14 = solution.asteroidCollision(asteroids14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Input: {asteroids14}")
    print(f"  Output: {result14} ✓")
    
    # Test case 15: Large values
    print("\nTest 15: Large values - [100, -50, 200, -150]")
    asteroids15 = [100, -50, 200, -150]
    expected15 = [100, 200]
    result15 = solution.asteroidCollision(asteroids15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Input: {asteroids15}")
    print(f"  Output: {result15} ✓")
    
    # Test case 16: Edge case - all explode except one
    print("\nTest 16: All explode except one - [1, -1, 1, -1, 5]")
    asteroids16 = [1, -1, 1, -1, 5]
    expected16 = [5]
    result16 = solution.asteroidCollision(asteroids16)
    assert result16 == expected16, f"Test 16 failed: expected {expected16}, got {result16}"
    print(f"  Input: {asteroids16}")
    print(f"  Output: {result16} ✓")
    
    # Test case 17: Negative at start
    print("\nTest 17: Negative at start - [-5, 3, 2, -1]")
    asteroids17 = [-5, 3, 2, -1]
    expected17 = [-5, 3, 2]
    result17 = solution.asteroidCollision(asteroids17)
    assert result17 == expected17, f"Test 17 failed: expected {expected17}, got {result17}"
    print(f"  Input: {asteroids17}")
    print(f"  Output: {result17} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()