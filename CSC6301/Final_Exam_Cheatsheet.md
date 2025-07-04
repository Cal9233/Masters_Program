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

## 📚 WEEK 6: Version Control and Issue Tracking

## 1. Version Control Fundamentals

### What is Version Control?

Version control is the management of changes to documents, computer programs, and other collections of information. It's essential because:

- Every software development project will have multiple versions
- Even "one-time" code projects need version management
- It tracks all changes made to code over time

**➤ SIMPLIFIED:** Think of version control like saving your video game progress - it's like having multiple save files for your code so you can go back to older versions if something breaks. Every software project needs this, even simple ones.

---

### Software Version Numbering (M.N.b Format)

- **M** = Major release (significant changes, new features)
- **N** = Minor release (small improvements, bug fixes)
- **b** = Build/Patch (very small fixes, patches)

**Example**: Version 2.1.3

- Major version: 2
- Minor version: 1
- Build/Patch: 3

**➤ SIMPLIFIED:** Version numbers are like software updates on your phone (like iOS 16.2.1). **Major** = Big changes (iPhone getting a completely new look), **Minor** = Small improvements (new emoji or small features), **Build** = Tiny fixes (fixing a small bug).

---

### Version Control System Structure

- Uses a **Directed Acyclic Graph (DAG)** structure
- **Trunk/Main**: The main development line
- **Branches**: Separate development paths for features or experiments
- **Merges**: Combining branches back into the main line
- **Tags**: Markers for specific versions or releases

**➤ SIMPLIFIED:** **Main Line** = Your main project (like the trunk of a tree), **Branches** = Side projects or experiments (like tree branches), **Merging** = Combining your experiments back into the main project.

---

## 2. Environments and Compatibility

### Development Environment

The complete set of tools, libraries, and their specific versions used to build software.

### Why Version Compatibility Matters

When reusing software packages, you might choose older versions for:

- **Familiarity**: You've used it before or documentation is better
- **Compatibility**: Different versions have different functions, parameters, or complexity

### Managing Dependencies

- **Requirements File**: Lists all packages and their exact versions
- **Environment Encapsulation**: Some systems bundle all necessary package versions together
- **Python Example**: `pip install -r requirements.txt` installs specific versions listed in requirements.txt

**➤ SIMPLIFIED:** Like LEGO building instructions - different versions of software tools work differently, like needing specific LEGO pieces for a specific set. You need to write down exactly which pieces (versions) you used. Environment files are like a shopping list of all the software tools and their versions, helping others build the same thing you built - like sharing a recipe with exact ingredient brands and amounts.

---

## 3. Version Documentation

### Full Version Documentation Requirements

When releasing a complete version, document:

- Changes from the previous version
- Requirements changes (new dependencies)
- New and deprecated features (classes, functions, etc.)
- Bugs that were fixed

### Code Revision Documentation

For every patch or working revision, include:

- Target audience (public, developers, testers, beta testers)
- Implementation issues addressed
- All items from full version documentation

**➤ SIMPLIFIED:** Documentation is like writing detailed notes about what you changed in your project - like keeping a diary of all the improvements and fixes you made so others (and future you) can understand what happened.

---

## 4. Issue Tracking Systems

### Evolution from Bug Tracker to Issue Tracker

- **Originally**: Bug trackers only handled software defects
- **Now**: Issue trackers handle any project concerns, not just bugs
- **Purpose**: Keep track of problems that don't have simple solutions and need periodic attention

**➤ SIMPLIFIED:** Issue tracking is like a to-do list for problems. It's not just bugs - could be new features or questions, like having a notebook to track all homework assignments.

---

### Collaborative Project Types

#### Proprietary Projects

- Split into multiple teams
- **Global Software Engineering**: Coordinated/specialized teams across locations
- **Follow the Sun**: Teams in different time zones work continuously
- **Real-time collaboration**: Teams work together simultaneously

#### Open Source Projects

- **Board managed**: Organized leadership (like Linux Operating System)
- **Crowdsourcing**: Community-driven contributions (like Kaggle for machine learning)

**➤ SIMPLIFIED:** **Company Projects** = Teams work together like a relay race, some teams work while others sleep (around the world), everyone coordinates to build one big thing. **Open Source Projects** = Like community gardening - everyone can help. Some have leaders (like Linux), others are completely volunteer-driven (like Wikipedia).

---

### Issue Tracking Approaches

#### Repository-Based (GitHub Style)

