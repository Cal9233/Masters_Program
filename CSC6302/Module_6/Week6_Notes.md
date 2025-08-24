# CSC 6302 - Database Principles: Week 6 Study Notes

## Storage Systems

### Physical Storage Media Classification

**Volatile Storage**: Loses contents when power is switched off
- Cache memory
- Main memory (RAM)

**Non-volatile Storage**: Contents persist even when power is switched off
- Secondary storage (flash memory, magnetic disks)
- Tertiary storage (magnetic tape, optical storage)
- Battery-backed main memory

**Factors Affecting Storage Choice**:
- Speed of data access
- Cost per unit of data
- Reliability

### Storage Hierarchy (Most to Least Volatile)

1. **Cache** - Fastest, most volatile
2. **Main Memory** - Fast, volatile
3. **Flash Memory** - Moderate speed, non-volatile
4. **Magnetic Disk** - Moderate speed, non-volatile
5. **Optical Disk** - Slower, non-volatile
6. **Magnetic Tapes** - Slowest, least volatile

**Primary Storage**: Fastest media but volatile (cache, main memory)
**Secondary Storage**: Non-volatile, moderately fast (flash memory, magnetic disks) - also called "on-line storage"
**Tertiary Storage**: Non-volatile, slow access time (magnetic tape, optical storage) - also called "off-line storage" for archival

## Magnetic Hard Disk Mechanism

### Components
- **Read-write head**: Reads/writes data
- **Tracks**: Circular divisions on platter surface (50K-100K tracks per platter)
- **Sectors**: Smallest unit of data that can be read/written (typically 512 bytes)
- **Sectors per track**: 500-1000 (inner tracks) to 1000-2000 (outer tracks)
- **Cylinders**: Same track position across multiple platters
- **Spindle**: Central rotating shaft holding multiple platters (1-5 usually)
- **Arm assembly**: Positions heads on correct tracks

### Performance Measures

**Access Time** = Seek Time + Rotational Latency
- **Seek Time**: Time to reposition arm over correct track (4-10 ms typical)
- **Rotational Latency**: Time for sector to appear under head (4-11 ms typical, average is half)
- **Overall Latency**: 5-20 ms depending on disk model

**Data Transfer Rate**: Rate at which data can be retrieved/stored
**IOPS**: I/O Operations Per Second (50-200 IOPS on current magnetic disks)

### Access Patterns
- **Sequential Access**: Successive requests for successive blocks (efficient, only one seek needed)
- **Random Access**: Successive requests anywhere on disk (inefficient, requires seek for each access)

### Disk Controller Functions
- Interfaces between computer and disk hardware
- Accepts high-level commands (read/write sector)
- Computes and attaches checksums for data verification
- Ensures successful writing by reading back after writing
- Performs bad sector remapping

## Mean Time to Failure (MTTF)

**Single Disk**: Average time disk expected to run without failure
- Example: MTTF = 100,000 hours

**Multiple Disks**: System MTTF = Single Disk MTTF ÷ Number of Disks
- Example: 100 disks with 100,000-hour MTTF = 1,000 hours system MTTF (≈41 days)
- **Key Point**: Failure probability increases significantly with more disks

## RAID (Redundant Arrays of Independent Disks)

### Purpose
- Increase data integrity and availability
- Improve performance through parallelism
- Enhance data security through redundancy

### Key Benefits
1. Increased data reliability and redundancy
2. Enhanced speed
3. Higher data capacity

### Improvement Methods

**Redundancy (Reliability)**:
- **Mirroring**: Duplicate every disk, write to both copies
- Data loss only occurs if both disks in mirror pair fail
- Mean Time to Data Loss (MTTDL) = MTTF² ÷ (2 × MTTR)
- Example: MTTDL = (100,000)² ÷ (2 × 10) = 500 million hours ≈ 57,000 years

**Parallelism (Performance)**:
- **Load Balancing**: Multiple small accesses to increase throughput
- **Large Access Parallelization**: Reduce response time
- **Block-level Striping**: Block i goes to disk (i mod n) + 1

### RAID Levels

**RAID 0**: Block striping, non-redundant
- High performance, no fault tolerance
- Used where data loss is not critical

