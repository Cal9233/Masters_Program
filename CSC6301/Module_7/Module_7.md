# CSC 6301 Week 7 Study Guide: Software Debugging, Testing, and Profiling

## Table of Contents

1. [Debugging Fundamentals](#debugging-fundamentals)
2. [Testing Fundamentals](#testing-fundamentals)
3. [Code Profiling](#code-profiling)
4. [State Design Pattern](#state-design-pattern)
5. [Key Concepts Summary](#key-concepts-summary)
6. [Practice Questions](#practice-questions)

---

## Debugging Fundamentals

### Core Concept

**Debugging happens when you are coding. Testing happens after.**

The coding activity implies producing the most accurate code as possible:

- **Effective**: Should produce the correct output
- **Efficient**: Should run as fast as possible

### Types of Debugging

#### 1. **Reactive vs Preemptive Debugging**

- **Reactive**: When a malfunction is identified and needs to be fixed
- **Preemptive**: When the developer explores possible malfunctions

#### 2. **Types of Bugs/Errors**

- **Runtime bugs**: Error appears when code is executed
  - Examples: Invalid array index, division by zero
- **Logic bugs**: Error appears when program logic is flawed
  - Examples: Never-ending while loop, if statement never executed
- **Pre-running bugs**: Compilation or interpretation errors
  - Examples: Missing compiled file (building error), syntax errors

### Debugging Tools

#### 1. **Ad Hoc Visualization**

- **Basic approach**: Insert print/visualization commands in your code
- **Example**: Adding `print()` statements and `input()` for step-through debugging
- **Use case**: Simple debugging for understanding variable values

#### 2. **Ad Hoc Invariant Tests**

- **Sophisticated approach**: Insert invariant tests in your code
- **Purpose**: Check that certain conditions hold true at specific points
- **Example**: In bubble sort, verify that after each iteration, the last i+1 elements are ordered

#### 3. **Regular Debuggers (IDE)**

- **Most frequent option**: Using IDE debugger (like VS Code)
- **Key Features**:
  - **Continue**: Run until next breakpoint
  - **Step Over**: Don't step into function calls
  - **Step In**: Go into function calls
  - **Step Out**: Return to caller
  - **Restart**: Close and run again
  - **Stop**: Stop debugging
- **Benefits**: View active breakpoints and variable contents in real-time

---

## Testing Fundamentals

### Core Philosophy

**"One eye could be as good as two, but four eyes are always better than two."**

Industries keep different teams working on coding and testing to catch problems the coder might have missed.

### Testing Classifications

#### 1. **According to Way of Testing**

##### **Passive Testing**

- Analyzes logs and traces of system execution
- No direct interaction with code itself

##### **Active Testing**

- **Static Testing**: Observing code thoroughly without running it (proofreading)
  - Less commonly employed in industrial environments
- **Dynamic Testing**: Executing code with or without debugger
  - Often similar to debugging, considered redundant in many situations

#### 2. **According to Test Awareness**

##### **Transparent-Box Testing** (White-box)

- Tester is aware of actual code implementation
- Also known as: white-box, clear box, glass box, structural testing
- More frequently used for unit testing

##### **Black-Box Testing**

- Tester is NOT aware of exact implementation
- Only knows functionality of test subject
- Also known as: opaque-box, component interface, functional testing

##### **Grey-Box Testing**

- Middle ground approach
- Tester aware of code implementation BUT test based on functional aspects

#### 3. **According to Depth Level**

##### **Unit Testing**

- Tests specific section of code (function, method, class)
- Usually transparent-box testing

##### **Integration Testing**

- Evaluates software interfaces between already tested units
- Usually black-box testing
- **System Testing**: Specific case encompassing whole system

##### **Acceptance Testing**

- **User Acceptance**: Comply with user requirements
- **Operational Acceptance**: Verify overall functioning
- **Contractual/Regulatory Acceptance**: Legal compliance
- **Alpha/Beta Tests**: Initial deployment testing

### Key Testing Concepts

- **Faults (bugs)** can cause wrong results leading to software failure
- Testing verifies absence of faults across all combinations of:
  - **Preconditions**: Initial states
  - **Input combinations**: Usage cases

---

## Code Profiling

### Core Concept

**Profiling happens when the team assesses the efficiency of the code.**

While testing aims at software effectiveness, profiling assesses efficiency. Software profiling tools act as an "x-ray" of a software system.

### Types of Profiling

#### 1. **Time Profiling (Flat-Profiler)**

- Comprehensive dynamic analysis of time spent by each code portion

#### 2. **Memory Usage (Space Flat-Profiler)**

- Analysis of memory consumption patterns

#### 3. **Call-Chain Profiler**

- Analysis of actual function calling graph and execution characteristics

### Profiling Approaches

#### 1. **User Programmed Profiling**

- Software profiling implemented within observed system code
- Example: Inserting commands for memory usage and time snapshots

#### 2. **Package Supported Profiling**

- Import packages that provide seamless basic profile information
- **Python Example**: `cProfile` package

#### 3. **Dedicated Profiling Tools**

- External tools that plug into program execution
- **Example**: DataDog profiler with comprehensive graphical information

### Profiler Limitations

#### **Measurement Challenges**

- **Core Problem**: Profiler runs simultaneously with observed system
- Makes exact time measurements difficult

#### **Traditional Approaches**

- **Event Profilers**: Collect measures at key execution points
- **Issue**: Must stop observed system to run profiler tool
- **Result**: Considerable imprecisions due to OS process interference

#### **Statistical Profilers**

- **Approach**: Based on periodical samples rather than exact measurements
- **Trade-off**: Sacrifice fine-grain precision for overall precision

---

## State Design Pattern

### Definition

The State design pattern allows an object to change its behavior when its internal state changes. Used to manage state transitions within an object.

### Key Components

#### 1. **State Interface**

```java
public interface State {
    void doAction(TrafficLightContext context);
}
```

#### 2. **Concrete States**

- Implement State interface
- Define behavior specific to each state
- Handle state transitions

#### 3. **Context Class**

- Maintains instance of concrete state
- Allows state to be changed
- Provides method to trigger state transitions

### Common Use Cases

1. **Video Player**: Play, Pause, Stop states
2. **Vending Machine**: Waiting for money, Has money, Dispensing states
3. **ATM Machine**: Idle, Card inserted, PIN entered, Transaction states
4. **Text Editor**: Editing, Spell check, Save modes
5. **Document Workflow**: Draft, Review, Approved states
6. **Turnstile**: Locked, Unlocked states
7. **TCP Connection**: Established, Listening, Closed states
8. **Game Development**: Character states (Idle, Running, Jumping)
9. **Printer**: Ready, Printing, Error states

### Benefits

- Clean separation of different behaviors into distinct classes
- Eliminates complex conditional logic (if-else, switch statements)
- Makes code easier to manage and scale
- Behavior changes dynamically as internal state evolves

---

## Key Concepts Summary

### Remember the Sequence

1. **Debugging**: During coding phase - programmer produces best possible code
2. **Testing**: After coding - tester verifies effectiveness of programmer's code
3. **Profiling**: Assesses efficiency of the code (can happen during coding or maintenance)

### Critical Distinctions

- **Effectiveness vs Efficiency**: Testing focuses on correctness, profiling on performance
- **Reactive vs Preemptive**: Debugging can be response to problems or exploration of potential issues
- **Static vs Dynamic**: Code analysis without execution vs with execution
- **Box Testing Types**: Awareness level of implementation details

### Design Pattern Key

- **State Pattern**: Use when object behavior depends on current state and state transitions must be managed cleanly

---

## Practice Questions

### Debugging Questions

1. What are the three main types of bugs, and give an example of each?
2. When would you use invariant tests vs simple print statements for debugging?
3. What are the six main debugger control operations in VS Code?

### Testing Questions

4. Explain the difference between transparent-box, black-box, and grey-box testing.
5. What is the progression from unit testing to acceptance testing?
6. Why do industries often keep separate teams for coding and testing?

### Profiling Questions

7. What are the main limitations of software profilers?
8. Compare event profilers vs statistical profilers - what are the trade-offs?
9. Name the three main types of profiling and what each measures.

### State Pattern Questions

10. What problem does the State design pattern solve?
11. Give three real-world examples where State pattern would be appropriate.
12. What are the key components needed to implement State pattern?

### Integration Questions

13. How do debugging, testing, and profiling complement each other in the software development process?
14. In what scenarios might you use multiple debugging approaches simultaneously?
15. How does the State pattern relate to the concept of managing complexity in software systems?

---

## Quick Reference

### Week 7 Tasks Checklist

- [ ] **In-class Exercise**: Debug bubble sort code, explain why lines 12-13 need k==0 test (Due: Tuesday)
- [ ] **Programming Project #7**: Use cProfile on findPrimes program, optimize and report (Due: Next Tuesday)
- [ ] **Quiz #3**: Covers weeks 5, 6, and 7 content (Due: Tuesday)

### Key Terminology

- **Bug/Fault**: Error that can cause wrong results
- **Effectiveness**: Produces correct output
- **Efficiency**: Runs as fast as possible
- **Preconditions**: Initial states for testing
- **Invariant**: Condition that should always hold true
- **Profiling**: Assessment of code efficiency
- **State Transition**: Change from one state to another in State pattern