- Issues stored alongside code
- Blog-like entries for discussions
- Effective for open source projects
- Ad hoc procedure (informal)

#### Specialized Tools

- Centralized systems for controlled tracking
- Used across coding, testing, and maintenance phases
- Systematic registry of issues and outcomes
- Examples: Google Issue Tracker, Jira, etc.

### Issue Resolution Strategies

When dealing with issues, teams can:

- Fix the bug
- Find a way to avoid the issue
- Document the issue for future reference
- Collect data about the issue for analysis

**➤ SIMPLIFIED:** How to handle issues: **Fix it** = Actually solve the problem, **Avoid it** = Find a workaround, **Document it** = Write it down for later, **Study it** = Collect information to understand it better.

---

## 5. GitHub Repository

### Key Statistics

- 83 million developers worldwide
- 200 million repositories (28 million public)
- Acquired by Microsoft in 2018
- Free for basic use (registration required to store, not to download)

### GitHub Features

- Version control using Git
- Issue tracking integration
- Documentation hosting
- Collaborative development tools
- Repository management

**➤ SIMPLIFIED:** GitHub is like Google Drive for programmers. It's a website where programmers store and share code. 83 million people use it (bigger than most countries!), it's free to use for basic features, Microsoft owns it but it's still free. It stores your code safely in the cloud, lets multiple people work on the same project, tracks all changes automatically, and helps teams discuss problems and solutions.

---

## 6. Code Testing and Quality Assurance

### Unit Testing Principles

Testing individual components of code to ensure they work correctly.

#### Key Testing Methods

- **Assertion Testing**: Verify expected outcomes
- **Edge Case Testing**: Test boundary conditions (like division by zero)
- **Multiple Test Cases**: Cover various scenarios for each function

#### Good Test Coverage Includes

- Basic functionality testing
- Edge cases and error conditions
- Integration between components

**➤ SIMPLIFIED:** Unit testing is like proofreading an essay - testing small pieces of code one at a time, like checking each math problem separately on homework. Make sure each piece works before putting them together. Good testing includes: **Normal cases** = Testing with typical inputs, **Edge cases** = Testing with unusual inputs (like dividing by zero), **Error cases** = Testing what happens when things go wrong.

---

### Static Code Analysis

#### Purpose

Examine source code for:

- Potential errors
- Code smells (poor programming practices)
- Adherence to coding standards
- All without executing the program

#### Popular Static Analysis Tools

- **Checkstyle**: Focuses on coding standards and style
- **PMD**: Detects code smells, potential bugs, and style issues
- **FindBugs/SpotBugs**: Identifies potential bugs in programs
- **SonarQube**: Comprehensive platform integrating multiple analysis tools

#### Static Analysis Process

1. Choose appropriate tools
2. Install and configure tools
3. Set up configuration files defining rules
4. Run analysis using build tools or command line
5. Review generated reports
6. Fix identified issues
7. Integrate into CI/CD pipeline for continuous monitoring

**➤ SIMPLIFIED:** Static analysis is like spell-check for code. Computer programs read your code and find problems without running your program - just look at the text. They find issues like potential bugs, bad coding style, and code that's hard to understand.

---

## 7. Observer Design Pattern

### What is the Observer Pattern?

A behavioral design pattern where:

- An object (Subject) maintains a list of dependents (Observers)
- When the Subject's state changes, all Observers are automatically notified
- Useful for event management and keeping objects synchronized

**➤ SIMPLIFIED:** The Observer Pattern is like a newsletter subscription - one object (the newsletter) tells many objects (subscribers) when something changes, like YouTube notifying all subscribers when you upload a new video. The subscribers don't need to constantly check - they get told automatically.

---

### Pattern Components

#### Observer Interface

Defines the `update()` method that all observers must implement

#### Subject Class

- Maintains list of observers
- Provides methods to add/remove observers
- Notifies all observers when state changes

#### Concrete Observer Classes

- Implement the Observer interface
- Define specific responses to updates

**➤ SIMPLIFIED:** Think of it like a group text message system - the phone (Subject) keeps a list of people in the group (Observers), and when someone sends a message, everyone gets notified automatically.

---

### Real-World Applications

#### 1. User Interface (UI) Event Handling

- Button clicks, text input, mouse events
- Multiple components respond to user actions

**➤ SIMPLIFIED:** Like when you click a button on a website and multiple things happen - the button changes color, a popup appears, and data gets saved.

