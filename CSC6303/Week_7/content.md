# CSC 6303 Week 7 Study Notes: Virtual Machines and Operating Systems

## Overview
Week 7 covers Virtual Machines (VMs) and major Operating Systems (Linux, MacOS, Windows), focusing on virtualization principles, practical VM implementation, and OS characteristics.

---

## Virtual Machines (VMs)

### Historical Context
- **Past:** You bought hardware, then chose software including the OS
- **Late 1980s/Early 1990s:** Machines began coming with pre-installed OS
- **Present:** VMs allow us to return to choosing OS for our hardware
- **Key Principle:** "All machines are hardware, but all we actually use is software"

### VM Definition
**A Virtual Machine (VM) is a software-based computer that:**
- Acts like a physical computer
- Runs on a physical computer (Host Machine)
- Has its own operating system, storage, networking, and configuration settings
- Is separate from the physical computer it's running on
- Can run programs/applications, various operating systems, store data, and connect to networks

### VM Architecture
```
VM1, VM2, VM3, VMn (Guest OS)
         ↓
Virtualization Software (Hypervisor)
         ↓
Physical Host (Host OS)
         ↓
Physical Hardware (CPU-RAM-DISK-NIC)
```

### How VMs Work
- **VM application acts as a translator**
- Allows another OS to run and execute apps designed for it
- Your native OS grants access to applications designed for your OS
- Cannot grant access to applications not designed for your OS (different protocols)
- VM bridges this compatibility gap

---

## Hypervisor Types

### Type 1 (Bare-metal)
| Aspect | Details |
|--------|---------|
| **Location** | Runs directly on hardware |
| **Performance** | High (closer to hardware) |
| **Use Case** | Data centers, servers |
| **Examples** | VMware ESXi, Microsoft Hyper-V |

### Type 2 (Hosted)  
| Aspect | Details |
|--------|---------|
| **Location** | Runs on top of an OS |
| **Performance** | Slower (extra OS layer) |
| **Use Case** | Personal computers, testing |
| **Examples** | VirtualBox, VMware Workstation |

---

## Virtual Machines vs Containers

### Virtual Machines
- Run a full operating system
- Use hypervisor for virtualization
- Better for running multiple OS types
- **Analogy:** Like separate houses in a neighborhood

### Containers
- Share the host OS kernel
- Use container runtime (like Docker) for isolation
- Lighter and faster than VMs
- Ideal for fast, scalable app deployment on same OS
- **Analogy:** Like rooms within a single house

---

## Types of Virtual Machine Solutions

### Traditional Virtual Machine Apps
**Local virtualization on your hardware:**
- Oracle's VirtualBox
- Parallels
- VMware's Desktop products

### Cloud-Based Virtual Machines
**Remote virtualization through browser:**
- Microsoft's Azure
- Amazon's AWS
- Paperspace's Gradient
- Google's Colab

---

## Oracle VirtualBox

### Key Features
- **Free software standard**
- **Cross-platform:** Install and run any major OS
- **Terminology:**
  - **Host OS:** Your native OS
  - **Guest OS:** OS installed on the virtual machine

### Common Issues and Solutions

#### Mouse Cursor Release
- **Mac:** Left Command key (left of space bar)
- **PC (Windows/Linux):** Right Shift key (right of question mark)

#### Screen Resolution
- Change resolution in guest OS, VirtualBox will adjust

#### Installation Tips
- **Windows 11 on Intel Mac:** Turn off EFI option
- **macOS on PC:** May need keyboard adjustment in VirtualBox
- **Important:** Remember main user name and password
- **Performance:** VMs may be extremely slow - be patient

---

## Google Colab

### Overview
- **Cloud-based VM service** by Google
- **Free tier** available for simple programs
- **Default Guest OS:** Linux
- **Integration:** Access to Google Drive files
- **Requirements:** Google account (Gmail or institutional)

### Use Cases
- Alternative to local VM installation
- Particularly useful for MacOS M1/M2 users (VirtualBox installation challenges)
- Python programming environment
- Machine learning and data science projects

---

## Operating System Examples

### Professional Requirement
**"A Computer Scientist cannot say I don't know an OS, just like a chef cannot say I don't know a kitchen."**

- All programming languages can complete similar tasks, but some are better suited for certain tasks
- Same principle applies to Operating Systems
- CS professionals should be able to work with MacOS, Windows, or Linux
- Good developers should be able to develop for any OS

---

## Linux (Ubuntu)

### Overview
- **Not a single OS** but a family of open-source OS
- **Distribution covered:** Ubuntu Desktop 22.04.02
- **Philosophy:** Open-source, community-driven

### Key Features
- **Terminal access:** Click app menu at bottom-left corner
- **Version check:** `cat /etc/os-release`
- **Native browser:** Firefox
- **File manager:** File app
- **Productivity suite:** LibreOffice (alternative to Microsoft Office)
- **Settings:** Accessible through app menu
- **Gaming:** Try Mahjongg game

