# CSC 6303 Week 8 Study Notes: Multi-threading, Parallelization, and Scheduling

## Overview
This week covers advanced operating system concepts focusing on how systems handle multiple tasks simultaneously through concurrency, parallelism, and process scheduling.

---

## Part 1: Multi-threading and Parallelization

### Historical Context
- **Concurrency**: Introduced in the 1970s
  - Managing multiple tasks that run in **overlapping time periods**
  - Existed even before multi-core processors
  - Tasks don't run simultaneously but appear to through time-slicing

- **Parallelism**: Evolution of concurrency with multi-core architectures
  - Tasks run **simultaneously** on multiple cores
  - True parallel execution rather than just overlapping time periods

### Key Distinction
> **"With one processor, you have concurrency. With more than one, you have parallelism."**

---

## Concurrency Fundamentals

### Definition
- **Concurrency**: Multiple tasks running in overlapping time periods
- Tasks are managed so they don't interfere with each other
- Operating system switches between tasks rapidly (time-slicing)

### Examples of Concurrent vs Sequential Tasks

#### Sequential Task Example: Factorial Calculation
```python
def factorial(n):
    ans = 1
    for i in range(n):
        ans *= i+1
    return ans
```
- **Problem**: Each iteration depends on the previous result
- **Cannot be parallelized** - must compute sequentially

#### Concurrent Task Example: Matrix Multiplication
```python
def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                ans[i][j] += A[i][k] * B[k][j]
    return ans
```
- **Advantage**: Each element `ans[i][j]` can be computed independently
- **Can be parallelized** - elements computed in any order or simultaneously

### Real-World Concurrency Example
**Scenario**: Matrix elements come from remote data server
- Data arrives at different times
- Start all n × m tasks concurrently
- Complete tasks as data becomes available
- More efficient than waiting for sequential data delivery

---

## Advantages of Concurrency

### For I/O-Bound Programs
- **Problem**: I/O operations are extremely slow compared to CPU processing
- **Solution**: Overlap I/O waiting times
- **Example**: While waiting for file read, CPU can work on other tasks

### For CPU-Bound Programs
- **Context**: Your program competes with other programs for OS scheduling
- **Solution**: Create more threads = more competitive for CPU execution slots
- **Advantage**: Better performance on multi-core machines

### Multi-core Machine Definition
> A computer with a processor containing multiple cores/processing units within a single chip. Each core can independently execute instructions, allowing multiple tasks or threads to be processed simultaneously.

---

## Concurrency in Python

### Threading Library
```python
import threading
import requests

def download(url):
    print(f"Downloading {url}")
    resp = requests.get(url)
    print(f"Finished {url}: {len(resp.content)} bytes")

urls = ['http://example.com', 'http://example.org']
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

**Key Features**:
- Creates lightweight threads
- Tasks run seemingly at the same time
- Especially useful for I/O-bound tasks
- **Example use case**: Download multiple web pages concurrently instead of sequentially

---

## Parallelism

### Definition
- Tasks that can be executed **in any order** become candidates for parallel execution
- Requires multiple processors/cores for true parallelism
- Focus on **fork** (what can be parallelized) and **join** (what needs synchronization)

### Fork-Join Model
- **Fork**: Split tasks that can run independently
- **Join**: Synchronize results when tasks complete
- **Master Thread**: Coordinates parallel tasks

### Key Principle
> **"If you have multiple tasks running at the same (parallel) or overlapping (concurrent) time, one task cannot rely on the output of another"**

---

## Parallelism in Python

### Multiprocessing Library
```python
import multiprocessing as mp

def square(n):
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    with mp.Pool(mp.cpu_count()) as p:
        result = p.map(square, numbers)
    print(result)
```

**Key Features**:
- **`Pool(mp.cpu_count())`**: Creates worker processes equal to CPU cores
- **`map()` method**: Distributes tasks across the pool
- **Forking**: Launches threads using specified function and parameters
- **Joining**: Collects results when tasks complete
- **Best for**: CPU-bound tasks utilizing multiple CPU cores

### Advanced Example: Parallel Image Processing
```python
from multiprocessing import Pool
from PIL import Image, ImageFilter
import os

def process_image(path):
    img = Image.open(path)
    img = img.filter(ImageFilter.CONTOUR)
    img.save("processed_" + os.path.basename(path))

image_paths = ['img1.jpg', 'img2.jpg', 'img3.jpg']
with Pool() as pool:
    pool.map(process_image, image_paths)