#### 2. Model-View-Controller (MVC) Architecture

- Views automatically update when model data changes
- Keeps user interface synchronized with underlying data

**➤ SIMPLIFIED:** Like when you edit a Google Doc and everyone else sees the changes immediately on their screen.

#### 3. Notification Systems

- Email, SMS, push notifications
- Social media followers get notified of new posts

**➤ SIMPLIFIED:** When someone posts on Instagram, all their followers get notified - the poster doesn't manually tell each follower.

#### 4. Real-time Data Streaming

- Stock price updates
- Weather data
- Live sports scores

**➤ SIMPLIFIED:** Like a sports app that updates the score for everyone watching at the same time during a live game.

#### 5. Distributed Event-Driven Systems

- Microservices architecture
- Event bus systems (Apache Kafka, Google Cloud Pub/Sub)

**➤ SIMPLIFIED:** Like when you order something online - automatically the payment system, inventory system, and shipping system all get notified at once.

#### 6. Document-View Architecture

- Microsoft Office applications
- Google Docs collaboration
- Multiple views of same document stay synchronized

**➤ SIMPLIFIED:** When multiple people edit the same Google Doc, everyone sees the changes in real-time automatically.

#### 7. Game Development

- Multiplayer games
- Real-time state updates across all players

**➤ SIMPLIFIED:** In online games, when your character's health changes, the health bar updates; when you gain points, the scoreboard updates - multiple parts of the screen change from one action.

#### 8. Logging Frameworks

- Multiple log handlers receive the same log messages
- File loggers, console loggers, monitoring systems

**➤ SIMPLIFIED:** Like keeping multiple diaries of the same events - one for yourself, one for your teacher, one for your parents - all automatically updated at the same time.

#### 9. Database Triggers

- Database changes trigger actions in other systems
- Cache updates, business logic execution

**➤ SIMPLIFIED:** Like when you update your address in one system and it automatically updates everywhere else that needs to know.

#### 10. Messaging Applications

- Real-time message delivery
- Status updates (message read receipts)

**➤ SIMPLIFIED:** Group chat apps where when one person sends a message, everyone in the group gets it automatically.

### Observer Pattern Benefits

- **Loose Coupling**: Subject and observers are independent
- **Dynamic Relationships**: Observers can be added/removed at runtime
- **Broadcast Communication**: One change notifies multiple objects
- **Separation of Concerns**: Each observer handles its specific responsibilities

**➤ SIMPLIFIED:** Why this pattern is useful: **Less Work** = Don't have to manually notify everyone, **Flexible** = Easy to add or remove subscribers, **Organized** = Everyone gets the same information at the same time, **Independent** = The newsletter and subscribers don't need to know details about each other.

---

## Key Points to Remember for Your Exam

### Technical Concepts:

1. **Version Control** is essential for all software projects and uses structured numbering systems
2. **Environment Management** ensures compatibility by tracking specific package versions
3. **Issue Tracking** evolved from simple bug tracking to comprehensive project management
4. **GitHub** is a major platform combining version control with collaborative features
5. **Testing and Static Analysis** are crucial for code quality and early error detection
6. **Observer Pattern** is fundamental for event-driven programming and maintaining object synchronization
7. **Documentation** at both version and revision levels is critical for project maintenance

### **➤ SIMPLIFIED KEY POINTS:**

1. **Version Control** = Saving different versions of your work safely
2. **Issue Tracking** = Keeping organized lists of problems and tasks
3. **GitHub** = Popular website for storing and sharing code
4. **Testing** = Checking your code works correctly before sharing it
5. **Static Analysis** = Computer programs that check your code for problems
6. **Observer Pattern** = One object automatically telling many others when something changes

**Think of these concepts like tools in a toolbox - each one helps solve specific problems in software development!**

## 📚 WEEK 7: Software Debugging, Testing, and Profiling

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

### Key Terminology

- **Bug/Fault**: Error that can cause wrong results
- **Effectiveness**: Produces correct output
- **Efficiency**: Runs as fast as possible
- **Preconditions**: Initial states for testing
- **Invariant**: Condition that should always hold true
- **Profiling**: Assessment of code efficiency
- **State Transition**: Change from one state to another in State pattern

## 📚 WEEK 8: Software Design Methodologies

## Design Methodologies Overview

### Core Understanding

**Software development methodologies are how the industry develops software.**

### Key Distinction

