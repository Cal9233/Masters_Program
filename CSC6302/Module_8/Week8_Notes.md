# Database Query Processing and Optimization Study Guide

## Unit 8: Query Processing and Optimization

### Table of Contents

1. [Basic Steps in Query Processing](#basic-steps)
2. [Measures of Query Cost](#query-cost)
3. [Selection Operations](#selection-operations)
4. [Join Operations](#join-operations)
5. [Sorting Algorithms](#sorting)
6. [Other Operations](#other-operations)
7. [Execution Plans](#execution-plans)
8. [Practice Challenges](#challenges)

---

## Basic Steps in Query Processing {#basic-steps}

### The Three Fundamental Steps

1. **Parsing and Translation**

   - Translate query into internal form
   - Convert to relational algebra
   - Parser checks syntax and verifies relations

2. **Optimization**

   - Generate equivalent evaluation plans
   - Choose plan with lowest estimated cost
   - Use statistical information from database catalog

3. **Evaluation**
   - Query execution engine executes the chosen plan
   - Returns results to user

### Key Concept: Relational Algebra

Relational algebra is the internal query language used by database engines.

| Operation         | SQL Equivalent           | Relational Algebra       |
| ----------------- | ------------------------ | ------------------------ |
| Selection         | `SELECT *`               | σ(predicate)(table)      |
| Projection        | Returns specific columns | Π(attributeNames)(table) |
| Cartesian Product | Cartesian Product        | (table1) X (table2)      |
| Join              | `JOIN`                   | (t1) ⋈(predicate)(t2)    |

---

## Measures of Query Cost {#query-cost}

### Cost Components

- **Disk access** (primary focus)
- **CPU processing** (often ignored for simplicity)
- **Network communication** (for distributed systems)

### Disk Cost Formula

```
Total Cost = (Number of seeks × average-seek-cost) +
            (Number of blocks read × average-block-read-cost) +
            (Number of blocks written × average-block-write-cost)
```

### Cost Measurement Approaches

1. **Response Time**: Total elapsed time
2. **Resource Consumption**: Total resources used (preferred)

### Important Notes

- We use total resource consumption as our cost metric
- Buffer management can significantly affect actual costs
- Worst-case estimates assume no data is initially buffered
- More optimistic estimates are used in practice

---

## Selection Operations {#selection-operations}

### File Scan (Linear Search)

- **Method**: Scan each block and test all records
- **Applicable**: Works regardless of selection condition, ordering, or indices
- **Performance**: O(n) - examines every record
- **When to Use**: No suitable index available

### Index Scans

#### Clustering Index (Primary Index)

- **Equality on Key**: Single record retrieval using B+ tree
- **Equality on Non-key**: Multiple records in consecutive blocks
- **Comparison Operations**:
  - For σA≥V: Use index to find first tuple ≥ v, scan sequentially
  - For σA≤V: Scan sequentially until first tuple > v

#### Secondary Index (Non-clustering)

- **Purpose**: Index that points to another index
- **Foreign Keys**: Typically have secondary indices
- **Performance**: Can be costly for non-key searches

### Complex Selection Algorithms

#### Conjunction (AND operations)

- **A7**: Use one index, test other conditions in memory
- **A8**: Use composite (multi-key) index
- **A9**: Intersection of identifiers from multiple indices

#### Disjunction (OR operations)

- **A10**: Union of identifiers if all conditions have indices
- **Fallback**: Linear scan if indices unavailable

#### Negation (NOT operations)

- Typically requires linear scan
- Sometimes can optimize by using index for positive condition

### Bitmap Index Scan (PostgreSQL)

- **Purpose**: Bridge between index scan and linear file scan
- **Method**: Create bitmap with 1 bit per page
- **Performance**: Adapts well to different selectivity levels

---

## Join Operations {#join-operations}

### Join Algorithm Types

1. **Nested-Loop Join**
2. **Block Nested-Loop Join**
3. **Indexed Nested-Loop Join**
4. **Merge-Join**
5. **Hash-Join**

### Nested-Loop Join

```pseudocode
for each tuple tr in r do begin
    for each tuple ts in s do begin
        test pair (tr,ts) for join condition θ
        if satisfied, add tr • ts to result
    end
end
```

**Cost Analysis:**

- Worst case: nr × bs + br block transfers
- If smaller relation fits in memory: br + bs block transfers

### Block Nested-Loop Join

- **Improvement**: Process blocks instead of individual tuples
- **Cost**: br × bs + br block transfers (worst case)
- **Optimization**: Use M-2 blocks for outer relation buffering

### Indexed Nested-Loop Join

- **Requirements**: Equi-join or natural join with index on inner relation
- **Cost**: br(tT + tS) + nr × c
- **Strategy**: Use relation with fewer tuples as outer relation

### Merge-Join

**Algorithm:**

1. Sort both relations on join attribute
2. Merge sorted relations
3. Handle duplicate values carefully

**Cost**: br + bs + sorting costs
**Limitation**: Only works for equi-joins and natural joins

### Hash-Join

**Algorithm:**

1. Partition both relations using hash function h
2. For each partition i:
   - Load si into memory, build hash index
   - Probe ri against hash index

**Cost Analysis:**

- No recursive partitioning: 3(br + bs) + 4nh block transfers
- With recursive partitioning: More complex formula
- Optimal: br + bs (if build input fits in memory)

### Hash-Join Variations

#### Hybrid Hash-Join

- **Key Feature**: Keep first partition of build relation in memory
- **Benefit**: Reduces I/O for immediate processing
- **Best When**: M >> √bs

---

## Sorting Algorithms {#sorting}

### In-Memory Sorting

- Use quicksort for relations that fit in memory

### External Sort-Merge

**Phase 1: Create Sorted Runs**

1. Read M blocks into memory
2. Sort in-memory blocks
3. Write sorted runs to disk

**Phase 2: Merge Runs**

1. Use N blocks for input buffers, 1 for output
2. Merge runs until single sorted relation

**Cost Formula:**

- Block transfers: br(2⌈log⌊M/bb⌋-1(br/M)⌉ + 1)
- Multiple passes if N ≥ M

---

## Other Operations {#other-operations}

### Duplicate Elimination

- **Sorting Method**: Adjacent duplicates are easily removed
- **Hashing Method**: Duplicates fall into same bucket
- **Optimization**: Remove during intermediate steps

### Projection

1. Perform projection on each tuple
2. Follow with duplicate elimination

### Aggregation

- **Method**: Group tuples using sorting or hashing
- **Partial Aggregation**: Combine during intermediate steps
- **Functions**: COUNT, MIN, MAX, SUM, AVG

### Set Operations (∪, ∩, -)

- **Hashing Approach**: Partition both relations, process each partition
- **Sorting Approach**: Sort both relations, then merge

### Outer Joins

- **Left Outer**: Add null-padded non-participating tuples from left
- **Implementation**: Modify merge-join algorithm
- **Cost**: Similar to inner join plus null-padding overhead

---

## Execution Plans {#execution-plans}

### Cost-Based Optimization Steps

1. **Generate** logically equivalent expressions using equivalence rules
2. **Annotate** expressions to get alternative query plans
3. **Choose** cheapest plan based on estimated cost

### Plan Cost Estimation Based On:

- **Statistical Information**: Number of tuples, distinct values
- **Intermediate Results**: Cost estimation for complex expressions
- **Algorithm Costs**: Formulas computed using statistics

### Viewing Execution Plans

#### MySQL

- **Visual Plan**: Change output to "Execution Plan" after running query
- **Text Plan**: Use `EXPLAIN ANALYZE <query>`
- **Important**: First run shows initial plan, subsequent runs may show optimized plan

#### Other Databases

- **Oracle**: `EXPLAIN PLAN FOR <query>`
- **SQL Server**: `SET SHOWPLAN_TEXT ON`
- **PostgreSQL**: Shows costs as f..l (first tuple cost..last tuple cost)

### MySQL Execution Plan Caveats

- First execution shows initial plan
- Subsequent executions may show optimized plans
- UI doesn't indicate when you're seeing optimized plan
- Great for planning new queries
- Less reliable for performance analysis of repeated queries

---

## Key Performance Concepts

### Index Types and Performance

- **Clustered Index**: Data stored in index order (primary index)
- **Secondary Index**: Points to clustered index or data
- **Composite Index**: Multi-column index for complex conditions

### Memory and Buffering

- **Buffer Management**: Significant impact on actual performance
- **Worst-Case Assumptions**: No initial buffering, minimum memory
- **Real Systems**: More optimistic estimates, consider buffer state

### Algorithm Selection Criteria

- **Data Size**: Small relations vs. large relations
- **Index Availability**: Can dramatically change optimal algorithm
- **Join Selectivity**: How many tuples match join condition
- **Memory Constraints**: Available buffer space

---

## Practice Challenges {#challenges}

### Write Queries to Generate These Execution Plan Operations:

1. **File Scan**
2. **Index Scan**
3. **Nested Loop**
4. **Clustered Index Scan**
5. **Non-Clustered Index Scan**

### Analyze How These Show Up in Execution Plans:

- Inner join
- Right outer join
- Subquery
- ORDER BY
- GROUP BY
- HAVING
- BETWEEN
- String comparison

### Cost Calculation Practice

Using the examples from the slides:

- **Student relation**: 5,000 records, 100 blocks
- **Takes relation**: 10,000 records, 400 blocks

Calculate costs for:

1. Nested-loop join (both directions)
2. Block nested-loop join
3. Hash join with different memory sizes
4. Merge join with and without sorting

---

## Important Formulas Summary

### Join Cost Formulas

- **Nested-Loop**: nr × bs + br
- **Block Nested-Loop**: br × bs + br
- **Indexed Nested-Loop**: br(tT + tS) + nr × c
- **Merge-Join**: br + bs + sorting_cost
- **Hash-Join**: 3(br + bs) + 4nh (no recursion)

### External Sort Cost

- **Block Transfers**: br(2⌈log⌊M/bb⌋-1(br/M)⌉ + 1)
- **Seeks**: 2⌈br/M⌉ + ⌈br/bb⌉(2⌈log⌊M/bb⌋-1(br/M)⌉ - 1)

---

## Study Tips

### For Exams

1. **Memorize** basic cost formulas
2. **Practice** cost calculations with different scenarios
3. **Understand** when each algorithm is optimal
4. **Know** the trade-offs between algorithms

### For Practical Application

1. **Always** consider alternative ways to write queries
2. **Test** with realistic data volumes
3. **Use** EXPLAIN ANALYZE for accurate performance data
4. **Remember**: The engine isn't always smarter than you!

### Key Takeaways

- Query optimization can mean the difference between seconds and days
- Understanding execution plans is crucial for database performance
- Different algorithms have different strengths based on data characteristics
- Always test with production-scale data volumes
