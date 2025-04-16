### Dom Manipulation

## window

window is an object representing the entire window that has methods for dom manipulation.
Good practice to have is to first load all contents of html before incorporating javascript logic, using "DOMContentLoaded" in event listener.
"DOMContentLoaded" waits for the browser to load the DOM tree.
Ex.
//script.js
window.addEventListener("DOMContentLoaded", main); // main function is just a function with all logic we'd want

You can also use "Load", this is similar only it also waits to load all css style sheets and images.
Ex.
//script.js
window.addEventListener("load", main);

You can do this in html instead to make it look better and less crowded with the "defer" attribute in the script tag
Ex:

<script src="script.js" defer></script>

## document

document is an object representing the DOM tree, which contains functions for interactions within the DOM.

# JavaScript Document Object Cheat Sheet

## Selection Methods

| Method                         | Description                                            | When to Use                                                    |
| ------------------------------ | ------------------------------------------------------ | -------------------------------------------------------------- |
| `getElementById(id)`           | Returns element with matching ID                       | When you need a single specific element with a unique ID       |
| `getElementsByClassName(name)` | Returns HTMLCollection of elements with matching class | When you need all elements with a specific class               |
| `getElementsByTagName(name)`   | Returns HTMLCollection of elements with matching tag   | When you need all elements of a specific type (e.g., all divs) |
| `querySelector(selector)`      | Returns first element matching CSS selector            | When you need one element using CSS selector syntax            |
| `querySelectorAll(selector)`   | Returns NodeList of elements matching CSS selector     | When you need all elements matching a CSS selector             |

## Element Creation and Modification

| Method/Property                        | Description                     | When to Use                                          |
| -------------------------------------- | ------------------------------- | ---------------------------------------------------- |
| `createElement(tagName)`               | Creates a new HTML element      | When dynamically adding new elements to the page     |
| `createTextNode(text)`                 | Creates a text node             | When adding pure text content to an element          |
| `appendChild(node)`                    | Adds a node as the last child   | When adding an element inside another element        |
| `removeChild(node)`                    | Removes a child node            | When removing an element from the DOM                |
| `replaceChild(newNode, oldNode)`       | Replaces a child node           | When swapping one element for another                |
| `insertBefore(newNode, referenceNode)` | Inserts before a reference node | When adding an element at a specific position        |
| `cloneNode(deep)`                      | Clones an element               | When duplicating elements (true to include children) |

## HTML Content Manipulation

| Property      | Description                                 | When to Use                                          |
| ------------- | ------------------------------------------- | ---------------------------------------------------- |
| `innerHTML`   | Gets/sets HTML content of element           | When changing multiple elements or HTML structure    |
| `innerText`   | Gets/sets visible text content              | When working with only the visible text              |
| `textContent` | Gets/sets text content                      | When working with all text including hidden elements |
| `outerHTML`   | Gets/sets HTML including the element itself | When replacing an element completely                 |

## Attributes and Properties

| Method/Property             | Description                          | When to Use                             |
| --------------------------- | ------------------------------------ | --------------------------------------- |
| `getAttribute(name)`        | Gets attribute value                 | When reading HTML attributes            |
| `setAttribute(name, value)` | Sets attribute value                 | When setting HTML attributes            |
| `removeAttribute(name)`     | Removes an attribute                 | When removing HTML attributes           |
| `hasAttribute(name)`        | Checks if attribute exists           | When testing for presence of attributes |
| `dataset`                   | Access to all custom data attributes | When working with data-\* attributes    |

## CSS and Styling

| Property/Method             | Description                    | When to Use                                        |
| --------------------------- | ------------------------------ | -------------------------------------------------- |
| `style`                     | Direct access to inline styles | For quick style changes to individual elements     |
| `classList`                 | List of classes (with methods) | For adding, removing, or toggling classes          |
| `classList.add(class)`      | Adds a class                   | When adding a CSS class to an element              |
| `classList.remove(class)`   | Removes a class                | When removing a CSS class                          |
| `classList.toggle(class)`   | Toggles a class                | When switching a class on/off                      |
| `classList.contains(class)` | Checks if class exists         | When checking if an element has a class            |
| `getComputedStyle(element)` | Gets all applied styles        | When you need the actual computed styles after CSS |

## Document Information and Metadata

| Property/Method            | Description         | When to Use                               |
| -------------------------- | ------------------- | ----------------------------------------- |
| `document.title`           | Page title          | When reading or changing the page title   |
| `document.URL`             | Complete URL        | When you need the current page URL        |
| `document.domain`          | Domain name         | When working across subdomains            |
| `document.documentElement` | Root element (html) | When accessing the top-level HTML element |
| `document.head`            | Head element        | When accessing the document head          |
| `document.body`            | Body element        | When accessing the document body          |
| `document.cookie`          | Document cookies    | When reading or setting cookies           |
| `document.readyState`      | Loading state       | When checking if document is fully loaded |

