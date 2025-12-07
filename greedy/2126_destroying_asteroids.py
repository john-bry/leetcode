"""
2126. Destroying Asteroids
Difficulty: Medium

You are given an integer mass, which represents the original mass of a planet. You are also given an 
array asteroids, where asteroids[i] is the mass of the ith asteroid.

You can arrange for the planet to collide with the asteroids in any order. If the mass of the planet 
is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains 
the mass of the asteroid. Otherwise, the planet is destroyed.

Return true if all asteroids can be destroyed. Otherwise, return false.

Example 1:
Input: mass = 10, asteroids = [3,9,19,5,21]
Output: true
Explanation: One way to order the asteroids is [9,5,3,21,19]:
- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 5. New planet mass: 19 + 5 = 24
- The planet collides with the asteroid with a mass of 3. New planet mass: 24 + 3 = 27
- The planet collides with the asteroid with a mass of 21. New planet mass: 27 + 21 = 48
- The planet collides with the asteroid with a mass of 19. New planet mass: 48 + 19 = 67
All asteroids are destroyed.

Example 2:
Input: mass = 5, asteroids = [4,9,23,4]
Output: false
Explanation: 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other 3 asteroids (adding 4 + 9 + 4 = 17 to the planet's mass), 
the planet will have a mass of 5 + 17 = 22, which is less than 23.

Constraints:
- 1 <= mass <= 10^5
- 1 <= asteroids.length <= 10^5
- 1 <= asteroids[i] <= 10^5

Notes:
- Key insight: This is a greedy problem. Always destroy the smallest available asteroid first.
- By sorting asteroids and processing them in ascending order, we maximize our chances of accumulating 
  enough mass to destroy larger asteroids.
- If we can destroy an asteroid, we add its mass to our current mass (gaining mass).
- If an asteroid's mass exceeds our current mass, we cannot destroy it (return False).
- Time complexity: O(n log n) due to sorting, where n is the number of asteroids
- Space complexity: O(1) if we sort in-place, O(n) if we create a new sorted list
- Alternative approaches:
  - Greedy with sorting: O(n log n) time - current approach (optimal)
  - Try all permutations: O(n!) time - too slow, not practical
  - Dynamic programming: O(n * mass) time - overkill for this problem
- Edge cases: Empty asteroids list, single asteroid, all asteroids smaller than mass, 
  all asteroids larger than mass, asteroids equal to mass
"""

from typing import List


