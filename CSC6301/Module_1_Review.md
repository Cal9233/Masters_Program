# Python Documentation with PyDoc - Complete Guide

## Table of Contents

1. [The Importance of Documentation](#the-importance-of-documentation)
2. [Types of Documentation](#types-of-documentation)
3. [Python Docstrings](#python-docstrings)
4. [PyDoc Commands](#pydoc-commands)
5. [Documentation Examples](#documentation-examples)
6. [Best Practices](#best-practices)
7. [Project Assignment](#project-assignment)

## The Importance of Documentation

Documentation is **for humans**, not computers. We use documentation to understand the logic behind running code for several key reasons:

### Maintenance Issues

- **To fix a software bug** - understanding existing code
- **To change software functionality** - modifying existing features

### Reuse Issues

- **To decide using a software module** - evaluating if code fits current needs

### Documentation Types by Purpose

**Software Readability** (open code):

- Classes: purposes, methods, interfaces, dependencies, limitations
- Methods: function, mutator/accessor, input/output parameters
- Variables: type, meaning, usage, invariants
- Constants: type, meaning, usage, impact
- Functions: function, i/o parameters, dependencies, algorithm, limitations
- Modules: constituents, purpose, dependencies
- Packages: constituents, purpose, dependencies

**Software Specification** (encapsulated code):

- Classes: purposes, methods, interfaces, dependencies, limitations
- Methods: function, input and output parameters
- Constants: type, meaning
- Functions: function, i/o parameters, dependencies, limitations
- Modules: constituents, purpose, dependencies
- Packages: constituents, purpose, dependencies

> **Important:** Version/date and author should always be stated

## Types of Documentation

### Documentation for Readability

Helps with software maintenance when you need to:

- Debug existing code
- Modify functionality
- Understand implementation details

### Documentation for Specification

Helps with software reuse when you need to:

- Decide if a module fits your needs
- Understand the interface without implementation details
- Integrate modules into larger systems

## Python Docstrings

### What are Docstrings?

Python docstrings are strings using triple single or double quotes used for documentation:

```python
''' This is a single quoted docstring
string defined in two lines. '''

""" This is a double quoted docstring
string defined in two lines. """
```

### Where to Place Docstrings

1. **Module/Package Level**

   - Multiline comment with triple quotation at the first line of the file

2. **Class Level**

   - Multiline comment with triple quotation at the first line after class declaration

3. **Function/Method Level**
   - Multiline comment with triple quotation at the first line after function/method definition

## PyDoc Commands

### Reading Documentation

#### Basic Command Line Usage

```bash
# Start PyDoc server (Python 3)
pydoc3 -b

# Alternative for some systems
python -m pydoc -b

# On macOS specifically
pydoc3 -b
```

#### Command Line Options

```bash
# Show text documentation for a module
pydoc <name>

# Search for keyword in synopsis lines
pydoc -k <keyword>

# Start HTTP server (default: localhost)
pydoc -n <hostname>

# Start HTTP server on specific port
pydoc -p <port>

# Start HTTP server and open browser
pydoc -b

# Write HTML documentation to file
pydoc -w <name>
```

### Accessing Docstrings Programmatically

```python
# Access docstring of any object using __doc__
print(MyClass.__doc__)
print(my_function.__doc__)

# Example output
Tree.__doc__ = "This class defines a binary tree.\n"+ \
               "It has a single instance variable:\n"+ \
               " - the tree root."
```

## Documentation Examples

### Complete Example: Binary Tree Class

```python
"""
This module holds the classes node of a binary tree and
tree, the binary tree itself.

Author: Your Name
Date: January 2025
Version: 1.0
"""

class Node:
    """
    This class defines a node of a binary tree.
    It has three instance variables:
    - a data holder;
    - a pointer to the left child;
    - a pointer to the right child.
    """

    def __init__(self, d):
        """
        The constructor of a node that assign the data d
        and two empty pointers to the node's children.

        Parameters:
        d: The data to be stored in the node
        """
        self.data, self.left, self.right = d, None, None

class Tree:
    """
    This class defines a binary tree.
    It has a single instance variable:
    - the tree root.
    """

    def __init__(self, d=None):
        """
        The constructor of a tree that either:
        - it creates an empty tree (root pointing to no node); or
        - it assigns data d to a root node.

        Parameters:
        d (optional): Data for the root node. If None, creates empty tree.
        """
        if (d == None): # an empty tree
            self.root = None
        else:
            self.root = Node(d)

    def insert(self, data):
        """
        Insert a new node with given data into the binary tree.

        Parameters:
        data: The data to be inserted into the tree

        Returns:
        bool: True if insertion was successful, False otherwise
        """
        if self.root is None:
            self.root = Node(data)
            return True

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return True
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return True
                current = current.right
            else:
                return False  # Data already exists

    def search(self, data):
        """
        Search for a node with the specified data.

        Parameters:
        data: The data to search for

        Returns:
        bool: True if data is found, False otherwise
        """
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self):
        """
        Perform inorder traversal of the tree.

        Returns:
        list: List of data elements in inorder sequence
        """
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)

        _inorder(self.root)
        return result
```

### Minimal Example: Calculator Class

```python
"""
Simple calculator module for basic arithmetic operations.

Author: Student Name
Date: January 2025
Version: 1.0
"""

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    Maintains a running total that can be reset.
    """

    def __init__(self):
        """
        Initialize calculator with total set to zero.
        """
        self.total = 0

    def add(self, value):
        """
        Add a value to the current total.

        Parameters:
        value (float): The number to add

        Returns:
        float: The new total after addition
        """
        self.total += value
        return self.total

    def subtract(self, value):
        """
        Subtract a value from the current total.

        Parameters:
        value (float): The number to subtract

        Returns:
        float: The new total after subtraction
        """
        self.total -= value
        return self.total

    def multiply(self, value):
        """
        Multiply the current total by a value.

        Parameters:
        value (float): The number to multiply by

        Returns:
        float: The new total after multiplication
        """
        self.total *= value
        return self.total

    def divide(self, value):
        """
        Divide the current total by a value.

        Parameters:
        value (float): The number to divide by (must not be zero)

        Returns:
        float: The new total after division

        Raises:
        ZeroDivisionError: If value is zero
        """
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.total /= value
        return self.total

    def reset(self):
        """
        Reset the calculator total to zero.

        Returns:
        float: Always returns 0
        """
        self.total = 0
        return self.total

    def get_total(self):
        """
        Get the current total without modifying it.

        Returns:
        float: The current total
        """
        return self.total
```

## Best Practices

### Documentation Best Practices

1. **Use punctuation marks** - Write complete sentences
2. **Do not repeat obvious information** - Avoid redundancy with code
3. **Do not mix remarks (#) with documentation (''')** - Keep them separate
4. **Be concise but complete** - Provide necessary details without being verbose
5. **Include version/date and author** - Essential metadata
6. **Document parameters and return values** - Specify types when helpful
7. **Document exceptions** - List what exceptions might be raised

### PyDoc Best Practices

1. **Test your documentation** - Use `pydoc -b` to preview generated docs
2. **Keep docstrings up to date** - Modify docs when changing code
3. **Use consistent formatting** - Follow the same style throughout
4. **Include examples when helpful** - Show how to use complex functions

### Common Documentation Elements

#### For Classes:

- Purpose and responsibility
- Key attributes/properties
- Important methods overview
- Usage examples
- Dependencies and limitations

#### For Methods/Functions:

- What the function does
- Parameters (type, meaning, constraints)
- Return value (type, meaning)
- Side effects
- Exceptions that might be raised
- Algorithm complexity (if relevant)

#### For Modules:

- Overall purpose
- Main classes/functions provided
- Dependencies
- Author and version information
- Usage examples

## Using PyDoc to Browse Documentation

### Starting PyDoc Server

```bash
# Start the PyDoc server
pydoc3 -b
```

This opens a webpage in your browser showing:

- **Built-in Modules**: Core Python modules like `itertools`, `collections`, etc.
- **Library Modules**: Installed third-party packages
- **Your Local Modules**: Your own Python files (when in Python path)

### Navigating PyDoc Interface

- **Module Index**: Browse all available modules
- **Topics**: Python language topics
- **Keywords**: Search functionality
- **Search**: Find specific modules or functions

### Example: Exploring itertools

The `itertools` module provides functional tools for creating and using iterators, including:

- `combinations(iterable, r)`: Returns successive r-length combinations
- `permutations(p, r)`: Returns successive r-length permutations
- `product(p, q, ...)`: Cartesian product of iterables