```

**Advantages**:
- Each image processed on separate CPU core
- Much faster than sequential processing
- Equivalent to for loop but utilizes multiple cores

---

## Concurrency vs Parallelism Summary

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| **Hardware** | Single processor | Multiple processors/cores |
| **Execution** | Overlapping time periods | Simultaneous execution |
| **Task Management** | Time-slicing/context switching | Distributed across cores |
| **Best For** | I/O-bound tasks | CPU-bound tasks |
| **Python Library** | `threading` | `multiprocessing` |

### Visual Understanding
- **Concurrency**: One CPU rapidly switching between tasks
- **Parallelism**: Multiple CPUs each handling different tasks simultaneously

---

## Part 2: Scheduling

### Operating System Role
- **Core Function**: OS manages multiple programs (processes) running simultaneously
- **Challenge**: How does an OS do more than one thing at a time?
- **Solution**: Process scheduling combined with multithreading, concurrency, and parallelism

### Job Scheduler Fundamentals
- **Process**: Every running program becomes a process under OS management
- **PID**: Process ID - unique number assigned to each process
- **Competition**: Processes compete for execution slots to become "alive"
- **Distribution**: In multi-core machines, tasks distributed across cores

---

## Process Management

### Checking Process Status

#### Unix/Linux Systems
```bash
# Real-time process monitoring
top

# List current processes
ps

# Process information includes:
# - PID (Process ID)
# - CPU usage
# - Memory usage  
# - Process state
# - Command/program name
```

#### Process Information Display
- **Load Average**: System utilization over time
- **CPU Usage**: Percentage of CPU time used
- **Memory**: Physical and virtual memory usage
- **Process State**: Running, sleeping, stopped, zombie

### Process Control Operations
Once you know a process PID, you can:
- **Remove/Kill processes**: `kill PID`
- **Change priority levels**: `nice`, `renice`
- **Monitor resource usage**: CPU, memory consumption
- **Control process execution**: pause, resume, terminate

### Multi-core Process Distribution
- **Single-core**: All processes share one execution line
- **Multi-core**: Each core has dedicated processing line
- **Load balancing**: OS distributes processes across available cores
- **Scheduling algorithms**: OS decides which processes run when and where

---

## Key Concepts for Exam

### Essential Differences
1. **Concurrency vs Parallelism**
   - Concurrency: Overlapping execution on single processor
   - Parallelism: Simultaneous execution on multiple processors

2. **I/O-bound vs CPU-bound Tasks**
   - I/O-bound: Benefits from threading (overlapping wait times)
   - CPU-bound: Benefits from multiprocessing (multiple cores)

3. **Python Libraries**
   - `threading`: For concurrency, I/O-bound tasks
   - `multiprocessing`: For parallelism, CPU-bound tasks

### Process Management
- **PID**: Process identification number
- **Job Scheduler**: OS component managing process execution
- **Process States**: Running, waiting, sleeping, terminated
- **Commands**: `top`, `ps` for monitoring processes

### Programming Considerations
- **Task Independence**: Parallel tasks cannot depend on each other's output
- **Synchronization**: Use join operations to collect results
- **Resource Management**: Consider CPU cores, memory, and I/O resources

---

## Final Exam Preparation Topics

### Code Translation/Adaptation
- Be able to write concurrent/parallel versions of sequential algorithms
- Understand when tasks can be parallelized vs when they must be sequential
- Practice with threading and multiprocessing examples

### Conceptual Understanding
- Explain difference between concurrency and parallelism
- Describe advantages of each approach
- Identify appropriate use cases for threading vs multiprocessing

### Operating Systems Knowledge
- Understand process scheduling concepts
- Know how to monitor and control processes
- Explain how multi-core systems handle parallel execution

### Practical Skills
- Use `top` and `ps` commands
- Understand process states and resource usage
- Know how to terminate or modify process priorities

---

## Study Tips

1. **Practice Examples**: Try converting sequential algorithms to parallel versions
2. **Understand Dependencies**: Identify which tasks can run independently
3. **Library Usage**: Know when to use threading vs multiprocessing
4. **Process Management**: Practice using system commands to monitor processes
5. **Real-world Applications**: Think about practical uses of concurrency and parallelism

Remember: The key insight is that concurrency and parallelism are fundamental to how operating systems work - they're not just programming techniques, but core OS implementation strategies.