- **Design phase**: When the software product is defined
- **Design methodology** (industry context): Usually encompasses several phases leading to software production
- **In this context**: Software design methodologies relate to software development

### Fundamental Concept

**Design Methodologies relate to going from no software to a running software.**

---

## SDLC Revisited

### Important Note

**There is no common understanding of the phases in the Software Development Life Cycle.**

### SDLC Phases

1. **Planning**
2. **Requirements Definition**
3. **Design and Prototyping**
4. **Coding**
5. **Testing**
6. **Deployment**
7. **Operations and Maintenance**

### Design Methodologies Consensus

However, there is consensus that Design methodologies cover the activities in:

- **Design and Prototyping**
- **Coding**
- **Testing**

These three phases are highlighted as the core focus of design methodologies.

---

## Design Methodologies - Stricto Sensu

### Academic Perspective

From a specific (academic) point of view, design methodologies concern the initial steps of software production.

### Four Main Design Approaches

#### 1. **Level-Oriented Design**

- **Approach**: Stepwise refinement, a top-down process
- **Focus**: Breaking down complex problems into smaller, manageable parts

#### 2. **Data-Flow-Oriented Design**

- **Approach**: Structured design, it derives the program structure
- **Focus**: Following data flow through the system

#### 3. **Data Structure-Oriented Design**

- **Approach**: Emphasis on the input and output data, the data transformation
- **Focus**: How data is structured and transformed

#### 4. **Object-Oriented Design**

- **Key Principles**:
  - **Abstraction**: Hiding complex implementation details
  - **Information hiding**: Encapsulating data and methods
  - **Modularity**: Breaking system into discrete, interchangeable components

---

## Software Development Methodologies (SDM)

### Definition

Sometimes referred to as design methodologies, software development methodologies concern how to develop software in the best possible way.

### Four Key Goals

#### 1. **As Fast as Possible**

- The short time to produce software is often a value in itself in the industry

#### 2. **As Reliable as Possible**

- A software absent of faults is sometimes required, but often better than a faulty one

#### 3. **As Reusable as Possible**

- Time and reliability can sometimes be achieved in scale, not in a single instance of software production

#### 4. **As Accountable as Possible**

- Some projects might need records of the development process

### SDM Basics

- **An agreement between people working together to produce software**
- **Dogmatic or Pragmatic approaches** available
- **A compromise between**:
  - **Strict discipline** (stiffness according to detractors)
  - **Flexibility to circumstances** (reckless according to detractors)

### Important Reality

**Most real industry methodologies fall between these extremes, even if they say they are Waterfall or Lean.**

---

## Major SDM Approaches

### 1. Waterfall Methodology

#### Philosophy

_"I wish the world was so simple that we could just go ahead and never look back."_

#### Characteristics

- **Process management methodology** more than product development methodology
- **Very effective with very well planned projects**
- Projects simple enough tend to be more easily well planned
- **Forces a structured organization**
- Everyone involved can easily follow the process
- Some Waterfall initiatives allow ad hoc adaptations

#### Best For

- Simple, well-defined projects
- Situations requiring clear structure and documentation
- Teams that need explicit guidance

---

### 2. Lean Methodology

#### Philosophy

_"I wish the world was so simple that we could just go ahead, or any other direction."_

#### Characteristics

- **Employed as process management methodology** in many areas
- **Very effective with very experienced teams**
- Projects simple enough tend to be more easily handled by experienced teams
- **Encourages people involved to be responsible**
- Everyone involved needs to be committed to the process
- Some Lean initiatives include enforcement of additional supporting rules

#### Best For

- Experienced, self-motivated teams
- Situations requiring flexibility and adaptation
- Organizations with strong commitment culture

---

### 3. Agile Methodology

#### Philosophy

_"It is better to be fast and good, than slow and bad... duh!"_

#### Characteristics

- **Attempt to break the stiffness of Waterfall**
- **Key Difference**: While Waterfall treats project as a whole, Agile breaks tasks into smaller tasks
- **Challenge**: The choice of granularity of tasks is often an issue
- **Practical results are impressive**
- **Limitation**: Rarely considered for reliable software where risk appetite is very small

#### Best For

- Projects requiring rapid iteration
- Situations where requirements may change
- Teams comfortable with frequent communication

---

### 4. DevOps Methodology

#### Philosophy

_"The more the merrier... duh!"_

#### Characteristics

- **Attempt to break barriers between Development and Operations teams**
  - **Development team**: Handles coding & testing
  - **Operations team**: Handles deployment & maintenance
