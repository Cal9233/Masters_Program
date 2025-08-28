# HTML, CSS, and JavaScript Quiz Study Guide

## Question 1: HTML Hyperlink Target Attribute
**Which attribute is defined within a hyperlink HTML element to define the hyperlink to be opened in a new tab?**

**Answer:** target

*Usage: `<a href="url" target="_blank">Link</a>` - The `target` attribute with value `_blank` opens the link in a new tab.*

---

## Question 2: JavaScript Runtime Environments
**Statement:** Node, Deno, and Bun are Javascript Engines that power the Javascript Environment.

**Answer:** False

*Clarification: Node.js, Deno, and Bun are JavaScript **runtime environments**, not engines. They use JavaScript engines (like V8) but are not engines themselves. V8, SpiderMonkey, and JavaScriptCore are examples of JavaScript engines.*

---

## Question 3: Required HTML Image Element Properties
**Required properties in an image HTML element:**

- ✅ **alt** (alternative text for accessibility)
- ✅ **src** (source URL of the image)
- ❌ height (optional)
- ❌ width (optional)

*The `src` attribute specifies the image source, and `alt` provides alternative text for screen readers and when images fail to load.*

---

## Question 4: CSS Implementation Types
**The code snippet showing `<style>` tags in the HTML head is:**

**Answer:** Internal CSS

*CSS Implementation Types:*
- **Internal:** CSS within `<style>` tags in the HTML document
- **External:** CSS in separate .css files linked via `<link>` tag
- **Inline:** CSS directly in HTML elements via `style` attribute

---

## Question 5: Responsive CSS Units
**Responsive units for box model width property:**

- ✅ **%** (percentage - relative to parent element)
- ✅ **em** (relative to font size)
- ❌ px (pixels - absolute unit)
- ❌ in (inches - absolute unit)

*Responsive units scale with screen size or parent elements, while absolute units remain fixed.*

---

## Question 6: DOM Element Selection
**For the HTML element:** `<p class="not" id="message"> Click on the item </p>`

**Correct DOM call to change foreground color:**

**Answer:** `document.getElementById('message').style.color='red';`

*Key Points:*
- Use `getElementById()` to select by ID attribute
- The ID is "message", not the class "not"
- `getElementByTag()` is not a valid DOM method

---

## Question 7: Asynchronous Functions in JavaScript
**In JavaScript, an Asynchronous Function always returns a:**

**Answer:** Promise

*Async functions automatically wrap their return value in a Promise, even if you don't explicitly return a Promise.*

---

## Question 8: HTML Form Dropdown Element
**Which HTML element creates a dropdown selection menu?**

**Answer:** `<select>`

*Usage:*
```html
<select>
    <option value="option1">Option 1</option>
    <option value="option2">Option 2</option>
</select>
```

---

## Question 9: JavaScript Closure Definition
**What is it called when a function has access to variables from its outer scope even after the outer function has finished executing?**

**Answer:** Closure

*A closure gives you access to an outer function's scope from an inner function. The inner function will have access to the variables in the outer function scope, even after the outer function has returned.*

---

## Question 10: JavaScript HTTP Requests
**Which built-in JavaScript function allows you to perform a request to a RESTful web service?**

**Answer:** `fetch()`

*Example usage:*
```javascript
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data));
```

---

## Key Concepts Summary

### HTML Essentials
- `target="_blank"` for new tab links
- `alt` and `src` are required for `<img>` elements
- `<select>` creates dropdown menus

### CSS Fundamentals
- Internal CSS uses `<style>` tags
- Responsive units: %, em, rem, vw, vh
- Absolute units: px, pt, in, cm

### JavaScript Core Concepts
- Async functions return Promises
- Closures maintain access to outer scope
- `fetch()` for HTTP requests
- DOM manipulation with `getElementById()`

### Runtime vs Engine
- **Engines:** V8, SpiderMonkey, JavaScriptCore
- **Runtimes:** Node.js, Deno, Bun (use engines to execute code)