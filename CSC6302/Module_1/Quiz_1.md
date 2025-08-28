# SQL and Database Concepts Quiz Study Guide

## Question 1: SQL Query Construction
**Complete the SQL query to return first and last name of users with id > 10, ordered alphabetically by last name:**

```sql
SELECT first_name, last_name
FROM users
WHERE id > 10
ORDER BY last_name ASC
```

**Key Components:**
- `SELECT` - specifies columns to retrieve
- `FROM` - specifies the table
- `WHERE` - filters rows based on conditions
- `ORDER BY` - sorts results (ASC = ascending, DESC = descending)

---

## Question 2: Database Dependencies
**Statement:** If you know the value of A, you can find out the value of B. Therefore, A is the dependent and B is the determinant.

**Answer:** False

*Correction: If knowing A allows you to find B, then **A is the determinant** and **B is the dependent**. The determinant determines the dependent variable.*

---

## Question 3: Database Schema Management
**The process of breaking down a complex database schema into simpler, more manageable sub-schemas is known as:**

**Answer:** Decomposition

*Decomposition is a fundamental concept in database design, often used in normalization to reduce redundancy and improve data integrity.*

---

## Question 4: SQL Execution Order
**Order that the Database Engine reads SQL instructions:**

1. **FROM** - Identifies source tables
2. **WHERE** - Filters rows
3. **GROUP BY** - Groups rows
4. **HAVING** - Filters groups
5. **SELECT** - Chooses columns
6. **ORDER BY** - Sorts final results

*Note: This is the logical execution order, not the syntax order you type.*

---

## Question 5: Database Architecture Layers
**The three main layers of a database are:**

- ✅ **View Layer** (External level - user interface)
- ✅ **Logical Layer** (Conceptual level - data relationships)  
- ✅ **Physical Layer** (Internal level - data storage)
- ❌ Application Layer (not one of the main database layers)

---

## Question 6: ACID Properties
**ACID stands for:**

**Answer:** Atomicity, Consistency, Isolation, Durability

**ACID Properties Explained:**
- **Atomicity:** Transactions are all-or-nothing
- **Consistency:** Database remains in valid state
- **Isolation:** Concurrent transactions don't interfere
- **Durability:** Committed changes persist permanently

---

## Question 7: Relational Model Terms
**Statement:** In the relational model, a Domain is the same as a Row.

**Answer:** False

*Clarification: A **Domain** is the set of allowable values for an attribute (column), while a **Row** is a tuple/record containing actual data values.*

---

## Question 8: Composite Keys
**Statement:** A Primary Key that has more than one attribute is called a Composite Key.

**Answer:** True

*A Composite Key consists of multiple columns that together uniquely identify each row in a table.*

---

## Question 9: SQL Join Types
**Which option is NOT considered a join in SQL?**

**Answer:** Between Join

**Valid SQL Joins:**
- Inner Join
- Outer Join (Left, Right, Full)
- Natural Join
- Cross Join

*"Between Join" is not a valid SQL join type. BETWEEN is a comparison operator used in WHERE clauses.*

---

## Question 10: SQL LIKE Pattern Matching
**Query:** `SELECT name FROM users WHERE name LIKE '_***l%'`
*(Spaces removed for actual execution)*

**Pattern Explanation:**
- `_` = exactly one character
- `*` = literal asterisk character  
- `%` = zero or more characters
- Pattern: `_***l%` = one char + three asterisks + 'l' + any chars

**Matching Values:**
- ✅ **Pauline** (P + *** + l + ine)
- ✅ **Paula** (P + *** + l + a)  
- ✅ **Paulo** (P + *** + l + o)
- ❌ **Peter** (doesn't contain '***l')

---

## Key Concepts Summary

### SQL Fundamentals
- **Query Structure:** SELECT → FROM → WHERE → ORDER BY
- **Execution Order:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- **Pattern Matching:** `_` (one char), `%` (any chars), literal characters

### Database Design
- **Normalization:** Decomposition reduces redundancy
- **Dependencies:** Determinant → Dependent relationship
- **Keys:** Composite keys use multiple attributes

### Database Architecture
- **Three Layers:** View, Logical, Physical
- **ACID Properties:** Ensure reliable transactions
- **Relational Model:** Domains ≠ Rows (domains are value sets)

### Join Operations
- Multiple join types exist (Inner, Outer, Natural)
- "Between Join" is not a valid join type
- BETWEEN is a comparison operator, not a join