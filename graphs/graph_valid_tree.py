"""
261. Graph Valid Tree
Difficulty: Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Example 2:
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1) / 2

Notes:
- Key insight: A valid tree must have exactly n-1 edges and be connected (no cycles).
- Two conditions: (1) edges == n-1, (2) graph is connected with no cycles.
- Use Union-Find to detect cycles, or DFS/BFS to check connectivity.
"""

from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach 1: Union-Find (Optimal)
        Time Complexity: O(n * α(n)) where α is inverse Ackermann function
        Space Complexity: O(n)
        
        Check if graph has exactly n-1 edges and no cycles using Union-Find.
        """
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  # Cycle detected
            parent[root_x] = root_y
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False  # Cycle found
        
        return True
    
    def valid_tree_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach 2: DFS to Check Connectivity and Cycles
        Time Complexity: O(n + E)
        Space Complexity: O(n + E)
        
        Use DFS to check if graph is connected and has no cycles.
        """
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False  # Cycle detected
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor != parent:  # Don't go back to parent
                    if not dfs(neighbor, node):
                        return False
            
            return True
        
        # Check if connected and no cycles
        if not dfs(0, -1):
            return False
        
        # Check if all nodes are visited (connected)
        return len(visited) == n


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Valid tree
    print("Test 1: Valid tree")
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    expected1 = True
    result1 = solution.valid_tree(n1, edges1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Cycle detected
    print("Test 2: Cycle detected")
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    expected2 = False
    result2 = solution.valid_tree(n2, edges2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Too few edges (disconnected)
    print("Test 3: Too few edges (disconnected)")
    n3 = 5
    edges3 = [[0, 1], [0, 2]]
    expected3 = False
    result3 = solution.valid_tree(n3, edges3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Too many edges
    print("Test 4: Too many edges")
    n4 = 3
    edges4 = [[0, 1], [1, 2], [2, 0]]
    expected4 = False
    result4 = solution.valid_tree(n4, edges4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    # Test case 5: Single node
    print("Test 5: Single node")
    n5 = 1
    edges5 = []
    expected5 = True
    result5 = solution.valid_tree(n5, edges5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    
    # Test case 6: Two nodes
    print("Test 6: Two nodes")
    n6 = 2
    edges6 = [[0, 1]]
    expected6 = True
    result6 = solution.valid_tree(n6, edges6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    
    # Test case 7: Compare different approaches
    print("Test 7: Compare different approaches")
    test_n = 4
    test_edges = [[0, 1], [1, 2], [2, 3]]
    result_uf = solution.valid_tree(test_n, test_edges)
    result_dfs = solution.valid_tree_dfs(test_n, test_edges)
    expected = True
    assert result_uf == expected, f"Test 7.1 Union-Find failed: expected {expected}, got {result_uf}"
    assert result_dfs == expected, f"Test 7.2 DFS failed: expected {expected}, got {result_dfs}"
    
    # Test case 8: Linear tree
    print("Test 8: Linear tree")
    n8 = 4
    edges8 = [[0, 1], [1, 2], [2, 3]]
    expected8 = True
    result8 = solution.valid_tree(n8, edges8)
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    
    # Test case 9: Star tree
    print("Test 9: Star tree")
    n9 = 4
    edges9 = [[0, 1], [0, 2], [0, 3]]
    expected9 = True
    result9 = solution.valid_tree(n9, edges9)
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()