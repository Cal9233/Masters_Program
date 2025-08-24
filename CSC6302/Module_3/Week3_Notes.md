# CSC 6302 Database Principles - Week 3 Study Notes

## Database Keys

### Key Definitions
- **Decomposition**: Breaking complex tables into simpler ones that preserve information
- **Superkey**: A set of one or more attributes that collectively allow us to identify uniquely a tuple in the relation
- **Candidate Key**: A superkey that uses the fewest attributes necessary (minimal superkey)
- **Primary Key**: A candidate key we choose to identify tuples in our relation based on our needs and goals

### Project 2 Key Insights
- There are 12 superkeys total in the vessel booking system
- Two candidate keys identified:
  - {Date, Departure_Time, Vessel_ID}
  - {Date, Departure_Time, Passenger_ID}
- Formula: 2^n - 1 gives potential superkeys, but only if they all uniquely identify rows

## Normal Forms

### First Normal Form (1NF)
- Row order doesn't store information
- Single datatype in each column
- Must have primary key
- No repeating data groups
- Unique names for columns

### Second Normal Form (2NF)
- Must be in 1NF
- No partial key dependencies

### Third Normal Form (3NF)
- Must be in 2NF
- No transitive dependencies

### Functional Dependencies
- **Functional Dependency**: For K → R, if two tuples agree on the values of attributes in K, they must also agree on values of all attributes in R
- **Transitive Dependencies**: When attributes depend on other non-key attributes rather than directly on the primary key

## Database Joins

### Join Types
- **Natural Join**: Join on all matching attributes - lets DBMS decide which attributes
- **Inner Join**: Joining attribute must be present in both tables to join tuples - excludes those with null values or that don't have a match
- **Left Outer Join**: All tuples from the left table with matching tuples from the right, or null values
- **Right Outer Join**: All tuples from the right table with matching tuples from the left, or null values

## Entity Relationship Diagrams (ERDs)

### Purpose
ERDs map relationships between tables in relational databases, providing efficiencies in storing and retrieving information.

### Cardinality Types
- **One to One**: First table and second table only have one tuple each that will be matched together
- **One to Many**: First table has unique values in matched attribute, second table has repeated values
- **Many to Many**: Both tables have repeated values in the matched attribute

## SQL Aggregation

### Aggregation Functions
- SUM, AVG, MIN, MAX, COUNT
- Use aggregation functions in SELECT statement
- Include all non-aggregated columns in GROUP BY statement
- Filter aggregated fields using HAVING statement

### Example Syntax
```sql
SELECT dept_name, sum(salary)
FROM instructor
GROUP BY dept_name
HAVING sum(salary) > 100000;
```

## Views

### Definition
Views are virtual relations that allow us to repeat a saved query in the future.

### Advantages
- Can query them just like any other relation
- Can make views from views
- Store commonly used queries

### Basic Syntax
```sql
CREATE VIEW viewname AS 
SELECT x
FROM y
```

### Examples
```sql
-- View without salary information
CREATE VIEW faculty AS
SELECT ID, name, dept_name
FROM instructor;

-- Query the view
SELECT name
FROM faculty
WHERE dept_name = 'Biology';

-- View with aggregation
CREATE VIEW departments_total_salary(dept_name, total_salary) AS
SELECT dept_name, sum(salary)
FROM instructor
GROUP BY dept_name;
```

## Transactions

### Key Properties
- Group a series of statements, queries, and actions together
- Each transaction is a unit of work (atomic transactions)
- Must end in a commit or rollback:
  - **Commit**: Updates become permanent
  - **Rollback**: All updates in the transaction are undone
- If transaction doesn't complete, it's as if it never happened
- Separates transactions that happen at the same time

## Variables and Delimiters

### Variable Types
- **Session Scope**: Used in SQL scripts (prefixed with @)
- **Local Variables**: Used in scope of single function or stored procedure (defined with begin/end block)
- **System Variables**: Used for system admin tasks (prefixed with @@)

### Session Variable Example
```sql
SET @start=1;
SET @end=10;
SELECT * FROM Series WHERE Id BETWEEN @start AND @end;
```

### Delimiters
- Tell code when a statement ends
- MySQL uses semicolon as default
- Change delimiter to group statements with semicolons together

```sql
DELIMITER $$
BEGIN
    STATEMENT A;
    STATEMENT B;
END$$
DELIMITER ;
```

## Functions

### Purpose
Repeatable snippets of code that return a value or values.

### Example Function
```sql
DROP FUNCTION IF EXISTS GetFacultyId;
DELIMITER $$
CREATE FUNCTION GetFacultyId (desiredFacultyName VARCHAR(200)) RETURNS INT 
DETERMINISTIC
BEGIN
    DECLARE desiredId INT;
    SELECT DISTINCT ID INTO desiredId
    FROM instructor
    WHERE name = desiredFacultyName;
    RETURN desiredId;
END$$
DELIMITER ;

-- Usage
SELECT GetFacultyID('Einstein');
```

## Stored Procedures

### Purpose
Repeatable groups of statements that can use queries, variables, views, functions, etc. Allow defining common actions to call later.

### Basic Example
```sql
DROP PROCEDURE IF EXISTS GetAllCourses; 
DELIMITER $$
CREATE PROCEDURE GetAllCourses (desiredDeptName VARCHAR(200))
BEGIN
    SELECT *
    FROM course
    WHERE dept_name = desiredDeptName;
END$$
DELIMITER ;

-- Usage
CALL GetAllCourses('Comp.Sci.');
```

### Advanced Example with Parameters
```sql
CREATE PROCEDURE dept_count_proc (IN dept_name VARCHAR(20), OUT d_count INTEGER)
BEGIN
    SELECT COUNT(*) INTO d_count
    FROM instructor
    WHERE instructor.dept_name = dept_count_proc.dept_name;
END

-- Usage
DECLARE d_count INTEGER;
CALL dept_count_proc('Physics', d_count);
```

### Parameter Types
- **IN**: Parameters expected to have values assigned to them
- **OUT**: Parameters whose values are set in the procedure to return results

## Important Notes

### Project 2 Corrections
1. Cost per hour should be calculated from length of trip and total cost, then loaded into vessel table with UPDATE statement
2. Data should be transferred with SQL, not hard-coded
3. Cost per hour should be associated with a vessel, not a trip

### Schedule Notes
- No office hours during week 3
- Project 3 grading will be delayed
- Project 3 will use functions, views, and procedures to add value to the booking system