# Mobile Development and Web Technologies Quiz Study Guide

## Question 1: SDK Definition
**What does SDK stand for in mobile development context?**

**Answer:** Software Development Kit

*An SDK provides developers with tools, libraries, documentation, code samples, and guides to build applications for a specific platform.*

---

## Question 2: Geolocation API Functions
**Match each function with when it executes:**

```javascript
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        function (position) { funcA(position); },
        function (e) { funcB(e) },
        { enableHighAccuracy: true }
    );
} else {
    funcC()
}
```

- **funcA()** → Executed when the geolocation request is answered and **allowed** (success callback)
- **funcB()** → Executed when the geolocation request is answered but **denied** (error callback)  
- **funcC()** → Executed when the geolocation API is **not supported** by the browser

---

## Question 3: Native App Performance
**Statement:** Native apps are built specifically for a platform (iOS or Android) and can directly access device hardware and APIs, resulting in faster execution and better performance.

**Answer:** True

*Native apps have direct access to platform-specific APIs and hardware, leading to superior performance compared to web or hybrid apps.*

---

## Question 4: Virtual DOM Pioneer
**The framework that made the Virtual DOM mainstream was:**

**Answer:** React

*React popularized the Virtual DOM concept, which creates a virtual representation of the DOM in memory for efficient updates.*

---

## Question 5: Web vs Native App Security
**Statement:** Web applications generally offer stronger security protections than native applications.

**Answer:** False

*Native applications typically have stronger security protections due to platform-level security measures, app store review processes, and controlled distribution channels.*

---

## Question 6: Server Side Rendering (SSR) Process
**Correct order of SSR steps:**

1. **Browser requests page**
2. **Server runs JavaScript to generate full HTML**
3. **Server sends complete HTML to browser**
4. **Browser displays content immediately**
5. **JavaScript "hydrates" to make it interactive**

*SSR pre-renders content on the server, sending complete HTML for immediate display, then adds interactivity through hydration.*

---

## Question 7: Transpiler Definition
**Statement:** A transpiler is a tool that translates code written in one programming language into binary code.

**Answer:** False

*A transpiler translates code from one high-level language to another high-level language (e.g., TypeScript to JavaScript), not to binary code. Compilers translate to binary/machine code.*

---

## Question 8: JavaScript Destructuring
**The code example shows:**

```javascript
const person = { name: 'John', age: 30 };
const { name, age } = person;
const numbers = [1, 2, 3];
const [first, second] = numbers;
```

**Answer:** Destructuring

*Destructuring allows unpacking values from arrays or properties from objects into distinct variables.*

---

## Question 9: TypeScript to JavaScript Conversion
**Converting code from TypeScript to JavaScript is an example of:**

**Answer:** Transpiling

*Transpiling converts source code from one language to another at the same abstraction level (high-level to high-level).*

---

## Question 10: Platform-Specific Technologies
**Match technologies to their platforms:**

### iOS Technologies:
- ✅ **UI Kit** (iOS UI framework)
- ✅ **Xcode** (iOS development IDE)
- ✅ **App Store** (iOS app distribution)
- ✅ **Swift UI** (modern iOS UI framework)

### Android Technologies:
- ✅ **Jetpack Compose** (Android UI toolkit)
- ✅ **Play Store** (Android app distribution)
- ✅ **Android Studio** (Android development IDE)
- ✅ **Kotlin** (preferred Android programming language)

### Cross-Platform/Web:
- **Vue** (JavaScript framework)
- **React** (JavaScript framework)

---

## Key Concepts Summary

### Mobile Development Terms
- **SDK:** Software Development Kit - tools for building apps
- **Native Apps:** Platform-specific apps with direct hardware access
- **Transpiling:** Converting between high-level languages

### Web Technologies
- **Virtual DOM:** In-memory representation for efficient UI updates
- **SSR:** Server-side rendering for faster initial page loads
- **Destructuring:** Extracting values from objects/arrays into variables

### Development Processes
- **Geolocation API:** Requires user permission, has success/error callbacks
- **Hydration:** Adding interactivity to server-rendered content

### Security Hierarchy
Native Apps > Web Apps (generally, due to platform controls and review processes)