### Terminal Commands
```bash
# Check OS version
cat /etc/os-release

# Access applications through app menu
# Terminal, Firefox, File manager, Settings all accessible
```

---

## Windows

### Overview
- **Proprietary OS family** by Microsoft
- **Current editions:**
  - Windows 11 (personal use)
  - Windows 11 Enterprise (business features)
  - Windows Server 2022 (enterprise-level server management)

### Key Features
- **Terminal:** PowerShell (access through main menu)
- **Version check:** `C:\Windows\System32\systeminfo`
- **Native browser:** Edge
- **Settings:** Accessible through main menu

### PowerShell Commands
```powershell
# Check system information
C:\Windows\System32\systeminfo

# Access PowerShell through Start Menu search
```

---

## MacOS

### Overview
- **Apple's proprietary OS** with multiple versions
- **Unix-based system** (since macOS X in 2001)
- **Current version:** macOS 14 Sequoia (2024)
- **Previous versions:** macOS 13 Ventura (2022), macOS 12 Monterey (2021)

### Key Features
- **Terminal access:** Applications → Utilities → Terminal
- **Version check:** `sw_vers` command
- **Native browser:** Safari
- **File manager:** Finder
- **Settings:** Through Applications folder

### Terminal Commands
```bash
# Check macOS version
sw_vers

# Access through Applications/Utilities/Terminal
```

---

## Other Operating Systems

### Mobile Operating Systems
- iOS (Apple)
- watchOS (Apple)
- Android (Google)
- Mobile Linux
- Windows 11 Mobile

### Less Popular Desktop Options
- **ChromeOS:** Free OS by Google, available for desktop/laptop installation
- **Solaris:** By Oracle (originally Sun Microsystems), Unix-like OS for servers

### Professional Standards
- CS professionals should work comfortably with MacOS, Windows, and Linux
- Good developers should be able to develop for any OS
- Cross-platform competency is essential in modern computing

---

## Week 7 Assignments

### Discussion Post (In-Class Exercise Grade)
**Topic:** VirtualBox Installation Experience

**Options:**
- **Preferred:** Download and install VirtualBox, share experience
- **Alternative:** Create Google Colab account for remote VM access

**Discussion points:**
- Installation success/challenges
- Installation time
- Common uses for VM applications
- Why people need/use VMs
- Previous VM experience

**Due dates:**
- Post by Friday
- Reply to 2 peers by Monday

### Programming Project #7 (Coding Projects Grade)

#### VirtualBox Option
**Requirements:**
1. Install VirtualBox on your machine
2. Install Linux Ubuntu VM in VirtualBox
3. Install VSCode in Ubuntu
4. Run provided Python code (Module 7 OS Discovery Python Code)

**Screenshot must show:**
- Ubuntu VM running successfully
- Host machine OS visible in background
- VSCode running on Ubuntu VM
- Python code output
- OS clearly stated in terminal
- Your name somewhere on screen

#### Google Colab Alternative
**For users with installation issues (especially M1/M2 Mac users):**
1. Create Google Colab account
2. Run Module 7 OS Discovery Python Code
3. Alternative: Use different VM provider (AWS)

### Quiz #3 (Quizzes Grade)
**Coverage:** Weeks 5, 6, and 7 content
**Format:**
- 10 questions
- Not timed
- Open notes (consult slide materials)
- One submission only
- Must be your own work

**Due:** Monday 11:59 PM

---

## Key Concepts for Exam Preparation

### Virtual Machine Fundamentals
1. **Definition and purpose** of VMs
2. **Hypervisor types** (Type 1 vs Type 2)
3. **VMs vs Containers** comparison
4. **Host vs Guest OS** terminology
5. **Use cases** for virtualization

### Operating System Knowledge
1. **Terminal/command line access** for each OS
2. **Version checking commands** for Linux, Windows, macOS
3. **Native applications** (browsers, file managers)
4. **Professional requirements** for OS competency

### Practical Skills
1. **VirtualBox installation** and configuration
2. **Common troubleshooting** issues
3. **VM performance** considerations
4. **Cloud vs local** virtualization options

### Study Tips
- Practice VM installation and configuration
- Memorize version checking commands for each OS
- Understand the analogy: VMs = separate houses, Containers = rooms in house
- Know the difference between Type 1 and Type 2 hypervisors
- Understand when to use VMs vs containers vs native installation

### Important Commands to Remember
```bash
# Linux version check
cat /etc/os-release

# macOS version check  
sw_vers

# Windows system info
C:\Windows\System32\systeminfo
```

This knowledge forms the foundation for understanding modern computing environments and virtualization technologies essential for systems programming and IT infrastructure management.