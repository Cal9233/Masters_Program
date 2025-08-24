# CSC 6302 Database Principles - Week 2 Study Notes

## Course Information
**Course:** CSC 6302 - Database Principles  
**Instructor:** Amanda Menier  
**Institution:** Merrimack College  
**Week:** 2

---

## Week 2 Agenda
- Information Redundancy
- Primary Keys and Uniqueness
- Decomposition
- Foreign Keys and Relationships
- Normal Forms
- Joins
- Clean and Transform

---

## Project 1 Notes - Data Type Selection Guidelines

**When choosing datatypes, consider how data will be used in the future:**

### Numeric Data
- **For mathematical operations (add/subtract/multiply):** Choose number types
- **For precision requirements:** Use `DECIMAL`
- **When using DECIMAL:** Consider the magnitude of values

### Text Data
- **For categories or identifiers:** Choose string/text types
- **VARCHAR:** Variable Character length - good for names/addresses where length varies
- **CHAR:** Fixed length strings

### Date/Time Data
- **Always use date/time types** for date/time information to enable special operations

---

## Information Redundancy Problems

### The Core Problem
If we must enter repeated information, we risk errors. **Goal:** One "Source of Truth" for each important piece of information.

### Data Anomalies

#### Insertion Anomaly
- **Problem:** Unable to insert data
- **Common causes:** Required fields that are null, wrong data types

#### Deletion Anomaly
- **Problem:** Deleting a record causes errors in related tables
- **Impact:** Loss of important information when removing records

#### Update Anomaly
- **Problem:** Same information exists in multiple places
- **Issue:** One location gets updated but others don't, creating data inconsistencies

---

## Solution: Decomposition and Normalization

### Decomposition
The process of breaking down a complex database schema into simpler, more manageable sub-schemas.

### Normalization
Creating new tables following a set of rules about good relational design.

**Goal:** A database in "good" form has no redundant data and can be queried quickly and efficiently.

---

## Key Concepts

### Superkey
A set of one or more attributes that collectively allow us to identify uniquely a tuple in the relation.

### Candidate Key
A minimal superkey. Requires the fewest attributes to uniquely identify a tuple.

### Primary Key
The candidate key that best suits our design.

### Foreign Key
The primary key of one table included in the attributes of a second table to create a link between the two.

---

## Normal Forms

### First Normal Form (1NF)
1. **Cannot use row order** to convey information
2. **Cannot mix data types** within the same column
3. **Cannot have tables without a primary key**
4. **Cannot have repeating data groups**
   - Example: Scores column (10, 9, 10, 4, 2, 10)
5. **Cannot have columns with the same name**
   - DBMS usually won't let you do this

### Second Normal Form (2NF)
1. **Must be in First Normal Form**
2. **Each non-key attribute must depend on the entire Primary Key**
   - **No Partial Key Dependencies**
   - Non-key columns cannot depend on only part of a composite primary key

### Third Normal Form (3NF)
1. **Must be in 2NF**
2. **Remove transitive dependencies**
   - **Transitive Dependency:** If a non-key column depends more on another column than it does the primary key

---

## Decomposition Process

### Steps
1. **Identify Functional Dependencies**
2. **Apply Normal Forms**
3. **Ensure Lossless Join**
4. **Check Dependency Preservation**

### Functional Dependency
Describes a relationship between two sets of attributes in a database when one attribute uniquely determines another attribute.

**Rule:** If two tuples agree on the values of attributes α, they must also agree on the values of attributes β.

### Lossless vs Lossy Decomposition

#### Lossy Decomposition (Bad)
- Cannot reconstruct original data perfectly
- **Example:** Employee(ID, name, street, city, salary) split incorrectly
- **Problem:** If two employees have the same name, we cannot reconstruct the original employee relation

#### Lossless Decomposition (Good)
- Can perfectly reconstruct original data by joining tables
- Maintains all original information and relationships

---

## SQL Implementation

### Setting Primary and Foreign Keys

```sql
-- Composite Primary Key with Foreign Key Constraints
CREATE TABLE prereq (
    course_id VARCHAR(8), 
    prereq_id VARCHAR(8),
    PRIMARY KEY (course_id, prereq_id),
    FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE CASCADE,
    FOREIGN KEY (prereq_id) REFERENCES course (course_id)
);
```

### Auto-Increment Primary Keys

```sql
CREATE TABLE classroom (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    building VARCHAR(15),
    room_number VARCHAR(7),
    capacity NUMERIC(4,0)
);
```

### UPDATE Operations

```sql
-- May need to disable safe updates first
SET SQL_Safe_updates = 0;

-- Complex UPDATE with subquery
UPDATE course
SET CostPerHour = (
    SELECT DISTINCT(CAST(replace(Cost,"$","") as decimal(5,2))/ LengthOfTrip) 
    FROM Bookings 
    WHERE Vessel = "Sea Breeze"
)
WHERE Name = "Sea Breeze";
```

---

## Advanced SQL Features

### Table Aliasing
Give shorter names to tables for easier referencing:

