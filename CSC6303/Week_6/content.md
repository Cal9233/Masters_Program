# CSC 6303 Week 6: Study Notes - File System Basic Concepts and Styles

## Overview
File systems are the foundation for data storage and retrieval. While storing large amounts of information is easy, retrieving it efficiently becomes complex. This week covers file system principles, types, and practical usage across different operating systems.

## Historical Evolution of File Systems

### Timeline of Storage Technology
| Era | Technology | Characteristics |
|-----|------------|-----------------|
| **1950s** | Magnetic tapes | Sequential searches required |
| **1960s** | Magnetic hard disks | Direct access, tree-like structures |
| **1970s-2000s** | Floppy disks | Portable storage (phased out early 2000s) |
| **1990s-2000s** | Hard Disk Drives (HDDs) | NTFS, ext3, HFS+ with journaling |
| **2000s-Present** | Solid-State Drives (SSDs) | Faster speeds, no moving parts |
| **2000s-Present** | Cloud-based systems | Remote storage with internet access |

### Modern Cloud Storage Types

#### Distributed File Systems (DFS)
- Files broken into pieces across multiple servers
- Appear as single file to user
- Benefits: backup, reliability, large data handling
- Examples: Google File System, Hadoop HDFS

#### Object Storage
- Files stored as independent objects with unique IDs
- Includes metadata instead of traditional folders
- Scalable, API-accessible
- Good for cloud backups and streaming
- Examples: Amazon S3, Google Cloud Storage

## File System Principles

### Core Concepts

#### Space Management
- **Sectors**: Memory divided into sectors for storing files/folders
- **Non-adjacent storage**: Sectors don't need to be physically adjacent
- **Indexing**: Uses item names as keys to locate sectors
- **Methods**: Hash tables, red-black trees, etc.
- **Goal**: Optimize storage for easier retrieval

#### Item Names as Keys
- Each OS has specific naming conventions
- Names used to locate files in the system
- Case sensitivity varies by system

#### Security Features
- System areas vs personal areas
- Access rights management
- Permission systems (owner-group-all)

### Space Management Details

#### File Creation Process
1. File system chooses sector based on criteria:
   - First available
   - Random choice
   - Best fit
   - Physical device considerations

#### File Access
- File sectors are read when item is accessed
- Multiple sectors may need to be read for large files

#### File Deletion
- **Important**: Only control section is updated
- Actual data remains until overwritten
- **This is why deleted data can sometimes be recovered**

## File Naming Conventions

### Best Practices for Cross-Platform Compatibility

#### Case Sensitivity Rules
- **Old systems (DOS)**: Converted to uppercase (not case-preserving)
- **Case-preserving but insensitive**: "File.txt" = "file.TXT" = "file.txt"
- **Case-sensitive**: "FILE.txt" ≠ "file.txt"

#### Naming Guidelines
- Always use consistent case
- Start with letters (avoid numbers/symbols)
- Use only: letters, digits, ".", "_"
- **Dot (.)**: Separates parts, including extensions
- **Underscore (_)**: Separates parts (avoid camelCase in filenames)
- **Space ( )**: Can cause complications in scripts

## Types of File Systems

### Classification by Media Type
- **Tape file systems**
- **Disk file systems**
- **Flash file systems**

### Classification by Usage
- **Standard file systems**
- **Database file systems**
- **Transactional file systems**
- **Network file systems**

### Classification by OS Features
- **Unix-like operating systems oriented**
- **Old Windows compatible**
- **New Windows compatible**

## Common File System Examples

### Major File Systems

#### exFAT
- Extension of FAT and FAT32
- **Compatibility**: Readable by most OSs and devices
- **Best for**: Cross-platform portable storage

#### NTFS
- First modern Microsoft file system for Windows servers
- **Compatibility**: Readable by most OSs
- **Features**: Advanced permissions, journaling

#### EXT4
- Latest Linux-based file system (after EXT2, EXT3)
- **Compatibility**: Readable by most Unix-like OSs
- **Features**: Improved performance, large file support

#### APFS (Apple File System)
- Apple's modern file system
- **Features**: Efficient, configurable
- **Compatibility**: Usually readable by Apple, has Linux modules

