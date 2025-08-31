# CSC 6303 Week 3 Study Notes: Go and Swift Languages

## Overview
Week 3 covers the transition from Python to modern languages: Go (Google) and Swift (Apple), focusing on their purpose, syntax, and key differences from Python.

---

## Setting Up Development Environment

### Online Options (Recommended for Learning)
**Go interpreters:**
- Better Go Playground
- Replit
- JDoodle

**Swift interpreters:**
- Replit
- JDoodle
- Swiftfiddle

**Important:** Always keep local copies of your code when using online servers.

### Local Installation
- **IDE Recommendation:** Visual Studio Code (free, cross-platform, lightweight)
- **Go:** Easily installed on any machine
- **Swift:** Easy on Mac OS/Linux, more complex on Windows
- **Note:** These languages are still evolving, as are their development environments

---

## Go Programming Language

### History and Purpose
- **Created:** 2009 by Google
- **Goal:** Be as efficient as C, as easy as Python, improve upon C++
- **Purpose:** Provide lighter syntax for modern demands while ensuring code safety

### Modern Demands Go Addresses
1. **Web development, Cloud and Network services**
   - Fast and scalable packages
   - APIs for providers

2. **Command-line interfaces, DevOps and site reliability**
   - Standard library
   - Syntax support
   - Documentation generator

### Safety Features (Avoiding "Sloppy Code")
- **Typed language**
- **Index verification** (prevents accessing elements outside valid range)
- **Lean syntax**
- **Google tool support**

### Program Structure
- Packages and a main function calling everything else
- Methods without classes
- C++ similar style with `{}` brackets
- **No semicolons required**

### Basic Commands

