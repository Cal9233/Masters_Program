CSC 6301 Week 1 & 2 Study Guide
Software Design & Documentation

📚 WEEK 1: Python Documentation with pydoc
Core Concepts to Master

1. The Importance of Documentation
   Why Documentation Matters:

Documentation is for humans, not computers
Essential for software maintenance and reuse
Helps with bug fixes, functionality changes, and code understanding
"Undocumented software is often useless"

Two Main Purposes:

Software Readability (maintenance) - understanding open code
Software Specification (reuse) - understanding encapsulated code

2. Python Docstrings
   What to Document:

Modules/Packages: First line of file with triple quotes
Classes: First line after class declaration
Functions/Methods: First line after function definition

Docstring Syntax:
pythondef my_function(param1, param2):
"""
Brief description of function.

    Longer description if needed.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value
    """
    return result

3. pydoc Tool Usage
   Reading Documentation:

Command line: pydoc3 -b (opens web browser)
Access docstrings: object.**doc**
Browse built-in modules and packages

Best Practices:

Use punctuation marks
Don't repeat obvious information
Don't mix remarks (#) with documentation
Keep documentation concise but clear

📚 WEEK 2: Java Documentation with javadoc
Core Concepts to Master

1. Python to Java Transition
   Key Differences:
   PythonJavaUntyped variablesAll variables must be typedFunctions can exist independentlyEverything must be in a classIndentation for structureCurly braces {} and semicolons ;Documentation after definitionDocumentation before definition
   Basic Java Structure:
   javapublic class HelloWorld {
   public static void main(String[] args) {
   System.out.println("Hello Java");
   }
   }
2. javadoc Documentation System
   Three Documentation Levels:

Class Level: Documents the entire class
Field Level: Documents class variables
Method Level: Documents individual methods

javadoc Syntax:
java/\*\*

- Brief description of class/method.
-
- Longer description if needed.
-
- @param param Name Description of parameter
- @return Description of return value
- @throws ExceptionType When this exception is thrown
- @author Your Name
- @version 1.0
- @since Week 2 of CSC6301
  \*/
  public class MyClass {
  // implementation
  }
  Common javadoc Tags:

@param - Parameter description
@return - Return value description
@throws - Exception documentation
@author - Author information
@version - Version information
@since - When feature was added

3. Java Coding Guidelines
   Naming Conventions:

Variables/Methods: camelCase (start lowercase)
Classes/Interfaces: CamelCase (start uppercase)
Constants: ALL_CAPS_WITH_UNDERSCORES
Packages: lowercase

Code Organization:

Static class variables
Public instance variables
Protected instance variables
Private instance variables
Constructors (fewest parameters first)
Static class methods
Get/Set methods
Other public methods
Protected methods
Private methods

Documentation Requirements:

Every public class must have javadoc
Every public method must have javadoc
First sentence should be concise summary
Don't document bugs or fixes in javadoc

🎯 Practice Questions
Week 1 - Python Documentation

1. Multiple Choice: What is the primary purpose of documentation?
   a) To help the computer execute code faster
   b) To help humans understand and maintain code
   c) To make code files larger
   d) To replace comments in code
2. Fill in the blank: Python docstrings use **\_\_\_** quotes and are placed **\_\_\_** the definition.
3. True/False: You should always mix regular comments (#) with docstrings for better documentation.
4. Code Analysis: What's wrong with this docstring?
   pythondef add_numbers(a, b):
   """
   adds two numbers
   """
   return a + b
5. Command Question: What command opens pydoc in a web browser?
   Week 2 - Java Documentation
6. Multiple Choice: In Java, javadoc comments use:
   a) /\* _/
   b) /\*\* _/
   c) // //
   d) ''' '''
7. Code Conversion: Convert this Python function to Java with proper javadoc:
   pythondef calculate_area(length, width):
   """Calculate the area of a rectangle."""
   return length \* width
8. True/False: In Java, documentation goes AFTER the method definition, just like Python.
9. Naming Convention: Which is the correct Java variable name?
   a) MessageText
   b) messageText
   c) message_text
   d) MESSAGETEXT
10. Fill in the blanks: The three levels of javadoc documentation are **\_\_\_**, **\_\_\_**, and **\_\_\_**.

💡 Practical Exercises
Exercise 1: Python Documentation
Create a Python class Calculator with methods for basic operations. Include proper docstrings for the class and all methods.
Exercise 2: Java Translation
Convert your Python Calculator to Java with proper javadoc documentation.
Exercise 3: Documentation Generation
Generate HTML documentation from both your Python and Java code using pydoc and javadoc respectively.

🔧 Tools and Commands Reference
Python Tools
bash# Open pydoc browser interface
pydoc3 -b

# View specific module documentation

pydoc3 module_name

# Access docstring in Python

print(object.**doc**)
Java Tools
bash# Generate javadoc
javadoc -author -version ClassName.java

# View javadoc help

javadoc -help

# Compile Java file

javac ClassName.java

# Run Java program

java ClassName

⚠️ Common Mistakes to Avoid

Python: Don't mix # comments with docstrings
Java: Don't forget semicolons and proper braces
Both: Don't document obvious things ("this variable stores a number")
Java: Don't put javadoc AFTER the method (it goes before)
Naming: Don't mix naming conventions within the same language
Documentation: Don't document bugs or temporary fixes in official docs

📋 Quick Reference Checklist
Before any exam/quiz, make sure you can:

Write proper Python docstrings for modules, classes, and functions
Use pydoc to generate and view documentation
Convert basic Python programs to Java
Write proper javadoc comments with common tags
Follow Java naming conventions
Generate HTML documentation with javadoc
Explain the differences between Python and Java documentation approaches
Organize Java code according to best practices

🎓 Study Tips

Practice coding in both languages - The best way to master this is hands-on practice
Generate actual documentation - Use pydoc and javadoc tools regularly
Read existing documentation - Look at well-documented open source projects
Focus on the "why" - Understand why documentation is important, not just how to write it
Memorize common javadoc tags - @param, @return, @throws are frequently used
Practice naming conventions - These are often tested and essential for good code

Remember: Good documentation is as important as good code!RetryCcan you format this for a md file?Editmarkdown# CSC 6301 Week 1 & 2 Study Guide

## Software Design & Documentation

---

## 📚 WEEK 1: Python Documentation with pydoc

### Core Concepts to Master

#### **1. The Importance of Documentation**

**Why Documentation Matters:**

- Documentation is for **humans**, not computers
- Essential for software **maintenance** and **reuse**
- Helps with bug fixes, functionality changes, and code understanding
- **"Undocumented software is often useless"**

**Two Main Purposes:**

1. **Software Readability** (maintenance) - understanding open code
2. **Software Specification** (reuse) - understanding encapsulated code

#### **2. Python Docstrings**

**What to Document:**

- **Modules/Packages**: First line of file with triple quotes
- **Classes**: First line after class declaration
- **Functions/Methods**: First line after function definition

**Docstring Syntax:**

```python
def my_function(param1, param2):
   """
   Brief description of function.

   Longer description if needed.

   Args:
       param1: Description of first parameter
       param2: Description of second parameter

   Returns:
       Description of return value
   """
   return result
3. pydoc Tool Usage
Reading Documentation:

Command line: pydoc3 -b (opens web browser)
Access docstrings: object.__doc__
Browse built-in modules and packages

Best Practices:

Use punctuation marks
Don't repeat obvious information
Don't mix remarks (#) with documentation
Keep documentation concise but clear


📚 WEEK 2: Java Documentation with javadoc
Core Concepts to Master
1. Python to Java Transition
Key Differences:
PythonJavaUntyped variablesAll variables must be typedFunctions can exist independentlyEverything must be in a classIndentation for structureCurly braces {} and semicolons ;Documentation after definitionDocumentation before definition
Basic Java Structure:
javapublic class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}
2. javadoc Documentation System
Three Documentation Levels:

Class Level: Documents the entire class
Field Level: Documents class variables
Method Level: Documents individual methods

javadoc Syntax:
java/**
 * Brief description of class/method.
 *
 * Longer description if needed.
 *
 * @param paramName Description of parameter
 * @return Description of return value
 * @throws ExceptionType When this exception is thrown
 * @author Your Name
 * @version 1.0
 * @since Week 2 of CSC6301
 */
public class MyClass {
    // implementation
}
Common javadoc Tags:

@param - Parameter description
@return - Return value description
@throws - Exception documentation
@author - Author information
@version - Version information
@since - When feature was added

3. Java Coding Guidelines
Naming Conventions:

Variables/Methods: camelCase (start lowercase)
Classes/Interfaces: CamelCase (start uppercase)
Constants: ALL_CAPS_WITH_UNDERSCORES
Packages: lowercase

Code Organization:

Static class variables
Public instance variables
Protected instance variables
Private instance variables
Constructors (fewest parameters first)
Static class methods
Get/Set methods
Other public methods
Protected methods
Private methods

Documentation Requirements:

Every public class must have javadoc
Every public method must have javadoc
First sentence should be concise summary
Don't document bugs or fixes in javadoc


🎯 Practice Questions
Week 1 - Python Documentation
1. Multiple Choice: What is the primary purpose of documentation?

a) To help the computer execute code faster
b) To help humans understand and maintain code
c) To make code files larger
d) To replace comments in code

2. Fill in the blank: Python docstrings use _______ quotes and are placed _______ the definition.
3. True/False: You should always mix regular comments (#) with docstrings for better documentation.
4. Code Analysis: What's wrong with this docstring?
pythondef add_numbers(a, b):
    """
    adds two numbers
    """
    return a + b
5. Command Question: What command opens pydoc in a web browser?
Week 2 - Java Documentation
6. Multiple Choice: In Java, javadoc comments use:

a) /* */
b) /** */
c) // //
d) ''' '''

7. Code Conversion: Convert this Python function to Java with proper javadoc:
pythondef calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
8. True/False: In Java, documentation goes AFTER the method definition, just like Python.
9. Naming Convention: Which is the correct Java variable name?

a) MessageText
b) messageText
c) message_text
d) MESSAGETEXT

10. Fill in the blanks: The three levels of javadoc documentation are _______, _______, and _______.

💡 Practical Exercises
Exercise 1: Python Documentation
Create a Python class Calculator with methods for basic operations. Include proper docstrings for the class and all methods.
Exercise 2: Java Translation
Convert your Python Calculator to Java with proper javadoc documentation.
Exercise 3: Documentation Generation
Generate HTML documentation from both your Python and Java code using pydoc and javadoc respectively.

🔧 Tools and Commands Reference
Python Tools
bash# Open pydoc browser interface
pydoc3 -b

# View specific module documentation
pydoc3 module_name

# Access docstring in Python
print(object.__doc__)
Java Tools
bash# Generate javadoc
javadoc -author -version ClassName.java

# View javadoc help
javadoc -help

# Compile Java file
javac ClassName.java

# Run Java program
java ClassName

⚠️ Common Mistakes to Avoid

Python: Don't mix # comments with docstrings
Java: Don't forget semicolons and proper braces
Both: Don't document obvious things ("this variable stores a number")
Java: Don't put javadoc AFTER the method (it goes before)
Naming: Don't mix naming conventions within the same language
Documentation: Don't document bugs or temporary fixes in official docs


📋 Quick Reference Checklist
Before any exam/quiz, make sure you can:

 Write proper Python docstrings for modules, classes, and functions
 Use pydoc to generate and view documentation
 Convert basic Python programs to Java
 Write proper javadoc comments with common tags
 Follow Java naming conventions
 Generate HTML documentation with javadoc
 Explain the differences between Python and Java documentation approaches
 Organize Java code according to best practices


🎓 Study Tips

Practice coding in both languages - The best way to master this is hands-on practice
Generate actual documentation - Use pydoc and javadoc tools regularly
Read existing documentation - Look at well-documented open source projects
Focus on the "why" - Understand why documentation is important, not just how to write it
Memorize common javadoc tags - @param, @return, @throws are frequently used
Practice naming conventions - These are often tested and essential for good code

Remember: Good documentation is as important as good code!

📝 Answer Key
Practice Questions Answers:

b) To help humans understand and maintain code
triple quotes and are placed after the definition
False - Don't mix remarks (#) with docstrings
Missing proper capitalization and punctuation. Should be: "Adds two numbers."
pydoc3 -b
b) /** */


java/**
 * Calculate the area of a rectangle.
 *
 * @param length The length of the rectangle
 * @param width The width of the rectangle
 * @return The area of the rectangle
 */
public static double calculateArea(double length, double width) {
    return length * width;
}

False - Java documentation goes BEFORE the method definition
b) messageText (camelCase starting with lowercase)
class, field, and method


This markdown file is ready to be saved as a `.md` file and will render properly on GitHub, in markdown viewers, or any platform that supports markdown formatting. The formatting includes proper headers, code blocks, tables, lists, checkboxes, and other markdown elements for optimal readability.
```

