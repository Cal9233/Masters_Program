# Sorted Stack Program

A Java program that reads integer numbers from user input and maintains them in a sorted Stack using the Java Collections Framework. This is a maintenance update from the original LinkedList implementation to demonstrate Stack-based data structures.

## Author

Calvin Malagon  
CSC6301 - Module 5 (Maintenance Update from Module 4)

## Program Description

This program demonstrates:

- Use of Java Collections Framework (Stack)
- Sorted data structure implementation using LIFO operations
- Object-oriented design principles (SOLID)
- Extensive code reuse rather than reimplementation
- Professional documentation and Javadoc generation
- Stack-specific sorting algorithms with temporary stack operations

The program reads integers from console input and automatically maintains them in a Stack with sorted order from smallest to largest (when displayed) using an efficient stack-based insertion algorithm that leverages LIFO (Last In, First Out) operations.

## Stack Implementation Details

### Key Differences from LinkedList Version:

- **Data Structure**: Uses `Stack<Integer>` instead of `LinkedList<Integer>`
- **Sorting Strategy**: Implements sorted insertion using temporary stack operations
- **LIFO Operations**: Leverages Last-In-First-Out stack behavior for intelligent sorting
- **Display Logic**: Converts stack to sorted list for user-friendly display

### Stack Sorting Algorithm:

1. When adding a new number, pop elements smaller than the new number to a temporary stack
2. Push the new number onto the main stack
3. Push all elements back from the temporary stack
4. This maintains sorted order with largest on top, smallest on bottom
5. For display, reverse the stack contents to show smallest to largest

## Prerequisites

- Java Development Kit (JDK) 8 or higher
- Command line terminal
- No IDE required

## How to Run the Program

### Step 1: Navigate to the Program Directory

```
cd CSC6301/Module_5
```

### Step 2: Compile the Program

```
javac *.java
```

### Step 3: Run the Program

```
cd ../..
java CSC6301.Module_5.SortedStack
```

### Step 4: Using the Program

1. The program will display a welcome message with Stack-specific instructions
2. Enter integer numbers one per line when prompted
3. Press Enter on an empty line to finish input
4. The program will display your numbers sorted from smallest to largest
5. The program shows the total count of numbers in the Stack

## Example Usage

```
=== Sorted Stack Program ===
Enter integer numbers (one per line).
Press Enter on an empty line to finish input.
Numbers will be stored in a Stack and displayed sorted from smallest to largest.
The Stack uses LIFO (Last In, First Out) operations with intelligent sorting.

Enter number: 25
Added 25
Enter number (or press Enter to finish): 10
Added 10
Enter number (or press Enter to finish): 30
Added 30
Enter number (or press Enter to finish): 15
Added 15
Enter number (or press Enter to finish):

=== Final Results ===
Stack contents sorted (smallest to largest): [10, 15, 25, 30]
Total numbers in Stack: 4
```

## Generating Documentation

### Generate Javadoc

Navigate to the Module_5 directory first:

```
cd CSC6301/Module_5
javadoc -d javadoc -author -version -use -windowtitle "Sorted Stack Program" -doctitle "CSC6301 Module 5 - Sorted Stack Implementation" *.java
```

### View Documentation

After generating Javadoc, open the documentation in your web browser:

**Option 1 - File Explorer/Finder:**
Navigate to the `CSC6301/Module_5/javadoc/` folder and double-click `index.html`

**Option 2 - Command Line:**

```
# macOS
open javadoc/index.html

# Windows
start javadoc/index.html

# Linux
xdg-open javadoc/index.html
```

## Project Structure

```
CSC6301/
├── Module_5/
│   ├── ConsoleDisplayManager.java    # Handles display output (Stack version)
│   ├── ConsoleInputHandler.java      # Handles user input (unchanged)
│   ├── DisplayManager.java           # Display interface (unchanged)
│   ├── InputHandler.java             # Input interface (unchanged)
│   ├── SortedCollection.java         # Collection interface (unchanged)
│   ├── SortedIntegerStack.java       # Stack implementation (NEW)
│   ├── SortedStack.java             # Main program coordinator (Stack version)
│   └── javadoc/                     # Generated documentation (after running javadoc)
├── Stack_UML.pdf                    # UML design diagram (updated for Stack)
└── README.md                        # This file
```

