# CSC 6303 Week 5 Study Notes: Operating Systems Basic Concepts and Organization

## Course Overview
- **Course**: CSC 6303 Systems & Languages Survey - Week 5
- **Instructor**: Maggie Mulhall
- **Institution**: Merrimack College
- **Focus**: Operating systems fundamentals and command line interfaces

---

## What is an Operating System?

### Definition
**"An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs."**

### Key Characteristics
- **Basic program**: Runs continuously from computer startup
- **First contact**: Users interact with computers through the OS
- **Universal presence**: Found in all devices (computers, phones, TV sets, etc.)
- **Historical continuity**: Been essential since 1950s computers

### Fundamental Question
**"Is a device defined by the hardware or by the software?"**
- The OS often defines the user experience more than hardware

---

## Operating System History

### Early Computing (Pre-1950s)
- **No OS existed**: Computers used simple resident monitors
- **Resident Monitor**: Simple loader program that would:
  - Load a single task into memory
  - Execute it
  - Stop
  - Require manual intervention for next task

### Birth of OS Concept (Late 1950s)
- **Innovation**: Single program capable of continuously loading and starting user-defined programs
- **Environment**: All computers were mainframes controlled by terminals
- **Interface**: Only command line interfaces (CLI) available

### Evolution to Personal Computers
- **User-friendly shift**: CLI became too burdensome for general users
- **Two main paths**:
  - **Microsoft**: DOS → Windows
  - **Academic/Research**: Unix → Linux and macOS

### Important Technical Note
**OS code is written in high-level languages (like C or C++) that are compiled into machine code - not written directly in machine code.**

---

## OS Basic Concepts and Organization

### Hardware Management
An OS manages both **peripherals** and **internal units**:

#### Peripherals (External Hardware)
- **Input devices**: keyboard, mouse, trackpad, camera
- **Output devices**: display, printer, speakers
- **Bi-directional**: external hard drives, network adapters, USB flash drives

#### Internal Units (Internal Hardware)
- **Processing unit management**: CPUs and cores
- **Thread management**: mono and multi-core threading
- **Memory hierarchy**: including memory virtualization

### OS Architecture

#### Two Main Components:

##### 1. The Kernel
**Core responsibilities**:
- CPU (cores) scheduling
- Memory hierarchy management
- File system management
- Calls to hardware drivers

##### 2. Hardware Drivers
**Functions**:
- Interface with peripherals
- Often developed by peripheral manufacturers
- Default options come with OS

### System Layer Diagram
```
Users
↕
Applications
↕
The OS Kernel
↕
The OS Drivers
↕
Hardware
```

---

## Command Line Interface (CLI)

### Definition and Purpose
- **CLI**: Text-based interface for interacting with the OS
- **Alternative to GUI**: More efficient for systematic actions
- **Professional necessity**: Essential for CS professionals
- **Remote access**: Sometimes the only option for remote systems

### Key Advantages
- **Automation**: Can automate repetitive tasks
- **Bypass limitations**: Can bypass certain GUI restrictions
- **Speed**: Faster for systematic operations
- **Scripting**: Enables powerful script creation

### Shell Concept
**"sh" refers to both the shell itself and the scripting language used within that shell**

---

## Accessing CLI

### Unix-based Systems (Linux/macOS)
- **Access method**: Terminal native program
- **macOS specific**: Applications → Utilities → Terminal app
- **Shell type**: Usually bash (Bourne Again Shell)

### Windows Systems
- **Legacy option**: Command Line Prompt (old systems)
- **Modern option**: PowerShell (since 2022)
- **Current access**: Terminal app can host command-line interface

---

## Shell Scripting Languages

### Unix/Linux/macOS: bash (Bourne Again Shell)

#### Historical Context
- **Bourne Shell**: Original CLI for Unix-like OS
- **bash**: Enhanced version by Brian Fox
- **Name joke**: "Bourne Again Shell" (play on "born again")
- **Purpose**: Access to core OS services, especially file system

#### Essential bash Commands
| Command | Purpose |
|---------|---------|
| `cd <destination>` | Navigate to folder |
| `pwd` | Display current directory |
| `ls` | List directory contents |
| `ls -lag` | Detailed directory listing |
| `cat <file>` | Display file contents |
| `cp <source> <dest>` | Copy file |
| `mv <source> <dest>` | Move/rename file |
| `mkdir <name>` | Create directory |
| `rm <file>` | Delete file |
| `man <command>` | Display manual for command |