# CSC 6301 Study Guide - Software Design & Documentation

## Weeks 3-4: Java Classes, UML, and Software Reuse

---

## Table of Contents

1. [Java Classes & Inheritance](#java-classes--inheritance)
2. [Polymorphism & Interfaces](#polymorphism--interfaces)
3. [UML Class Diagrams](#uml-class-diagrams)
4. [Coding Guidelines](#coding-guidelines)
5. [Software Reuse](#software-reuse)
6. [Java Collections Framework](#java-collections-framework)
7. [Spring & Hibernate Frameworks](#spring--hibernate-frameworks)
8. [SOLID Principles](#solid-principles)
9. [Design Patterns](#design-patterns)
10. [Practice Questions](#practice-questions)

---

## Java Classes & Inheritance

### Key Concepts

- **Java**: Fundamentalist approach to Object-Oriented programming
- **Everything is an object** except primitive data types and native commands
- **Inheritance**: One of the three pillars of OOP (along with Encapsulation and Polymorphism)

### Inheritance Syntax

```java
// Python style (for comparison)
class Man(Human):
    pass

// Java style
public class Man extends Human {
    // class body
}
```

### Important Points

- **Subclass**: A class that inherits from another class
- **Superclass**: The class being inherited from
- Use `extends` keyword in Java
- Use `super()` to call parent constructor
- **Golden Rule**: Don't reuse code ignoring class meaning

### Study Questions

1. What keyword is used for inheritance in Java?
2. What is the difference between a subclass and superclass?
3. How do you call a parent class constructor in Java?

---

## Polymorphism & Interfaces

### Interface Definition

- **Interface**: Abstract type containing a collection of methods and constant variables
- Used for defining standard methods
- Enables polymorphism - same interface, different implementations

### Interface Syntax

```java
interface Animal {
    public void sound();
}

interface Mammal {
    public void milk();
}

class Dog implements Animal, Mammal {
    public void sound() {
        System.out.println("The dog says: ouf, ouf");
    }

    public void milk() {
        System.out.println("Dog's milk is just for dogs");
    }
}
```

### Key Benefits

- Allows algorithms to work with all classes implementing the interface
- Promotes code reusability
- Enables multiple inheritance of type (not implementation)

### Study Questions

1. What is an interface in Java?
2. How does an interface enable polymorphism?
3. Can a class implement multiple interfaces?

---

## UML Class Diagrams

### What is UML?

- **Unified Modeling Language** - semi-formal, general-purpose modeling language
- Current version: UML 2.0
- Provides standard way to visualize system design

### UML Characteristics

- **Semi-formal**: No automatic code generation from UML
- **Developmental**: Can be changed during application development
- **General-purpose**: Used in any context, environment, language, or platform

### UML Diagram Types

#### Structural Diagrams:

- Class diagram ⭐ (most important for OOP)
- Component diagram
- Composite structure diagram
- Deployment diagram
- Object diagram
- Package diagram
- Profile diagram

#### Behavioral Diagrams:

- Activity diagram
- Communication diagram
- Interaction overview diagram
- Sequence diagram
- State diagram
- Timing diagram
- Use case diagram

### Class Diagram Elements

#### Relationships:

- **Association** → (static relationship)
- **Inheritance** ▷ (subclass-superclass)
- **Realization/Implementation** ⇠⇠⇠ (dashed line with triangle)
- **Dependency** ⇠⇠⇠ (dashed line with arrow)
- **Aggregation** ◇ (catalog relationship)
- **Composition** ♦ (whole-part relationship)

### Study Questions

1. What does UML stand for and what is its purpose?
2. What's the difference between structural and behavioral diagrams?
3. How do you represent inheritance in a UML class diagram?
4. What's the difference between aggregation and composition?

---

## Coding Guidelines

### Modularity and Encapsulation Guidelines

#### Classes Should:

- Have **one single responsibility**
- Depend on **abstractions, not concrete details**
- Have instance variables used by multiple methods OR referenced between multiple calls

#### Access Modifiers (Java):

- **Private**: Only the class (recommended for most data fields)
- **Default** (package-private): Class & package
- **Protected**: Subclass access
- **Public**: No restriction (use sparingly)

**Golden Rule**: Private, maybe Protected, rarely Public!

### Law of Demeter

**Definition**: A module should not know about the innards of the objects it manipulates.

**Rule**: A method `f` of class `C` should only call methods of:

1. Class C itself
2. An object created by method f
3. An object passed as an argument to method f
4. An object held in an instance variable of class C

**Benefits**:

- Reduces coupling
- Improves maintainability
- Promotes encapsulation

### Objects vs Data Structures

- **Objects**: Hide data, expose behavior through methods
- **Data Structures**: Expose data, have minimal behavior
- **Avoid hybrids** of objects and data structures
- Minimize use of getters/setters
- Keep variables private for flexibility

### Study Questions

1. What is the Law of Demeter?
2. List the four types of objects a method can call methods on.
3. Why should most data fields be private?
4. What's the difference between objects and data structures?

---

## Software Reuse

### Types of Software Reuse

#### By Motivation:

- **Opportunistic**: Realization of existing components
- **Planned**: Strategic design for future reuse

#### By Scope:

- **Internal**: Team/developer reuses own components ✅
- **External**: Reuse components from others ✅ (with caution)

#### By Integration:

- **Referenced**: Code is referenced (linked) ✅
- **Forked**: Code is copied ❌ (discouraged)

### Best Practices

- **Internal + Planned + Referenced** = Ideal
- **External + Opportunistic + Referenced** = Common and acceptable
- **Forked reuse** = Discouraged (no benefit from updates/patches)
- Always verify external sources are reliable and well-documented

### Composition vs Aggregation

#### Composition

- Object of Class A **contains** object of Class B
- Class B object is **created within** Class A
- When A ceases to exist, B ceases to exist
- **Strong ownership**

```java
class Program {
    private List<Course> courses;

    public void addCourse(String name, List<Student> students) {
        Course c = new Course(name, students); // Created here
        this.courses.add(c);
    }
}
```

#### Aggregation

- Object of Class A **uses** object of Class B
- Class B object is **created outside** Class A
- When A ceases to exist, B continues to exist
- **Weak ownership**

```java
class Course {
    private List<Student> students;

    Course(String name, List<Student> students) {
        this.name = name;
        this.students = students; // Created elsewhere
    }
}
```

### Study Questions

1. What are the three dimensions of software reuse classification?
2. Why is forked reuse discouraged?
3. What's the difference between composition and aggregation?
4. In composition, what happens to the contained object when the container is destroyed?

---

## Java Collections Framework

### Overview

- Part of `java.util` package
- Provides interfaces and basic data structure classes
- Essential for software reuse in Java

### Key Interfaces

#### List Interface

- **LinkedList**: Double-linked list implementation
- **ArrayList**: Dynamic array implementation

##### LinkedList Methods:

```java
LinkedList<Integer> list = new LinkedList<>();
list.addLast(56);           // Add to end
list.addFirst(10);          // Add to beginning
list.removeLast();          // Remove from end
list.removeFirst();         // Remove from beginning
list.get(i);                // Get i-th element
ListIterator<Integer> iter = list.listIterator();
```

#### Queue Interface (FIFO)

```java
Queue<String> q = new LinkedList<>();
q.add("Adams");     // Add to tail
q.remove();         // Remove from head
q.peek();           // View head without removing
```

#### Stack Class (LIFO)

```java
Stack<String> s = new Stack<>();
s.push("Adams");    // Add to top
s.pop();            // Remove from top
s.peek();           // View top without removing
```

#### Map Interface

```java
Map<String, Integer> age = new HashMap<>();  // Hash table
Map<String, Integer> age = new TreeMap<>();  // Red-black tree

age.put("Elizabeth", 96);
age.get("Elizabeth");
age.remove("Elizabeth");
for (String key : age.keySet()) { /* iterate */ }
```

### Study Questions

1. What package contains the Java Collections Framework?
2. What's the difference between Queue and Stack?
3. How do you iterate through a LinkedList?
4. What's the difference between HashMap and TreeMap?

---

## Spring & Hibernate Frameworks

### Spring Framework

- **Created**: 2002, maintained by VMware
- **Purpose**: Comprehensive programming and configuration model for Java enterprise applications
- **Features**:
  - Development environment with project initializer
  - Multiple templates
  - Full framework (virtually impossible to grasp all features)
  - Integration with other frameworks

### Hibernate Framework

- **Created**: 2001, maintained by Red Hat
- **Purpose**: Object Relational Mapping (ORM) framework
- **Function**: Data persisting and retrieving from databases
- **Integration**: Works with Spring Framework

### ORM (Object Relational Mapping)

- Provides relational database access in object-oriented environment
- Bridges the gap between objects and relational databases
- Reduces boilerplate database code

### Study Questions

1. What company maintains the Spring Framework?
2. What is the primary purpose of Hibernate?
3. What does ORM stand for and what does it do?
4. How do Spring and Hibernate work together?

---

## SOLID Principles

### S - Single Responsibility Principle (SRP)

**Definition**: "Every software module should have only one reason to change"

- One class = one responsibility
- One method = one responsibility
- Reduces testing complexity
- Improves maintainability

### O - Open-Closed Principle (OCP)

**Definition**: "Software modules should be closed for modifications but open for extensions"

- Extend functionality through inheritance
- Use decorator design patterns
- Avoid modifying existing working code

### L - Liskov Substitution Principle (LSP)

**Definition**: "Subclasses should be substitutable for base classes"

- Child classes must be able to replace parent classes
- Implement by making base class abstract
- Defer implementation to derived classes

### I - Interface Segregation Principle (ISP)

**Definition**: "Clients should not be forced to implement interfaces they don't use"

- Many specific interfaces > one general interface
- Break fat interfaces into multiple smaller ones
- Clients depend only on methods they use

### D - Dependency Inversion Principle (DIP)

**Definition**: "High level modules should not depend upon low level modules. Rather, both should depend upon abstractions"

- Depend on abstractions, not concrete classes
- Use interfaces and abstract classes
- Enables flexibility and testability

### Study Questions

1. What does each letter in SOLID represent?
2. How does SRP reduce testing complexity?
3. What's the difference between "closed for modification" and "open for extension"?
4. Why should high-level modules not depend on low-level modules?

---

## Design Patterns

### What are Design Patterns?

- **Definition**: Reusable solutions to commonly occurring problems
- **Origin**: "Gang of Four" (GoF) book - "Design Patterns: Elements of Reusable Object-Oriented Software"
- **Authors**: Enrich Gamma, Richard Helm, Ralph Johnson, John Vlissides
- **Language Independent**: Focus on design, not implementation

### Categories of Design Patterns

#### 1. Creational Patterns (Deal with instantiation)

- **Singleton** ⭐
- Abstract Factory
- Factory Method
- Builder
- Prototype

#### 2. Structural Patterns (Deal with class composition)

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

#### 3. Behavioral Patterns (Deal with object communication)

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

### Singleton Pattern (Detailed)

#### Definition

- **Creational pattern** ensuring only one instance of a class
- Provides global access point to that instance
- Private constructor prevents external instantiation

#### When to Use Singleton

- Database connections
- Configuration management
- GUI components/controllers
- Device managers
- Printing services
- Logging systems

#### Implementation (Double-Checked Locking)

```java
class Singleton {
    private static volatile Singleton obj = null;

    private Singleton() {} // Private constructor

    public static Singleton getInstance() {
        if (obj == null) {
            synchronized (Singleton.class) {
                if (obj == null) {
                    obj = new Singleton();
                }
            }
        }
        return obj;
    }
}
```

#### Advantages

- Solves name collisions
- Supports eager/lazy initialization
- Thread safety (when properly implemented)
- Reduced memory footprint

#### Disadvantages

- Testing difficulties (global state)
- Concurrency issues (if not properly implemented)
- Limited extensibility
- Global dependency
- Hard to subclass
- Lifecycle management challenges

### Study Questions

1. Who are the "Gang of Four" and what did they contribute?
2. What are the three categories of design patterns?
3. When would you use the Singleton pattern?
4. What is the double-checked locking pattern and why is it used?
5. Name three advantages and three disadvantages of Singleton pattern.

---

## Golden Rules in Object-Oriented Design

1. **Program to Interface Not Implementation**
2. **Don't Repeat Yourself (DRY)**
3. **Encapsulate What Varies**
4. **Depend on Abstractions, Not Concrete Classes**
5. **Least Knowledge Principle** (Law of Demeter)
6. **Favor Composition over Inheritance**
7. **Hollywood Principle** ("don't call us, we'll call you")
8. **Apply Design Patterns wherever possible**
9. **Strive for Loosely Coupled System**
10. **Keep it Simple and Straightforward (KISS)**

---

## Practice Questions

### Multiple Choice Questions

1. **Which keyword is used for inheritance in Java?**
   a) inherits
   b) extends
   c) implements
   d) super

2. **What does UML stand for?**
   a) Universal Modeling Language
   b) Unified Modeling Language
   c) Universal Markup Language
   d) Unified Markup Language

3. **Which SOLID principle states "classes should have one reason to change"?**
   a) Open-Closed Principle
   b) Liskov Substitution Principle
   c) Single Responsibility Principle
   d) Dependency Inversion Principle

