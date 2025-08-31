# CSC 6303 Week 1 Study Notes: Programming Language Classification and Families

## Course Overview
- **Course**: CSC 6303 Systems & Languages Survey
- **Instructor**: Maggie Mulhall
- **Institution**: Merrimack College
- **Focus**: Introduction to popular programming languages and operating systems

## Key Theoretical Foundations

### Turing Machine Fundamentals
- **Definition**: A tape with symbols that can be read or written
- **Core Innovation**: Capacity to read the tape and decide which command to execute (1920s)
- **Formal Equivalence**: Turing Machine can execute anything any modern programming language can (and vice versa)
- **Von Neumann Architecture** (1940s): Introduced memory-stored programs

### Universal Programming Principle
**All programming languages have the same expressiveness and follow Von Neumann architecture**

---

## Programming Language Families

### 1. Procedural Languages

#### Definition
Languages that define commands executed sequentially in a control flow (stored program)

#### Key Characteristics
- **Imperative**: High-level description of mandatory commands reflecting machine language
- **Control Flow**: Dictates execution order
- **Modular**: When commands can be encapsulated into modules (also called modular languages)
- **Algorithm Mapping**: Directly correspond to flowchart algorithms

#### Historical Evolution

##### Early Languages
- **Assembly Languages**: Procedural, close to machine code
- **ALGOL** (Algorithmic Language): First high-level procedural language
  - Inspiration for modern procedural languages
  - Focus on programming paradigms rather than applications

##### Application-Specific Languages
- **COBOL**: Database manipulation
- **FORTRAN**: Scientific (physics) processing
- **BASIC**: Occasional coding

##### Modern Procedural Languages
- **PASCAL & ADA**: Very close to ALGOL
- **C** (Dennis Ritchie, 1972): Ergonomic version of ALGOL ideas

### 2. The C Language Family

#### C Language Features
- **Short reserved words**: `int` instead of `Integer`
- **Compact commands**: 
  - `for (i=0; i<10; i++)` for loops
  - `a=(b<c)?b:c` for conditional assignment
- **Efficiency over clarity**: `&a` refers to memory address
- **Best suited for**: Close-to-hardware applications (embedded systems)

#### C's Children
- **C++ (1985)**:
  - Added object-oriented concepts
  - Maintained C compatibility
  - Popular in academia
  
- **Java (1995)**:
  - Deeper object-oriented concepts
  - Focus on industry standards and software reuse
  - Large industry adoption

#### C's Grandchildren
- **C# (Microsoft)**: Embedded checking, internationalization, .NET integration
- **Python**: Easy-to-code interpreted language
- **JavaScript**: Web scripting (unrelated to Java despite name)
- **Go (Google)**: General purpose with cross-compiler capabilities
- **Swift (Apple)**: Mobile and standalone device applications

---

## Execution Formats

### Compiled Languages
- **Process**: High-level code → compiler → machine language → execution
- **Examples**: C, C++
- **Advantage**: Performance
- **Disadvantage**: Less flexibility

### Interpreted Languages
- **Process**: High-level code → interpreter → execution
- **Examples**: Python, JavaScript
- **Advantage**: Flexibility
- **Disadvantage**: Lower performance
- **Note**: Interpreter itself is a compiled program

**Important**: Any code can be compiled OR interpreted - it's a choice of implementation

---

## Object-Oriented Programming (OOP)

### Definition
A subset of procedural programming that organizes code around modules for specific data structures. Combined data structures and methods are called **objects**.

### OOP Spectrum
- **No OOP**: C (can define data structures but no OOP concepts)
- **Optional OOP**: C++, Python (programmer decides how much OOP to use)
- **Full OOP**: Java (everything is an object, even the main program)

### Core OOP Concepts
- **Abstraction**
- **Encapsulation** 
- **Inheritance**
- **Polymorphism**

---

## Non-Procedural Languages

### Functional Languages
- **Concept**: Extreme modular programming where every definition is a function
- **Mathematical Foundation**: f(x) → y (function f receives input x, produces output y)
- **Examples**: Haskell, LISP
- **Application**: Can be applied to traditional procedural languages

### Logic Languages
- **Concept**: Based on mathematical logic expressions
- **Structure**: Series of facts and logic propositions
- **Execution**: Application of inference rules over facts and propositions
- **Nature**: Declarative (vs. imperative procedural languages)
- **Example**: Prolog (Datalog)
- **Historical Note**: Researched mainly in the 1990s
- **Future Potential**: May become important with quantum computing

---

## Machine Language & Assembly

### Machine Language
- **Definition**: Binary code specific to each processor/chipset
- **Components**: Commands, memory addresses, I/O peripheral access all in binary
- **Historical**: Originally hand-written by humans

### Assembly Language
- **Purpose**: Human-readable language converted to machine language
- **Process**: Assembly → compiler/interpreter → machine language
- **Classification**: Still procedural languages

---

## Study Tips for Exam

### Key Concepts to Memorize
1. **Turing Machine equivalence**: All programming languages have same expressiveness
2. **Von Neumann Architecture**: Memory-stored programs (1940s)
3. **Language families**: Procedural vs. Non-procedural
4. **Execution types**: Compiled vs. Interpreted
5. **OOP spectrum**: C (none) → C++/Python (optional) → Java (full)

### Language Timeline
1. **1920s**: Turing Machine concept
2. **1940s**: Von Neumann Architecture
3. **1972**: C language (Dennis Ritchie)
4. **1985**: C++
5. **1995**: Java and JavaScript

### Classification Framework
```
Programming Languages
├── Procedural
│   ├── By Execution: Compiled vs Interpreted
│   └── By Paradigm: Traditional vs Object-Oriented
└── Non-Procedural
    ├── Functional (Haskell, LISP)
    └── Logic (Prolog)
```

### Practical Applications
- **C**: Embedded systems, close-to-hardware
- **C++**: Academic applications, system programming
- **Java**: Enterprise applications, platform independence
- **Python**: Scripting, data science, ease of development
- **JavaScript**: Web development, scripting

---

## Important Notes
- **Performance vs Flexibility**: Compiled languages are faster, interpreted are more flexible
- **All languages are Turing complete**: Same computational power
- **OOP is optional**: Most languages allow choice of paradigm
- **Historical context matters**: Language design influenced by intended applications