#### bash Scripting Syntax
- **Variables**: `$<variable>` to reference content
- **Input**: `read <variable>`
- **Output**: `echo "<text>"`
- **Conditionals**: `if [ <condition> ] then <commands> else <commands> fi`
- **Directory check**: `-d "<name>"` checks if directory exists
- **Redirection**: `>` to save output to file

### Windows: PowerShell

#### Key Characteristics
- **Dual nature**: Both command-line shell and scripting language
- **Purpose**: Automating system administration tasks
- **Architecture**: Higher-level abstraction using Cmdlets
- **Compatibility**: Offers both Unix-like and legacy MS-DOS commands

#### PowerShell Command Aliases
- **Unix-like**: cat, cd, clear, cp, echo, ls, mv, pwd, rm
- **Legacy MS-DOS**: gc, chdir, clr, copy, echo, dir, move, gl, del

#### PowerShell Syntax
- **Variables**: `$<variable> = Read-Host -Prompt <msg>`
- **Conditionals**: `if ( <condition> ) { <commands> } else { <commands> }`
- **Output**: `Write-Host "<msg>"`
- **Create items**: `New-Item <name> -ItemType <Directory or File>`

---

## System Calls from High-Level Languages

### Universal Availability
**All programming languages offer system calls**

### Implementation Examples

#### Python
```python
import os
os.system("<command and parameters>")
```

#### C++
```cpp
#include <stdlib.h> // or <cstdlib>
int system("<command and parameters>")
// Returns 0 for successful execution
```

#### Go
```go
import "os/exec"
var <variable> = exec.Command(<command name>, arg1, arg2)
// Returns command output to variable
```

### Important Consideration
**Careful with subtle differences between OSs!**

---

## Practical CLI Exercise

### Basic File Operations
1. **Open terminal/command prompt**
2. **Create directory**: `mkdir QuickTest` (or `md QuickTest` on Windows)
3. **Navigate**: `cd QuickTest`
4. **Create file**: 
   - Unix/macOS: `touch testfile.txt`
   - Windows: `type nul > testfile.txt`
5. **List contents**: `ls` (Unix/macOS) or `dir` (Windows)
6. **Delete file**: `rm testfile.txt` (Unix/macOS) or `del testfile.txt` (Windows)

---

## Study Tips for Exam

### Key Concepts to Memorize
1. **OS Definition**: System software managing hardware, software resources, and common services
2. **Historical progression**: Resident monitor → OS concept → Modern OS
3. **Architecture**: Kernel + Drivers structure
4. **CLI advantages**: Automation, efficiency, remote access capability
5. **Shell types**: bash (Unix-like) vs PowerShell (Windows)

### Command Comparison Chart
| Function | bash (Unix/macOS) | PowerShell (Windows) | Legacy Windows |
|----------|-------------------|---------------------|----------------|
| List files | `ls` | `ls` or `dir` | `dir` |
| Change directory | `cd` | `cd` | `cd` |
| Copy file | `cp` | `cp` or `copy` | `copy` |
| Display file | `cat` | `cat` or `gc` | `type` |
| Create directory | `mkdir` | `mkdir` or `md` | `md` |

### System Calls Pattern
```
High-level Language → System Call → OS → Hardware
```

### Critical Understanding Points
- **OS as intermediary**: Between applications and hardware
- **Driver importance**: Specialized software for hardware communication
- **CLI persistence**: Despite GUI dominance, CLI remains essential
- **Cross-platform awareness**: Commands vary between systems
- **Automation power**: Scripts can automate complex task sequences

---

## Week 5 Assignment Tasks

### Discussion Post
**Topic**: Common uses of shell script language
- **Questions to address**:
  - Who uses shell scripts?
  - Common applications?
  - Personal likelihood of using them?
  - Technical rationale for usage

### Programming Project #5
**Task**: Python program with system calls
- **Requirements**:
  - Ask user for folder name
  - Check if folder exists (using system calls)
  - Remove and recreate if exists
  - Generate 100 random numbers (0-1000)
  - Save to "numbers100.txt" in created folder
- **Key requirement**: Must use system calls to OS
- **Documentation**: Include name and OS version tested

---

## Important Notes for Exam
- **Historical context**: Understanding the evolution from resident monitors to modern OS
- **Architecture clarity**: Distinguish between kernel and driver responsibilities
- **CLI vs GUI**: When and why to use command line interfaces
- **Cross-platform differences**: Awareness of Unix vs Windows command variations
- **System integration**: How high-level languages interact with OS through system calls

The material emphasizes practical skills while building theoretical understanding of how operating systems manage computer resources and provide interfaces for user interaction.