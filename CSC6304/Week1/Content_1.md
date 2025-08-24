# CSC 6304 - Advanced Programming Concepts
## Week 1: Git, Containers, and Software Methodologies

### Course Information
- **Professor:** Rob Sand
- **Institution:** Merrimack College
- **Course:** Advanced Programming Concepts
- **Contact:** sandro@merrimack.edu

## Course Format

### Schedule
- **Live Sessions:** Every Tuesday 6:30pm to 8:30pm (Zoom link in Main Menu)
- **Office Hours:** Every Thursday 6:30pm to 7:30pm (Zoom link in Main Menu)
- **Attendance:** Optional but strongly recommended

### Assessment Components
- **Quizzes:** Tuesday to Monday, 10 multiple choice questions, open book/notes
- **Project Assignments:** Programming tasks submitted on GitLab, due next Monday
- **Sprint Reviews:** Due after project completion
- **Final Exam:** 8 questions, 4 hours to complete, open book/notes, due last Saturday by 11:59PM

---

## Software Development Methodologies

Software projects follow different development methodologies based on company policy and project requirements focusing on:
- Speed
- Human resources
- Financial resources
- Reliability
- Target environment

### 1. Waterfall Methodology
**Best for:** Long-term or complex projects, government and defense systems, healthcare and engineering projects

**Characteristics:**
- Sequential phases: Requirement Analysis → Design → Implementation → Testing → Maintenance
- Each phase must be completed before moving to the next
- Detailed documentation at each stage
- Less flexibility for changes once project begins

### 2. Rapid Application Development (RAD)
**Best for:** Web and mobile app development, e-commerce and enterprise solutions, prototyping for innovation

**Characteristics:**
- Prototype cycles: Build → Demonstrate → Refine
- Focus on rapid prototyping and iterative development
- User feedback incorporated throughout development
- Faster time to market

### 3. DevOps
**Goal:** Integrate software development (Dev) with IT operations (Ops)

**Benefits:**
- Improves collaboration between development and operations teams
- Automates processes throughout the software development lifecycle
- Shortens development lifecycle
- Enables continuous integration and deployment

**Key Concepts:**
- **Continuous Integration:** Frequent code integration and automated testing
- **Continuous Deployment:** Automated deployment to production
- **Infrastructure as Code:** Managing infrastructure through code
- **Monitoring and Feedback:** Continuous monitoring of applications and infrastructure

### 4. Agile Methodology
**Core Principles:**
- Deliver working software frequently (1-4 week sprints)
- Embrace changing requirements, even late in development
- Foster daily collaboration between developers and business stakeholders

**Common Frameworks:**
- Scrum
- Kanban
- Extreme Programming (XP)
- Scaled Agile Framework (SAFe)

**Key Components:**

**Roles:**
- **Product Owner:** Defines requirements and priorities
- **Development Team:** Builds the software
- **Scrum Master:** Facilitates the process and removes obstacles

**Artifacts:**
- **Product Backlog:** Complete list of features and requirements
- **Sprint Backlog:** Items selected for current sprint
- **Increment:** Working software produced at end of sprint

**Events:**
- **Sprint Planning:** Plan work for upcoming sprint
- **Daily Stand-ups:** Brief daily progress meetings
- **Sprint Review:** Demonstrate completed work to stakeholders
- **Sprint Retrospective:** Team reflects on process improvements

---

## Docker Containerization

### What is Docker?
An open-source platform for developing, shipping, and running applications using containerization technology.

### Problems Docker Solves
- **Dependency Hell:** Consistent environment across different systems
- **"Works on My Machine" Problem:** Eliminates environment-specific issues
- **Simplified Deployment and Scaling:** Easy to deploy and scale applications
- **Development Workflow Improvements:** Streamlined development processes
- **Operational Benefits:** Reduced overhead compared to virtual machines
- **Cost and Time Savings:** Efficient resource utilization

### Containers vs. Virtual Machines
**Containers:**
- Share the host operating system kernel
- Lightweight and fast startup
- Isolated but share OS resources
- More efficient resource usage

**Virtual Machines:**
- Each VM has its own complete operating system
- Heavier resource requirements
- Slower startup times
- Complete isolation including OS

### Docker Architecture

**Client-Server Architecture:**
- **Client:** CLI tool, Docker Desktop
- **Server (Docker Daemon):** Runs in background, listens for API requests, manages Docker objects

**Docker Objects:**
- **Images:** Read-only templates with instructions for creating containers
- **Containers:** Runnable instances of images, isolated from other containers
- **Volumes:** Persistent data storage for containers (like file links)
- **Networks:** Enable container communication

### Docker Registry (Docker Hub)
- World's largest public registry for Docker images
- Cloud-based service for storing, sharing, and managing container images
- The "app store" for containerized applications

### Docker Networking
- **Outgoing:** Enabled automatically by default
- **Incoming:** Ports must be exposed and mapped to host
  - Example: `--p 8080:80` maps port 8080 on host to port 80 in container

### Essential Docker Commands

**Image Management:**
```bash
docker pull [image name]     # Download an image
docker images                # List local images
docker rmi [image id]        # Remove an image
docker build -t [tag] .      # Build image from Dockerfile
```

