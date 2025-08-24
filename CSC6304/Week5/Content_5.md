# CSC 6304 Week 5 - JavaScript Build Tools and Frameworks

## Overview

**Course:** CSC 6304 - Advanced Programming Concepts  
**Professor:** Rob Sand  
**Topic:** JavaScript Build Tools and Frameworks

## JavaScript Evolution

### Early JavaScript Challenges

JavaScript initially faced numerous problems that led to the development of modern tools and frameworks:

#### Browser and Development Issues
- **Browser Compatibility Nightmares** - Inconsistent implementations across browsers
- **Verbose DOM Manipulation** - Complex code required for simple operations
- **Event Handling Inconsistencies** - Different approaches needed per browser
- **Ajax Complexity** - Difficult asynchronous JavaScript and XML handling
- **Limited CSS Selector Support** - Basic querying capabilities
- **Animation Difficulties** - Manual timing and state management
- **No Built-in Utilities** - Lack of standard helper functions

#### State Management Problems
- **No Standardized Patterns** - No consistent approach to managing state
- **Global Variables Scattered** - State spread throughout codebase
- **State Stored in DOM Elements** - Mixing data with presentation
- **Closures in Various Models** - Inconsistent encapsulation patterns
- **Ad Hoc Object Properties** - Unstructured data organization

#### UI Update Challenges
- **Imperative UI Updates** - Manual specification of every UI change step
- **Scattered DOM Manipulation** - No centralized update logic
- **No Clear Data-UI Relationship** - Tight coupling between data and presentation
- **Manual Synchronization** - Manual coordination between state and display
- **Difficulty Testing** - Hard to test imperative code
- **Performance Issues** - Inefficient DOM operations

### Early Solutions

#### Browser Detection
```javascript
if (navigator.userAgent.indexOf('MSIE') > -1) {
    // Internet Explorer specific code
} else if (navigator.userAgent.indexOf('Firefox') > -1) {
    // Firefox specific code
}
```

#### Cross-Browser AJAX
Complex XMLHttpRequest handling with fallbacks for Internet Explorer using ActiveXObject.

#### DOM Manipulation Utilities
Custom functions for common operations like `getElementsByClass`, `hasClass`, and `addClass`.

#### Animation Functions
Manual animation using `setTimeout` and opacity calculations.

### jQuery Revolution (2006)

jQuery became the standard library addressing cross-browser issues:

```javascript
// DOM Manipulation
$('.menu-item').addClass('active').show();

// AJAX Requests
$.get('/api/users', function(data) {
    updateUserList(data);
});

// Event Handling
$('#button').on('click', function() {
    alert('Clicked!');
});

// Animation
$('#modal').fadeOut(300);
```

**jQuery Benefits:**
- Unified API for cross-browser compatibility
- Simplified DOM manipulation and traversal
- Easy event handling and AJAX
- Built-in animations
- **Limitation:** Still not ideal for state management

## Module Systems Evolution

### CommonJS (2009)

- **Originally called ServerJS**
- **Purpose:** Module system for JavaScript on server and native applications
- **Limitation:** Cannot run in browser without transpilation
- **Loading:** Synchronous module loading (blocks thread)
- **Browser Solution:** Browserify enabled CommonJS in browsers

#### CommonJS Syntax
```javascript
// CommonJS way
const fs = require('fs'); // synchronous
fs.readFileSync('./file.txt');

// Dynamic import way 
const { default: fs } = await import('fs'); // asynchronous
fs.readFileSync('./file.txt');
```

### Node.js Impact (2009)

- **Creator:** Ryan Dahl
- **Introduced at:** JS Conf
- **Module System:** Originally CommonJS (now also supports ESM)
- **Impact:** Allowed JavaScript to run on servers
- **Result:** Made CommonJS mainstream

### ECmaScript Modules - ESM (ES2015)

- **Introduction:** ES6/ES2015
- **Syntax:** Import/Export statements
- **Compatibility:** Works in both server and browser
- **Loading:** Asynchronous module loading
- **Feature:** Commonly used with destructuring

