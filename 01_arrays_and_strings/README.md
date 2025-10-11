# Arrays and Strings

## Overview

This folder contains problems involving array manipulation and string processing. These are fundamental problems that form the basis for more complex algorithms.

## Common Patterns

### 1. Two Pointers

- **Left and Right Pointers**: Move from both ends towards center
- **Fast and Slow Pointers**: Different speeds through array
- **Sliding Window**: Maintain a window of elements

### 2. Hash Table/Frequency Counting

- Count occurrences of elements
- Track indices of elements
- Group elements by some property

### 3. Sorting and Searching

- Sort array first, then apply logic
- Binary search on sorted arrays
- Custom sorting with lambda functions

### 4. String Manipulation

- Character frequency counting
- String reversal and rotation
- Pattern matching

## Key Techniques

### Array Manipulation

```python
# Reverse array
nums.reverse()

# Two pointers technique
left, right = 0, len(nums) - 1
while left < right:
    # Process elements
    left += 1
    right -= 1

# Sliding window
for right in range(len(nums)):
    # Expand window
    while condition:
        # Shrink window
        left += 1
```

### String Processing

```python
# Character frequency
from collections import Counter
freq = Counter(s)

# String reversal
s[::-1]

# Check palindrome
def is_palindrome(s):
    return s == s[::-1]
```

## Common Problems

1. **Two Sum** - Hash table approach
2. **Valid Anagram** - Character frequency counting
3. **Group Anagrams** - Sorting and grouping
4. **Longest Substring Without Repeating Characters** - Sliding window
5. **Container With Most Water** - Two pointers

## Time Complexity Patterns

- **O(n)**: Single pass through array
- **O(n log n)**: Sorting + processing
- **O(n²)**: Nested loops
- **O(n)**: Hash table operations

## Space Complexity Patterns

- **O(1)**: Two pointers, in-place operations
- **O(n)**: Hash table, additional array
- **O(k)**: Where k is the size of character set
