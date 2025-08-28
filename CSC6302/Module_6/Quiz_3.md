# Storage, Memory, and Database Privileges Quiz Study Guide

## Question 1: Volatile vs Non-Volatile Memory
**Statement:** Memory that can persist when the power is off is known as Volatile Memory.

**Answer:** False

**Correct Definitions:**
- **Volatile Memory:** Lost when power is off (RAM, cache)
- **Non-Volatile Memory:** Persists when power is off (hard drives, SSDs, flash memory)

*Memory that persists without power is **non-volatile**, not volatile.*

---

## Question 2: Storage Type Classifications
**Match storage types to their categories:**

- **Magnetic Tapes** → Tertiary Storage
- **Magnetic Disks** → Secondary Storage  
- **Main Memory** → Primary Storage

**Storage Hierarchy:**
- **Primary Storage:** CPU cache, RAM (fastest, most expensive)
- **Secondary Storage:** Hard drives, SSDs (moderate speed/cost)
- **Tertiary Storage:** Tape drives, optical storage (slowest, cheapest)

---

## Question 3: Storage Volatility Hierarchy
**Order from least volatile (1) to most volatile (6):**

1. **Magnetic Tapes** (least volatile)
2. **Optical Disks**
3. **Magnetic Disks**
4. **Flash Memory**
5. **Main Memory**
6. **Cache** (most volatile)

*Lower volatility = data persists longer without power*

---

## Question 4: Non-Volatile Memory Definition
**Statement:** Memory that is lost when power is off is known as Non-volatile Memory.

**Answer:** False

**Correct Definition:**
- **Non-volatile Memory:** Retains data when power is off
- **Volatile Memory:** Loses data when power is off

*Memory that is lost when power goes off is **volatile**, not non-volatile.*

---

## Question 5: Disk Reliability Metric
**The average time a disk is expected to run continuously without failure is:**

**Answer:** Mean Time To Failure (MTTF)

*MTTF is a key reliability metric used to predict hardware lifespan and plan maintenance schedules.*

---

## Question 6: RAID Configurations
**RAID Level that uses mirrored disks with block striping is:**

**Answer:** RAID 1

**Common RAID Levels:**
- **RAID 0:** Striping (performance, no redundancy)
- **RAID 1:** Mirroring (redundancy, exact copies)
- **RAID 5:** Striping with parity (balance of performance and redundancy)
- **RAID 6:** Striping with double parity (higher fault tolerance)

---

## Question 7: Database User Privileges
**The four basic privileges users can have in a database are:**

- ✅ **CREATE** (create new objects)
- ✅ **READ** (query/select data)
- ✅ **UPDATE** (modify existing data)
- ✅ **DELETE** (remove data)
- ❌ ENTER (not a standard database privilege)
- ❌ DESTROY (not a standard database privilege)

---

## Question 8: SQL GRANT Statement
**Complete the GRANT statement to give admins modify privileges on users table:**

```sql
GRANT INSERT, UPDATE, DELETE
ON users
TO admins;
```

**GRANT Syntax:**
- `GRANT` - keyword to assign privileges
- `privilege_list` - specific permissions to grant
- `ON table_name` - target database object
- `TO user/role` - recipient of privileges

---

## Question 9: Authorization Definition
**Statement:** Authorization is determining whether an entity has permission to do something.

**Answer:** True

**Security Concepts:**
- **Authentication:** Verifying identity ("Who are you?")
- **Authorization:** Checking permissions ("What can you do?")

*Authorization comes after authentication in the security process.*

---

## Question 10: Mean Time To Data Loss Formula
**To find MTTDL (Mean Time To Data Loss), use the formula:**

**Answer:** MTTF² / (2 × MTTR)

**Formula Components:**
- **MTTF:** Mean Time To Failure
- **MTTR:** Mean Time To Repair
- **MTTDL:** Mean Time To Data Loss

*This formula calculates expected time before data loss in redundant systems.*

---

## Key Concepts Summary

### Memory and Storage Types
- **Volatile:** Loses data without power (RAM, cache)
- **Non-volatile:** Retains data without power (disks, flash)
- **Storage Hierarchy:** Primary → Secondary → Tertiary (speed/cost decreases)

### Storage Technologies
- **Volatility Order:** Cache > RAM > Flash > Magnetic Disks > Optical > Tapes
- **RAID 1:** Mirroring for redundancy
- **MTTF:** Reliability measurement for hardware

### Database Security
- **Authentication:** Identity verification
- **Authorization:** Permission checking
- **Basic Privileges:** CREATE, READ, UPDATE, DELETE
- **SQL GRANT:** Assigns specific permissions to users/roles

### Reliability Calculations
- **MTTDL = MTTF² / (2 × MTTR):** Predicts data loss timing in fault-tolerant systems
- Used for planning backup strategies and system maintenance