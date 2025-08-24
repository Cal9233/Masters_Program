# Marine Rental Company (MRC) Management System

## Overview

This application demonstrates a three-layer architecture for managing a marine rental company's database operations. The system includes vessel management, passenger tracking, and trip scheduling functionality.

## Architecture

- **View Layer** (View.py): Handles user interaction and data presentation
- **Business Logic Layer** (BLL.py): Manages business rules and data processing
- **Data Access Layer** (DAL.py): Handles direct database operations

## Prerequisites

1. **Python 3.7 or higher**
2. **MySQL Server** running with the MRC database set up
3. **Required Python packages:**
   ```bash
   pip install mysql-connector-python
   ```

## Database Setup

1. **Create the database** using the provided SQL script:

   - Run the complete SQL script in your MySQL environment
   - This will create the `mrc` database with all tables, views, functions, and procedures
   - Sample data will be inserted automatically

2. **Verify the database** contains:
   - Tables: `vessels`, `passengers`, `trips`
   - Views: `all trips`, `total revenue by vessel`
   - Functions: `getVesselID`, `getPassengerID`
   - Procedures: `addTrip`, `addVessel`, `addPassenger`, etc.

## File Structure

```
MRC_Project/
├── DAL.py          # Data Access Layer
├── BLL.py          # Business Logic Layer
├── View.py         # Presentation Layer (Main entry point)
└── README.md       # This file
```

## Running the Application

### Install required Package

```bash
pip install mysql-connector-python
```

### Direct Execution

```bash
python view.py
```

## Application Flow

When you run the application, it will:

1. **Prompt for database credentials:**

   - Database Host (default: localhost)
   - Username
   - Password
   - Database name (default: mrc)

2. **Execute demonstration steps:**
   - Display total revenue by vessel
   - Test vessel ID lookups (existing and non-existing)
   - Add trips (existing entities and new entities)
   - Display all trips in user-friendly format

## Sample Database Credentials

If you used the default setup from the SQL script:

- **Host:** localhost (or 127.0.0.1)
- **Username:** root
- **Password:** (your MySQL root password)
- **Database:** mrc

## Expected Output

The application will display:

- Formatted tables showing revenue data
- Vessel lookup results with success/failure indicators
- Trip addition confirmations
- Complete trip listings with passenger and vessel details
- All currency amounts properly formatted
- Dates and times in readable formats

## Features Demonstrated

- **Database connectivity** with error handling
- **Stored procedure calls** for data operations
- **Function calls** for ID lookups
- **View queries** for complex data retrieval
- **Transaction management** with commits
- **User-friendly data formatting**
- **Error handling and validation**

## Troubleshooting

### Common Issues:

1. **"Access denied" errors:** Check your MySQL username and password
2. **"Unknown database" errors:** Ensure the MRC database was created properly
3. **"Table doesn't exist" errors:** Run the complete SQL script to create all objects
4. **Import errors:** Install required packages with pip

### Database Connection Issues:

- Verify MySQL server is running
- Check that the user has proper permissions on the mrc database
- Ensure the database contains all required tables, views, and procedures

## Sample Run Commands

```bash
# Navigate to the project directory
cd Malagon_MRCapplication

# Install required package
pip install mysql-connector-python

# Run the application
python view.py

# Follow the prompts to enter your database credentials
# The application will run automatically and display results
```

## Sample Interactive Session

```
============================================================
  Marine Rental Company - Database Setup
============================================================
Please provide your database connection details:
Database Host (default: localhost): 127.0.0.1
Database Username: root
Database Password: password
Database Name (default: mrc): mrc
```

## Notes

- The application runs from start to finish automatically after database connection
- All database operations are committed automatically
- The connection is properly closed when the application ends
- Sample data demonstrates both successful and error cases
- Output is formatted for non-technical users with clear headers and tables
- The view layer prompts for database parameters as required by the specifications
