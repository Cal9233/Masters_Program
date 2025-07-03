# CSC 6301 - Final Exam Cheat Sheet

## 📚 WEEK 1: Python Documentation with pydoc

#### **1. The Importance of Documentation**

**Why Documentation Matters:**

- Documentation is for **humans**, not computers
- Essential for software **maintenance** and **reuse**
- Helps with bug fixes, functionality changes, and code understanding
- **"Undocumented software is often useless"**

**Two Main Purposes:**

1. **Software Readability** (maintenance) - understanding open code
2. **Software Specification** (reuse) - understanding encapsulated code

#### **2. Pydoc (Python docstrings)**

- **Modules/Packages**: First line of file with triple quotes
- **Classes**: First line after class declaration
- **Functions/Methods**: First line after function definition

- Use double quotes or triple single quotes
- Never mix comments with docstrings
- Don't repeat nor state the obvious in docstrings

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
```

Command line: pydoc3 -b (opens web browser)

## 📚 WEEK 2: Java Documentation with javadoc

#### **1. Three levels of Documentation**

**1. Class Level.**

This level Documents the whole class

- One class per file

**2. Field Level.**

Documents class variables

**3. Method Level.**

Documents individual levels

#### **2. Java Docstring**

**Java Docstring Syntax:**

```java

