# CSC 6303 Week 2: Study Notes - From Python to Java and C/C++

## Overview
This week covers the transition from Python to more traditional programming languages (Java and C/C++), focusing on visible and subtle differences between these languages.

## Language History and Purpose

### Key Timeline
| Language | Created | Major Revisions | Initial Purpose |
|----------|---------|-----------------|-----------------|
| C | 1972 | 1990, 1999, 2017 | Simple code |
| C++ | 1985 | 1998, 2011 | Add OO to C |
| Java | 1995 | 2006, 2017... | Bring OO to industry |
| Python | 1991 | 2000, 2008 | Solve practical problems fast |

### Current Market Position
- **C**: Stable, embedded systems
- **C++**: Stable, classical CS/academia
- **Java**: Declining, big industry/large projects
- **Python**: Growing, open source/AI

## Development Environment Options

### Online Compilers/Interpreters
**C++ Options**: OnlineGDB, W3Schools, CPPsh
**Java Options**: OnlineGDB, JDoodle, Online Java

### Local Installation
- **Recommended IDE**: Visual Studio Code (free, cross-platform, lightweight)
- **Installation Requirements**: Proper compiler for your OS
- **Important**: Online servers behave as interpreters but call themselves compilers

## Visible Differences

### Program Structure

#### Python
- Packages, scripts (.py files)
- Sometimes main function, sometimes classes
- **Block Structure**: Indentation-based

#### C
- Packages with main function calling everything
- **Block Structure**: Delimited with `;` and `{ }`

#### C++
- Packages with main function + frequently classes
- **Block Structure**: Delimited with `;` and `{ }`

#### Java
- Packages with main method + classes (fully OO)
- **Block Structure**: Delimited with `;` and `{ }`

### Decision Structures

#### Python
- `if - elif - else`
- `match - case - _`

#### C/C++/Java
- `if - else`
- Conditional operator (`? :`)
- `switch - case - default`

### Variable Types

#### C
- Integers, floating points (different precisions)
- Pointers, doubles, chars, short, long, booleans
- Enumerations, arrays
- **Requirement**: Declaration and allocation needed

#### C++/Java
- Everything in C, plus strings
- **Requirement**: Declaration and allocation needed

#### Python
- Integers, floating points, booleans, lists, strings, dictionaries
- **Advantage**: No declaration or allocation needed

### Loop Structures

#### Python
- `for` loop with `range`, `break`, `continue`, `pass`, `else`
- `while` loop with `break`, `continue`, `else`

#### C/C++
- `for`, `while`, `do-while` loops
- `break`, `continue`, `goto`

#### Java
- `for`, `while`, `do-while` loops
- `break`, `continue` (no `goto`)

### Functions/Methods

#### Python
- **Untyped** functions
- Default parameter values allowed
- Pass by value (simple vars) or reference (lists)
- Multiple return values possible

#### C/C++/Java
- **Explicitly typed** (including `void`)
- Function overloading supported
- Programmer controls pass by value/reference
- Single return value only
- In Java: called "methods" since everything is a class

### Pass by Value vs Pass by Reference

**Pass by Value**:
- Copy of parameter passed to function
- Changes don't affect original variable

**Pass by Reference**:
- Reference/address of parameter passed
- Changes affect original variable

## Object-Oriented Programming

### Language Capabilities

#### C
- **No classes** - only user-defined abstract data types
- Data structures without methods

#### C++
- Goal: OO concepts without sacrificing C performance
- 1998: Standard Template Library (STL) added
- Abstract classes based on Java interfaces

#### Python
- Goal: OO concepts with minimal coding complexity
- Gradual evolution of OO features

#### Java
- Strictly follows all OO concepts
- Initially sacrificed performance for OO principles

### OO Concept Support

| Concept | Python | C++ | Java |
|---------|--------|-----|------|
| Objects, Classes, Inheritance | ✓ (syntax differences) | ✓ | ✓ |
| Polymorphism | Partial | ✓ | ✓ |
| Abstraction | Emulated | Abstract Classes | Interfaces |
| Encapsulation | Variable levels | Variable levels | Variable levels |

### OO Concepts Definitions

**Abstract Classes**: Structured way to define interfaces and shared behavior
**Polymorphism**: Ability to use one function/class in different ways
**Inheritance**: Class derives properties from parent class
**Data Abstraction**: Group classes together, hide unnecessary information
**Encapsulation**: Group data and methods into one unit with restricted access

## Subtle Differences (The Real Challenges)

### Package Availability
- **Major Challenge**: Different packages for similar functionality
- **Example - Linear Algebra**:
  - Python: numpy
  - C++: Eigen, LAPACK++
  - Java: Jblas

### Package Management
- **Python**: Dynamic, requires requirements.txt for version tracking
- **C++**: Precompiled packages, less version variability
- **Java**: Pre-interpreted modules, stable versions

### Documentation and Resources
**Official Sources**: Language/package documentation
**Community Sources**: GeeksForGeeks, W3Schools, TutorialsPoint
**Warning**: Always verify information - deprecated/wrong info exists online
**Key Principle**: "A good programmer always seeks help"

### Memory Management

#### C/C++
- **Explicit** memory allocation and release
- Performance maximized by user choices
- Code optimization during compilation

#### Java
- **Explicit** allocation, **optional** release
- **Garbage Collection** for unused memory
- Performance shared between user and JVM

#### Python
- **Implicit** allocation, **optional** release
- Performance depends on interpreter and package choices
- **Note**: Algorithm complexity matters for all languages

## Study Tips

### Key Differences to Remember
1. **Syntax learning** is easy (few days with good references)
2. **Real challenges** are in packages, documentation, and implementation
3. **Rosetta Stone** resources help with language translation
4. **Package adaptation** is the main obstacle to automatic conversion

### Important Resources
- Bubble Sort examples in multiple languages
- Matrix multiplication implementations
- Official language documentation
- Developer forums and communities

## Week 2 Assignments

### Discussion Post (Due Friday)
- Topic: Dream CS job and important programming languages
- Include personal and technical reasons

### Programming Project #2 (Due Monday)
- Convert C++ prime number program to Java
- Must produce identical output
- Test both versions before submission

### Quiz #1 (Available Friday, Due Monday)
- Covers Week 1 and Week 2 content
- 10 questions, multiple choice
- Open notes, one submission only
- Not timed, but due by Monday 11:59pm

## Next Week Preview
From Python to Go, Swift, and modern languages

---

**Remember**: The main problems in changing programming languages are NOT the languages themselves, but the ecosystem around them (packages, documentation, implementation details).