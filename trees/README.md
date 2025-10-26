# Trees

## Overview

This folder contains problems involving binary trees, binary search trees, and tree traversals. Trees are fundamental data structures that appear frequently in coding interviews.

## Common Patterns

### 1. Tree Traversal

- **Preorder**: Root → Left → Right
- **Inorder**: Left → Root → Right (gives sorted order for BST)
- **Postorder**: Left → Right → Root
- **Level Order**: Breadth-first traversal

### 2. Recursive vs Iterative

- **Recursive**: Natural for tree problems, uses call stack
- **Iterative**: Uses explicit stack/queue, better space control

### 3. Tree Properties

- **Height/Depth**: Maximum path from root to leaf
- **Diameter**: Longest path between any two nodes
- **Balanced**: Height difference ≤ 1 for all subtrees

## Key Techniques

### Recursive DFS

```python
def dfs(root):
    if not root:
        return 0

    left = dfs(root.left)
    right = dfs(root.right)

    return max(left, right) + 1
```

### Iterative DFS

```python
def dfs_iterative(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### BFS (Level Order)

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

## Common Problems

1. **Maximum Depth of Binary Tree** - Basic recursion
2. **Same Tree** - Tree comparison
3. **Symmetric Tree** - Mirror property
4. **Binary Tree Level Order Traversal** - BFS
5. **Convert Sorted Array to BST** - BST construction
6. **Validate Binary Search Tree** - BST properties
7. **Lowest Common Ancestor** - Tree navigation
8. **Path Sum** - Tree path problems

## Binary Search Tree (BST) Properties

- **Left subtree**: All values < root
- **Right subtree**: All values > root
- **Inorder traversal**: Gives sorted sequence
- **Search**: O(log n) average, O(n) worst case
- **Insert/Delete**: O(log n) average, O(n) worst case

## Tree Construction Patterns

### From Array

```python
def build_tree(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = build_tree(nums[:mid])
    root.right = build_tree(nums[mid+1:])

    return root
```

### From Preorder and Inorder

```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    root_idx = inorder.index(root_val)

    root.left = build_tree(preorder[1:root_idx+1], inorder[:root_idx])
    root.right = build_tree(preorder[root_idx+1:], inorder[root_idx+1:])

    return root
```

## Time Complexity Patterns

- **O(n)**: Visit every node once
- **O(log n)**: Balanced BST operations
- **O(h)**: Where h is height of tree
- **O(n log n)**: Sort + tree operations

## Space Complexity Patterns

- **O(h)**: Recursion depth (height of tree)
- **O(n)**: Store all nodes (worst case for skewed tree)
- **O(w)**: BFS queue size (width of tree)
