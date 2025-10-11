"""
Template for Graph problems
"""

from collections import defaultdict, deque
from typing import Dict, List, Optional, Set


class Solution:
    """
    Problem: [Problem Name]
    Difficulty: Easy/Medium/Hard
    
    Problem Statement:
    [Describe the problem here]
    
    Example:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]]
    Output: [expected output]
    Explanation: [explanation]
    """
    
    def dfs_solution(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach 1: DFS
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            return True
        
        # Check all components
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True
    
    def bfs_solution(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach 2: BFS
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque()
        
        for start in range(n):
            if start not in visited:
                queue.append(start)
                visited.add(start)
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return len(visited) == n
    
    def union_find_solution(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach 3: Union-Find
        Time Complexity: O(V + E * α(V))
        Space Complexity: O(V)
        """
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        # Process edges
        for u, v in edges:
            union(u, v)
        
        # Check if all nodes are connected
        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False
        
        return True


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Connected graph
    n1, edges1 = 3, [[0,1],[1,2],[2,0]]
    expected1 = True
    result1 = solution.dfs_solution(n1, edges1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Disconnected graph
    n2, edges2 = 4, [[0,1],[2,3]]
    expected2 = False
    result2 = solution.dfs_solution(n2, edges2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single node
    n3, edges3 = 1, []
    expected3 = True
    result3 = solution.dfs_solution(n3, edges3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