- **Assumes several revision and update tasks**
- **Challenge**: The choice of granularity of tasks is often an issue
- **Compatibility**: DevOps and Agile are compatible

#### Best For

- Organizations wanting seamless development-to-production pipeline
- Projects requiring frequent deployments
- Teams seeking better collaboration between dev and ops

---

### SDM - Other Options

The industry employs several methodologies, with more appearing frequently:

- **Scrum Software Development**
- **Rapid Application Development**
- **Feature Driven Development**
- **Rational Unified Process**
- **Challenge-based Development**

### Important Notes

- **Choice is rarely discussed with developers**, but it pays to know where you're going
- **Different companies, even different teams**, may have different views of the same methodology

---

## Additional Concepts

### Design Patterns Categories

#### **Creational Patterns** - Deal with instantiation

- Singleton
- Abstract Factory
- Factory
- Builder
- Prototype patterns

#### **Structural Patterns** - Deal with class composition to add functionality

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy patterns

#### **Behavioral Patterns** - Deal with object communication

- Chain of responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Visitor patterns

### SOLID Principles in OOP

#### **S** - Single Responsibility Principle

- Each class should have one reason to change

#### **O** - Open-Closed Principle

- Open for extension, closed for modification

#### **L** - Liskov Substitution Principle

- Child class must be substitutable for its parent class
- Ensures child class can assume parent's place without errors

#### **I** - Interface Segregation Principle

- Interface should be as small as possible in terms of cohesion
- Should do ONE thing

#### **D** - Dependency Inversion Principle

- High-level modules should not depend on low-level modules
- Both should depend on abstractions
- Abstractions should not depend on details

### Guidelines - Modularity and Encapsulation

#### Access Control Philosophy

**"Private, maybe Protected, rarely Public!"**

#### Access Levels

- **Private**: Only the class
- **Default**: Class & package
- **Protected**: Subclass too
- **Public**: No restriction

#### Best Practices

- **All data fields are almost always private**
  - Exception: Constants needed by code outside the class
- **Public classes and methods**: Only when intended for use outside associated class
- **Private classes and methods**: Used only within the public class where associated

### UML 2.0 - Unified Modeling Language

#### Structural Diagrams

- Class diagram (most important for OO development)
- Component diagram
- Composite structure diagram
- Deployment diagram
- Object diagram
- Package diagram
- Profile diagram

#### Behavioral Diagrams

- Activity diagram
- Communication diagram
- Interaction overview diagram
- Sequence diagram
- State diagram
- Timing diagram
- Use case diagram

---

## Key Concepts Summary

### Remember the Main Distinction

- **Academic design methodologies**: Focus on initial design approaches (level-oriented, data-flow, etc.)
- **Industry design methodologies**: Encompass broader development process (Waterfall, Lean, Agile, DevOps)

### Critical SDM Insights

- **No one-size-fits-all**: Different methodologies suit different projects and teams
- **Hybrid approaches**: Most real implementations combine elements from multiple methodologies
- **Context matters**: Team experience, project complexity, and risk tolerance drive methodology choice

### Methodology Spectrum

- **Waterfall**: Structure and predictability (but less flexibility)
- **Lean**: Experience and responsibility (but requires commitment)
- **Agile**: Speed and adaptability (but potentially less reliable for critical systems)
- **DevOps**: Collaboration and continuous delivery (but requires cultural change)

### Design Quality Factors

- **Requirements-driven**: Everything should be based on requirements
- **Good design foundation**: Draw your design, use patterns
- **Object-oriented**: Follow SOLID principles
- **Iterative approach**: Break into small achievable chunks
- **Continuous feedback**: Demo progress to wide audience
- **Quality assurance**: Unit tests with 100% coverage, automated testing, CI/CD

---

## Final Exam Preparation

### Week 8 Key Focus Areas

- **Methodology Selection**: Understanding when to use different approaches
- **SDLC Integration**: How design methodologies fit into overall development
- **Design Principles**: SOLID, encapsulation, and OOP concepts
- **Real-world Application**: Hybrid approaches and practical considerations

### Study Strategy

- Review all four major methodologies and their trade-offs
- Understand the progression from academic to industry design approaches
- Practice identifying which methodology fits different scenarios
- Remember that most real implementations are hybrid approaches

### Essential Takeaway

**"Keep It Simple and Straightforward"** - The fundamental principle underlying all good software design and methodology selection.

---