## Operating System Differences

### Unix-like Systems (macOS, Linux)

#### Drive Structure
- **Unified file system** with single root directory (/)
- Main OS volume at root
- Other devices in:
  - `/dev/` (device representation)
  - `/Volumes/` (mount points)
- **Example**: Flash drive "RWCred4" appears as:
  - Device: `/dev/disk4s1`
  - Mount point: `/Volumes/RWCred4`

#### File/Folder Characteristics
- **Case sensitivity**: Depends on drive configuration
- **Spaces in names**: Represented as "\ " in command line
- **Permission system**: owner-group-all read-write-execute
- **Graphical interface**: Finder (macOS)
- **CLI access**: Full visibility plus `su` (super user) privileges

#### Permission Format
```
- rwx rwx rwx
| ||| ||| |||
| ||| ||| ||+-- Execute (all users)
| ||| ||| |+--- Write (all users)
| ||| ||| +---- Read (all users)
| ||| ||+------ Execute (group)
| ||| |+------- Write (group)
| ||| +-------- Read (group)
| ||+---------- Execute (owner)
| |+----------- Write (owner)
| +------------ Read (owner)
+-------------- File type (- = file, d = directory)
```

### Windows Systems

#### Drive Structure
- **Explicit drive letters**: A:, B:, C:, D:, etc.
- **Historical**: A: and B: were floppy drives
- **Current**: C: onwards for hard drives and removable media
- **Network drives**: Also receive drive letters

#### File/Folder Characteristics
- **Path separators**: Backslash (\) vs forward slash (/) in Unix
- **Spaces in names**: Full name in quotations ("My file.txt")
- **Current directory**: C:text.txt (current directory of C:)
- **Root directory**: C:\text.txt (root of C: drive)
- **Security**: Access Control Lists (ACL) with granular permissions and inheritance

## Links and Shortcuts

### Unix-like Systems

#### Three Types of Links

**Aliases** (macOS Finder)
- Available through GUI only
- Simple shortcuts that update in real time
- Jump from one location to another

**Symbolic Links** (CLI only)
- Similar to aliases but CLI-based
- **Important limitation**: Don't update when target moves
- Can become "broken links"

**Hard Links** (CLI only)
- Create bound connection to original file
- **Key feature**: Cannot delete original while link exists
- Essentially additional name/reference to same file on disk

### Windows Systems

#### Two Main Types

**Shortcuts**
- Windows equivalent of macOS aliases
- Available through right-click menu
- Update when target moves

**Symbolic Links**
- Available through CLI (Command Prompt or PowerShell)
- Command: `New-Item -ItemType SymbolicLink -Path "Link" -Target "Target"`
- Similar functionality to Unix symbolic links

## Virtual Drives and Remote Access

### Virtual Drive Formats

#### ISO-9660
- **Standard format** for emulating CDs, DVDs, flash drives
- **Compatibility**: Automatically recognized by macOS and Windows
- **Usage**: Double-click to mount or right-click → mount
- **ISO**: International Standards Organization

#### DMG (Apple Disk Image)
- **Platform**: macOS specific
- **Function**: Similar to ISO images
- **Status**: Slightly outdated but still used

### File Transfer Protocol (FTP)

#### Basic Concepts
- **One of earliest internet services**
- **Purpose**: Exchange files between machines
- **Architecture**: Client-server model
- **Modern version**: SFTP (Secure FTP)

#### FTP Usage Methods
- **Command Line Interface (CLI)**
- **Graphical User Interface (GUI)**
- **Dedicated Applications**:
  - macOS: Transmit
  - Windows: WinSCP

#### Cloud Integration
- **Modern approach**: FTP web services
- **Examples**: Google Drive, OneDrive, Dropbox
- **Features**: 
  - Built-in visualization tools
  - Editing capabilities
  - File transfer between local and cloud
  - Cross-platform file system compatibility

## Practical Exercises

### Hands-on File Systems Exercise
1. Create folder "TestFolder" on local drive
2. Create text file "testfile" inside folder
3. Create desktop shortcut/alias to folder
4. Use CLI commands to navigate and modify files

### Permission Exercise
**Question**: What's the permission string for a regular f