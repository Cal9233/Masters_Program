# CSC 6302 Database Principles - Week 4 Study Notes

## Project 3 Notes
1. Make dates user-friendly
2. Address rounding issues

## Application Architecture Overview

### Application Purpose
- Most database users do not use SQL directly
- Application programs act as intermediaries between users and databases
- Applications are split into three main layers

### Application Layer Structure

#### Front-end (Presentation Layer)
- **Question**: How do I present my data?
- **Components**:
  - GUI (Graphical User Interface)
  - Websites
  - Mobile applications

#### Middle Layer (Application Layer)
- **Question**: How do I process my data?
- **Components**:
  - Business logic
  - Data access

#### Backend (Data Layer)
- **Question**: How do I store my data?
- **Components**:
  - Database

## Architecture Evolution

### Historical Development
1. **Mainframe Era**: Terminals connected to mainframe computers via proprietary networks or dial-up phone lines
2. **Personal Computer Era**: Desktop PCs connected via Local Area Networks to databases
3. **Web Era**: Web browsers connected via Internet to Web Application Servers and databases

### Two-Tier vs Three-Tier Architecture

#### Two-Tier Architecture
- Client applications connect directly to data source
- Simpler structure but less scalable

#### Three-Tier Architecture
- Client applications connect to application server
- Application server connects to data source
- Better separation of concerns and scalability

## Modern Application Architecture

### Modern Era Characteristics
Most applications include varied presentation layers:

#### Application Types
- **Personal Computer Application**:
  - Requires installation
  - Hardware requirements come into play
- **Client Application Connected to Server**:
  - Allows multi-user application
  - Must handle cases when client cannot communicate with server
- **Web Application in Browser**:
  - Multi-user application that removes hardware dependencies
  - Allows use of offsite servers, cloud storage
  - Loss of network connectivity will have impact
- **Mobile Application**:
  - Adds convenience factor
  - Access anywhere there is network connection

### Application Layers Detail

#### View Layer
- **User Types**: Naive users (tellers, agents, web users), application programmers, sophisticated users (analysts), database administrators
- **Interfaces**: Application interfaces, application programs, query tools, administration tools

#### Logical Layer
- **Components**: Compiler and linker, DML queries, DDL interpreter, application program object code, DML compiler and organizer, query evaluation engine

#### Physical Layer
- **Components**: Buffer manager, file manager, authorization and integrity manager, transaction manager, storage manager, disk storage (indices, data dictionary, data, statistical data)

## Presentation Layer: Web Advantages

Web browsers have become the de-facto standard user interface to databases because they:
- Enable large numbers of users to access databases from anywhere
- Avoid need for downloading/installing specialized code while providing good graphical user interface
- Support JavaScript and other scripting languages that run in browser but are downloaded transparently
- Allow access on mobile devices
- Avoid need to download large amounts of code or data (especially important in mobile environment)
- **Examples**: Banks, airline and rental car reservations, university course registration and grading

## Model-View-Controller (MVC) Architecture

### Components
- **Model**: Business Logic and Data Access
- **View**: Presentation layer (user interface)
- **Controller**: Server that manages communication between Model and View

### Application Layer Functions

#### Business Logic Layer
- Provides high-level view of data and actions on data
- Often uses object data model
- Hides details of data storage schema
- Abstraction of entities (students, courses, etc.)
- Enforces business rules (can only register if prerequisites are met)
- Supports workflows among multiple participants (handles submitting of application by student and reviewing by admissions)
- Handles sequence of steps to be followed
- Handles errors or omissions (what if letter of recommendation is not submitted?)

#### Data Access Layer (DAL)
- Interfaces between business logic layer and underlying database
- Provides mapping from object model of business layer to relational model of database
- Provides abstraction of database contents
- Programmers don't care about tables and foreign keys or how underlying database is set up
- Programmers want to populate their data structures with data they need for business logic
- Database should only be accessed from the DAL
- Formats data from database in readable way
- Sometimes stores integer and maps to enum
- Sometimes maps multiple columns to single data member

## Application Architecture Concerns

### Connectivity Concerns
**What happens when**:
- Internet is not available?
- Mobile networks are not available?
- Local internet connection goes down?
- Particular server cannot be reached?
- Database server goes down?
- Someone accidentally unplugs something?