**Container Management:**
```bash
docker run [options] [image]        # Create and start container
docker ps                           # List running containers
docker stop [container id]          # Stop a container
docker rm [container id]            # Remove a container
docker exec -it [container] bash    # Execute commands in running container
```

### Docker Instructions Files

**Dockerfile:**
- Blueprint for building Docker images
- Contains setup instructions: get base images, set up volumes, copy files, run scripts
- The "DNA" of your image

**Docker Compose:**
- YAML file for defining and running multi-container applications
- Manages multiple containers as a single application
- Simplifies complex deployments

---

## Version Control with Git

### The Problem Without Version Control
```
project_final.doc
project_final_v2.doc
project_ACTUALLY_final.doc
project_final_final_USE_THIS_ONE.doc
```

### Benefits of Version Control
- Complete history of all changes
- Track who made what changes and when
- Ability to revert to any previous state
- Collaborative work without conflicts

### Brief History of Version Control

**First Generation (Local VCS):**
- RCS (Revision Control System) - 1980s
- Stored patches between file versions locally

**Second Generation (Centralized VCS):**
- CVS (1990), Subversion/SVN (2000)
- Central server model with single point of failure

**Third Generation (Distributed VCS):**
- **Git (2005)** - Created by Linus Torvalds for Linux kernel
- Mercurial, Bazaar
- Every copy is a complete repository

### Why Git Won

**Key Advantages:**
- **Speed:** Blazingly fast operations (most commands are local)
- **Distributed:** No single point of failure
- **Data Integrity:** Everything checksummed with SHA-1 hashes
- **Branching:** Lightweight, fast branch creation and merging
- **Staging Area:** Review changes before committing
- **Open Source:** Free and continuously improved

**Real-World Impact:**
- GitHub (2008) made Git accessible to millions
- Used by 95%+ of professional developers
- Essential for modern DevOps and CI/CD pipelines

### How Git Works: The Three Trees

```
Working Directory ——→ Staging Area ——→ Repository
   (modified)           (staged)         (committed)
```

**Workflow Commands:**
- `git status` - Check your changes
- `git add [file name]` - Track your changes
- `git commit -m "Message"` - Lock in your changes

### Basic Git Workflow

1. Initialize or clone a repository
2. Modify files in your working directory
3. Stage changes you want to commit
4. Commit staged changes to the repository
5. Push commits to remote repository (GitHub/GitLab)

```
[Working Dir] ——add——> [Staging] ——commit——> [Local Repo] ——push——> [Remote Repo]
```

### Creating Your First Repository

**Option 1: Initialize New Repository**
```bash
mkdir my-project
cd my-project
git init
```

**Option 2: Clone Existing Repository**
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### Essential Git Commands

**Checking Status:**
```bash
git status              # See which files are modified/staged
git status --short      # Compact output
```

**Staging Files:**
```bash
git add filename.txt    # Stage a specific file
git add folder/         # Stage all files in a folder
git add .              # Stage all changes in current directory
git add -A             # Stage all changes in entire repository
```

**Viewing Changes:**
```bash
git diff               # See unstaged changes
git diff --staged      # See staged changes
```

**Making Commits:**
```bash
git commit -m "Add user authentication feature"  # Commit with inline message
git commit                                       # Open editor for longer message
git commit -am "Fix bug and update docs"         # Stage all and commit
```

**Viewing History:**
```bash
git log                    # Full commit history
git log --oneline          # Compact history
git log --graph --oneline  # Visual branch history
```

**Undoing Changes:**
```bash
# Unstage changes
git reset HEAD filename.txt    # Unstage a specific file
git reset HEAD                # Unstage all files

# Discard working directory changes
git checkout -- filename.txt  # Restore file from last commit
git restore filename.txt       # Modern equivalent

# Undo commits
git revert HEAD                # Create new commit that undoes last commit
git reset --soft HEAD~1        # Undo last commit, keep changes staged
git reset --hard HEAD~1        # Undo last commit, discard changes (DANGEROUS!)
```

---

## GitLab Setup

### SSH Key Setup
1. Create private and public key pair in your `.ssh` folder
2. Upload public key to GitLab account
3. Configure SSH authentication for secure repository access

### Repository Setup
1. Create a repository on GitLab
2. Copy SSH link from repository
3. In local folder: `git clone [copied SSH link]`

### Issue Management with Commit Messages

GitLab recognizes specific keywords in commit messages that automatically close issues:

**Keywords:**
- Close, closes, closed
- Fix, fixes, fixed
- Implement, implements, implemented

**Examples:**
```bash
git commit -m "Fix user authentication bug Closes #123"
git commit -m "Add new payment gateway Fixes #456, #789"
git commit -m "Resolve database connection issues Resolved #321"
```

---

## Week 1 Tasks

### Assignments
- [ ] Complete Project #1
- [ ] Complete Sprint Review/Retrospective

### Study Tips for Exam
1. Understand the differences between software methodologies and when to use each
2. Know Docker architecture components and basic commands
3. Understand Git workflow and essential commands
4. Practice GitLab setup and SSH configuration
5. Review Agile components (roles, artifacts, events)
6. Understand the evolution of version control systems

---

## Additional Resources
- **Communication:** sandro@merrimack.edu
- **Zoom Sessions:** Available in Main Menu
- **Repository Submissions:** GitLab platform
- **Documentation:** Course materials and slides