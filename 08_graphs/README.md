# Graphs

## Overview

Graph problems involve nodes (vertices) connected by edges. Graphs can be directed or undirected, weighted or unweighted, and may contain cycles.

## Graph Representations

### 1. Adjacency List

```python
# Most common representation
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
```

### 2. Adjacency Matrix

```python
# For dense graphs
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```

### 3. Edge List

```python
# For algorithms that process edges
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
```

## Common Algorithms

### 1. Depth-First Search (DFS)

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result

# Iterative DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))

    return result
```

### 2. Breadth-First Search (BFS)

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))

    return result
```

### 3. Shortest Path Algorithms

#### Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

#### Floyd-Warshall (All Pairs)

```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

### 4. Topological Sort

```python
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result
```

## Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True
```

## Common Graph Problems

### 1. Connectivity

- **Number of Islands**: Count connected components
- **Course Schedule**: Detect cycles in DAG
- **Redundant Connection**: Find cycle in undirected graph

### 2. Shortest Path

- **Network Delay Time**: Single source shortest path
- **Cheapest Flights Within K Stops**: BFS with constraints
- **Path With Minimum Effort**: Dijkstra on grid

### 3. Topological Sort

- **Course Schedule II**: Topological ordering
- **Alien Dictionary**: Custom ordering
- **Task Scheduling**: Dependency resolution

### 4. Cycle Detection

- **Course Schedule**: Detect cycle in directed graph
- **Redundant Connection**: Find cycle in undirected graph
- **Graph Valid Tree**: Check if graph is tree

## Graph Traversal Patterns

### Connected Components

```python
def count_components(graph):
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            dfs_component(graph, node, visited)
            components += 1

    return components

def dfs_component(graph, start, visited):
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_component(graph, neighbor, visited)
```

### Bipartite Check

```python
def is_bipartite(graph):
    color = {}

    for node in graph:
        if node not in color:
            if not dfs_bipartite(graph, node, color, 0):
                return False

    return True

def dfs_bipartite(graph, node, color, current_color):
    if node in color:
        return color[node] == current_color

    color[node] = current_color

    for neighbor in graph.get(node, []):
        if not dfs_bipartite(graph, neighbor, color, 1 - current_color):
            return False

    return True
```

## Time Complexity Patterns

- **O(V + E)**: DFS/BFS on adjacency list
- **O(V²)**: DFS/BFS on adjacency matrix
- **O(E log V)**: Dijkstra's algorithm
- **O(V³)**: Floyd-Warshall algorithm
- **O(V + E)**: Topological sort

## Space Complexity Patterns

- **O(V)**: Visited set, recursion stack
- **O(V + E)**: Adjacency list representation
- **O(V²)**: Adjacency matrix representation
- **O(V)**: Union-Find data structure
