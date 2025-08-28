# Database Security and Architecture Quiz Study Guide

## Question 1: Authentication vs Authorization
**Statement:** Authentication is determining whether an entity has permission to do something.

**Answer:** False

**Correct Definitions:**
- **Authentication:** Verifying the identity of a user (who you are)
- **Authorization:** Determining what permissions a user has (what you can do)

*Remember: Authentication = Identity, Authorization = Permissions*

---

## Question 2: First Normal Form (1NF)
**Which of the following is permitted in First Normal Form?**

**Answer:** Tables with a primary key

**1NF Requirements:**
- ✅ Each column contains atomic (indivisible) values
- ✅ No repeating groups or arrays
- ✅ Each column contains values of a single data type
- ✅ Each column has a unique name
- ✅ Order of rows/columns doesn't matter

**Not Allowed in 1NF:**
- ❌ Mixing data types within the same column
- ❌ Using row order to convey information
- ❌ Repeating data groups

---

## Question 3: SQL Delimiters
**Statement:** Everything between two delimiters is logically a single statement.

**Answer:** True

*Delimiters (like semicolons or custom delimiters) mark the boundaries of SQL statements, treating everything between them as one logical unit.*

---

## Question 4: SQL Return Types
**In SQL, which of the following always returns a single value?**

**Answer:** Function

**SQL Components:**
- **Function:** Always returns a single value (scalar or aggregate)
- **Procedure:** Can return multiple values, result sets, or nothing
- **Statement:** Can return various types of results
- **Prepared Statement:** A pre-compiled statement template

---

## Question 5: Data Access Layer
**Statement:** The layer that interfaces between business logic layer and the underlying database is the data access layer.

**Answer:** True

*The Data Access Layer (DAL) acts as an intermediary between the business logic and the database, handling all database operations and queries.*

---

## Question 6: Application Layer Architecture
**Inside the application layer, the layer responsible for communicating with the user is:**

**Answer:** View/Presentation Layer

**Three-Tier Architecture:**
- **Presentation/View Layer:** User interface and interaction
- **Business Logic Layer:** Application rules and processing
- **Data Access Layer:** Database communication

---

## Question 7: Business Logic Layer
**The layer that provides abstractions of entities and enforces rules for carrying out actions is:**

**Answer:** Business Logic Layer

*The Business Logic Layer contains the core functionality, business rules, calculations, and data processing logic of the application.*

---

## Question 8: Database Result Sets ⚠️
**Statement:** In an application, the results set returned from the database should be returned to the business logic layer.

**Answer:** False *(You answered True - incorrect)*

**Correct Data Flow:**
Database → Data Access Layer → Business Logic Layer → Presentation Layer

*The result set should first go to the Data Access Layer, which then processes and passes appropriate data to the Business Logic Layer.*

---

## Question 9: SQL Permissions
**Which valid SQL keyword do you grant so a user can query the database?**

**Answer:** SELECT

**SQL Permission Keywords:**
- **SELECT:** Read/query data
- **INSERT:** Add new data
- **UPDATE:** Modify existing data
- **DELETE:** Remove data

*Usage: `GRANT SELECT ON table_name TO user_name;`*

---

## Question 10: Outer Join Types ⚠️
**The three forms of an outer join are:** *(You got 3.33/10 points)*

**Correct Answers:**
- ✅ **Left Outer Join** *(You got this)*
- ✅ **Right Outer Join** *(You got this)*
- ✅ **Full Outer Join** *(You missed this)*

**Your Incorrect Answers:**
- ❌ **Inner Outer Join** *(Not a valid join type)*

**Join Types Summary:**
- **Inner Join:** Only matching records
- **Left Outer Join:** All from left table + matches from right
- **Right Outer Join:** All from right table + matches from left  
- **Full Outer Join:** All records from both tables

---

## Areas for Improvement ⚠️

### Question 8 - Data Flow Architecture
You need to understand that result sets flow through layers in order:
1. Database returns results to Data Access Layer
2. Data Access Layer processes and sends to Business Logic Layer
3. Business Logic Layer sends processed data to Presentation Layer

### Question 10 - Join Types
Remember the three outer joins:
- **Left** (keep all left table records)
- **Right** (keep all right table records)  
- **Full** (keep all records from both tables)

*"Inner Outer Join" is not a valid SQL join type.*

---

## Key Concepts Summary

### Security Concepts
- **Authentication:** Who you are (identity verification)
- **Authorization:** What you can do (permission checking)

### Database Normalization
- **1NF:** Atomic values, no repeating groups, primary key required

### Application Architecture
- **Presentation Layer:** User interface
- **Business Logic Layer:** Rules and processing
- **Data Access Layer:** Database interface

### SQL Fundamentals
- **Functions:** Always return single values
- **SELECT permission:** Required for querying
- **Outer Joins:** Left, Right, Full (three types)