4. **In the Singleton pattern, what should the constructor be?**
   a) Public
   b) Private
   c) Protected
   d) Package-private

5. **What type of relationship exists when an object ceases to exist if its container ceases to exist?**
   a) Aggregation
   b) Composition
   c) Association
   d) Dependency

### Short Answer Questions

1. **Explain the difference between composition and aggregation with examples.**

2. **List and briefly explain the three types of software reuse classifications.**

3. **What is the Law of Demeter and why is it important?**

4. **Compare HashMap and TreeMap in Java Collections Framework.**

5. **What are the main disadvantages of the Singleton pattern?**

### Code Analysis Questions

1. **Identify the design pattern used in this code:**

```java
class DatabaseConnection {
    private static DatabaseConnection instance;

    private DatabaseConnection() {}

    public static DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
}
```

2. **Which SOLID principle is violated in this code and how would you fix it?**

```java
class EmailService {
    public void sendEmail(String message) {
        // Send email logic
    }

    public void logEmail(String message) {
        // Log email logic
    }

    public void validateEmail(String email) {
        // Validation logic
    }
}
```

### Essay Questions

1. **Discuss the importance of UML in software design and explain how class diagrams help in system architecture.**

2. **Compare and contrast the use of inheritance versus composition in object-oriented design. When would you choose one over the other?**

3. **Explain how the Java Collections Framework promotes software reuse and provide examples of when you would use different collection types.**

---

## Answer Key

### Multiple Choice Answers:

1. b) extends
2. b) Unified Modeling Language
3. c) Single Responsibility Principle
4. b) Private
5. b) Composition

### Code Analysis Answers:

1. **Singleton Pattern** - This implements the basic Singleton pattern (though not thread-safe)
2. **Single Responsibility Principle violation** - The EmailService class has multiple responsibilities. Should be split into separate classes: EmailSender, EmailLogger, EmailValidator.

---

## Study Tips

1. **Practice coding examples** - Write your own implementations of the patterns and principles discussed
2. **Draw UML diagrams** - Practice creating class diagrams for real-world scenarios
3. **Understand the "why"** - Don't just memorize patterns, understand when and why to use them
4. **Connect concepts** - See how SOLID principles relate to design patterns and good OOP practices
5. **Use real examples** - Think about how popular frameworks like Spring apply these concepts
6. **Review regularly** - These concepts build on each other, so regular review is essential

---

_Remember: Good software design is about creating maintainable, extensible, and robust systems. Focus on understanding the principles behind the patterns rather than just memorizing syntax._

# CSC 6301 Week 5 Study Guide: Software Development Lifecycle & Design Patterns

## Table of Contents

