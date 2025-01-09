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

Understanding Complexity 🤔
What is Time Complexity?
Time complexity is like measuring how long it takes to complete a task as the task gets bigger.
Simple Example: Finding a toy in your room

If your toys are organized (sorted array): You can look in specific places quickly! (O(log n))
If your room is messy (unsorted array): You need to look everywhere! (O(n))

Common Time Complexities (from fastest to slowest):

O(1) - Constant Time

Like grabbing your favorite toy from a specific spot
No matter how many toys you have, it takes the same time
Example: Getting the first element of an array

def get_first(array):
    return array[0]  # Always takes same time!

O(log n) - Logarithmic Time

Like finding a word in dictionary - you split book in half each time
Gets slightly slower as input grows
Example: Binary search

def find_page(book, target_page):
    left = 1
    right = book.total_pages
    while left <= right:
        middle = (left + right) // 2
        if middle == target_page:
            return "Found it!"
        elif middle < target_page:
            left = middle + 1
        else:
            right = middle - 1

O(n) - Linear Time

Like counting all your toys one by one
Time increases directly with input size
Example: Finding maximum number

def find_biggest_number(numbers):
    biggest = numbers[0]
    for number in numbers:  # Check each number once
        if number > biggest:
            biggest = number
    return biggest

O(n log n) - Linearithmic Time

Like organizing your books by title
Common in good sorting algorithms
Example: Merge sort


O(n²) - Quadratic Time

Like comparing every toy with every other toy
Gets much slower as input grows
Example: Bubble sort

def compare_all_toys(toys):
    for toy1 in toys:           # First loop
        for toy2 in toys:       # Second loop
            compare(toy1, toy2)  # Compare each toy with every other toy


What is Space Complexity? 📦
Space complexity is like measuring how many boxes you need to store things while doing a task.
Simple Example: Making copies of homework

If you just read it: You need no extra paper (O(1) space)
If you make one copy: You need space for one more paper (O(1) space)
If you make a copy for each student: You need space for n papers (O(n) space)

Common Space Complexities:

O(1) - Constant Space

Like using the same box no matter how many toys you count
Example: Finding maximum number

def find_max(numbers):
    max_num = numbers[0]  # Only needs one variable!
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

O(n) - Linear Space

Like needing one box for each toy
Example: Creating a copy of an array

def copy_array(array):
    new_array = []  # New space grows with input
    for item in array:
        new_array.append(item)
    return new_array

O(n²) - Quadratic Space

Like creating a grid where you match each toy with every other toy
Example: Creating a multiplication table

def multiplication_table(n):
    table = []  # Creates n×n grid
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        table.append(row)
    return table


How to Find Time & Space Complexity 🔍
Simple Steps to Find Time Complexity:

Count the loops:

No loops = O(1)
One loop = O(n)
Nested loop = O(n²)
Half the input each time = O(log n)


Look for keywords:

"For each element" = Usually O(n)
"Divide in half" = Usually O(log n)
"Nested iterations" = Usually O(n²)



Simple Steps to Find Space Complexity:

Count new variables:

Fixed number of variables = O(1)
Array size matches input = O(n)
Matrix/2D array = O(n²)


Look for:

Creating new arrays
Recursive calls (each needs stack space)
Temporary data structures



Example Analysis: Finding a Name in a Phone Book 📱
def find_in_phone_book(phone_book, name):
    left = 0
    right = len(phone_book) - 1  # O(1) space for variables
    
    while left <= right:  # O(log n) time - cuts book in half each time
        middle = (left + right) // 2
        if phone_book[middle] == name:
            return "Found!"
        elif phone_book[middle] < name:
            left = middle + 1
        else:
            right = middle - 1
    return "Not found!"

Time Complexity: O(log n)

Why? We cut the phone book in half each time
If book has 1000 pages, we need only about 10 checks!

Space Complexity: O(1)

Why? We only use three variables (left, right, middle)
No matter how big the phone book, we need same space