#### Functions (`func`)
```go
func sumMinMax(a, b int) (sum, min, max int) {
    sum = a + b
    if a < b { min, max = a, b }
    else     { min, max = b, a }
    return
}
```
- **Explicitly typed** if returning something
- Parameters passed by **value or reference** (programmer's choice)
- **Multiple typed returns** supported

#### Variables
**Declaration methods:**
- `var` keyword → Explicit type declaration
- Function parameters → Explicit type required
- `:=` operator → Implicit type inference (inside functions only)

**Data types:**
- Integers, Floats, Complex numbers (several precisions)
- Booleans, Strings

#### Decision Making
- `if - else if - else`
- `switch - case - default` (expression and type switches)

#### Loops (Only `for` loops)
1. **Traditional for loops**
   ```go
   for i := 0; i < 10; i++ {
       fmt.Printf("Iteration %d", i)
   }
   ```

2. **Infinite loops**
   ```go
   for {
       if i == 10 { break }
       // code here
   }
   ```

3. **Conditional loops**
   ```go
   for i < 10 {
       // similar to while loops
   }
   ```

4. **Range loops**
   ```go
   for index, element := range myList {
       fmt.Println(index, element)
   }
   ```

5. **String loops**
   ```go
   for index, character := range "abcdef" {
       fmt.Println(index, character)
   }
   ```

6. **Maps loops**
   ```go
   for key, data := range myMap {
       fmt.Println(key, data)
   }
   ```

7. **Channel loops** (for concurrency)

### Object-Oriented Features in Go
Go **does not have** standard OOP features like classes and inheritance, but provides:

#### User-Defined Data Structures
```go
type Rectangle struct {
    length int
    width  int
}
```

#### Methods
```go
// Accessor method (by value)
func (r Rectangle) Area() int {
    return r.length * r.width
}

// Mutator method (by reference)
func (r *Rectangle) SetDimensions(l, w int) {
    r.length = l
    r.width = w
}
```

### Advanced Go Features
- **Concurrency:** Goroutines with `go` keyword
- **Channels:** Communication between subroutines
- **Built-in services:**
  - `godoc` (documentation like javadocs/pydoc)
  - `go install` (package installation like pip)
  - `go mod` (dependency management)
  - `gorename` (safe variable renaming)
  - `go test` (unit testing)
  - `go vet` (static code analysis)

### Go's Bridge Philosophy
- **Light syntax** like Python (multiple assignments)
- **Coding safeguards** like C++ (typed variables)

---

## Swift Programming Language

### History and Purpose
- **Created:** 2014 by Apple
- **Goal:** Replace Objective-C (C extension with OO concepts from 1980s)
- **Purpose:** Integrate existing language concepts and offer easier fundamentals for Apple products
- **Evolution:** Expanded to other systems and platforms

### Historical Context
- **Objective-C:** Created by NeXT for OpenStep OS (with Steve Jobs)
- **Mac OS X:** Evolved from OpenStep using Objective-C
- **Swift:** Modern replacement to prevent common C bugs

### C Bugs Addressed by Swift

#### Null-pointer Dereferencing
- **C:** Crashes at runtime
- **Swift:** Uses **optionals** - clearly shows when values might be missing, requires checking before use

#### Code Reliability Enhancements
- **Assertions:** Check conditions during development
- **Protocols:** Define requirements that types must implement

### Program Structure
- Packages, sometimes main functions, frequently classes
- C++ similar style with `{}` brackets
- **Semicolons are optional**

### Basic Commands

#### Functions (`func`)
```swift
func sumMinMax(a: Int, b: Int) -> (sum: Int, min: Int, max: Int) {
    var sum: Int
    var min: Int
    var max: Int
    sum = (a + b)
    if a < b { min = a; max = b }
    else     { min = b; max = a }
    return (sum, min, max)
}
```
- **Explicitly typed** if returning something
- **Function overloading** supported
- Input parameters **typed**, passed by value or reference

#### Constants & Variables
- **Type safe:** `var age: Int = 25`
- **Data types:** Integers, Floats (several precisions), Booleans, Strings, Optional, Tuples
- **Keywords:**
  - `var` for variables
  - `let` for constants
  - `enum` for enumerations
  - `typealias` for aliases
  - `struct` for data structures
  - `class` for objects

#### Decision Making
- `if - else if - else`
- **Conditional operator:** `condition ? value1 : value2`
- `switch - case - default`
  - **Fallthrough** keyword (break is default)

#### Loops
1. **For-in loops**
   ```swift
   for v in values {
       print(v)
   }
   ```

2. **While loops**
   ```swift
   while i < 10 {
       print(i)
       i += 1
   }
   ```

3. **Repeat-while loops** (like do-while)
   ```swift
   repeat {
       print(i)
       i += 1
   } while i < 10
   ```

### Object-Oriented Concepts in Swift

#### Similarities with Python
- Subclasses for inheritance
- Methods and constructors
- Instance variables

#### Differences from Python
- **Method overloading** allowed
- **Polymorphism** with functions passed as parameters
- **Explicit overriding** of superclass methods (requires `override` keyword)

```swift
class Student : Person {
    var major: String
    
    override func card() -> String {
        return self.name+" "+self.familyName+" "+self.major
    }
}
```

---

## Key Comparisons: Python vs Go vs Swift

| Feature | Python | Go | Swift |
|---------|--------|----|----|
| **Typing** | Dynamic | Static (with inference) | Static (type safe) |
| **OOP** | Full OOP | Structs + Methods | Full OOP |
| **Syntax** | Indentation | Braces, no semicolons | Braces, optional semicolons |
| **Performance** | Interpreted | Compiled | Compiled |
| **Platform** | Cross-platform | Cross-platform | Apple-focused (expanding) |
| **Concurrency** | Limited | Goroutines/Channels | GCD/async-await |

---

## Week 3 Assignments

### Discussion Post (In-Class Exercise Grade)
**Question:** What are the advantages of using Go instead of Python?
- **Due:** Post by Friday, reply to 2 colleagues by Monday
- **Focus:** Technical characteristics, personal reasons with technical backing

### Programming Project #3 (Coding Projects Grade)
**Task:** Convert Python tribonacci program to Go
- **Requirements:** 
  - Exact same behavior (same input → same output)
  - Test both programs before submitting
  - Submit Go code + files in zipped folder
- **Due:** Next Monday 11:59 PM

**Python Code to Convert:**
```python
def tribonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [1, 1, 1]
        for i in range(3, n):
            next_num = fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3]
            fib_seq.append(next_num)
        return fib_seq

print(tribonacci(20))
```

---

## Study Tips for Exam

1. **Practice syntax conversion** between Python, Go, and Swift
2. **Understand key differences** in typing systems, OOP approaches, and concurrency
3. **Know the historical context** and purposes of each language
4. **Practice writing basic programs** in Go and Swift syntax
5. **Understand when to use each language** based on their strengths and intended use cases

### Common Exam Topics
- Language comparison tables
- Syntax translation exercises  
- Understanding Go's unique features (goroutines, channels, no classes)
- Swift's safety improvements over C
- Setting up development environments
- Basic programming constructs in each language