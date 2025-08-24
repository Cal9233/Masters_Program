# CSC 6302 - Database Principles: Week 7 Study Notes

## Database Storage Structure Overview

**Basic Storage Hierarchy**:
- **Database**: Collection of files (tables)
- **File**: Sequence of records (rows) 
- **Record**: Sequence of fields (columns)
- **Records are mapped to disk blocks**

## Fixed-Length Records

### Characteristics
- **Assumptions**:
  - Record size is fixed
  - Each file has single record type only
  - Different files used for different relations

### Storage Method
**Simple Approach**: Store record i starting from byte n × (i - 1), where n is the size of each record

### Deletion Strategies

**Method 1: Shift Records**
- Move records i+1, i+2, ... to positions i, i+1, ...
- Maintains sequential order but expensive for large files

**Method 2: Replace with Last Record**
- Move record n to position i
- Faster but loses original ordering

**Method 3: Free List**
- Don't move records
- Link all free records on a free list
- Use header to track first free record
- Most efficient for frequent insertions/deletions

## Variable-Length Records

### Causes of Variable-Length Records
1. **Multiple record types** in single file
2. **Variable-length fields** (e.g., VARCHAR strings)
3. **Optional fields** or null values

### Storage Structure
- **Attributes stored in order**
- **Variable-length attributes**: Represented by fixed-size (offset, length) pairs
- **Actual variable data**: Stored after all fixed-length attributes
- **Null values**: Represented by null-value bitmap

### Slotted Page Organization
**Header Contains**:
- Number of record entries
- End of free space in block
- Location and size of each record

**Key Features**:
- Records can be moved within page to maintain contiguity
- Pointers should reference header entry, not direct record location
- Enables efficient space management

## File Organization Methods

### 1. Heap File Organization
**Characteristics**:
- Records placed anywhere with free space
- Records usually don't move once allocated
- No particular ordering

**Free-Space Management**:
- **Free-space map**: Array with 1 entry per block
- Each entry uses few bits to record fraction of block that's free
- Example: 3 bits per block, value ÷ 8 = fraction free
- **Second-level free-space map**: Each entry stores maximum from 4 first-level entries

### 2. Sequential File Organization
**Characteristics**:
- Records ordered by search-key
- Suitable for sequential processing of entire file

**Operations**:
- **Deletion**: Use pointer chains to maintain order
- **Insertion**:
  - If free space exists: Insert in correct position
  - If no free space: Insert in overflow block
  - Update pointer chains in both cases
- **Reorganization**: Periodically needed to restore sequential order

### 3. Multi-table Clustering File Organization
**Purpose**: Store related records from multiple tables in same file
**Motivation**: Minimize I/O by keeping related records on same block
**Example**: Store department and instructor records together by department

## Storage Access and Buffer Management

### Buffer Management Concepts
- **Block**: Unit of both storage allocation and data transfer
- **Goal**: Minimize block transfers between disk and memory
- **Buffer**: Portion of main memory storing copies of disk blocks
- **Buffer Manager**: Subsystem allocating buffer space

### Buffer Manager Operations
**When program requests block**:
1. **If block in buffer**: Return memory address
2. **If block not in buffer**:
   - Allocate buffer space
   - Replace another block if needed (write back if modified)
   - Read block from disk to buffer
   - Return memory address

## Indexing Fundamentals

### Index Purpose
- **Tool for database developers** to give storage hints to database engine
- **Enables faster lookup** in volatile memory when used properly
- **Default indexes**: All primary key and foreign key columns
- **Trade-off**: Storage overhead vs. query performance

### Basic Index Concepts
- **Search Key**: Attribute(s) used to look up records
- **Index Entry Format**: (search-key, pointer)
- **Index files typically much smaller** than original files

### Index Types
**By Organization**:
1. **Ordered Indices**: Search keys stored in sorted order
2. **Hash Indices**: Search keys distributed via hash function

**By Relationship to Data**:
1. **Clustering Index (Primary)**:
   - Search key specifies sequential order of file
   - Usually (but not necessarily) the primary key
2. **Secondary Index (Non-clustering)**:
   - Search key specifies different order from file's sequential order

