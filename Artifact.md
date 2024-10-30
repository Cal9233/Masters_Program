# Algorithms and Data Structures Cheat Sheet

## Basic Data Structures

### Arrays
- **Definition**: Contiguous block of memory storing elements of the same type
- **When to use**: 
  - Need constant-time access to elements by index
  - Know size in advance
  - Need cache-friendly data structure
- **Time Complexities**:
  - Access: O(1)
  - Search: O(n)
  - Insert/Delete at end: O(1)
  - Insert/Delete at middle: O(n)

### Linked Lists
- **Definition**: Sequence of elements where each element points to the next
- **When to use**:
  - Need constant-time insertion/deletion at beginning
  - Don't know size in advance
  - Memory is fragmented
- **Time Complexities**:
  - Access: O(n)
  - Search: O(n)
  - Insert/Delete at beginning: O(1)
  - Insert/Delete at middle: O(n)

### Stack
- **Definition**: LIFO (Last In First Out) data structure
- **When to use**:
  - Need to track function calls/recursion
  - Undo/redo operations
  - Expression evaluation
- **Time Complexities**:
  - Push/Pop: O(1)
  - Peek: O(1)

### Queue
- **Definition**: FIFO (First In First Out) data structure
- **When to use**:
  - Need to process items in order they arrived
  - BFS algorithms
  - Task scheduling
- **Time Complexities**:
  - Enqueue/Dequeue: O(1)
  - Peek: O(1)

### Hash Table
- **Definition**: Data structure that maps keys to values using a hash function
- **When to use**:
  - Need fast lookups by key
  - Need to count frequencies
  - Need to detect duplicates
- **Time Complexities**:
  - Insert/Delete/Search: O(1) average, O(n) worst
  - Space: O(n)

### Binary Tree
- **Definition**: Hierarchical structure where each node has at most two children
- **When to use**:
  - Need to represent hierarchical data
  - Need ordered data structure with fast operations
- **Types**:
  - Binary Search Tree (BST)
  - AVL Tree (self-balancing)
  - Red-Black Tree (self-balancing)

### Heap
- **Definition**: Complete binary tree where parent nodes compare specially to children
- **When to use**:
  - Need to repeatedly find min/max element
  - Priority queue implementation
  - Heap sort
- **Time Complexities**:
  - Insert: O(log n)
  - Delete min/max: O(log n)
  - Get min/max: O(1)

### Graph
- **Definition**: Collection of vertices connected by edges
- **When to use**:
  - Need to represent relationships between objects
  - Need to find shortest paths
  - Need to analyze networks
- **Representations**:
  - Adjacency Matrix
  - Adjacency List

## Searching Algorithms

### Linear Search
- **Definition**: Check each element sequentially
- **When to use**:
  - Small datasets
  - Unsorted data
- **Time Complexity**: O(n)

### Binary Search
- **Definition**: Repeatedly divide sorted array in half
- **When to use**:
  - Sorted data
  - Need efficient search
- **Time Complexity**: O(log n)

## Sorting Algorithms

### Quick Sort
- **Definition**: Divide-and-conquer algorithm using pivot
- **When to use**:
  - Need efficient general-purpose sort
  - Space is a concern
- **Time Complexity**: 
  - Average: O(n log n)
  - Worst: O(n²)

### Merge Sort
- **Definition**: Divide-and-conquer algorithm that merges sorted subarrays
- **When to use**:
  - Need stable sort
  - Have extra memory available
- **Time Complexity**: O(n log n)

### Heap Sort
- **Definition**: Sort by building max heap and repeatedly extracting max
- **When to use**:
  - Need in-place sorting
  - Need guaranteed O(n log n)
- **Time Complexity**: O(n log n)

## Graph Algorithms

### Breadth-First Search (BFS)
- **Definition**: Explore graph level by level
- **When to use**:
  - Find shortest path in unweighted graph
  - Explore neighbors first
- **Time Complexity**: O(V + E)

### Depth-First Search (DFS)
- **Definition**: Explore graph by going as deep as possible
- **When to use**:
  - Find cycles
  - Topological sorting
  - Maze solving
- **Time Complexity**: O(V + E)

### Dijkstra's Algorithm
- **Definition**: Find shortest paths from source to all vertices
- **When to use**:
  - Need shortest path in weighted graph
  - No negative weights
- **Time Complexity**: O((V + E) log V)

### Dynamic Programming
- **Definition**: Solve complex problems by breaking into simpler subproblems
- **When to use**:
  - Problem has optimal substructure
  - Problem has overlapping subproblems
  - Need optimization
- **Common Applications**:
  - Fibonacci sequence
  - Knapsack problem
  - Longest common subsequence

## String Algorithms

### KMP (Knuth-Morris-Pratt)
- **Definition**: Pattern matching using prefix function
- **When to use**:
  - Need efficient string pattern matching
- **Time Complexity**: O(n + m)

### Trie
- **Definition**: Tree structure for storing strings, sharing prefixes
- **When to use**:
  - Need prefix-based operations
  - Autocomplete functionality
  - Dictionary implementation
- **Time Complexity**:
  - Insert/Search: O(m) where m is string length

## Tips for Algorithm Selection

1. **Consider the constraints**:
   - Input size
   - Time/space requirements
   - Is input sorted?
   - Frequency of operations

2. **Common problem patterns**:
   - Two pointers: Array/string problems
   - Sliding window: Subarrays/substring problems
   - Binary search: Sorted array problems
   - BFS: Shortest path, level-order
   - DFS: Exhaustive search, backtracking
   - Dynamic programming: Optimization problems

3. **Performance considerations**:
   - Choose based on:
     - Expected input size
     - Required operation frequencies
     - Memory constraints
     - Need for stability