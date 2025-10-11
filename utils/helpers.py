"""
Helper functions for LeetCode problems
"""

import heapq
from collections import defaultdict, deque
from typing import Any, List, Optional


def print_matrix(matrix: List[List[Any]]) -> None:
    """Pretty print a 2D matrix."""
    for row in matrix:
        print(row)


def print_linked_list(head) -> None:
    """Print linked list values."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))


def print_tree_inorder(root) -> None:
    """Print binary tree in inorder traversal."""
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)
    
    inorder(root)
    print()


def print_tree_preorder(root) -> None:
    """Print binary tree in preorder traversal."""
    def preorder(node):
        if not node:
            return
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)
    
    preorder(root)
    print()


def print_tree_postorder(root) -> None:
    """Print binary tree in postorder traversal."""
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=" ")
    
    postorder(root)
    print()


def print_tree_level_order(root) -> None:
    """Print binary tree in level order (BFS)."""
    if not root:
        return
    
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print(level_values)


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (alphanumeric only)."""
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find two numbers that sum to target."""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def binary_search(arr: List[int], target: int) -> int:
    """Binary search for target in sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_leftmost(arr: List[int], target: int) -> int:
    """Find leftmost position of target in sorted array."""
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_rightmost(arr: List[int], target: int) -> int:
    """Find rightmost position of target in sorted array."""
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple."""
    return a * b // gcd(a, b)


def is_prime(n: int) -> bool:
    """Check if number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def sieve_of_eratosthenes(n: int) -> List[bool]:
    """Generate boolean array where is_prime[i] indicates if i is prime."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return is_prime


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def permutations(nums: List[int]) -> List[List[int]]:
    """Generate all permutations of list."""
    if not nums:
        return [[]]
    
    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]
        for perm in permutations(rest):
            result.append([nums[i]] + perm)
    
    return result


def combinations(n: int, k: int) -> List[List[int]]:
    """Generate all combinations of k elements from 1 to n."""
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    result = []
    backtrack(1, [])
    return result


def manhattan_distance(p1: tuple, p2: tuple) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def euclidean_distance(p1: tuple, p2: tuple) -> float:
    """Calculate Euclidean distance between two points."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