### Dense vs Sparse Indexes
**Dense Index**: Contains index record for every search-key value
**Sparse Index**: 
- Contains index records for only some search-key values
- Only applicable when records sequentially ordered on search-key
- **Search Process**:
  1. Find index record with largest search-key value < K
  2. Search file sequentially from that point

### Secondary Index Structure
- **Purpose**: Index on non-ordering attribute (e.g., salary)
- **Structure**: Index record points to bucket containing pointers to all actual records with that search-key value
- **Required for non-unique search keys**

### Multilevel Indexes
**Problem**: If index doesn't fit in memory, access becomes expensive
**Solution**: Treat index as sequential file and create sparse index on it
- **Outer Index**: Sparse index of basic index
- **Inner Index**: The basic index file
- **Multiple Levels**: Can create additional levels if needed
- **Update Requirement**: All levels must be updated on insertion/deletion

## Data Structures for Indexing

### Performance Comparison
- **Array**: O(n) linear search - too slow
- **Binary Search Tree**: O(log n) average case, but O(n) worst case
- **Problem with BST**: Can degenerate to linked list with sorted input

### B+ Trees
**Why B+ Trees?**
- Guarantee O(log n) performance in all cases
- Self-balancing structure
- Optimized for disk-based storage

### B+ Tree Structure
**Internal Nodes**:
- Can have up to n pointers (children)
- Contains up to n-1 keys
- Keys serve as routing information

**Leaf Nodes**:
- Contains up to n-1 keys
- Pointer to next leaf node (enables sequential access)
- Contains actual data or pointers to data

### B+ Tree Operations
**Insertion with Node Splitting**:
1. **When node becomes full**: Must split into two nodes
2. **Promotion**: Median key promoted to parent node
3. **Recursive Splitting**: If parent becomes full, process continues up tree
4. **Root Splitting**: May create new root, increasing tree height

**B+(3) Tree Example**:
- Insert 1, 7: Simple insertion in leaf
- Insert 22: Node full (1,7,22), split needed
  - Split into (1) and (7,22)
  - Promote 7 to create root
- Insert 4: Add to left leaf (1,4)

### B+ Tree Benefits
- **Balanced**: All leaf nodes at same level
- **Efficient**: Guaranteed O(log n) operations
- **Sequential Access**: Leaf nodes linked for range queries
- **Disk-Optimized**: Minimizes disk I/O operations

## SQL Index Commands

### Creating Indexes
```sql
CREATE INDEX <index-name> ON <relation-name> (<attribute-list>);
```
**Example**:
```sql
CREATE INDEX users_name_index ON users(last_name);
```

### Unique Indexes
```sql
CREATE UNIQUE INDEX <index-name> ON <relation-name> (<attribute-list>);
```
- Enforces uniqueness constraint
- Not required if SQL UNIQUE constraint supported

### Dropping Indexes
```sql
DROP INDEX <index-name>;
```

### Database-Specific Features
- Most systems allow specification of:
  - Index type (B+, Hash, etc.)
  - Clustering properties
  - Storage parameters

## B+ Tree Visualization
**Recommended Tool**: https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html
- Interactive tool for understanding B+ tree operations
- Visualizes insertion, deletion, and splitting processes
- Helpful for practicing B+ tree construction

## Key Performance Concepts

### When to Use Indexes
- **Primary and Foreign Keys**: Always indexed by default
- **Frequently Queried Columns**: Good candidates for indexing
- **Range Queries**: B+ trees excel at range operations
- **Join Conditions**: Speed up table joins

### Index Trade-offs
- **Storage Overhead**: Indexes require additional disk space
- **Update Overhead**: Must maintain indexes during INSERT/UPDATE/DELETE
- **Query Performance**: Dramatic improvement for SELECT operations
- **Decision Criterion**: Index usefulness must outweigh storage/maintenance costs

### Clustering vs Non-clustering
- **Clustering Index**: One per table, determines physical order
- **Non-clustering Index**: Multiple allowed, don't affect physical order
- **Performance**: Clustering indexes generally provide better performance for range queries