**How to provide redundancy**:
- Virtualization and failure techniques
- RAID
- Some data may need to be stored locally
- How to keep data consistent if stored in multiple places?

### Performance Concerns
- Performance is issue for popular websites and applications
- May be accessed by millions of users every day, thousands of requests per second at peak time
- Know hardware requirements of your application to fit your requirements

**Caching techniques used to reduce cost**:
- Caching connections for reuse in connection pool
- Caching results of database queries
- Caching of generated HTML for web pages
- **Important**: Cached results must be updated if underlying database changes

### Security Concerns
- Never store passwords (such as database passwords) in clear text in scripts that may be accessible to users
  - On files accessible to web server
  - In database itself
- Limit database access to database servers
- Two-factor authentication is more secure than single-factor authentication
  - E.g., password plus one-time password sent by SMS or app
  - Device generates new pseudo-random number every minute and displays to user
  - User enters current number as password
  - Application server generates same sequence of pseudo-random numbers to check correctness
- Application controls user access to database
  - Application users cannot access database directly

### Audit Trails
- Applications must log actions to audit trail to detect who carried out update or accessed sensitive data

**Audit trails used after-the-fact to**:
- Detect security breaches
- Repair damage caused by security breach
- Trace who carried out the breach

**Audit trails needed at**:
- Database level
- Application level

**Exceptionally useful for debugging issues**:
- Product logs
- Database logs
- Operating system logs

## Database Connectivity: Python MySQL Connector

### Overview
- MySQLConnector is Python Driver for connecting to MySQL databases from Python programs
- Supplies API with functionality to connect to database
- Requires MySQLConnector to be installed on machine
- Ensure MySQL 4.0 or greater installed
- Security concerns with early versions of MySQL that MySQLConnector no longer supports

### Connection Process
```python
mysql.connector.connect(
    host="localhost",
    user="yourusername", 
    password="your_password",
    database="your_database"
)
```

**Connection Details**:
- **HostName**: Host where database is installed
- **Database Name**: Database you want to connect to
- Should be unique connection to each database for simplicity
- Returns database connection object

**Connection Management**:
- Can request new connection every time you query database (more secure but slow)
- Can cache database connection within DAL
- Business logic requests connection from DAL without worrying about details
- In larger applications, database server manages connections in connection pool

### Query Execution
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="admin_user",
    password="admin1234",
    database="SCHOOL"
)
cursor = mydb.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
cursor.close()
```

**Cursor Object**:
- Executes SQL statements against connection
- Can be executed
- Results of executing SQL statement stored in cursor
- **Must be closed when done**

### Data Retrieval Methods

#### FetchOne and FetchAll
- **FetchOne**: Returns first row of query result (similar to using LIMIT 1 in MySQL)
- **FetchAll**: Returns all rows of query result

```python
row = cursor.fetchone()
otherRow = cursor.fetchall()
```

#### Complete FetchAll Example
```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpass",
    database="yourdatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM STUDENT")
result = mycursor.fetchall()
for all in result:
    print(all)
```

### Stored Procedures with Python

#### Basic Stored Procedure Call
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpass",
    database="yourdatabase"
)
mycursor = mydb.cursor()
cursor.callproc('InsertRecipe')
for result in cursor.stored_results():
    print(result.fetchall())
```

#### Stored Procedures with Variables
- Method `Cursor.callproc` can optionally take list of arguments
- List must have exactly same number of arguments expected by stored procedure
- Order of arguments in list must match exactly to order expected by stored procedure
- Types of arguments must match exactly to types expected by stored procedure

## JDBC (Java Database Connectivity)

### Overview
- Java API that allows Java programs to access databases
- Requires JDBC Driver to be installed on system
- Classes that implement JDBC interfaces
- Must be compatible with currently installed version of Java

### Connection to Database
```java
DriverManager.getConnection(url, databaseName, user, password)
```

**URL Format**: `"jdbc:mysql://localhost:3306/"`
- Database servers are part of application layer
- For small applications, database is on localhost
- **Database Name**: JDBC can connect to multiple databases
- **Credentials**: admin_user, admin1234

### Connection Caching
- DriverManager.getConnection returns database connection object
- Can request new connection every time (more secure but slow)
- Can cache database connection within DAL
- In larger applications, database server manages connections in connection pool

### JDBC Statements

