"""
Common algorithms for LeetCode problems
"""

import heapq
from collections import defaultdict, deque
from typing import List, Optional, Tuple


def quick_sort(arr: List[int]) -> List[int]:
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heap_sort(arr: List[int]) -> List[int]:
    """Heap sort implementation."""
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


def dfs_recursive(graph: dict, start: int, visited: set = None) -> List[int]:
    """Depth-First Search recursive implementation."""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph: dict, start: int) -> List[int]:
    """Depth-First Search iterative implementation."""
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


def bfs(graph: dict, start: int) -> List[int]:
    """Breadth-First Search implementation."""
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


def dijkstra(graph: dict, start: int) -> dict:
    """Dijkstra's shortest path algorithm."""
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


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    """Floyd-Warshall all-pairs shortest path algorithm."""
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


def topological_sort(graph: dict) -> List[int]:
    """Topological sort using Kahn's algorithm."""
    in_degree = defaultdict(int)
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


def kosaraju_scc(graph: dict) -> List[List[int]]:
    """Find strongly connected components using Kosaraju's algorithm."""
    def dfs1(node, visited, stack):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs1(neighbor, visited, stack)
        stack.append(node)
    
    def dfs2(node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs2(neighbor, visited, component)
    
    # Step 1: Fill stack with vertices in order of finishing times
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs1(node, visited, stack)
    
    # Step 2: Create reversed graph
    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    # Step 3: Process vertices in reverse order
    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, visited, component)
            sccs.append(component)
    
    return sccs


def tarjan_scc(graph: dict) -> List[List[int]]:
    """Find strongly connected components using Tarjan's algorithm."""
    index = 0
    stack = []
    indices = {}
    lowlinks = {}
    on_stack = set()
    sccs = []
    
    def strongconnect(node):
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
            elif neighbor in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[neighbor])
        
        if lowlinks[node] == indices[node]:
            component = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == node:
                    break
            sccs.append(component)
    
    for node in graph:
        if node not in indices:
            strongconnect(node)
    
    return sccs


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """0/1 Knapsack problem using dynamic programming."""
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Longest Common Subsequence using dynamic programming."""
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


def edit_distance(word1: str, word2: str) -> int:
    """Edit distance (Levenshtein distance) using dynamic programming."""
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]


def kadane_algorithm(arr: List[int]) -> int:
    """Kadane's algorithm for maximum subarray sum."""
    max_ending_here = max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """Find maximum in each sliding window of size k."""
    from collections import deque
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove elements smaller than current element
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
