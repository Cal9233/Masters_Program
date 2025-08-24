# CSC 6304 Week 4: JavaScript Study Guide

## Course Information
- **Course**: Advanced Programming Concepts
- **Professor**: Rob Sand
- **Institution**: Merrimack College
- **Topic**: Code development for web-based applications using JavaScript (JS)

## Table of Contents
1. [JavaScript Overview](#javascript-overview)
2. [JavaScript Architecture](#javascript-architecture)
3. [JavaScript Environment vs Engine](#javascript-environment-vs-engine)
4. [Browser vs Server Environments](#browser-vs-server-environments)
5. [JavaScript Language Features](#javascript-language-features)
6. [Function Execution](#function-execution)
7. [Asynchronous JavaScript](#asynchronous-javascript)
8. [DOM Manipulation](#dom-manipulation)
9. [Event Listeners](#event-listeners)
10. [Common Pitfalls](#common-pitfalls)

## JavaScript Overview

### Key Facts
- **Created**: 1995 by Brendan Eich (in just 10 days!)
- **Original Purpose**: Scripting language for web browsers
- **Current Use**: Both client-side and server-side development
- **Core Web Technology**: One of three (HTML, CSS, JavaScript)

### JavaScript's Unique Position
- Only mainstream language that runs natively in browsers (WASM still uses JS for certain features)
- Same language for both client and server (full-stack development)
- Engines constantly improving performance
- Environments expanding capabilities
- Unified language = reduced context switching for developers

## JavaScript Architecture

### Two Main Components
1. **JavaScript Engine**: Core component that executes JavaScript code
2. **JavaScript Environment**: Context and APIs that JavaScript can access

**Analogy**: 
- Engine = Car engine (provides power)
- Environment = Complete vehicle (determines how power is used)

### Key Point
The same engine can be used in different environments:
- V8 powers both Chrome (browser) and Node.js (server)
- Different capabilities depending on the environment

## JavaScript Environment vs Engine

### The JavaScript Environment
- Context in which JavaScript code runs
- Provides access to APIs beyond core language features
- Determines what global objects are available
- Manages the event loop for asynchronous operations
- **Examples**: Browser, Node.js, Bun, and Deno

### The JavaScript Engine
- Core program that executes JavaScript code
- Converts human-readable code into optimized machine code
- Handles memory management (garbage collection)
- Follows ECMAScript specifications
- **Examples**: V8, SpiderMonkey, JavaScriptCore

### How JavaScript Engine Works
1. **Parsing**: Convert code to Abstract Syntax Tree (AST)
2. **Compilation**: Translate to bytecode/machine code using JIT compilation
3. **Optimization**: Apply runtime performance improvements
4. **Execution**: Run the actual code instructions
5. **Garbage Collection**: Manage memory automatically

## Browser vs Server Environments

### Browser Environment
- **Global Object**: `window`
- **DOM API**: Document manipulation
- **Web APIs**: fetch, localStorage, geolocation, etc.
- **Event-driven**: User interactions, timers
- **Security**: Same-origin policy, sandboxing

#### Browser Environment Components
- Contains JS Engine (different browsers have different JS engines)
- **Event Loop**: Continuously checks call stack and queues to make asynchronous JavaScript performant
- **APIs**: (Described by WebIDL) Browser functionality like XHR, Timeouts, Timers, DOM manipulation
- **Manages Queues**: (For Asynchronous JS) Micro-task queue/Priority and Task/Callback queue

### Server Environment
- **Global Object**: `global`
- **File System Access**: Read/write files
- **Network APIs**: Create servers, make requests
- **Module System**: CommonJS, ES modules
- **Process Control**: Access OS-level information

#### Server Environment Components
- Contains Engine (Most use V8, Bun uses JSCore)
- **Event Loop**: Manages I/O operations, threading, etc. (Node: LibUV, Bun: epoll/kqueue, Deno: Tokio Rust Async Runtime)
- **APIs**: (Managed by LibUV and Underlying OS) Network request, Timers, File system manipulation
- **Manages Task Queues**: Micro-task queue and Callback queue (setImmediate not available in browser or Deno)

### Code Example Differences
```javascript
// Browser: This works
document.getElementById('myElement').innerHTML = 'Hello!';
// Node.js: This fails (no document object)

// Instead, Node.js provides:
const fs = require('fs');
fs.writeFileSync('hello.txt', 'Hello!');
```

## JavaScript Language Features

### Key Characteristics
- **Prototype Based Language**
- **Variable Passing**: Primitive variables passed as value but Objects and Arrays passed by reference
- **Synchronous Thread of Execution**
- **Uses Environment APIs to become Asynchronous**
- **This keyword** (nuances)

## Function Execution

### 3 Main Components
1. **Global Memory** a.k.a "The Heap"
2. **Thread of Execution** (Context)
3. **The Callstack**

## Asynchronous JavaScript

### Event Loop Components
JavaScript uses APIs of its current environment:
1. **Event Loop**
2. **Task Queue** (Callback Queue)
3. **Microtask Queue** (Job Queue) - **Priority!!**

### Async/Await
- Uses Promises to keep the thread of execution open and asynchronous (non-blocking)
- Two ways to write code that both return promises (preferential)
- Async function always returns a Promise

#### Promise-based Approach (.then)
```javascript
fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    displayWeather(data);
    console.log("Called Display Weather");
  })
  .catch(function (error) {
    console.log(error);
  });
```

#### Async/Await Approach
```javascript
async function getWeatherAwait(office, gridX, gridY) {
  let url = "url here"
  
  let response = await fetch(url);
  let data = await response.json();
  console.log("Displaying Data Now...");
  return displayWeather(data); 
}
```
**Note**: Uses a generator function under the hood but still operates the same way as .then async function

### Queue Priority Example
```javascript
console.log('start');
setTimeout(() => {
  console.log('task 1');
  Promise.resolve().then(() => console.log('microtask in task'));
}, 0);
Promise.resolve().then(() => {
  console.log('microtask 1');
  Promise.resolve().then(() => console.log('nested microtask'));
});
console.log('end');

// Output:
// start
// end
// microtask 1
// nested microtask
// task 1
```

## DOM Manipulation

### Creating and Adding Elements
```javascript
// Create a New DOM Node
let newDiv = document.createElement('div'); 

// Get reference to an existing DOM Element
let main = document.getElementById('main'); 

// Add newly created Element to Existing Element
main.appendChild(newDiv);
```

**Important**: Just creating the DOM element is not enough. You must append the element to the DOM.

## Event Listeners

### Adding Event Listeners
```javascript
// Add event listener to the new div
newDiv.addEventListener('click', function() {
  console.log('Div was clicked!');
});

// Global event listener. Fires when any element is clicked.
window.addEventListener('click', (event) => {
  console.log('Clicked element:', event.target);
  // event.target shows what was actually clicked
});
```

## Common Pitfalls - Things to Watch Out For!

### Type Coercion Surprises
- `"5" + 3 = "53"` but `"5" - 3 = 2`

### Variable Hoisting
- Variables declared with `var` are "hoisted" to top of scope but only declarations not assignments

### Floating Point Math Precision
- `0.1 + 0.2 !== 0.3`

### Pass by Reference vs Value
- Primitive variables passed by value but objects and arrays are passed by reference

## Weekly Assignments
- Complete Project #4 on GitLab
- Take the quiz until next Monday
- Complete Sprint Review

## Next Week Preview
JavaScript Frameworks

---

*Study tip: Focus on understanding the relationship between JavaScript engines and environments, as well as the asynchronous execution model with event loops and queues.*