## Key Features

- **Collections Framework Usage**: Utilizes Java's Stack class with LIFO operations
- **Efficient Stack Sorting**: Custom insertion algorithm maintaining sorted order during insertion
- **Temporary Stack Operations**: Uses auxiliary stack for sorting during number insertion
- **Input Validation**: Handles invalid input gracefully (inherited from original architecture)
- **Clean Architecture**: Maintains SOLID principles with interface-based design
- **Extensive Code Reuse**: Leverages existing Java APIs and maintains existing interfaces
- **Professional Documentation**: Comprehensive Javadoc with Stack-specific code reuse elaboration

## Code Reuse Highlights

This Stack implementation extensively reuses existing Java components rather than reimplementing:

- **Stack from Collections Framework**: LIFO operations, capacity management, dynamic resizing
- **Collections.reverse()**: For efficient list reversal during display conversion
- **ArrayList**: For intermediate storage during stack-to-list conversion
- **Scanner**: For input processing (unchanged from LinkedList version)
- **Integer.parseInt()**: For type conversion (unchanged from LinkedList version)
- **StringBuilder**: For efficient string operations (unchanged from LinkedList version)

### Stack-Specific Reuse Benefits:

- Reuses Stack's natural LIFO behavior for insertion operations
- Reuses Collections framework for efficient sorting when conversion to list is needed
- Reuses existing interface contracts to maintain architectural consistency
- Reuses proven error handling patterns adapted for stack operations

## Maintenance Changes from LinkedList Version

### Modified Files:

1. **SortedList.java → SortedStack.java**: Updated class name, documentation, and default constructor
2. **SortedIntegerCollection.java → SortedIntegerStack.java**: Complete rewrite for Stack operations
3. **ConsoleDisplayManager.java**: Updated display messages for Stack context and LIFO explanations
4. **README.md**: Updated documentation for Stack implementation details

### Unchanged Files (Demonstrating Interface Benefits):

- **SortedCollection.java**: Interface remains identical
- **InputHandler.java**: Interface remains identical
- **DisplayManager.java**: Interface remains identical
- **ConsoleInputHandler.java**: Implementation works unchanged with Stack

## Performance Characteristics

- **Insertion**: O(n) for sorted insertion (worst case when new element is smallest)
- **Display**: O(n) for converting stack to sorted list
- **Space Complexity**: O(n) for main stack + O(n) for temporary stack during insertion
- **Stack Operations**: O(1) for push, pop, peek operations
- **Memory Usage**: Slightly higher than LinkedList due to temporary stack during insertion

## Commands Summary

| Task                | Command                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| Navigate to Program | `cd CSC6301/Module_5`                                                     |
| Compile             | `javac *.java`                                                            |
| Run Program         | `cd ../.. && java CSC6301.Module_5.SortedStack`                           |
| Generate Javadoc    | `javadoc -d javadoc -author -version -use *.java`                         |
| View Documentation  | Double-click `javadoc/index.html` or see platform-specific commands above |

## Version History

- **v1.0.0.0**: Original LinkedList implementation (Module 4)
- **v2.0.0.0**: Stack implementation maintenance update (Module 5)
  - Replaced LinkedList with Stack data structure
  - Implemented stack-based sorting algorithm using temporary stack
  - Updated documentation and examples for Stack operations
  - Maintained interface compatibility for seamless architecture preservation
  - Enhanced user experience with Stack operation explanations

## Testing Verification

The Stack implementation has been verified with:

- Empty stack handling
- Single element operations
- Pre-sorted input sequences (1,2,3,4)
- Reverse-sorted input sequences (4,3,2,1)
- Random order inputs (3,1,4,2)
- Duplicate number handling
- Large number ranges
- Invalid input error handling

All test cases demonstrate correct smallest-to-largest sorting behavior using Stack operations.

## Academic Learning Objectives Met

This maintenance project demonstrates:

- **Data Structure Adaptation**: Converting between different Collection types (LinkedList → Stack)
- **Algorithm Design**: Creating efficient sorting algorithms for LIFO structures
- **Code Reuse Principles**: Maximizing reuse of existing Java APIs and architectural patterns
- **Interface-Based Design**: Maintaining compatibility through proper abstraction
- **Professional Documentation**: Comprehensive technical documentation with maintenance change tracking