1. [Software Development Lifecycle (SDLC)](#sdlc)
2. [SDLC Strategies](#sdlc-strategies)
3. [Design Patterns](#design-patterns)
4. [Practice Questions](#practice-questions)
5. [Coding Exercises](#coding-exercises)
6. [Key Terms & Definitions](#key-terms)

---

## Software Development Lifecycle (SDLC) {#sdlc}

### Core Principle

**"The more effort you spend planning, the fewer patches are required."**

### The 7 Steps of SDLC

#### 1. Planning

- **Purpose**: Calculate time, resources, milestones, and timetables
- **Resources Include**:
  - Platforms (hardware, software, cloud)
  - People (managers, developers, etc.)
- **Detail Level**: Can be detailed or high-level

#### 2. Requirements Definition

- **Purpose**: Establish software modules and expected results
- **Methods**: UML specifications (Use cases, Class diagrams)
- **Also Known As**: Analysis phase
- **Granularity**: Can be coarse or fine-grained

#### 3. Design & Prototyping

- **Purpose**: Fine-grain specification of software
- **Includes**: Architecture, platforms, interfaces, security
- **Prototyping**: Proof of concept, can use different environments

#### 4. Coding

- **Characteristics**:
  - Central step in SDLC
  - Most studied and practiced phase
  - Can be straightforward when other phases are done well
  - Can use multiple programming languages

#### 5. Testing

- **Key Points**:
  - Close to coding phase, often cyclic
  - Different actors should perform coding vs. testing (reduce bias)
  - **Types**: Functional, unit, integration, system, statistical
  - Second most studied SDLC step

#### 6. Deployment

- **Focus**: Management issues rather than development
- **Challenge**: Interface with existing systems
- **Note**: Some authors disregard this step

#### 7. Operations & Maintenance

- **Characteristics**:
  - **Longest phase** in SDLC
  - Includes bug detection and correction
  - Spawns new full or partial cycles
  - Results in patches/new versions
  - Often involves different actors than initial development

---

## SDLC Strategies {#sdlc-strategies}

### Traditional Approaches

#### Waterfall

- **Characteristics**: Sequential, step-by-step advancement
- **Pros**: Simple, straightforward
- **Cons**: Not flexible, poor for evolving requirements
- **Best For**: Well-defined, stable requirements

#### V-Model

- **Characteristics**: Waterfall variation with testing after each step
- **Testing**: Verifications/validations throughout process
- **Advantage**: Early error detection

### Flexible Approaches

#### Iterative

- **Characteristics**: System refined at each step
- **Opposite**: Waterfall approach
- **Advantage**: Can adapt to changing requirements

#### Incremental

- **Characteristics**: Some system parts unknown initially
- **Relationship**: Variation of iterative strategy
- **Advantage**: Can develop known parts while discovering others

#### Spiral

- **Characteristics**: Cyclical application of all phases
- **Includes**: Full replanning, requirements redefinition
- **Advantage**: Most flexible strategy

### Modern Approaches

#### Lean

- **Philosophy**: "Don't do today what can be done tomorrow"
- **Focus**: Reduce overhead
- **Trade-off**: May sacrifice documentation

#### Agile

- **Characteristics**: Iterative + incremental combination
- **Philosophy**: Encourages early mistakes/errors
- **Popularity**: Compromise between Waterfall and DevOps

#### DevOps

- **Characteristics**: Agile + Lean combination
- **Approach**: Planning often forsaken
- **Risk**: May be too wild for reliable code

### Strategy Comparison

| Strategy  | Flexibility | Documentation | Speed     | Reliability |
| --------- | ----------- | ------------- | --------- | ----------- |
| Waterfall | Low         | High          | Low       | High        |
| V-Model   | Low         | High          | Low       | High        |
| Iterative | Medium      | Medium        | Medium    | Medium      |
| Spiral    | High        | Medium        | Medium    | Medium      |
| Agile     | High        | Low           | High      | Medium      |
| DevOps    | Very High   | Very Low      | Very High | Low         |

---

## Design Patterns {#design-patterns}

### Three Categories of Design Patterns

#### 1. Creational Patterns (Deal with Instantiation)

- **Singleton**: Ensures single instance
- **Abstract Factory**: Creates families of objects
- **Factory**: Creates objects without specifying exact class
- **Builder**: Constructs complex objects step by step
- **Prototype**: Creates objects by cloning existing instances

#### 2. Structural Patterns (Deal with Class Composition)

- **Adapter**: Allows incompatible interfaces to work together
- **Bridge**: Separates abstraction from implementation
- **Composite**: Composes objects into tree structures
- **Decorator**: Adds new functionality to objects dynamically
- **Facade**: Provides simplified interface to complex subsystem
- **Flyweight**: Shares objects efficiently
- **Proxy**: Provides placeholder/surrogate for another object

#### 3. Behavioral Patterns (Deal with Object Communication)

- **Chain of Responsibility**: Passes requests along handler chain
- **Command**: Encapsulates requests as objects
- **Interpreter**: Defines grammar representation
- **Iterator**: Provides way to access elements sequentially
- **Mediator**: Defines object interaction
- **Memento**: Captures and restores object state
- **Observer**: Notifies multiple objects of state changes
- **State**: Changes object behavior when internal state changes
- **Visitor**: Defines new operations without changing classes

---

## Detailed Pattern Examples

### Decorator Pattern (Structural)

#### Purpose

Adds behavior to objects dynamically without affecting other objects from the same class.

#### Key Components

1. **Component Interface**: Defines common interface (e.g., Coffee)
2. **ConcreteComponent**: Basic implementation (e.g., SimpleCoffee)
3. **Decorator Class**: Abstract wrapper class (e.g., CoffeeDecorator)
4. **ConcreteDecorators**: Specific decorators (e.g., MilkDecorator, SugarDecorator)

#### Implementation Steps

```java
// 1. Component Interface
interface Coffee {
    String getDescription();
    double getCost();
}

// 2. Concrete Component
class SimpleCoffee implements Coffee {
    public String getDescription() { return "Simple coffee"; }
    public double getCost() { return 5.0; }
}

// 3. Decorator Class
class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;
    public CoffeeDecorator(Coffee coffee) { this.decoratedCoffee = coffee; }
    public String getDescription() { return decoratedCoffee.getDescription(); }
    public double getCost() { return decoratedCoffee.getCost(); }
}

// 4. Concrete Decorators
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) { super(coffee); }
    public String getDescription() { return decoratedCoffee.getDescription() + ", milk"; }
    public double getCost() { return decoratedCoffee.getCost() + 1.5; }
}
```

### Observer Pattern (Behavioral)

#### Purpose

Notifies multiple objects of state changes to keep them synchronized.

#### Key Components

1. **Observer Interface**: Defines update method
2. **Subject Class**: Maintains observer list, notifies changes
3. **ConcreteObserver**: Implements specific update behavior
4. **Client**: Demonstrates pattern usage

#### Use Cases

- Model-View-Controller (MVC)
- Event management systems
- GUI event handling

### State Pattern (Behavioral)

#### Purpose

Allows object to change behavior when internal state changes.

#### Example: Traffic Light System

- **States**: Red, Yellow, Green
- **Transitions**: Each state defines next state
- **Context**: TrafficLightContext manages current state

---

## Practice Questions {#practice-questions}

### SDLC Fundamentals

1. **What is the longest phase in SDLC and why?**

   - Answer: Operations & Maintenance - includes bug fixes, updates, and spawns new cycles

2. **List the 7 steps of SDLC in order:**

   - Planning → Requirements Definition → Design & Prototyping → Coding → Testing → Deployment → Operations & Maintenance

3. **Why should different actors perform coding and testing?**

   - To reduce bias and improve objectivity in finding defects

4. **What's the key principle about planning in SDLC?**
   - The more effort spent planning, the fewer patches are required

### SDLC Strategies

5. **Compare Waterfall vs. Agile approaches:**

   - Waterfall: Sequential, rigid, high documentation, low flexibility
   - Agile: Iterative, flexible, encourages early errors, medium documentation

6. **What makes Spiral model unique?**

   - Cyclical application of all phases with full replanning and requirements redefinition

7. **What is the main philosophy of Lean methodology?**

   - "Don't do today what can be done tomorrow, because tomorrow it may not be needed anymore"

8. **Which strategy is considered a compromise between Waterfall and DevOps?**
   - Agile methodology

### Design Patterns

9. **Name the three categories of design patterns and their purposes:**

   - Creational: Deal with instantiation
   - Structural: Deal with class composition to add functionality
   - Behavioral: Deal with object communication

10. **What pattern would you use to add functionality to coffee orders dynamically?**

    - Decorator Pattern

11. **In Observer pattern, what are the two main classes involved?**

    - Observable (Subject) - where data changes occur
    - Observer - interface for objects interested in events

12. **What pattern manages state transitions in objects?**
    - State Pattern

### Application Questions

13. **You need to notify multiple UI components when data changes. Which pattern?**

    - Observer Pattern

14. **Your project requirements keep changing. Which SDLC strategy would you choose?**

    - Spiral or Agile methodology

15. **You're building a traffic light system. Which pattern for state management?**
    - State Pattern

---

## Coding Exercises {#coding-exercises}

### Exercise 1: Implement Simple Observer Pattern

Create a weather station that notifies multiple displays when temperature changes.

### Exercise 2: Extend Coffee Decorator

Add new decorators: WhipCreamDecorator, VanillaDecorator, ExtraShotDecorator

### Exercise 3: State Pattern Extension

Extend the traffic light example to include a pedestrian crossing state.

### Exercise 4: SDLC Planning

Plan a simple calculator application using the 7 SDLC steps.

---

## Key Terms & Definitions {#key-terms}

**SDLC**: Software Development Life Cycle - systematic process for developing software

**UML**: Unified Modeling Language - standardized modeling language for software design

**Prototype**: Early model built to test concepts and requirements

**Refactoring**: Restructuring existing code without changing external behavior

**Design Pattern**: Reusable solution to commonly occurring problems in software design

**Decorator**: Pattern that allows behavior to be added to objects dynamically

**Observer**: Pattern where subject maintains list of dependents and notifies them of changes

**State**: Pattern that allows object to alter behavior when internal state changes

**Waterfall**: Linear sequential SDLC approach

**Agile**: Iterative and incremental SDLC approach emphasizing flexibility

**Sprint**: Short development cycle in Agile methodology

**Stakeholder**: Person with interest or concern in the project

---

## Study Tips

1. **Understand the "why"** behind each SDLC phase
2. **Practice drawing** UML diagrams for design patterns
3. **Code examples** of each pattern discussed
4. **Compare and contrast** different SDLC strategies
5. **Think of real-world applications** for each pattern
6. **Review the trade-offs** between different approaches
7. **Focus on the relationships** between pattern components

## Assignment Reminders

- **Discussion Post**: Compare advantages/disadvantages of at least 2 SDLC strategies (Due: Friday midnight)
- **Programming Project #5**: Convert LinkedList project to Stack using Collections Framework (Due: Tuesday midnight)
- **Reply to Colleagues**: Respond to discussion posts (Due: Tuesday midnight)

# CSC 6301 Week 6 Study Guide: Version Control & Issue Tracking

## 📚 Overview

This study guide covers Version Control systems, Issue Tracking, Unit Testing, Static Code Analysis, and the Observer Design Pattern from CSC 6301 Week 6.

---

## 🎯 Learning Objectives

By the end of this week, you should be able to:

- Understand version numbering conventions (Major.Minor.Build)
- Explain the importance of environments and compatibility
- Use version control systems effectively
- Implement issue tracking in collaborative projects
- Create and run unit tests in Java
- Perform static code analysis
- Implement the Observer design pattern

---

## 📖 Key Concepts

### 1. Version Control Systems

#### **Version Numbering Convention**

- **Format**: M.N.b (Major.Minor.Build)
  - **M (Major)**: Significant changes, new features, breaking changes
  - **N (Minor)**: Small improvements, bug fixes, backward compatible
  - **b (Build/Patch)**: Bug fixes, patches, hotfixes

**Examples:**

- macOS Monterey 12.0.1
- Windows 11 (Build 21996.1)
- Python 3.10.7
- Java SE 19 Platform JSR 394

#### **Key Principles**

- Version control manages source code revisions
- Not all revisions become public software versions
- Can also manage documentation versions
- Structure follows DAG (Directed Acyclic Graph) with trunk, branches, and merges

### 2. Environments and Compatibility

#### **Why Version Management Matters**

- **Familiarity**: Previous experience with specific versions
- **Documentation**: Better documentation for certain versions
- **Compatibility**: Different versions have different characteristics

#### **Development Environment**

- Must track version numbers of ALL packages used
- Your software depends on specific versions used during build
- Some environments encapsulate package versions automatically

#### **Python Example with pip**

```bash
pip -r install requirements.txt
```

**Sample requirements.txt:**

```
absl-py==0.13.0
astor==0.8.1
cachetools==4.2.2
certifi==2021.5.30
numpy==1.18.5
```

### 3. Version Documentation

#### **Full Version Documentation**

Must include:

- Changes from previous version
- Requirements changes
- New and deprecated features
- Bugs addressed

#### **Code Revision Documentation**

Must state:

- Target audience (public, developers, testers, beta testers)
- Implementation issues
- All full version documentation items

### 4. Issue Tracking Systems

#### **Evolution: Bug Tracker → Issue Tracker**

- Originally tracked software bugs for maintenance
- Evolved to handle all types of issues, not just bugs
- Used in collaborative projects for discussion and resolution

#### **Issue Resolution Approaches**

- Fixing the bug
- Finding ways to avoid the issue
- Documenting the issue
- Collecting data about the issue

#### **Two Main Approaches**

**1. Issue Tracking Practices** (GitHub-style)

- Blog-like entries in repositories
- Effective for open software
- Ad hoc procedure
- Community-driven

**2. Issue Tracking Tools** (Centralized)

- Specialized software systems
- Controlled approach
- Systematic registry
- Used across SDLC phases (coding, testing, maintenance)

### 5. GitHub Repository

#### **Key Statistics**

- 83 million developers
- 200 million repositories (28 million public)
- Acquired by Microsoft in 2018
- Free registration required to store (not to download)

#### **Features**

- Version control
- Issue tracking
- Documentation standardization
- Collaborative development

---

## 🧪 Unit Testing in Java

### **Calculator Class Example**

```java
public class Calculator {
    public static int add(int a, int b) { return a + b; }
    public static int subtract(int a, int b) { return a - b; }
    public static int multiply(int a, int b) { return a * b; }

    public static int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
}
```

### **Test Class Components**

- **testAdd()**: Tests addition functionality
- **testSubtract()**: Tests subtraction functionality
- **testMultiply()**: Tests multiplication functionality
- **testDivide()**: Tests division functionality
- **testDivideByZero()**: Tests exception handling

### **Running Tests**

```bash
javac -d bin Calculator.java
java -cp bin --ea CalculatorTest.java
```

### **Code Coverage Benefits**

- Tests basic functionality
- Tests edge cases (division by zero)
- Uses assertions for validation
- Provides clear pass/fail feedback

---

## 🔍 Static Code Analysis

### **Purpose**

Examines source code for:

- Potential errors
- Code smells
- Adherence to coding standards
  **WITHOUT executing the program**

### **Popular Java Tools**

#### **1. Checkstyle**

- **Focus**: Coding standards and style
- **Configuration**: google_checks.xml
- **Integration**: Maven/Gradle plugins

#### **2. PMD**

- **Focus**: Code smells, potential bugs, style issues
- **Rules**: category/java/bestpractices.xml
- **Features**: Copy-paste detection (CPD)

#### **3. FindBugs/SpotBugs**

- **Focus**: Potential bugs identification
- **Settings**: effort='max', reportLevel='high'
- **Output**: XML/HTML reports

#### **4. SonarQube**

- **Focus**: Comprehensive platform
- **Features**: Integrates multiple tools
- **Benefits**: Detailed analysis dashboard

### **Implementation Steps**

1. Choose appropriate tool(s)
2. Install via Maven/Gradle
3. Configure rules and settings
4. Run analysis
5. Review and fix issues
6. Integrate with CI/CD pipeline

---

## 🎭 Observer Design Pattern

### **Definition**

Behavioral design pattern where a subject maintains a list of dependents (observers) and notifies them of state changes.

### **Key Components**

#### **1. Observer Interface**

```java
interface Observer {
    void update(String message);
}
```

#### **2. Subject Class**

```java
class Subject {
    private List<Observer> observers = new ArrayList<>();
    private String message;

    public void addObserver(Observer observer) { observers.add(observer); }
    public void removeObserver(Observer observer) { observers.remove(observer); }
    public void notifyObservers() { /* notify all observers */ }
    public void setMessage(String message) { /* update and notify */ }
}
```

#### **3. Concrete Observers**

```java
class ConcreteObserverA implements Observer {
    private String name;
    public void update(String message) { /* handle update */ }
}
```

### **Real-World Applications**

1. **UI Event Handling**: Button clicks, form inputs
2. **MVC Architecture**: Model changes notify views
3. **Notification Systems**: Email, SMS, push notifications
4. **Real-time Data**: Stock prices, weather updates
5. **Distributed Systems**: Event-driven microservices
6. **Document-View**: Microsoft Word, Google Docs
7. **Game Development**: Multiplayer game state updates
8. **Logging Frameworks**: Multiple log handlers
9. **Database Triggers**: Automatic actions on data changes
10. **Messaging Apps**: Real-time message delivery

### **Benefits**

- Loose coupling between objects
- Dynamic observer registration/removal
- Broadcast communication
- Event-driven architecture support

---

## 📝 Study Questions

### **Version Control Questions**

1. **What does each component of version number 3.7.2 represent?**

   - 3 = Major version
   - 7 = Minor version
   - 2 = Build/Patch version

2. **Why might you choose an older version of a software package?**

   - Familiarity with previous versions
   - Better documentation
   - Compatibility requirements
   - Stability concerns

3. **What is a development environment in version control context?**

   - Collection of specific package versions used to build software
   - Ensures reproducible builds
   - Tracks all dependencies

4. **What must be included in version documentation?**
   - Changes from previous version
   - Requirements changes
   - New and deprecated features
   - Bugs addressed

### **Issue Tracking Questions**

5. **How did bug trackers evolve into issue trackers?**

   - Originally tracked only software bugs
   - Evolved to handle all types of issues
   - Recognized that not all problems were actual bugs
   - Expanded to include feature requests, improvements

6. **What are the two main approaches to issue tracking?**

   - **Practices**: GitHub-style, community-driven, ad hoc
   - **Tools**: Centralized, systematic, controlled

7. **List four ways to resolve issues in collaborative projects:**
   - Fixing the bug
   - Finding ways to avoid the issue
   - Documenting the issue
   - Collecting data about the issue

### **Unit Testing Questions**

8. **What are the five test methods in the Calculator example?**

   - testAdd(): Tests addition
   - testSubtract(): Tests subtraction
   - testMultiply(): Tests multiplication
   - testDivide(): Tests division
   - testDivideByZero(): Tests exception handling

9. **What command enables assertions when running Java tests?**

   ```bash
   java -cp bin --ea CalculatorTest.java
   ```

10. **What does good code coverage include?**
    - Basic functionality testing
    - Edge case testing
    - Exception handling
    - Boundary value testing

### **Static Analysis Questions**

11. **Name four popular Java static analysis tools and their focus:**

    - **Checkstyle**: Coding standards and style
    - **PMD**: Code smells and potential bugs
    - **FindBugs/SpotBugs**: Bug identification
    - **SonarQube**: Comprehensive analysis platform

12. **What are the six steps for implementing static code analysis?**

    1. Choose appropriate tool
    2. Install the tool
    3. Configure rules and settings
    4. Run the static analysis
    5. Review and fix issues
    6. Integrate with CI/CD pipeline

13. **What does static analysis examine without executing code?**
    - Potential errors
    - Code smells
    - Adherence to coding standards

### **Observer Pattern Questions**

14. **What are the three key components of the Observer pattern?**

    - Observer Interface (defines update method)
    - Subject Class (maintains observer list)
    - Concrete Observer Classes (implement specific responses)

15. **Name five real-world applications of the Observer pattern:**

    - UI Event Handling
    - MVC Architecture
    - Notification Systems
    - Real-time Data Streaming
    - Distributed Event-Driven Systems

16. **What are the main benefits of the Observer pattern?**
    - Loose coupling between objects
    - Dynamic observer registration/removal
    - Broadcast communication capability
    - Support for event-driven architecture

### **GitHub Questions**

17. **What are GitHub's key statistics mentioned in the presentation?**

    - 83 million developers
    - 200 million repositories (28 million public)
    - Acquired by Microsoft in 2018
    - Free for public repositories

18. **What standardization does GitHub often provide?**
    - Documentation standards
    - Issue tracking systems
    - Collaborative development workflows

---

## 💡 Practical Exercises

### **Exercise 1: Version Analysis**

Analyze these version numbers and explain what type of changes each might represent:

- 2.1.0 → 2.1.1
- 2.1.5 → 2.2.0
- 2.9.3 → 3.0.0

### **Exercise 2: Requirements File**

Create a requirements.txt file for a Python project that uses:

- numpy version 1.21.0
- pandas version 1.3.2
- matplotlib version 3.4.3

### **Exercise 3: Unit Test Design**

Design unit tests for a `StringUtils` class with methods:

- `reverseString(String input)`
- `isPalindrome(String input)`
- `countVowels(String input)`

### **Exercise 4: Observer Implementation**

Implement an Observer pattern for a weather monitoring system where:

- Subject: WeatherStation
- Observers: PhoneDisplay, WebDisplay, EmailNotifier

### **Exercise 5: Issue Classification**

Classify these issues as Bug, Feature Request, or Documentation:

- Application crashes when dividing by zero
- Add dark mode support
- Unclear error messages in API documentation
- Performance degradation with large datasets

---

## 🎯 Exam Preparation Tips

### **Key Terms to Know**

- **DAG (Directed Acyclic Graph)**: Structure of version control revisions
- **Trunk**: Main development branch
- **Branch**: Separate development line
- **Merge**: Combining branches
- **Code Smells**: Signs of poor code design
- **CI/CD Pipeline**: Continuous Integration/Continuous Deployment
- **Assertion**: Testing mechanism to verify expected outcomes

### **Important Concepts**

1. **Version numbering significance** and when to increment each component
2. **Environment consistency** and dependency management
3. **Issue tracking evolution** from bugs to comprehensive issue management
4. **Test coverage importance** and edge case handling
5. **Static analysis benefits** for code quality
6. **Observer pattern applications** in real-world scenarios

### **Practical Skills**

- Writing effective unit tests
- Configuring static analysis tools
- Implementing design patterns
- Managing version dependencies
- Using GitHub for collaboration

---

## 🚀 Next Week Preview: Software Debugging, Testing, and Profiling

Get ready to dive into:

- Debugging techniques and tools
- Advanced testing methodologies
- Performance profiling
- Code optimization strategies

# CSC 6301 Week 7 Study Guide: Software Debugging, Testing, and Profiling

## Table of Contents

1. [Core Concepts Overview](#core-concepts-overview)
2. [Debugging](#debugging)
3. [Testing](#testing)
4. [Code Profiling](#code-profiling)
5. [State Design Pattern](#state-design-pattern)
6. [Practice Questions](#practice-questions)
7. [Key Terms Glossary](#key-terms-glossary)
8. [Hands-on Exercises](#hands-on-exercises)

---

## Core Concepts Overview

### Key Distinction

- **Debugging**: Happens during coding phase - programmer fixes issues
- **Testing**: Happens after coding - tester verifies effectiveness
- **Profiling**: Assesses efficiency of code (speed, memory usage)

### Quality Goals

- **Effective**: Code produces correct output
- **Efficient**: Code runs as fast as possible

---

## Debugging

### Types of Debugging Approaches

1. **Reactive**: Fix identified malfunctions
2. **Preemptive**: Explore possible malfunctions before they occur

### Types of Bugs/Errors

#### 1. Runtime Bugs

- Errors that appear when code is executed
- **Examples**:
  - Invalid array index
  - Division by zero
  - Null pointer exceptions

#### 2. Logic Bugs

- Errors in program logic/flow
- **Examples**:
  - Never-ending while loop
  - If statement that never executes
  - Incorrect algorithm implementation

#### 3. Pre-running Bugs

- Errors before execution
- **Examples**:
  - Missing compiled files (building errors)
  - Syntax errors (compile/interpretation errors)
  - Missing dependencies

### Debugging Tools and Techniques

#### 1. Ad Hoc Visualization

- **Method**: Insert print statements and input prompts
- **Pros**: Simple, immediate feedback
- **Cons**: Clutters code, manual cleanup needed
- **Example**:

```python
print("i:", i, "j:", j, "data:", a, end=" - ")
input("hit enter to go on")
```

#### 2. Ad Hoc Invariant Tests

- **Method**: Insert assertions to check expected conditions
- **Purpose**: Verify algorithm correctness at key points
- **Example**: In bubble sort, verify that after each iteration, the last i+1 elements are correctly ordered

#### 3. Regular Debuggers (IDE)

- **Features**:
  - **Breakpoints**: Pause execution at specific lines
  - **Step Over**: Execute next line without entering functions
  - **Step In**: Enter function calls
  - **Step Out**: Return to caller
  - **Continue**: Run until next breakpoint
  - **Variable inspection**: View current variable values
  - **Call stack**: See function call hierarchy

### VS Code Debugger Controls

- **Continue**: Resume until next breakpoint
- **Step Over**: Don't step into function calls
- **Step In**: Go into function calls
- **Step Out**: Return to caller
- **Restart**: Close and run again
- **Stop**: Stop debugging

---

## Testing

### Testing Philosophy

> "One eye could be as good as two, but four eyes are always better than two."

### Purpose

- Detect problems overlooked by the coder
- Industries often use separate teams for coding and testing
- Verify absence of faults across all combinations of initial states and usage cases

### Testing Classifications

#### By Method (How Testing is Done)

##### 1. Passive Testing

- Analyzes logs and traces of system execution
- No direct interaction with code
- **Use case**: Post-mortem analysis, monitoring

##### 2. Active Testing

- **Static Testing**:
  - Observing code without running it
  - "Proofreading the code"
  - Less common in industrial environments
- **Dynamic Testing**:
  - Executing code with or without debugger
  - Similar to debugging itself
  - Often considered redundant

#### By Awareness (What Tester Knows)

##### 1. Transparent-Box Testing (White-Box)

- **Also known as**: Clear box, glass box, structural testing
- **Tester knows**: Actual code implementation
- **Focus**: Internal structure and logic
- **Common use**: Unit testing
- **Techniques**: Code coverage analysis, path testing

##### 2. Black-Box Testing

- **Also known as**: Opaque-box, component interface, functional testing
- **Tester knows**: Only functionality, not implementation
- **Focus**: Input-output behavior
- **Common use**: System and acceptance testing

##### 3. Grey-Box Testing

- **Combination**: Tester knows implementation but tests functionality
- **Middle ground**: Structural knowledge + functional testing
- **Use case**: Integration testing

#### By Depth Level (Scope of Testing)

##### 1. Unit Testing

- **Target**: Specific code sections (functions, methods, classes)
- **Approach**: Usually transparent-box
- **Goal**: Verify individual components work correctly
- **Characteristics**: Isolated, fast, automated

##### 2. Integration Testing

- **Target**: Software interfaces between tested units
- **Approach**: Usually black-box
- **Goal**: Verify components work together
- **Types**: Big bang, incremental, sandwich

##### 3. System Testing

- **Target**: Complete integrated system
- **Scope**: End-to-end functionality
- **Environment**: Production-like conditions
- **Focus**: Requirements compliance

##### 4. Acceptance Testing

Different types based on goals:

- **User Acceptance**: Comply with user requirements
- **Operational Acceptance**: Verify overall functioning
- **Contractual/Regulatory**: Legal compliance
- **Alpha/Beta Tests**: Initial deployment testing

---

## Code Profiling

### Purpose

- Assess code efficiency (speed, memory, resources)
- Software profiling tools act as "x-ray of software system"
- Usually performed during coding phase and maintenance

### Types of Profiling

#### 1. Time Flat-Profiler

- Measures time spent in each code portion
- Identifies performance bottlenecks
- Shows function execution times

#### 2. Space Flat-Profiler

- Analyzes memory usage
- Tracks memory allocation and deallocation
- Identifies memory leaks

#### 3. Call-Chain Profiler

- Maps actual function calling graph
- Shows call relationships and frequencies
- Helps understand program flow

### Profiling Approaches

#### 1. User Programmed Profiling

- **Method**: Insert profiling code into system
- **Example**: Commands for memory usage and time snapshots
- **Pros**: Full control, specific measurements
- **Cons**: Code modification required

#### 2. Package Supported Profiling

- **Method**: Import profiling libraries
- **Example**: Python's cProfile package
- **Pros**: Easy integration, standard metrics
- **Cons**: Limited customization

#### 3. Dedicated Profiling Tools

- **Method**: External tools that attach to program
- **Example**: DataDog profiler
- **Pros**: Comprehensive analysis, no code changes
- **Cons**: May require setup, potential overhead

### Profiler Limitations

#### Event vs Statistical Profilers

##### Event Profilers

- **Method**: Collect measures at key execution points
- **Problem**: Must stop observed system to run profiler
- **Result**: Imprecise measurements due to interference

##### Statistical Profilers

- **Method**: Periodic sampling instead of event-based
- **Trade-off**: Sacrifice fine-grain precision for overall accuracy
- **Benefit**: Less interference with observed system

#### Common Issues

- Profiler runs simultaneously with observed system
- Operating system processes cause interference
- Difficulty getting exact time measurements
- Overhead from profiler itself affects results

---

## State Design Pattern

### Definition

Design pattern that allows object to change behavior when internal state changes. Used to manage state transitions without complex conditional logic.

### Components

#### 1. State Interface

- Defines common interface for all concrete states
- Contains methods that vary by state

#### 2. Concrete States

- Implement State interface
- Define behavior specific to each state
- Handle state transitions

#### 3. Context Class

- Maintains reference to current state
- Delegates behavior to current state object
- Provides methods to change state

### Real-World Examples

#### 1. Video Player

- **States**: Play, Pause, Stop
- **Transitions**: Play→Pause, Pause→Play, any→Stop

#### 2. Vending Machine

- **States**: Waiting for Money, Has Money, Dispensing
- **Flow**: Wait→Insert Money→Select Product→Dispense→Wait

#### 3. ATM Machine

- **States**: Idle, Card Inserted, PIN Entered, Transaction, End
- **Security**: Each state controls allowed operations

#### 4. Document Workflow

- **States**: Draft, Review, Approved
- **Permissions**: Different editing rights per state

#### 5. TCP Connection

- **States**: Established, Listening, Closed
- **Protocol**: Network communication states

---

## Practice Questions

### Debugging Questions

1. **Identify the bug type**: A program crashes with "IndexError: list index out of range"

   - Answer: Runtime bug

2. **Debug scenario**: In the bubble sort invariant test, why do lines 12-13 need a test for k == 0?

   - Answer: Prevents accessing negative array indices (a[k-1] when k=0)

3. **Tool selection**: When would you use ad hoc visualization vs IDE debugger?
   - Ad hoc: Quick debugging, simple issues, limited IDE access
   - IDE: Complex debugging, step-through needed, variable inspection required

### Testing Questions

4. **Testing type identification**: Testing a login function by only providing different username/password combinations without seeing the code

   - Answer: Black-box testing

5. **Depth level**: Testing whether individual functions work correctly in isolation

   - Answer: Unit testing

6. **Method classification**: Analyzing server logs to find performance issues

   - Answer: Passive testing

7. **Awareness type**: A tester knows the code structure but tests based on functional requirements
   - Answer: Grey-box testing

### Profiling Questions

8. **Profiler type**: Tool that shows which functions consume the most CPU time

   - Answer: Time flat-profiler

9. **Limitation**: Why might event profilers be inaccurate?

   - Answer: They stop the observed system to collect measurements, causing interference

10. **Tool selection**: When would you choose cProfile over manual timing code?
    - cProfile: Standard metrics, easy integration, comprehensive analysis
    - Manual: Specific measurements, full control, custom metrics

### State Pattern Questions

11. **Pattern application**: Design states for a traffic light system

    - Answer: Red, Yellow, Green states with appropriate transitions

12. **Component identification**: In State pattern, what manages the current state?
    - Answer: Context class

---

## Key Terms Glossary

**Ad Hoc Debugging**: Manual insertion of debugging code (prints, assertions)

**Black-Box Testing**: Testing without knowledge of internal implementation

**Call-Chain Profiler**: Tool that maps function calling relationships

**Dynamic Testing**: Testing by executing the code

**Event Profiler**: Profiler that collects data at specific execution points

**Fault**: Bug that can cause wrong results or software failure

**Grey-Box Testing**: Testing with knowledge of implementation but focused on functionality

**Integration Testing**: Testing interfaces between already tested units

**Invariant Test**: Assertion that checks expected conditions during execution

**Logic Bug**: Error in program logic or flow

**Passive Testing**: Analyzing logs and traces without interacting with code

**Profiling**: Assessing code efficiency (time, memory, resources)

**Reactive Debugging**: Fixing identified malfunctions

**Runtime Bug**: Error that appears during code execution

**State Pattern**: Design pattern for managing object behavior based on internal state

**Static Testing**: Code analysis without execution

**Statistical Profiler**: Profiler using periodic sampling instead of event-based collection

**Transparent-Box Testing**: Testing with full knowledge of code implementation

**Unit Testing**: Testing individual code components in isolation

**White-Box Testing**: Another term for transparent-box testing

---

## Hands-on Exercises

### Exercise 1: Debug Analysis

```python
# Bubble sort with invariant test
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

        # Invariant test - why is this needed?
        for k in range(len(a)-1, len(a)-(i+2), -1):
            if (k == 0):  # Why this test?
                break
            if (a[k] < a[k-1]):
                print("Error at i =", i)
                break
```

**Task**: Explain why the `k == 0` test is necessary and what happens without it.

### Exercise 2: Testing Classification

Classify each scenario:

1. A QA engineer tests a web form by entering various inputs without seeing the backend code
2. A developer reviews code line-by-line for potential security vulnerabilities
3. Testing team verifies that user registration, login, and profile modules work together
4. Analyzing application logs to identify crash patterns
5. Developer tests individual functions with knowledge of the algorithm used

### Exercise 3: Profiling Analysis

Given cProfile output:

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.020    0.000    0.030    0.000   prime.py:6(isPrime)
100     0.500    0.005    2.000    0.020   prime.py:13(findPrimes)
1       0.001    0.001    2.001    2.001   prime.py:1(<module>)
```

**Questions**:

- Which function should be optimized first?
- What does 'tottime' vs 'cumtime' indicate?
- How many times was isPrime called?

### Exercise 4: State Pattern Implementation

Design a state pattern for a simple music player with states: Stopped, Playing, Paused.

**Requirements**:

- Define appropriate state transitions
- Implement state-specific behaviors
- Handle invalid transitions gracefully

### Exercise 5: Debugging Tool Selection

For each scenario, choose the best debugging approach and justify:

1. Intermittent crash in production system
2. Algorithm producing wrong results in development
3. Performance issue in sorting function
4. Memory leak in long-running application
5. Logic error in conditional statements

---

## Quiz Preparation Tips

### Week 5-7 Topics to Review

- Object-oriented design principles
- Design patterns (especially State pattern)
- Debugging techniques and tools
- Testing methodologies and classifications
- Code profiling concepts and tools
- Software development lifecycle phases

### Study Strategy

1. **Understand concepts**: Don't just memorize definitions
2. **Practice classification**: Be able to categorize testing types
3. **Hands-on experience**: Use debuggers and profiling tools
4. **Real-world applications**: Understand when to use each technique
5. **Code analysis**: Be able to identify bugs and suggest fixes

### Common Question Types

- Definition matching
- Scenario classification
- Tool selection for specific problems
- Code debugging exercises
- Design pattern implementation
- Profiling output interpretation

Remember: The quiz is open book, so focus on understanding concepts and their applications rather than pure memorization!

# CSC 6301 Week 8 - Software Design Methodologies Study Guide

## Table of Contents

1. [Key Concepts Overview](#key-concepts-overview)
2. [Design Methodologies](#design-methodologies)
3. [Software Development Life Cycle (SDLC)](#software-development-life-cycle-sdlc)
4. [Software Development Methodologies](#software-development-methodologies)
5. [Design Patterns](#design-patterns)
6. [SOLID Principles](#solid-principles)
7. [Code Quality & Testing](#code-quality--testing)
8. [UML Diagrams](#uml-diagrams)
9. [Practice Questions](#practice-questions)
10. [Key Takeaways Checklist](#key-takeaways-checklist)

---

## Key Concepts Overview

### What are Design Methodologies?

- **Industry Context**: Software development methodologies are how the industry develops software
- **Academic Context (Stricto Sensu)**: Design methodologies concern the initial steps of software production
- **Relationship**: Design methodologies relate to going from **no software to running software**

### Core SDLC Phases Covered by Design Methodologies

1. **Design and Prototyping**
2. **Coding**
3. **Testing**

---

## Design Methodologies

### Academic Design Approaches (Stricto Sensu)

#### 1. Level-Oriented Design

- **Approach**: Stepwise refinement
- **Process**: Top-down process
- **Focus**: Breaking down complex problems into simpler components

#### 2. Data-Flow-Oriented Design

- **Approach**: Structured design
- **Process**: Derives the program structure
- **Focus**: How data flows through the system

#### 3. Data Structure-Oriented Design

- **Focus**: Emphasis on input and output data
- **Process**: Data transformation
- **Goal**: Design around data requirements

#### 4. Object-Oriented Design

- **Core Principles**:
  - **Abstraction**: Hiding implementation details
  - **Information Hiding**: Encapsulation of data
  - **Modularity**: Breaking system into modules

---

## Software Development Life Cycle (SDLC)

### Complete SDLC Phases

1. **Planning**
2. **Requirements Definition**
3. **Design and Prototyping** ← _Design Methodologies Focus_
4. **Coding** ← _Design Methodologies Focus_
5. **Testing** ← _Design Methodologies Focus_
6. **Deployment**
7. **Operations and Maintenance**

### Key Points

- No common understanding of SDLC phases exists across industry
- Design methodologies consensus covers: Design/Prototyping, Coding, Testing
- These phases transform requirements into working software

---

## Software Development Methodologies

### Goals of SDM

Software development should be:

- **As fast as possible**: Short time to market is valuable
- **As reliable as possible**: Fault-free software preferred
- **As reusable as possible**: Efficiency through scale
- **As accountable as possible**: Process documentation when needed

### Core SDM Concepts

- **Agreement**: Between people working together
- **Compromise**: Between strict discipline vs. flexibility
- **Reality**: Most methodologies fall between extremes

---

### 1. Waterfall Methodology

**Philosophy**: _"I wish the world was so simple that we could just go ahead and never look back."_

#### Characteristics

- **Primary Use**: Process management methodology
- **Best For**: Very well-planned projects
- **Structure**: Forces structured organization
- **Transparency**: Everyone can easily follow the process
- **Adaptability**: Some initiatives allow ad hoc adaptations

#### When to Use

- Simple, well-understood projects
- Projects with stable requirements
- When thorough documentation is required
- Regulatory environments

---

### 2. Lean Methodology

**Philosophy**: _"I wish the world was so simple that we could just go ahead, or any other direction."_

#### Characteristics

- **Scope**: Process management methodology (multiple areas)
- **Best For**: Very experienced teams
- **Responsibility**: Encourages individual responsibility
- **Commitment**: Everyone must be committed to the process
- **Flexibility**: Some initiatives include additional supporting rules

#### When to Use

- Experienced, self-motivated teams
- Projects with changing requirements
- When waste elimination is priority
- Fast-paced environments

---

### 3. Agile Methodology

**Philosophy**: _"It is better to be fast and good, than slow and bad... duh!"_

#### Characteristics

- **Purpose**: Break the stiffness of Waterfall
- **Structure**: Project broken into smaller tasks
- **Challenge**: Granularity of tasks often an issue
- **Results**: Impressive practical results
- **Limitation**: Rarely used for high-reliability software (low risk appetite)

#### Key Principles

- Iterative development
- Customer collaboration
- Responding to change
- Working software over documentation

---

### 4. DevOps Methodology

**Philosophy**: _"The more the merrier... duh!"_

#### Characteristics

- **Purpose**: Break barriers between Development and Operations teams
- **Team Structure**:
  - **Development Team**: Handles coding & testing
  - **Operations Team**: Handles deployment & maintenance
- **Process**: Assumes several revision and update tasks
- **Compatibility**: DevOps and Agile are compatible

#### Benefits

- Faster deployment cycles
- Improved collaboration
- Automated processes
- Continuous integration/delivery

---

### Other SDM Options

- **Scrum Software Development**
- **Rapid Application Development (RAD)**
- **Feature Driven Development (FDD)**
- **Rational Unified Process (RUP)**
- **Challenge-based Development**

**Important Note**: Different companies and teams may have different interpretations of the same methodology.

---

## Design Patterns

### Three Categories of Design Patterns

#### 1. Creational Patterns

**Purpose**: Deal with object instantiation

**Examples**:

- **Singleton**: Ensures only one instance of a class
- **Abstract Factory**: Creates families of related objects
- **Factory**: Creates objects without specifying exact classes
- **Builder**: Constructs complex objects step by step
- **Prototype**: Creates objects by cloning existing instances

#### 2. Structural Patterns

**Purpose**: Deal with class composition to add new functionality

**Examples**:

- **Adapter**: Allows incompatible interfaces to work together
- **Bridge**: Separates abstraction from implementation
- **Composite**: Treats individual objects and compositions uniformly
- **Decorator**: Adds behavior to objects dynamically
- **Facade**: Provides simplified interface to complex subsystem
- **Flyweight**: Reduces memory usage through object sharing
- **Proxy**: Provides placeholder/surrogate for another object

#### 3. Behavioral Patterns

**Purpose**: Deal with object communication and responsibilities

**Examples**:

- **Chain of Responsibility**: Passes requests along handler chain
- **Command**: Encapsulates requests as objects
- **Interpreter**: Defines grammar for language interpretation
- **Iterator**: Provides way to access collection elements
- **Mediator**: Defines how objects interact
- **Memento**: Captures and restores object state
- **Observer**: Notifies multiple objects of state changes
- **State**: Allows object to alter behavior when state changes
- **Visitor**: Defines new operations without changing classes

---

## SOLID Principles

### S - Single Responsibility Principle (SRP)

- **Definition**: A class should have only one reason to change
- **Goal**: Each class should have only one job/responsibility

### O - Open-Closed Principle (OCP)

- **Definition**: Classes should be open for extension, closed for modification
- **Goal**: Add new functionality without changing existing code

### L - Liskov Substitution Principle (LSP)

- **Definition**: Child class must be substitutable for its parent class
- **Goal**: Ensure inheritance relationships work correctly
- **Key**: Child class can assume parent's place without errors

### I - Interface Segregation Principle (ISP)

- **Definition**: Interface should be as small as possible in terms of cohesion
- **Goal**: Interfaces should do ONE thing
- **Benefit**: Clients shouldn't depend on methods they don't use

### D - Dependency Inversion Principle (DIP)

- **Definition**:
  - High-level modules should not depend on low-level modules
  - Both should depend on abstractions
  - Abstractions should not depend on details
  - Details should depend on abstractions

---

## Code Quality & Testing

### Access Modifiers (Java)

**Guideline**: "Private, maybe Protected, rarely Public!"

#### Access Levels

- **Private**: Only the class itself
- **Default**: Class & package
- **Protected**: Subclass access too
- **Public**: No restrictions

#### Best Practices

- **Data Fields**: Almost always private (except constants)
- **Public Methods**: Only when intended for external use
- **Private Methods**: Used only within associated class

### Unit Testing & Code Coverage

#### Testing Goals

- **Basic Functionality**: Test arithmetic operations
- **Edge Cases**: Test division by zero, boundary conditions
- **Coverage**: Aim for 100% code coverage
- **Automation**: Implement automated testing

#### Code Analysis Tools

- **Linters**: Check coding standards and style
- **Static Analysis**: Find potential bugs and issues
- **Coverage Tools**: Measure test coverage

### Linter Analysis Example Issues

1. **Missing Javadoc Comments**: Classes and methods need documentation
2. **Magic Numbers**: Use named constants instead of hard-coded values
3. **Variable Naming**: Use descriptive variable names
4. **Braces**: Use braces for all loops and conditionals
5. **Indentation**: Maintain consistent formatting

---

## UML Diagrams

### UML 2.0 - Unified Modeling Language

#### Structural Diagrams

- **Class Diagram**: Shows classes and relationships (most important for OO)
- **Component Diagram**: Shows component organization
- **Composite Structure Diagram**: Shows internal structure
- **Deployment Diagram**: Shows hardware/software mapping
- **Object Diagram**: Shows object instances
- **Package Diagram**: Shows package dependencies
- **Profile Diagram**: Shows UML extensions

#### Behavioral Diagrams

- **Activity Diagram**: Shows workflow/business processes
- **Communication Diagram**: Shows object interactions
- **Interaction Overview Diagram**: Shows interaction sequences
- **Sequence Diagram**: Shows message exchanges over time
- **State Diagram**: Shows state transitions
- **Timing Diagram**: Shows timing constraints
- **Use Case Diagram**: Shows system functionality

**Key Point**: For OO systems, the Class Diagram is often the most important design document.

---

## Practice Questions

### Conceptual Questions

1. **What are the three SDLC phases that design methodologies primarily cover?**

2. **Explain the difference between design methodologies in the academic sense (stricto sensu) vs. industry context.**

3. **What are the four main academic design approaches and their focus areas?**

4. **List and explain the goals of Software Development Methodologies (4 "as possible" criteria).**

5. **Compare and contrast Waterfall vs. Agile methodologies. When would you use each?**

### SOLID Principles Questions

6. **A class that handles both user authentication AND email sending violates which SOLID principle? Explain why.**

7. **Give an example of how the Liskov Substitution Principle could be violated.**

8. **How does the Dependency Inversion Principle improve code maintainability?**

### Design Patterns Questions

9. **You need to ensure only one database connection exists in your application. Which design pattern would you use and why?**

10. **You want to add logging functionality to existing classes without modifying them. Which pattern category and specific pattern would help?**

11. **Categorize these patterns: Observer, Factory, Adapter, Singleton, Command**

### Methodology Questions

12. **A startup with experienced developers building a mobile app with changing requirements should use which methodology? Justify your answer.**

13. **What are the key differences between Development and Operations teams in the context of DevOps?**

14. **Why might Agile not be suitable for safety-critical software systems?**

### Code Quality Questions

15. **What access modifier should be used for class data fields and why?**

16. **List 5 common issues that code linters typically identify.**

17. **What does "100% code coverage" mean and why is it important?**

### UML Questions

18. **For an object-oriented system, which UML diagram is typically most important for guiding development?**

19. **Differentiate between structural and behavioral UML diagrams with examples.**

### Scenario-Based Questions

20. **You're leading a team developing banking software with strict regulatory requirements. Which methodology would you recommend and what practices would you emphasize?**

---

## Answer Key (Selected Answers)

### Conceptual Answers

1. **Three SDLC phases**: Design and Prototyping, Coding, Testing

2. **Academic vs Industry**:

   - Academic (stricto sensu): Focuses on initial steps of software production
   - Industry: Encompasses several phases leading to software production, relates to entire development process

3. **Four academic approaches**:
   - Level-oriented: Stepwise refinement (top-down)
   - Data-flow-oriented: Structured design (program structure)
   - Data structure-oriented: Input/output data emphasis
   - Object-oriented: Abstraction, information hiding, modularity

### SOLID Answers

6. **Single Responsibility Principle** - One class should have one reason to change. Authentication and email are separate concerns.

7. **LSP Violation Example**: A Rectangle-Square inheritance where Square overrides setWidth/setHeight in ways that break Rectangle's expected behavior.

### Pattern Answers

9. **Singleton Pattern** - Ensures only one instance of a class exists (creational pattern)

10. **Categorization**:

- Observer: Behavioral
- Factory: Creational
- Adapter: Structural
- Singleton: Creational
- Command: Behavioral

---

## Key Takeaways Checklist

### Development Best Practices

- [ ] Base everything on requirements (MOST IMPORTANT!)
- [ ] Create good design before development
- [ ] Draw your design (pictures worth 1000 words)
- [ ] Use design patterns (don't reinvent the wheel)
- [ ] Make design object-oriented following SOLID principles
- [ ] Break plans into small achievable chunks
- [ ] Demo progress to wide audience (including customers)
- [ ] Implement meticulous unit tests with 100% coverage
- [ ] Use analysis tools for code quality
- [ ] Implement automated testing
- [ ] Use CI/CD/CAT (Continuous Integration/Deployment/Automated Testing)
- [ ] Diplomatically dissuade pure Waterfall approaches
- [ ] Keep It Simple and Straightforward (KISS)

### Final Exam Preparation

- [ ] Review all weekly content
- [ ] Understand relationship between design and development methodologies
- [ ] Know when to apply different methodologies
- [ ] Understand SOLID principles with examples
- [ ] Recognize design pattern categories and examples
- [ ] Understand code quality best practices
- [ ] Know UML diagram types and purposes

### Remember for Exam

- **8 questions, 30 minutes each maximum**
- **Open book, open notes, NO general internet search**
- **Submit as single PDF**
- **Deadline: Saturday 11:59 PM EST**
- **Worth 25% of course grade**

---

## Final Review Tips

1. **Focus on Concepts**: Understand the 'why' behind each methodology
2. **Compare and Contrast**: Know when to use each approach
3. **Real-world Application**: Think about how you'd apply these in actual projects
4. **Patterns Recognition**: Be able to identify which pattern solves which problem
5. **Best Practices**: Remember the development checklist items
6. **Time Management**: Practice explaining concepts concisely (30 min per question)

**Good luck with your final exam!**
