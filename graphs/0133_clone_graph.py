"""
133. Clone Graph
Difficulty: Medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Notes:
- Key insight: Use DFS or BFS with a hash map to track cloned nodes.
- Map original nodes to cloned nodes to handle cycles.
- Recursive DFS is clean and efficient for this problem.
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional


class Solution:
    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach 1: DFS with Hash Map (Optimal)
        Time Complexity: O(V + E) where V is vertices, E is edges
        Space Complexity: O(V) for hash map and recursion stack
        """
        if not node:
            return None

        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
    
    def clone_graph_bfs(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach 2: BFS with Hash Map
        Time Complexity: O(V + E)
        Space Complexity: O(V) for hash map and queue
        """
        if not node:
            return None
        
        clones = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                clones[current].neighbors.append(clones[neighbor])
        
        return clones[node]


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1: Single node with no neighbors
    print("Test 1: Single node with no neighbors")
    node1 = Node(1)
    result1 = solution.clone_graph(node1)
    assert result1 is not None, "Test 1 failed: result is None"
    assert result1.val == 1, f"Test 1 failed: expected val=1, got {result1.val}"
    assert result1.neighbors == [], f"Test 1 failed: expected empty neighbors, got {result1.neighbors}"
    assert result1 is not node1, "Test 1 failed: should be a copy, not the same object"
    
    # Test case 2: Two connected nodes
    print("Test 2: Two connected nodes")
    node2_1 = Node(1)
    node2_2 = Node(2)
    node2_1.neighbors = [node2_2]
    node2_2.neighbors = [node2_1]
    
    result2 = solution.clone_graph(node2_1)
    assert result2 is not None, "Test 2 failed: result is None"
    assert result2.val == 1, f"Test 2 failed: expected val=1, got {result2.val}"
    assert len(result2.neighbors) == 1, f"Test 2 failed: expected 1 neighbor, got {len(result2.neighbors)}"
    assert result2.neighbors[0].val == 2, f"Test 2 failed: neighbor should have val=2"
    assert result2.neighbors[0] is not node2_2, "Test 2 failed: neighbor should be a copy"
    
    # Test case 3: Empty graph
    print("Test 3: Empty graph")
    result3 = solution.clone_graph(None)
    assert result3 is None, "Test 3 failed: should return None for empty graph"
    
    # Test case 4: Four nodes forming a cycle
    print("Test 4: Four nodes forming a cycle")
    node4_1 = Node(1)
    node4_2 = Node(2)
    node4_3 = Node(3)
    node4_4 = Node(4)
    node4_1.neighbors = [node4_2, node4_4]
    node4_2.neighbors = [node4_1, node4_3]
    node4_3.neighbors = [node4_2, node4_4]
    node4_4.neighbors = [node4_1, node4_3]
    
    result4 = solution.clone_graph(node4_1)
    assert result4 is not None, "Test 4 failed: result is None"
    assert result4.val == 1, f"Test 4 failed: expected val=1, got {result4.val}"
    assert len(result4.neighbors) == 2, f"Test 4 failed: expected 2 neighbors, got {len(result4.neighbors)}"
    assert set(n.val for n in result4.neighbors) == {2, 4}, "Test 4 failed: neighbors should be 2 and 4"
    
    # Test case 5: Compare different approaches
    print("Test 5: Compare different approaches")
    node5_1 = Node(1)
    node5_2 = Node(2)
    node5_1.neighbors = [node5_2]
    node5_2.neighbors = [node5_1]
    
    result5_dfs = solution.clone_graph(node5_1)
    result5_bfs = solution.clone_graph_bfs(node5_1)
    
    assert result5_dfs is not None and result5_bfs is not None, "Test 5 failed: results are None"
    assert result5_dfs.val == result5_bfs.val, "Test 5 failed: DFS and BFS should produce same result"
    assert len(result5_dfs.neighbors) == len(result5_bfs.neighbors), "Test 5 failed: neighbor counts should match"
    
    # Test case 6: Linear graph
    print("Test 6: Linear graph")
    node6_1 = Node(1)
    node6_2 = Node(2)
    node6_3 = Node(3)
    node6_1.neighbors = [node6_2]
    node6_2.neighbors = [node6_1, node6_3]
    node6_3.neighbors = [node6_2]
    
    result6 = solution.clone_graph(node6_1)
    assert result6 is not None, "Test 6 failed: result is None"
    assert result6.val == 1, "Test 6 failed: root should have val=1"
    assert len(result6.neighbors) == 1, "Test 6 failed: root should have 1 neighbor"
    assert result6.neighbors[0].val == 2, "Test 6 failed: neighbor should have val=2"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()