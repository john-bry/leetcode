"""
207. Course Schedule
Difficulty: Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

Notes:
- Key insight: This is a cycle detection problem in a directed graph.
- Use DFS with state tracking: 0=unvisited, 1=visiting (in current path), 2=visited (completed).
- If we encounter a node with state 1 during DFS, we found a cycle.
- Alternative: Use topological sort (Kahn's algorithm with BFS).
"""

from typing import List


class Solution:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach 1: DFS with State Tracking (Cycle Detection)
        Time Complexity: O(V + E) where V is courses, E is prerequisites
        Space Complexity: O(V + E) for graph and recursion stack
        
        Detect cycles in the prerequisite graph.
        State: 0=unvisited, 1=visiting (in current path), 2=visited (completed).
        """
        # Part 1: Build graph
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Part 2: Track states
        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(course):
            if state[course] == 1:  # Cycle detected: found node in current path
                return True
            if state[course] == 2:  # Already processed, no cycle from here
                return False
            
            state[course] = 1  # Mark as visiting (in current DFS path)
            
            for prereq in graph[course]:
                if dfs(prereq):  # Check if cycle exists in prerequisites
                    return True
            
            state[course] = 2  # Mark as visited (completed processing)
            return False
        
        for course in range(numCourses):
            if dfs(course):  # If cycle found, can't finish
                return False
        return True
    
    def can_finish_topological(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach 2: Topological Sort (Kahn's Algorithm with BFS)
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        
        Use BFS to process nodes with no incoming edges.
        If we can process all nodes, no cycle exists.
        """
        from collections import deque

        # Build graph and in-degree count
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Reverse: prereq -> course
            in_degree[course] += 1
        
        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        
        while queue:
            course = queue.popleft()
            count += 1
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return count == numCourses


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: No prerequisites
    print("Test 1: No prerequisites")
    numCourses1 = 2
    prerequisites1 = []
    expected1 = True
    result1 = solution.can_finish(numCourses1, prerequisites1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Simple valid schedule
    print("Test 2: Simple valid schedule")
    numCourses2 = 2
    prerequisites2 = [[1, 0]]
    expected2 = True
    result2 = solution.can_finish(numCourses2, prerequisites2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Cycle detected
    print("Test 3: Cycle detected")
    numCourses3 = 2
    prerequisites3 = [[1, 0], [0, 1]]
    expected3 = False
    result3 = solution.can_finish(numCourses3, prerequisites3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Multiple courses, no cycle
    print("Test 4: Multiple courses, no cycle")
    numCourses4 = 3
    prerequisites4 = [[1, 0], [2, 1]]
    expected4 = True
    result4 = solution.can_finish(numCourses4, prerequisites4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Multiple courses with cycle
    print("Test 5: Multiple courses with cycle")
    numCourses5 = 3
    prerequisites5 = [[1, 0], [2, 1], [0, 2]]
    expected5 = False
    result5 = solution.can_finish(numCourses5, prerequisites5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Single course
    print("Test 6: Single course")
    numCourses6 = 1
    prerequisites6 = []
    expected6 = True
    result6 = solution.can_finish(numCourses6, prerequisites6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_numCourses = 4
    test_prerequisites = [[1, 0], [2, 1], [3, 2]]
    result_dfs = solution.can_finish(test_numCourses, test_prerequisites)
    result_topological = solution.can_finish_topological(test_numCourses, test_prerequisites)
    expected = True
    assert result_dfs == expected, f"Test 7.1 DFS failed: expected {expected}, got {result_dfs}"
    assert result_topological == expected, f"Test 7.2 Topological failed: expected {expected}, got {result_topological}"
    
    # Test case 8: Complex valid schedule
    print("Test 8: Complex valid schedule")
    numCourses8 = 5
    prerequisites8 = [[1, 0], [2, 0], [3, 1], [4, 2]]
    expected8 = True
    result8 = solution.can_finish(numCourses8, prerequisites8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Self-loop (if allowed, should be cycle)
    print("Test 9: Multiple prerequisites")
    numCourses9 = 3
    prerequisites9 = [[1, 0], [1, 2], [2, 0]]
    expected9 = True
    result9 = solution.can_finish(numCourses9, prerequisites9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()