# CSC 6301 Week 8 Study Guide: Software Design Methodologies

## Table of Contents

1. [Design Methodologies Overview](#design-methodologies-overview)
2. [SDLC Revisited](#sdlc-revisited)
3. [Design Methodologies - Stricto Sensu](#design-methodologies---stricto-sensu)
4. [Software Development Methodologies (SDM)](#software-development-methodologies-sdm)
5. [Major SDM Approaches](#major-sdm-approaches)
6. [Additional Concepts](#additional-concepts)
7. [Key Concepts Summary](#key-concepts-summary)
8. [Practice Questions](#practice-questions)

---

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

## Practice Questions

### Design Methodologies Fundamentals

1. What is the key difference between academic design methodologies and industry design methodologies?
2. Name and explain the four main academic design approaches (stricto sensu).
3. Which three SDLC phases do design methodologies typically cover according to industry consensus?

### Software Development Methodologies

4. What are the four key goals that SDM tries to achieve? Explain each.
5. Compare and contrast Waterfall vs Lean methodologies - when would you use each?
6. How does Agile address the "stiffness" of Waterfall? What are its limitations?

### Methodology Characteristics

7. What is the main goal of DevOps methodology, and how does it achieve this?
8. Why do most real industry methodologies fall between strict and flexible approaches?
9. Give three examples of "other" SDM options beyond the four main ones discussed.

### Design Principles

10. Explain the SOLID principles and give an example of how each improves code quality.
11. What does "Private, maybe Protected, rarely Public!" mean in terms of encapsulation?
12. Distinguish between Creational, Structural, and Behavioral design patterns with examples.

### UML and Documentation

13. What is the most important UML diagram for Object-Oriented development and why?
14. Name three structural diagrams and three behavioral diagrams in UML 2.0.
15. How do linters help improve code quality? Give three examples of issues they catch.

### Integration and Application

16. How would you choose between Agile and Waterfall for a critical healthcare system?
17. Explain how DevOps and Agile can work together in the same organization.
18. What role do design patterns play in the overall software development methodology?

### Course Integration

19. How do the debugging, testing, and profiling concepts from Week 7 fit into the SDM approaches?
20. Which SDM would be most compatible with the object-oriented design principles discussed in the course?

---

## Final Exam Preparation

### Week 8 Key Focus Areas

- **Methodology Selection**: Understanding when to use different approaches
- **SDLC Integration**: How design methodologies fit into overall development
- **Design Principles**: SOLID, encapsulation, and OOP concepts
- **Real-world Application**: Hybrid approaches and practical considerations

### Important Reminders

- **Final Exam**: Available on Canvas, 4-hour window once started
- **Deadline**: Saturday 11:59 PM EST (recommended: complete by Friday)
- **Format**: Single PDF submission, 8 questions (one per week topic)
- **Guidelines**: 30 minutes per question, open book/notes, no general internet search
- **Weight**: 25% of overall course grade

### Study Strategy

- Review all four major methodologies and their trade-offs
- Understand the progression from academic to industry design approaches
- Practice identifying which methodology fits different scenarios
- Remember that most real implementations are hybrid approaches

### Essential Takeaway

**"Keep It Simple and Straightforward"** - The fundamental principle underlying all good software design and methodology selection.

---

## Quick Reference Checklist

### Final Week Tasks

- [ ] **Complete all previous week assignments**
- [ ] **Take Final Exam** (by Friday recommended, Saturday deadline)
- [ ] **Submit everything by hard deadline**: July 5th (try July 4th)
- [ ] **Complete student surveys**

### Next Steps

Consider continuing with:

- CSC 6302
- CSC 6303
- CSC 6304

### Recommended Reading

- **"Head First Design Patterns"** by Eric Freeman & Elisabeth Freeman (O'Reilly)
- Check out recommended texts and videos from course materials