```sql
-- Basic aliasing
SELECT * 
FROM course c
LEFT JOIN department d 
ON c.dept_name = d.dept_name
ORDER BY title DESC;

-- Specific column selection with aliases
SELECT c.course_id, c.title, d.dept_name, d.building
FROM course c
LEFT JOIN department d 
ON c.dept_name = d.dept_name
ORDER BY title DESC;
```

### Clean and Transform Data

```sql
-- Move data from one table to another with transformation
INSERT INTO my_courses (my_course_id, my_title)
SELECT takes.course_id, course.title
FROM takes 
JOIN course ON takes.course_id = course.course_id
WHERE student_id = my_student_id;
```

### SQL Order of Execution

**Important:** SQL executes in a different order than written:

| Writing Order | Execution Order |
|---------------|-----------------|
| 1. SELECT     | 5. SELECT       |
| 2. FROM       | 1. FROM         |
| 3. WHERE      | 2. WHERE        |
| 4. GROUP BY   | 3. GROUP BY     |
| 5. HAVING     | 4. HAVING       |
| 6. ORDER BY   | 6. ORDER BY     |
| 7. LIMIT      | 7. LIMIT        |

---

## Enhanced SELECT Operations

### SELECT DISTINCT
Removes duplicates from results.

### Mathematical and String Operations
Transform data to get custom results in SELECT clause.

### Column Aliasing
```sql
SELECT (column or expression) AS AnotherName
```
Renames fields in results. **Note:** Underlying table and data remains unchanged.

### CAST Function
Convert data types for display or operations:

```sql
SELECT CAST(course_id AS DECIMAL(5,2)) FROM course;
SELECT CAST('123' AS DECIMAL(5,2));
```

### String Functions
- **CONCAT(s1, s2, ..., sn):** Combine strings and values
- **REPLACE(text_to_search, text_to_replace, replacement_text):** Replace text
  - **Tip:** Replace a character with empty string to delete it

---

## Advanced WHERE Clause

### Comparison Operators
`>`, `<`, `>=`, `<=`, `=`, `<>`, `LIKE`, `IS NULL`, `BETWEEN`, `IN`

### Logical Operators
- **NOT:** Negation to expand comparison options
- **AND, OR:** Create complex chains of logic through grouping

### Ordering Results
```sql
-- Single column with direction
SELECT department_name
FROM department
ORDER BY building_name DESC;

-- Multiple columns (each can have different direction)
ORDER BY building_name DESC, department_name ASC;
```

### Nested Subqueries
```sql
SELECT * FROM course
WHERE dept_name IN (
    SELECT dept_name
    FROM department
    WHERE building LIKE 'T%'
)
ORDER BY title DESC;
```

---

## JOIN Operations

### Purpose
Match columns from one table with another to combine data.

### Types of Joins

#### Natural Join
- DBMS decides where to make the relationship
- Automatic matching on columns with same names

#### Inner Join
- Excludes rows where the key in one table has no corresponding value
- Only shows matching records from both tables

#### Outer Join (Left, Right, Full)
- **Left Join:** All records from left table, matching from right
- **Right Join:** All records from right table, matching from left  
- **Full Outer Join:** All records from both tables
- Displays NULL value placeholders when no matching value found

### Join Visual Guide
- **Left Inclusive:** All of table A, matching parts of B
- **Right Inclusive:** All of table B, matching parts of A
- **Left Exclusive:** Only A records without matches in B
- **Right Exclusive:** Only B records without matches in A
- **Full Outer Inclusive:** Everything from both tables
- **Full Outer Exclusive:** Records that don't match in either direction
- **Inner Join:** Only matching records between both tables

---

## Project 2 Overview

**Scenario:** After setting up the MRC database, split the bookings table into three separate tables that can be joined together later. This provides opportunity to improve datatypes for better aggregation.

**Key Skills:**
- Database normalization implementation
- Table decomposition
- Data type optimization
- JOIN operations

### Opening Starter Code
**Best Practice:** Be in your local instance tab, then open the file using the open file dialog in MySQL Workbench.

---

## Key Takeaways

1. **Normalization prevents data anomalies** and improves database efficiency
2. **Choose data types based on intended use** - consider future operations
3. **Primary and foreign keys establish table relationships** for data integrity
4. **Decomposition must be lossless** to preserve all original information
5. **JOINs allow reconstruction** of data from normalized tables
6. **Understanding SQL execution order** helps write more efficient queries
7. **Proper normalization eliminates redundancy** while maintaining data relationships

---

## Reference Links
- [Anomalies in Relational Model](https://www.geeksforgeeks.org/anomalies-in-relational-model/)
- [2NF Partial Dependency](http://rdbms.opengrass.net/2_Database%20Design/2.2_Normalisation/2.2.5_2NF-Partial%20Dependancy.html)
- [3NF Transitive Dependency](http://rdbms.opengrass.net/2_Database%20Design/2.2_Normalisation/2.2.6_3NF-Transitive%20Dependency.html)
- [SQL Execution Order](https://www.kdnuggets.com/the-essential-guide-to-sql-execution-order)
- [MySQL CAST Function](https://www.w3schools.com/sql/func_mysql_cast.asp)
- [MySQL String Functions](https://www.w3schools.com/sql/sql_ref_mysql.asp)
- [Seven JOIN Techniques](https://medium.com/@authfy/seven-join-techniques-in-sql-a65786a40ed3)