class Solution:
    def asteroids_destroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        Approach: Greedy - Sort and Process Smallest First
        Time Complexity: O(n log n) where n is the number of asteroids
        Space Complexity: O(1) if sorting in-place
        
        Sort asteroids in ascending order and process them one by one.
        For each asteroid, if it's larger than current mass, return False.
        Otherwise, destroy it and add its mass to the planet.
        """
        asteroids.sort()
        earth_mass = mass

        for asteroid in asteroids:
            if asteroid > earth_mass:
                return False
                
            earth_mass += asteroid

        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    mass1 = 10
    asteroids1 = [3, 9, 19, 5, 21]
    expected1 = True
    result1 = solution.asteroids_destroyed(mass1, asteroids1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"  mass={mass1}, asteroids={asteroids1}")
    print(f"  Result: {result1} ✓")
    
    # Test case 2: Cannot destroy all asteroids
    print("\nTest 2: Cannot destroy all asteroids")
    mass2 = 5
    asteroids2 = [4, 9, 23, 4]
    expected2 = False
    result2 = solution.asteroids_destroyed(mass2, asteroids2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  mass={mass2}, asteroids={asteroids2}")
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Single asteroid that can be destroyed
    print("\nTest 3: Single asteroid that can be destroyed")
    mass3 = 10
    asteroids3 = [5]
    expected3 = True
    result3 = solution.asteroids_destroyed(mass3, asteroids3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  mass={mass3}, asteroids={asteroids3}")
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single asteroid that cannot be destroyed
    print("Test 4: Single asteroid that cannot be destroyed")
    mass4 = 5
    asteroids4 = [10]
    expected4 = False
    result4 = solution.asteroids_destroyed(mass4, asteroids4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  mass={mass4}, asteroids={asteroids4}")
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Empty asteroids list
    print("Test 5: Empty asteroids list")
    mass5 = 10
    asteroids5 = []
    expected5 = True
    result5 = solution.asteroids_destroyed(mass5, asteroids5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"  mass={mass5}, asteroids={asteroids5}")
    print(f"  Result: {result5} ✓")
    
    # Test case 6: All asteroids smaller than initial mass
    print("Test 6: All asteroids smaller than initial mass")
    mass6 = 100
    asteroids6 = [1, 2, 3, 4, 5]
    expected6 = True
    result6 = solution.asteroids_destroyed(mass6, asteroids6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"  mass={mass6}, asteroids={asteroids6}")
    print(f"  Result: {result6} ✓")
    
    # Test case 7: All asteroids larger than initial mass
    print("Test 7: All asteroids larger than initial mass")
    mass7 = 5
    asteroids7 = [10, 20, 30]
    expected7 = False
    result7 = solution.asteroids_destroyed(mass7, asteroids7)
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  mass={mass7}, asteroids={asteroids7}")
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Asteroids equal to mass
    print("Test 8: Asteroids equal to mass")
    mass8 = 10
    asteroids8 = [10, 10, 10]
    expected8 = True
    result8 = solution.asteroids_destroyed(mass8, asteroids8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  mass={mass8}, asteroids={asteroids8}")
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Need to accumulate mass to destroy larger asteroids
    print("Test 9: Need to accumulate mass to destroy larger asteroids")
    mass9 = 1
    asteroids9 = [1, 2, 3, 4]
    expected9 = True
    result9 = solution.asteroids_destroyed(mass9, asteroids9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  mass={mass9}, asteroids={asteroids9}")
    print(f"  Result: {result9} ✓")
    # Explanation: Destroy 1 (mass becomes 2), then 2 (mass becomes 4), then 3 (mass becomes 7), then 4 (mass becomes 11)
    
    # Test case 10: Cannot accumulate enough mass
    print("Test 10: Cannot accumulate enough mass")
    mass10 = 1
    asteroids10 = [1, 2, 3, 8]
    expected10 = False
    result10 = solution.asteroids_destroyed(mass10, asteroids10)
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  mass={mass10}, asteroids={asteroids10}")
    print(f"  Result: {result10} ✓")
    # Explanation: After destroying 1, 2, 3, mass becomes 7, but 8 > 7, so we cannot destroy it
    
    # Test case 11: Large numbers
    print("Test 11: Large numbers")
    mass11 = 1000
    asteroids11 = [500, 600, 700, 800, 900]
    expected11 = True
    result11 = solution.asteroids_destroyed(mass11, asteroids11)
    assert result11 == expected11, f"Test 11 failed: expected {expected11}, got {result11}"
    print(f"  mass={mass11}, asteroids={asteroids11}")
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Exactly enough mass to destroy all
    print("Test 12: Exactly enough mass to destroy all")
    mass12 = 1
    asteroids12 = [1, 2, 4]
    expected12 = True
    result12 = solution.asteroids_destroyed(mass12, asteroids12)
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  mass={mass12}, asteroids={asteroids12}")
    print(f"  Result: {result12} ✓")
    # Explanation: Destroy 1 (mass=2), destroy 2 (mass=4), destroy 4 (mass=8)
    
    # Test case 13: Middle asteroid too large
    print("Test 13: Middle asteroid too large")
    mass13 = 5
    asteroids13 = [1, 2, 15, 3]
    expected13 = False
    result13 = solution.asteroids_destroyed(mass13, asteroids13)
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  mass={mass13}, asteroids={asteroids13}")
    print(f"  Result: {result13} ✓")
    # After sorting: [1, 2, 3, 15]. Destroy 1 (mass=6), destroy 2 (mass=8), destroy 3 (mass=11), but 15 > 11, so False
    
    # Test case 14: All same size asteroids
    print("Test 14: All same size asteroids")
    mass14 = 5
    asteroids14 = [5, 5, 5, 5]
    expected14 = True
    result14 = solution.asteroids_destroyed(mass14, asteroids14)
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  mass={mass14}, asteroids={asteroids14}")
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Gradually increasing asteroids
    print("Test 15: Gradually increasing asteroids")
    mass15 = 1
    asteroids15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected15 = True
    result15 = solution.asteroids_destroyed(mass15, asteroids15)
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  mass={mass15}, asteroids={asteroids15}")
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
