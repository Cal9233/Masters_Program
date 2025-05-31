# Java Object-Oriented Programming and UML Notes

## Java's Object-Oriented Approach

Java is the fundamentalist approach of Object-Oriented programming. Everything is an object, your program is an object that have objects, composed by data and functions that are objects themselves, that may be composed of objects themselves and so on, until you have data stored in native data types (Integers, Doubles, Characters, Booleans, etc) and native commands (if, for, assignments, etc).

In such context, the hierarchy of classes is very important to draw a panorama of a Java program. The basic class hierarchy is defined by one of the three pillars of Object-Oriented programming: **Inheritance**.

### Key Terminology

- A class A that inherits from a class B is called **subclass** of B
- B is called **superclass** of A

## Inheritance Across Languages

In all programming languages with object-oriented concepts, there is the possibility to define subclasses:

- **Python**: A subclass can be defined indicating its superclass using parenthesis `()`
- **Java**: A subclass is defined indicating its superclass with the reserved word `extends`

### Building Subclasses

Building subclasses is often a matter of choosing the right amount of inheritance:

- Instance Variables
- Constructors
- Get and set methods
- Other methods

**Think about what is common to your class and the superclass:**

- That is your goal!

**Think about what is specific to your class:**

- That is your limit!

> 📹 **Video**: Java Inheritance and Constructors

⚠️ **Important**: Do not reuse code ignoring the class meaning

## Interfaces

An interface is an abstract type that contains a collection of methods and constant variables:

- Used for defining standard methods
- An algorithm can be implemented to all classes implementing the interface

> 📹 **Video**: Java Polymorphism

## UML - Unified Modeling Language

UML is a semi-formal general-purpose, developmental, modeling language in the field of software engineering that is intended to provide a standard way to visualize the design of a system.

### Key UML Characteristics

UML is:

- **Semi-formal**:

  - There are no way to automatically pass from an UML definition to a code, or other way around
  - One might decide how precise the UML definition needs to be

- **Developmental**:

  - It can be changed in each instance of application, during the application, or even by industry standards

- **General-purpose**:
  - It can be used in any context, environment, language, or platform
  - It can be used in any phase including, but not limited to design, development, and maintenance

> 🔗 **Reference**: [Wikipedia page on Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

### UML Diagram Types

#### Structural Diagrams

- Class diagram
- Component diagram
- Composite structure diagram
- Deployment diagram
- Object diagram
- Package diagram
- Profile diagram

**For systems based on Object-Oriented languages, the Class diagram is often the most important design document, the one that guides all development.**

> 🔗 **Reference**: [Wikipedia page on UML's Class Diagram](https://en.wikipedia.org/wiki/Class_diagram)

#### Behavioral Diagrams

- Activity diagram
- Communication diagram
- Interaction overview diagram
- Sequence diagram
- State diagram
- Timing diagram
- Use case diagram

## Class Diagrams

A class diagram is a graph where:

- **Nodes** are classes
- **Directed arcs** are relations between classes

### Types of Relations

#### Instance-level Relations

- **Association**: Instances of a class are connected to instances of another class
  - Association: a static relationship
  - Aggregation: a relation "catalog"
  - Composition: a relation whole-part
- **Dependencies**: A change in a class may affect another class

#### Class-level Relations

- **Generalizations**: subclass-superclass
- **Realizations**: a class implements the methods defined by another class/interface

> 🔗 **Reference**: [IBM - Relationships in class diagrams](https://www.ibm.com/docs/en/rational-soft-arch/9.7.0?topic=diagrams-relationships-in-class)

### Class Diagram - Generalization

The inheritance relations are indicated by arrows from subclass to superclass. Each class is composed by its identifier and instance variables. Methods can be represented too.

> 📹 **Video**: UML Class Diagram Tutorial

#### Example Class Hierarchy

```
Person
├── birth : int = 0
├── age : int = 0
├── Woman
│   └── sex : char = "F"
└── Man
    └── sex : char = "M"
```

# Java Documentation Best Practices and SOLID Principles

## Overview

Some documentation best practices are specific to the class definitions. Given the importance of classes in Java, those best practices are very important to the development of Java projects.

**Key Focus Areas:**

- Modularity and Encapsulation
- Objects and Data Structures

---

## Guidelines - Modularity and Encapsulation

### Class Design Principles

**Classes should:**

- Generally have one single responsibility
- Depend upon abstractions, not on concrete details
- Have instance variables that are either:
  - Used by multiple methods, OR
  - Referenced between multiple calls of a single method
- Have methods that manipulate one or more instance variables

> 📚 **Reference**: Clean Code by Robert C. Martin. Pearson, 2008.

### Design Goal

> 💡 **Key Principle**: Usually, the less arcs in the Class Diagram, the better. **Modularity is the word!**

### Access Modifiers - The Golden Rule

**"Private, maybe Protected, rarely Public!"**

#### Data Fields

- **All data fields are almost always private**
- **Only exception**: Constants defined within the class that are needed by code outside of the class

#### Classes and Methods

- **Public**: Should be made only when there is an intent to use it outside of its associated class
- **Private**: Must be used only within the public class in which it is associated

> 🔗 **Reference**: [Controlling Access to Members of a Class](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)

### Access Modifier Summary

| Modifier    | Scope           |
| ----------- | --------------- |
| `private`   | Only the class  |
| `default`   | Class & package |
| `protected` | Subclass too    |
| `public`    | No restriction  |

---

## The Law of Demeter

> 🎯 **Principle**: A module should not know about the innards of the objects it manipulates.

### Implementation Rule

A method `f` of class `C` should only call the methods of:

- Class `C`
- An object created by method `f`
- An object passed as an argument to method `f`
- An object held in an instance variable of class `C`

---

## Guidelines - Objects and Data Structures

### Best Practices

#### Data Abstraction

- **Don't express the details of your data. Express them in abstract terms**
- **Data Structures**: Expose their data and have no meaningful functions

#### Method Design

- **Avoid using getters/setters as much as possible**
- **Keep variables private for flexibility of change**

### Benefits

> ✅ **Result**: Encapsulation and Modularity promote reliability and facilitate optimization during maintenance.

---

## SOLID Principles in OOP

### S - Single Responsibility Principle

A class should have only one reason to change.

### O - Open–Closed Principle

Software entities should be open for extension, but closed for modification.

### L - Liskov Substitution Principle

> **Definition**: The Liskov substitution principle states that a child class must be substitutable for its parent class. Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.

### I - Interface Segregation Principle

> **Definition**: The interface segregation principle states that an interface should be as small as possible in terms of cohesion. In other words, it should do **ONE thing**.

### D - Dependency Inversion Principle

> **Definition**:
>
> - High-level modules should not depend on low-level modules. Both should depend on abstractions.
> - Abstractions should not depend on details. Details should depend on abstractions.

---