## Events

| Method/Property                                    | Description            | When to Use                                       |
| -------------------------------------------------- | ---------------------- | ------------------------------------------------- |
| `addEventListener(event, function, useCapture)`    | Adds event listener    | For handling user interactions or document events |
| `removeEventListener(event, function, useCapture)` | Removes event listener | When cleaning up event handlers                   |
| `dispatchEvent(event)`                             | Triggers an event      | When programmatically firing events               |
| `document.createEvent(type)`                       | Creates custom event   | When creating custom events                       |
| `document.onload`                                  | Page load event        | When running code after page loads                |
| `document.onreadystatechange`                      | Ready state change     | When monitoring document loading status           |

## Navigation and Location

| Method/Property     | Description                | When to Use                         |
| ------------------- | -------------------------- | ----------------------------------- |
| `document.location` | Current URL info           | When working with the page URL      |
| `document.referrer` | URL of referring page      | When tracking where users came from |
| `document.baseURI`  | Base URI for relative URLs | When resolving relative URLs        |
| `document.links`    | All links in document      | When working with all page links    |
| `document.images`   | All images in document     | When working with all page images   |
| `document.forms`    | All forms in document      | When accessing all forms on a page  |

## Document Structure and Traversal

| Property                 | Description              | When to Use                                        |
| ------------------------ | ------------------------ | -------------------------------------------------- |
| `parentNode`             | Parent of node           | When accessing parent element                      |
| `childNodes`             | All child nodes          | When accessing all children (including text nodes) |
| `children`               | Element children         | When accessing only element children               |
| `firstChild`             | First child node         | When accessing first child (may be text node)      |
| `lastChild`              | Last child node          | When accessing last child                          |
| `nextSibling`            | Next sibling node        | When accessing next adjacent node                  |
| `previousSibling`        | Previous sibling node    | When accessing previous adjacent node              |
| `firstElementChild`      | First element child      | When accessing first element child                 |
| `lastElementChild`       | Last element child       | When accessing last element child                  |
| `nextElementSibling`     | Next element sibling     | When accessing next element (skips text nodes)     |
| `previousElementSibling` | Previous element sibling | When accessing previous element                    |

## Focus and Selection

| Method/Property           | Description                  | When to Use                               |
| ------------------------- | ---------------------------- | ----------------------------------------- |
| `document.activeElement`  | Currently focused element    | When determining which element has focus  |
| `document.hasFocus()`     | Checks if document has focus | When checking if document is in focus     |
| `element.focus()`         | Sets focus to element        | When programmatically focusing an element |
| `element.blur()`          | Removes focus from element   | When removing focus from an element       |
| `document.getSelection()` | Gets current selection       | When working with user text selection     |

## Document Fragment

| Method                     | Description                              | When to Use                                      |
| -------------------------- | ---------------------------------------- | ------------------------------------------------ |
| `createDocumentFragment()` | Creates a lightweight document container | For batch DOM operations with better performance |

## Useful Measurements

| Property/Method                    | Description                 | When to Use                               |
| ---------------------------------- | --------------------------- | ----------------------------------------- |
| `element.getBoundingClientRect()`  | Element size and position   | When you need precise positioning info    |
| `element.clientWidth/clientHeight` | Element inner dimensions    | When measuring visible content area       |
| `element.offsetWidth/offsetHeight` | Element outer dimensions    | When measuring element with borders       |
| `element.scrollWidth/scrollHeight` | Scrollable dimensions       | When measuring content including overflow |
| `element.scrollLeft/scrollTop`     | Scroll position             | When getting or setting scroll position   |
| `element.offsetParent`             | Closest positioned ancestor | When finding positioning context          |

## Common Events

| Event                 | Triggered When                   |
| --------------------- | -------------------------------- |
| `click`               | Element is clicked               |
| `dblclick`            | Element is double-clicked        |
| `mousedown/mouseup`   | Mouse button is pressed/released |
| `mouseover/mouseout`  | Mouse enters/leaves an element   |
| `mousemove`           | Mouse is moved over element      |
| `keydown/keyup`       | Keyboard key is pressed/released |
| `focus/blur`          | Element gains/loses focus        |
| `input`               | Input value changes              |
| `change`              | Element value changes (on blur)  |
| `submit`              | Form is submitted                |
| `load`                | Resource has loaded              |
| `DOMContentLoaded`    | HTML is loaded and parsed        |
| `resize`              | Window is resized                |
| `scroll`              | Element is scrolled              |
| `touchstart/touchend` | Touch begins/ends on mobile      |
