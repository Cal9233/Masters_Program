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

## Polymorphism & Interfaces

### Interface Definition

- **Interface**: Abstract type containing a collection of methods and constant variables
- Used for defining standard methods
- Enables polymorphism - same interface, different implementations

#### **4. UML Diagram**

- Should be easily refactored as the code is
- Similar to code but should not be duplicate information
- Should include system level testing w/ input & output examples

#### **5. Design Documents**

-