#### ESM Syntax
```javascript
// Named imports use destructuring-like syntax
import { useState, useEffect } from 'react';

// Import everything
import * as React from 'react';

// Default imports (no destructuring)
import React from 'react';
```

### Destructuring (ES2015)

**Purpose:** Unpacks values from multiple JavaScript properties into distinct variables

```javascript
// Object destructuring
const person = { name: 'John', age: 30 };
const { name, age } = person;

// Array destructuring
const numbers = [1, 2, 3];
const [first, second] = numbers;
```

### NPM - Node Package Manager (2010)

- **Purpose:** Default package manager for Node.js
- **Functions:** Install, update, delete, and manage JavaScript libraries
- **Interface:** Convenient CLI tool
- **Scope:** Used beyond Node - build tools, frameworks, etc.

## JavaScript Build Tools

### Definition
Software that automates the process of transforming, optimizing, and preparing JavaScript code for production use.

### Build Tool Categories

#### Transpilers
- **Purpose:** Translate code between programming languages or versions
- **Use Cases:**
  - **Compatibility:** Use new features before widespread support
  - **Developer Experience:** Write in convenient syntax (CoffeeScript, TypeScript)
  - **Migration:** Gradually move between languages/versions
  - **Optimization:** Transform for better performance or smaller size

#### Common Transpilers
- **Same Language, Different Versions:**
  - Babel: ES2015+ JavaScript → ES5 JavaScript
  - TypeScript: TypeScript → JavaScript
- **Different Languages:**
  - CoffeeScript → JavaScript (Ruby-like syntax)
  - Sass/SCSS → CSS
  - JSX → JavaScript

#### Bundlers
- **Combine multiple files** into optimized builds with tree shaking and minification
- **Resolve dependencies** and create dependency graphs
- **Apply transpilers** during the build process
- **Generate source maps** for debugging
- **Manage code splitting** for performance
- **Provide development features** like hot reloading

#### Build Tools Evolution

**Older Tools:**
- Grunt
- Gulp  
- Browserify

**Newer Tools:**
- Webpack
- Vite
- EsBuild
- SWC

## JavaScript Frameworks

### Libraries vs Frameworks

#### Libraries
- Collection of pre-written functions and utilities
- **You control the flow** and decide when to use functionality
- **Example:** You call library functions when needed

#### Frameworks
- Structured foundation providing overall application architecture
- **Framework controls the flow** and calls your code at specific points
- **Example:** Framework defines when and how your code runs

### Framework Types

#### Component Frameworks
Handle component-based development:
- **Component Lifecycle:** Mount, update, destroy phases
- **Reactive State Management:** Automatic UI updates when data changes
- **Event Handling:** Declarative event binding
- **DOM Updates:** Efficient rendering and re-rendering

**Examples:**
- Angular.js
- React.js
- Vue.js
- Svelte.js
- Solid.js
- Preact.js

#### Application Frameworks
Provide full application development solutions:
- **File-based Routing:** Convention-based navigation
- **Server-side Rendering (SSR):** Pre-rendered HTML
- **API Routes:** Backend functionality
- **Build Optimization:** Production-ready builds
- **Deployment Adapters:** Platform-specific deployment (Vercel, Cloudflare, Netlify, AWS)

**Examples:**
- Angular Universal, Nx, Scully
- Next, Remix, Gatsby
- Nuxt, Quasar
- SvelteKit
- Solid Start
- Fresh (Deno)

## Framework Evolution

### AngularJS (2010)
- **Creator:** Misko Hevery (Google)
- **Innovation:** First major frontend framework
- **Architecture:** MVC/MVVM pattern
- **Benefits:**
  - Structured approach to frontend applications
  - Clear separation of concerns
  - Testable code structure
  - Organized large applications
  - Two-way data binding

### React.js (2013)
- **Talk:** "React: Rethinking Best Practices" - Pete Hunt
- **Innovation:** Virtual DOM (VDOM)
- **Key Concepts:**
  - **Declarative UI:** Describe what you want, not how to get there
  - **Component-Based:** Encapsulated, reusable pieces
  - **Unidirectional Data Flow:** Data flows down, events flow up
  - **Reconciliation:** Smart diffing algorithm for efficient updates
  - **JSX:** HTML-like syntax in JavaScript

