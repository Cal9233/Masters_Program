# CSC 6304 Week 8 Study Guide

## Programming Paradigms and Development Approaches

### Key Distinctions (Critical for Exam)

**Programming Paradigms**

- How we structure and organize code
- Examples: OOP, Functional, Procedural

**Development Approaches** (Don't confuse with Methodologies)

- How we create and build software (Technical construction process)
- The process and tools we use

---

## Programming Paradigms

### Definition

A fundamental style or approach to programming that shapes how code is organized and how problems are solved.

### Why Paradigms Matter

- Shape how we think about problems
- Influence the structure of our solutions
- Determine program behavior and properties
- Affect maintainability and scalability
- Understanding multiple paradigms expands your problem-solving toolkit

### Major Categories

#### Imperative Paradigm: Focus on HOW to execute

- **Procedural Programming**
- **Object-Oriented Programming**

#### Declarative Paradigm: Focus on WHAT to execute

- **Functional Programming**
- **Logic Programming**
- **Database Programming**

---

## Imperative Paradigm

### Procedural Programming

**Core Concept:** Programs as sequences of commands that change state

**Key Features:**

- Sequential execution
- Variables and assignments
- Control structures (if/else, loops)
- Procedures/functions for code organization

**Example Pattern:**

```c
void sortArray(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap elements
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```

### Object-Oriented Programming

**Core Concept:** Programs as collections of interacting objects

**Key Features:**

- Encapsulation (data + behavior)
- Inheritance (is-a relationships)
- Polymorphism (interface consistency)
- Classes as blueprints for objects

**Example Pattern:**

```java
public class SortAlgorithm {
    public void sort(int[] array) {
        // Default implementation
    }
}

public class BubbleSort extends SortAlgorithm {
    @Override
    public void sort(int[] array) {
        // Bubble sort implementation
    }
}
```

---

## Declarative Paradigm

### Functional Programming

**Core Concept:** Programs as evaluations of mathematical functions

**Key Features:**

- Pure functions (no side effects)
- Immutability (no state changes)
- First-class functions
- Higher-order functions
- Recursion over iteration

**Example Pattern (Haskell):**

```haskell
-- Quicksort implementation
quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    quicksort [y | y <- xs, y < x] ++
    [x] ++
    quicksort [y | y <- xs, y >= x]
```

### Database Programming

**Core Concept:** Programs as declarations of data relationships and queries

**Key Features:**

- Set-based operations
- Declarative constraints and relationships
- Query optimization by the system
- Abstraction of physical data storage
- Transaction management

**Example Pattern:**

```sql
-- Find customers who have placed large orders
SELECT c.customer_id, c.name, COUNT(o.order_id) as order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount > 1000
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;
```

---

## Development Approaches

### 1. Development with Built-in Commands

**Definition:** Building software using primarily language primitives and standard libraries

#### Advantages

- Complete control over implementation
- No external dependencies to manage
- Deep understanding of the code
- Potential for custom optimization
- Useful for educational purposes
- Essential for specialized algorithms

#### Disadvantages

- Significantly longer development time
- Greater potential for bugs
- "Reinventing the wheel"
- Higher maintenance burden
- May miss optimizations present in established libraries
- Steeper learning curve for new team members

#### When to Use

- Educational contexts
- Performance-critical components
- Specialized algorithms
- Security-sensitive applications
- Limited computing environments
- When learning a new language

### 2. Assembly Development (Code Reuse)

**Definition:** Building software by integrating existing libraries, frameworks, and components

#### Advantages

- Drastically reduced development time
- Leveraging tested, optimized code
- Industry standard approach
- Community support and documentation
- Regular updates and improvements
- Focus on business logic rather than infrastructure

#### Disadvantages

- Dependency management complexity
- "Black box" components
- Version compatibility issues
- Learning curve for library APIs
- Risk of over-engineering with too many dependencies
- Limited control over implementation details

#### When to Use

- Most professional software projects
- Standard business applications
- Projects with tight deadlines
- Well-understood problem domains
- When specialized libraries exist for your needs
- When performance is adequate with existing solutions

#### Real-World Warning: Ariane 5 Failure (1996)

- Reused software from Ariane 4 without adequate testing
- A single variable overflow crashed the guidance system
- $370 million lost in 37 seconds
- **Lesson:** Always understand the limitations of reused code and test thoroughly in new contexts

### 3. Assisted Development

**Definition:** Using tools to automatically generate or suggest code based on specifications

#### Evolution

**Traditional Tools:**

- Code snippets and templates
- Basic autocomplete
- Visual designers (GUI builders)

**Modern AI Tools:**

- GitHub Copilot
- ChatGPT / Claude
- Amazon CodeWhisperer
- Cursor

#### Advantages

- Dramatic productivity increases
- Reduces boilerplate and repetitive code
- Helps explore unfamiliar APIs or languages
- Suggests patterns and best practices
- Lowers barriers to entry for programming
- Accelerates prototyping and experimentation

#### Challenges

- Risk of introducing subtle bugs or security issues
- "Hallucinated" features that don't actually work
- Dependency on tool availability
- May generate inefficient or outdated patterns
- Over-reliance can hinder learning fundamentals
- Intellectual property and licensing concerns

#### When to Use

- Generating boilerplate code
- Implementing well-known algorithms
- Exploring unfamiliar APIs or languages
- Rapid prototyping
- Routine CRUD operations
- Standard data transformations
- Documentation generation

#### Best Practices for AI-Assisted Development

- Review all generated code thoroughly
- Test everything, especially edge cases
- Understand the code before using it
- Be specific in your prompts
- Use AI as a collaborative tool, not a replacement
- Stay updated on the tool's limitations

---

## Comparison Matrix

| Factor        | Built-in Commands         | Assembly (Reuse)     | Assisted (AI)            |
| ------------- | ------------------------- | -------------------- | ------------------------ |
| Speed         | Slow                      | Fast                 | Very Fast                |
| Control       | High                      | Medium               | Low-Medium               |
| Understanding | Deep                      | Moderate             | Varies                   |
| Maintenance   | High Effort               | Medium               | Requires Verification    |
| Best For      | Core algorithms, Learning | Most production code | Boilerplate, Prototyping |

---

## Modern Development Reality

Most real-world projects use **all three approaches**:

- **Core business logic:** Custom implementation (Built-in)
- **Infrastructure:** Libraries and frameworks (Assembly)
- **Boilerplate:** AI-assisted generation (Assisted)
- **Integration code:** Combination of approaches

**Key Insight:** The art of software engineering is knowing which approach to use for each component.

---

## Final Exam Information

**Critical Details:**

- Grade weight: 25% of overall course grade
- Available: Tuesday 8:00 PM EST
- Time limit: 4 hours from start
- Hard deadline: Saturday 11:59 PM EST
- Format: Essays on Canvas + GitLab repo
- Questions: 8 total, one per course topic
- Time allocation: ~30 minutes per question
- Open book, open notes
- **No general internet search allowed**

**Preparation Strategy:**

1. Complete Week 7 tasks first
2. Review all 8 course topics
3. Practice explaining concepts in essay format
4. Prepare code examples for GitLab submission

---

## Study Tips for Success

1. **Understand the distinctions** between paradigms and approaches
2. **Memorize key advantages/disadvantages** of each approach
3. **Practice code examples** in different paradigms
4. **Know when to use** each development approach
5. **Understand real-world applications** and the combined approach
6. **Review the Ariane 5 case study** as an example of code reuse risks
7. **Be ready to discuss AI-assisted development** pros and cons

Remember: Focus on conceptual understanding rather than memorization. The exam will likely test your ability to analyze scenarios and recommend appropriate paradigms/approaches.