public class Main {
    /** Brief description of class */
    public static void HelloWorld(Strings [] args){
        /** Brief description of method */

        /** @return Description of return value */
        return System.out.println("Hello Java");
    }
}
```

Common javadoc Tags:

@param - Parameter description
@return - Return value description
@throws - Exception documentation
@author - Author information
@version - Version information
@since - When feature was added

#### **3. Java Coding Guidelines**

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

#### **4. Design Documents**

- Should be easily refactored as the code is
- Similar to code but should not be duplicate information
- Should include system level testing w/ input & output examples
- Documentation is important for software reuse & maintenance issues

#### **5. Identifiers**

## Classes & Interfaces

- Usually nouns
  **defines objects**
- Avoid Acronyms

## Methods & Functions

- Usually verbs
  **defines actions**

## Constants

- Usually nouns

## Packages

- Usually one per file, but if you need to pack for system purposes name your package with clear &
  concrete definition of what is packed.

#### **6. Layout**

## Indentation

- Used to indicate position within the hierachy of declaration classes, methods, functions, etc

- Each level should be indented 4 spaces more than one before

- Same indent for common levels

**Assume use of 80 column code window**

## 📚 WEEK 3: Object Oriented Programming

In java everything is an object containing an object. In such context the heirachy of classes is defined by three pillars:

**Super Class**
**SubClass**
**Inheritance**

#### **1. Polymorphism & Interfaces**

### Interface Definition

- **Interface**: Abstract type containing a collection of methods and constant variables
- Used for defining standard methods
- Enables polymorphism - same interface, different implementations

- **Subclass**: (Child class / Derived class) inherits from **Super Class**
- **Super Class**: (Parent class / Base class) Top or general class
- **Inheritance**: The inheritance of methods and fields of a class to a derived class

#### **2. Modularity & Encapsulation**

- Classes should have one responsibility
- Classes should depend on abstraction
- Instance variables should either be used by multiple methods or be referenced between multiple calls of
  a singlle method
- Each class method should manipulate one or more instance variables

#### **3. Qualifiers**

- protected: Modifier of methods that give access to only within it's own package and subclass of it's own class
- private: member can only be accessed in its own class
  **All data fields are always private**
- (no modifier / package private): Only visible within its own package
- public: Visibile to all classes

#### **4. UML Diagram**

- A semi - formal general purpose, developmental, modeling language in the field of software engineering
  intended to provide visual design of a system design.

**Aggregation**: Object that refers to another created object elsewhere, relationship from this given class to the other

A -----<//> B

**Assosciation**: Object connected to another object

A ------> B

**Composition**: Object given of class creates object of another class as instance variable

A ----<> B

**Dependency**: Change in class that may affect another class

A - - - - > B

**Inheritance**: Derived class containing method/properties from other class

A -----/> B

**Realization/Implementation**: Subclass - Super Class. Implements methods defined by another class/interface

A - - - - /> B

#### **5. Law of Demeter**

A module should not know about the innards of the object it manipulates.

#### **6. S.O.L.I.D.**

**Single Responsibility Principle**
Every class, method, and function should have only one job

**Open-Closed Principle**
A class, method, and function should be open for extension but closed for modification

**Liskov Substitution Principle**
Child class must be substitutable for its arent class. Ensures that child class can assume the place of parent class
without errors

**Interface Segregation Principle**
An interface should be as small as possible, meaning it should do only one thing

**Dependency Inversion Principle**
High level modules should not depend on low level modules, both should depend on abstractions.
Abstractions should not depend on details, details should depend on abstractions.

## 📚 WEEK 4: Object Oriented Design

### Software reuse kinds

- Opportunistic
- Planned
- Internal
- External
- Referenced
- Forked

**Forked Software reusue is discouraged**

#### **1. Golden Rules in Object Oriented Design**

- Program to interface, Not implementation
- Dont repeat yourself
- Encapsulate what varies
- Depend on Abstractionsm not concrete classes
- Least knowledge principle
- Favor Composition over Inheritance
- Hollywood Principle ("don't call us, we'll call you")
- Apply Design Pattern wherever possible
- Strive for Loosely Coupled System
- Keep it Simple and Straightforward

#### **2. What is a Design Pattern**

### Creational Patterns

Deals with instantiation

**Singleton**:

- Design pattern to provide one and only instance of an object
- Make the constructors of the class private
- Store the object created privately
- Provide access to get the instance through a public method
- Can be extended to create a pool of objects

## Use Case of Pattern Singleton Method

• Database Connections: In applications where creating and managing database connections is an expensive operation, a
Singleton can be used to maintain a single database connection throughout the application.
• Configuration Management: When you have global configuration settings that need to be accessed by various
components of the application, a Singleton configuration manager can provide a single point of access to these settings.
• GUI Components: For graphical user interface (GUI) components or controllers, a Singleton can help manage the state
and actions of the UI, providing a single point of control.
• Device Managers: In embedded systems or applications interacting with hardware devices, a Singleton can be used to
manage and control access to hardware devices to avoid conflicts.
• Printing Service: In systems that involve printing documents or reports, a Singleton printing service can coordinate and
manage print jobs, ensuring efficient use of printing resources.

## Advantages of Singleton Method Design Pattern:

• Solves Name Collisions: In scenarios where a single point of control is needed to avoid naming conflicts or collisions,
the Singleton pattern ensures that there is only one instance with a unique name.
• Eager or Lazy Initialization: The Singleton pattern supports both eager initialization (creating the instance when the
class is loaded) and lazy initialization (creating the instance when it is first requested), providing flexibility based on the
use case.
• Thread Safety: Properly implemented Singleton patterns can provide thread safety, ensuring that the instance is
created atomically and that multiple threads do not inadvertently create duplicate instances.
• Reduced Memory Footprint: In applications where resource consumption is critical, the Singleton pattern can contribute
to a reduced memory footprint by ensuring that there is only one instance of the class.

## Disadvantages of Singleton Method Design Pattern:

• Testing Difficulties: Because Singletons introduce global state, unit testing can become challenging. Testing one
component in isolation may be more complicated if it relies on a Singleton, as the state of the Singleton may affect the
outcome of tests.
• Concurrency Issues: In a multi-threaded environment, there can be issues related to the creation and initialization of
the Singleton instance. If multiple threads attempt to create the Singleton simultaneously, it can result in race
conditions.
• Limited Extensibility: The Singleton pattern can make code less extensible. If you later decide that you need multiple
instances of the class or want to change the instantiation logic, it may require significant refactoring.
• Global Dependency: The Singleton pattern creates a global dependency, making it harder to replace the Singleton
with an alternative implementation or to use dependency injection for providing instances.
• Hard to Subclass: Subclassing a Singleton can be challenging. Because the constructor is typically private, extending
a Singleton requires additional care and may not follow standard inheritance patterns.
• Lifecycle Management: The Singleton pattern may not handle scenarios where the instance needs to be explicitly
destroyed or reset. Managing the lifecycle of the Singleton can become a concern.
• Global Access Point Abuse: While a global access point is an advantage, it can also be abused. Developers might be
tempted to use the Singleton for everything, leading to an overuse of global state and a less modular design.

- Abstract Factory

- Factory

- Builder

- Prototype patterns

### Structural Patterns

Deals with class composition to add new functionality

- Adapter

- Bridge

- Composite

- Decorator

- Facade

- Flyweight

- Proxy Pattern

### Behavioral Patterns

Deals with Object communication

- Chain of Responsibility

- Command

- Interpreter

- Iterator

- Mediator

- Memento

- Observer

- State

- Visitor Pattern

## 📚 WEEK 5: SDLC - Software Development Life Cycle

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