#### Statement Types
1. **Statement**:
   - Use for executing queries against database
   - **Pros**: Quick and easy
   - **Cons**: Hard coding SQL, SQL injection attacks, escaping SQL special characters is painful

2. **Prepared Statement**:
   - Executes parameterized queries
   - Allows database engine to cache query plans and reuse them
   - Better performance than Statement

3. **Callable Statement**:
   - Used to execute stored procedures and functions
   - Allows input and output parameters to be specified/accessed

#### Statement and ResultSet Example
```java
Connection myConnection = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/" + databaseName, user, password);
Statement myStatement = myConnection.createStatement();
String query = "SELECT * FROM STUDENT";
ResultSet myRelation = myStatement.executeQuery(query);

while (myRelation.next()) {
    String myRecipeName = myRelation.getString("RecipeName");
    int myIngredientId = myRelation.getInt("IngredientId");
}
```

#### Prepared Statement Example
```java
String query = "SELECT * FROM CookBook WHERE IsOnline=?";
PreparedStatement myPreparedStatement = myConnection.prepareStatement(query);
myPreparedStatement.setInt(1, 0);
ResultSet myRelation = myPreparedStatement.executeQuery();
```

#### Callable Statement Examples
**No Parameters**:
```java
CallableStatement myStoredProcedureCall = 
    myConnection.prepareCall("{Call GetRecipes()}");
ResultSet myResults = myStoredProcedureCall.executeQuery();
```

**With Parameters**:
```java
CallableStatement myStoredProcedureCall = 
    myConnection.prepareCall("{Call getStudentById(?)}");
myStoredProcedureCall.setString(1, 1);
ResultSet myResults = myStoredProcedureCall.executeQuery();
```

### Exception Handling in DAL

**Why important**:
- Bad connection throws exceptions (database doesn't exist, wrong credentials)
- Bad query throws exceptions (incorrect database, tables don't exist, schema changes, syntax errors)
- Disconnected concerns (host unreachable, MySQL not running)
- JDBC concerns (version incompatibility, authentication scheme mismatches)

### Data Structures

**Result Sets Stay in DAL**:
- Abstraction principle
- Result Sets provide more data than business logic layer needs
- Contains metadata, version information, too much data

**DAL provides data in format useful for business layer**:
- Data structure containing just what business layer needs
- Passed between layers, sent over network
- Sent to browser or mobile device with minimal data (XML or JSON)
- Common to return collection of data structures (Map, Array, List)

### Typical DAL Elements
- **DatabaseMgr class**: Provides interface for connecting to various databases
- **DataProvider Classes**: 
  - Takes input from business layer
  - Returns data structure to caller
  - Asks DataMgr for connection
  - Retrieves ResultSet
  - Maps ResultSet to collection of data structures
  - Multiple providers, each "owning" certain part of database
  - Based on product features
  - Goal: readable and maintainable design

## Node MySQL

### Setup
```bash
npm install mysql
```

**Node.js**: JavaScript runtime environment for server
**NPM**: Node Package Manager

### Connection
```javascript
const mysql = require('mysql');
const connection = mysql.createConnection({
    host: 'localhost',
    port: '3306',
    user: 'admin_user',
    password: 'admin1234',
    database: 'SCHOOL'
});
connection.connect();
```

### Query and Close
```javascript
connection.query('SELECT 1 + 1 AS solution', function (error, results, fields) {
    if (error) throw error;
    console.log('The solution is: ', results[0].solution);
});
connection.end();
```

### Stored Procedure Example
**Database Procedure**:
```sql
DELIMITER $$
CREATE PROCEDURE filterTodo(IN done BOOLEAN)
BEGIN
    SELECT * FROM todos WHERE completed = done;
END$$
DELIMITER ;
```

**Node.js Call**:
```javascript
connection.connect((err) => {
    if (err) return console.error(err.message);
    let sql = `CALL filterTodo(?)`;
    connection.query(sql, [false], (error, results, fields) => {
        if (error) return console.error(error.message);
        console.log(results);
    });
    connection.end();
});
```

## Project 4

**Objective**: Create command line application that connects to database and runs premade views, procedures, and functions from Week 3.

**Key Components**:
- Database connectivity using one of the covered technologies (Python MySQL Connector, JDBC, or Node MySQL)
- Integration with views, procedures, and functions created in Project 3
- Command line interface for user interaction