**RAID 1**: Mirrored disks with block striping
- Best write performance
- Popular for database log files
- 100% storage overhead

**RAID 5**: Block-interleaved distributed parity
- Distributes parity among all N+1 disks
- Can tolerate single disk failure
- Parity block location: disk (n mod 5) + 1
- More efficient than RAID 4 (avoids parity disk bottleneck)

**RAID 6**: P+Q redundancy
- Similar to RAID 5 but stores two error correction blocks
- Can tolerate multiple disk failures
- Better reliability at higher cost
- Becoming more important as storage sizes increase

### Parity Calculations
- **Parity Block**: Stores XOR of bits from corresponding blocks
- **Writing**: Must compute and write new parity (2 reads + 2 writes)
- **Recovery**: Compute XOR of all other blocks including parity

### RAID Level Selection Factors
- Monetary cost
- Performance during normal operation
- Performance during failure
- Performance during rebuild
- Time to rebuild failed disk

**RAID 1 vs RAID 5**:
- RAID 1: Better write performance (2 block writes vs 4 block operations)
- RAID 5: Lower storage cost, better for sequential large writes
- RAID 1: Better for random/small updates

## Hardware vs Software RAID

**Software RAID**: Implemented entirely in software, no special hardware
**Hardware RAID**: Special hardware implementation
- Uses non-volatile RAM for write operations
- Better protection against power failures
- Supports hot swapping (replace disk while running)
- Often includes spare disks for immediate replacement
- May have redundant power supplies and controllers

### Advanced Features
- **Data Scrubbing**: Continually scan for latent failures
- **Hot Swapping**: Replace failed disks without powering down
- **Spare Disks**: Online replacements for immediate use
- **Latent Failures**: Previously written data gets damaged over time

## Authentication & Authorization

### Definitions
- **Authentication**: Process of verifying identity of user or system
- **Authorization**: Process of determining if authenticated entity has permission to access resources or perform actions

### Database User Management

#### Database Administrator (Root User)
**Privileges**:
1. Create, Read, Update, Delete any user account
2. Grant and revoke privileges from other users
3. Start, stop, restart database server
4. CRUD database schemas and tables
5. Manage security policies, encryption, access controls

#### User Management Commands

**Create User**:
```sql
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
```

**Grant Privileges**:
```sql
GRANT <privilege list>
ON <relation name or view name>
TO <user/role list>;
```

**Role Management**:
```sql
CREATE ROLE teacher;
GRANT SELECT ON grades TO teacher;
CREATE ROLE principal;
GRANT teacher TO principal;
```

### Users of Database vs Users in Database

**Important Distinction**:
- **Database Users**: Have direct database access with specific privileges
- **Application End Users**: Access data through application layer, not directly to database

### Application Layer Security

#### End User Management
```sql
CREATE TABLE users (
    id INT,
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE roles (
    role ENUM('CEO', 'Sales Manager', 'Sales Rep')
);
```

#### Password Security with BCrypt

**Installation**:
```python
pip install bcrypt
```

**Password Hashing**:
```python
import bcrypt

password = "mypass12345!"
salt = bcrypt.gensalt(rounds=12)
hashed_pw = bcrypt.hashpw(password, salt)
# Store hashed_pw in database
```

**Password Verification**:
```python
# Retrieve hashed_pw from database
password = "mypass12345!"  # User input
is_valid = bcrypt.checkpw(password, hashed_pw)  # Returns boolean
```

#### Security Architecture
1. **View Layer**: User interface
2. **Application Layer**: 
   - Business Logic Layer: Authentication/authorization logic
   - Data Access Layer: Database interactions
3. **Database Layer**: Secure data storage

### Key Security Principles
- Hash passwords before storing (never store plain text)
- Use strong hashing algorithms (BCrypt with salt)
- Separate application users from database users
- Implement authentication at application layer
- Implement authorization based on user roles
- Use principle of least privilege for database access

## Project 5 Feedback Summary
1. Login screen incomplete - missing port specification
2. Missing UI components (dropdowns, date/time pickers)
3. Double booking prevention implementation needed
4. Hard-coded passwords cause portability issues between different MySQL instances