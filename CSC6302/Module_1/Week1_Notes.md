# CSC 6302 Database Principles - Week 1 Study Notes

## Course Overview

**Course:** CSC 6302 - Database Principles  
**Instructor:** Amanda Menier  
**Institution:** Merrimack College

### Course Objectives
- Apply entity-relationship and relational data models, data structures, integrity constraints, and operations using SQL
- Describe database design theory including functional dependencies, normal forms, and dependency preservation
- Develop SQL integration with Java/Python programs
- Understand database engines and storage systems impact on performance
- Perform query processing and optimization

### Course Structure (8 Weeks)
- **Live Sessions:** Wednesdays 6:30-8:30 PM EDT
- **Office Hours:** Fridays 8:00-9:00 PM EDT
- **Projects:** 6 total (30% of grade)
- **Quizzes:** 3 total (20% of grade)
- **Final Exam:** 20% of grade
- **Final Database:** 15% of grade
- **Final Application:** 15% of grade

### Grading & Academic Integrity
- **Acceptable:** Tutoring, AI for concept explanation, AI for test data, small code adaptations with attribution
- **Unacceptable:** Submitting others' work, AI writing assignments, AI creating images/ER diagrams, copying code without attribution

### Required Textbooks
- **Main:** Database System Concepts 7th edition (Silberschatz, Korth, Sudarshan)
- **Supplements:** SAMS Teach Yourself SQL (10 Minutes & 24 Hours), MySQL Crash Course

---

## Core Database Concepts

### What is a Database?
A collection of data that addresses fundamental questions:
- How do we store this data?
- How do we access this data?
- How do we define this data?
- How do we interact with this data?
- How do we manipulate this data?
- How do we trust this data?
- How does this data relate to itself?

### Database Management System (DBMS)
A collection of interrelated data and a set of programs to access that data.

**Primary Goal:** Store and retrieve database information that is both convenient and efficient.

### Types of DBMS
1. **Relational Database Management System (RDBMS)** - Example: MySQL
2. **Object-Relational Database Management System (ORDBMS)** - Example: PostgreSQL
3. **NoSQL Database Management System** - Example: MongoDB (Document Databases)

---

## From Database to Application

### CRUD Operations
Applications typically perform four basic operations:
- **Create:** Add new data
- **Read:** Retrieve existing data
- **Update:** Modify existing data
- **Delete:** Remove data

### Application Layers
1. **View Layer:** User interface (naive users, application programmers, sophisticated users, database administrators)
2. **Logical Layer:** DML queries, DDL interpreter, query evaluation engine, query processor
3. **Physical Layer:** Buffer manager, file manager, authorization manager, transaction manager, storage manager

---

## Data Trust and Integrity

### ACID Properties
- **Atomicity:** All or nothing - transactions either complete fully or not at all
- **Consistency:** Valid state transition - database remains in consistent state
- **Isolation:** Concurrent transactions do not interfere with each other
- **Durability:** Permanent changes once committed - data persists after system failures

### Authentication vs Authorization
- **Authentication:** Who are you? (Identity verification)
- **Authorization:** What can you do? (Permission management)

---

## Relational Model

### Terminology Mapping
| Common Term | Relational Term |
|-------------|-----------------|
| Table       | Relation        |
| Column      | Attribute       |
| Type        | Domain          |
| Row         | Tuple           |

### MySQL Data Types

#### Numeric Types
- `INT` - Integer values
- `FLOAT` - Floating-point numbers
- `DECIMAL` - Exact decimal numbers

#### String Types
- `CHAR` - Fixed-length strings
- `VARCHAR` - Variable-length strings
- `TEXT` - Large text data

#### Date/Time Types
- `DATE` - Date values
- `DATETIME` - Date and time values
- `TIMESTAMP` - Timestamp values
- `TIME` - Time values

#### Other Types
- `ENUM` - Enumerated values
- `BLOB` - Binary large objects
- `TINYINT` - Boolean values (1 for True, 0 for False)

### Special Considerations
- **NULL:** Indicates no value is present (different from empty string "")
- **Boolean:** MySQL uses `TINYINT` with 1/0 values for True/False
- Important when importing data to handle NULL vs empty values correctly

---

## SQL Basics

### SQL Command Categories
- **DDL (Data Definition Language):** CREATE, DROP, ALTER, TRUNCATE
- **DQL (Data Query Language):** SELECT
- **DML (Data Manipulation Language):** INSERT, UPDATE, DELETE, CALL
- **DCL (Data Control Language):** GRANT, REVOKE
- **TCL (Transaction Control Language):** COMMIT, SAVEPOINT, ROLLBACK

### Database Creation Best Practices
```sql
-- Drop database to avoid errors
DROP DATABASE University;

-- Create database with IF NOT EXISTS clause
CREATE DATABASE IF NOT EXISTS University;

-- Select the database to use
USE University;
```

### Table Creation Syntax
```sql
CREATE TABLE IF NOT EXISTS course (
    course_id    VARCHAR(8), 
    title        VARCHAR(50), 
    dept_name    VARCHAR(20),
    credits      NUMERIC(2,0) CHECK (credits > 0)
);
```

### Data Insertion Methods

#### Manual Insertion
```sql
INSERT INTO course (course_id, title, dept_name, credits) 
VALUES 
    ('CSC6302', 'Database Principles', 'Comp. Sci.', 4.0),
    ('CSC6013', 'Discrete Structures', 'Comp. Sci.', 4.0);
```

#### CSV Import
```sql
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.3/Uploads/courses.csv'
INTO TABLE University.courses 
FIELDS TERMINATED BY ','
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- Skip header row
```

**Important:** Use forward slashes in file paths even on Windows. Check `SHOW VARIABLES LIKE "secure_file_priv";` for allowed upload directory.

### Basic Query Structure
```sql
SELECT column_list    -- Attributes to return
FROM table_name      -- Source table
WHERE conditions;    -- Filter criteria
```

#### Example Query
```sql
SELECT ID
FROM instructor
WHERE dept_name = 'Comp. Sci.';
```

### String Matching with LIKE
- `=` operator is case-sensitive
- `LIKE` operator is case-insensitive
- `_` wildcard matches exactly one character
- `%` wildcard matches zero or more characters

#### Pattern Examples
- `'Intro%'` - Strings beginning with 'Intro'
- `'%Comp%'` - Strings containing 'Comp'
- `'___'` - Exactly three characters
- `'___%'` - At least three characters

### Comments in SQL
```sql
-- Single line comment

/* 
   Multi-line
   comment
*/
```

---

## Key Conventions
- SQL commands are not case-sensitive, but conventionally written in UPPERCASE
- Terminate all statements with semicolon (`;`)
- Use `IF NOT EXISTS` clauses to prevent errors
- Always specify column names in INSERT statements for clarity

---

## Project Information

### Project 1 Overview
**Scenario:** Create database application for Merrimack River Cruises
- **Part 1:** Convert CSV spreadsheet data to database table
- **Part 2:** Connect to cloud University database and execute specific queries

### Cloud Database Connection Details
- **Host:** csc6302-free-csc6302.f.aivencloud.com
- **Username:** student
- **Password:** csc6302
- **Port:** 13860
- **SSL:** Required (download CA certificate from Module 1)

**Test Query:**
```sql
SELECT * 
FROM course
WHERE dept_name LIKE 'COMP%';
```