## JavaScript Rendering Approaches

### Server-Side Rendering (SSR)

**Process:**
1. Browser requests page
2. Server runs JavaScript to generate full HTML
3. Server sends complete HTML to browser
4. Browser displays content immediately
5. JavaScript "hydrates" to make it interactive

**Benefits:** Fast initial page load, SEO-friendly, works without JavaScript

### Client-Side Rendering (CSR)

**Process:**
1. Browser requests page
2. Server sends minimal HTML + JavaScript bundle
3. Browser downloads, parses, and executes JavaScript
4. JavaScript creates DOM and renders page
5. JavaScript makes API calls for data
6. Component re-renders with actual data
7. User sees final content

**Benefits:** Rich interactivity, smooth navigation after initial load

### Hybrid Approaches

#### Island Architecture
- **Concept:** Interactive components (islands) surrounded by static HTML (ocean)
- **Benefit:** Only ship JavaScript for parts needing interactivity
- **Pioneer:** Astro framework

#### Qwik.js - O(1) Rendering
- **Creator:** Misko Hevery (Angular.js creator)
- **Innovation:** Serialized JavaScript into HTML on server
- **Goal:** Constant-time page loading regardless of app size

**Traditional Framework (O(n)):**
1. Download bundle.js (500KB)
2. Parse entire bundle
3. Initialize all components ← O(n) cost
4. Attach all event listeners
5. Page becomes interactive

**Qwik (O(constant)):**
1. HTML arrives (already interactive)
2. Load qwik-core.js (1KB) ← O(1) cost
3. Page immediately interactive
4. Load specific chunks on interaction ← O(1) cost

## Project Requirements

### Week 5 Project Tasks

1. **Setup Framework Project**
   - Create local repository
   - Initialize project with chosen framework

2. **Rebuild Weather Application**
   - Convert existing weather app to use framework
   - Implement component-based architecture

3. **Enhanced Functionality**
   - Add latitude/longitude input fetching
   - Implement Navigator Geolocation for user location
   - Auto-detect user's weather

4. **Deployment Setup**
   - Configure `.gitlab-ci.yml` for GitLab Pages
   - Ensure proper hosting configuration

5. **Sprint Review**
   - Complete `SprintReview.md` documentation

### Demo Command
```bash
npm create vite@latest week-5 -- --template react
```

### Development Workflow
1. Install node packages
2. Run in development mode
3. Build for production
4. Deploy to GitLab Pages

## Key Takeaways for Exam

### Evolution Timeline
- **Early JavaScript (1990s-2000s):** Browser compatibility issues, manual DOM manipulation
- **jQuery Era (2006):** Simplified cross-browser development
- **Module Systems (2009-2015):** CommonJS, Node.js, ESM
- **Build Tools:** From Grunt/Gulp to Webpack/Vite
- **Framework Revolution:** Angular → React → Modern frameworks

### Important Concepts
- **Transpilation:** Source-to-source code translation
- **Bundling:** Combining and optimizing multiple files
- **Component Architecture:** Reusable, encapsulated UI pieces
- **State Management:** Reactive data handling
- **Rendering Strategies:** SSR vs CSR vs Hybrid approaches

### Performance Considerations
- **Bundle Size:** Impact on initial load time
- **Code Splitting:** Load only necessary code
- **Tree Shaking:** Remove unused code
- **Hydration:** Making server-rendered content interactive
- **O(1) vs O(n):** Qwik's constant-time rendering approach

## Study Resources

- [The 7 Levels of JavaScript Modules](reference-link-from-slide)
- [What Serverside JavaScript Needs (2009)](reference-link-from-slide)
- [React: Rethinking Best Practices - Pete Hunt (2013)](reference-link-from-slide)

## Course Reminders

### Week 5 Deliverables
- Complete Project #5 on GitLab
- Complete Sprint Review

### Next Week
- **Topic:** Native Mobile Applications