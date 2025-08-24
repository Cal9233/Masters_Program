# CSC 6304 Week 3: Web Browser Rendering, HTML & CSS Study Guide

## Course Information
- **Course**: Advanced Programming Concepts
- **Professor**: Rob Sand
- **Institution**: Merrimack College
- **Topic**: Web Browser Rendering, HTML and CSS, responsive web design

## Table of Contents
1. [The World Wide Web](#the-world-wide-web)
2. [Web Browsers](#web-browsers)
3. [Rendering Engines](#rendering-engines)
4. [DOM and CSSOM](#dom-and-cssom)
5. [Web Interface Definition Language (IDL)](#web-interface-definition-language-idl)
6. [HTML Basics](#html-basics)
7. [CSS Fundamentals](#css-fundamentals)
8. [CSS Specificity](#css-specificity)
9. [CSS Box Model](#css-box-model)
10. [Responsive Web Design](#responsive-web-design)
11. [Modern CSS Layouts](#modern-css-layouts)
12. [CSS Variables and Animations](#css-variables-and-animations)
13. [GitLab Pages Deployment](#gitlab-pages-deployment)

## The World Wide Web

### Historical Evolution

#### Hypertext (1960s-1980s)
- Text displayed on a computer with references (hyperlinks) to other text
- **Non-linear reading** - jump between documents
- **Ted Nelson's Xanadu project** - early academic systems
- **Core concept**: documents can reference each other

#### Hypermedia (1980s)
- **Hypertext + multimedia** (images, audio, video)
- Links can connect not just text, but any media type
- Examples: HyperCard (Apple), early CD-ROM encyclopedias
- Rich, interconnected media experiences

#### HTTP and HTML (1990)
**HTTP (HyperText Transfer Protocol)**:
- Protocol to request and transfer HTML documents over networks
- Standardized way for computers to ask for and receive hypermedia
- The "delivery system" for HTML
- The communication rules that make the web work

**HTML (HyperText Markup Language)**:
- Specific markup language to create hypertext/hypermedia documents
- Standardized way to structure content and define links
- The "document format" for Tim's web vision
- The actual syntax for creating linked documents

**Creator**: Tim Berners-Lee (1990)

## Web Browsers

### What is a Browser?
- **Application primarily written in C++**
- **Main functionality**: Fetch, Interpret, Display and Interact with web documents
- **Interface** between humans and the web
- Companies realized the power that the web browser held

### Components of a Browser
- **Rendering Engine** (Layout Engine)
- **JavaScript Engine**
- **User Interface** (UI)
- **Data Storage**
- **Security Manager**
- **Plugin/Extension System**
- **APIs** to connect everything

### Browser History Timeline
- **WorldWideWeb (1990)** - Created by Tim Berners-Lee
- **Mosaic Web Browser (1993)** - Developers broke off to form Netscape
- **Netscape Navigator (1994)** - Ease of use, 96% market share by 1996

## Rendering Engines

### Historical Rendering Engines
- **Mosaic/Spyglass** - One of the earliest graphical web browsers (NCSA, 1993). Microsoft licensed this for Internet Explorer
- **Trident** - Developed by Microsoft for IE4 (1997). Dominant during IE's peak
- **KHTML** - Developed by KDE project for Konqueror (late 1990s). Foundation for WebKit
- **Presto** - Opera's proprietary engine (2003-2013), then switched to WebKit/Blink

### The Big 3 Modern Engines
1. **WebKit** - Apple forked KDE's KHTML in 2001. Used by Safari, Mail, App Store
2. **Blink** - Developed by Google. Used in Chrome, Microsoft Edge (Chromium), Opera
3. **Gecko** - Created by Netscape, used by Mozilla Firefox (development began 1997)

### Key Functions
- **Responsible for rendering HTML and CSS**
- **Creating DOM and CSSOM**
- **Painting pixels on screen**
- Can make sites look different in different browsers
- **WebIDL standardization** has improved cross-browser consistency

### Important Note
**On iOS devices, all browsers must use WebKit (except in EU)**

## DOM and CSSOM

### DOM - Document Object Model
- **API** that represents and interacts with markup-based languages
- **Node tree** created by the browser where each node represents part of the document
- **Allows code** in a browser to access and interact with the browser

### CSSOM - CSS Object Model
- **Set of APIs and tree-like representation** of all CSS styles associated with a web document
- **Represents CSS as structured tree** where styles are organized hierarchically
- **Crucial for rendering** - handles everything from basic styling to complex responsive designs, animations, and layout calculations

## Web Interface Definition Language (IDL)

### Purpose
- **Describes data types, interfaces, methods, properties** of browser components
- **Independent** of specific web programming language
- **Defines exactly** what types are expected and returned
- **Browser vendors don't need** to hand-write JavaScript↔C++ translation code

## HTML Basics

### Overview
- **HyperText Markup Language** - basic technology for the World Wide Web
- **Markup language** like XML, LaTeX - defines control tags for text interpretation
- **Usually employed with CSS**
- **Living standard** managed by W3C Web HyperText Application Technology Working Group (WHATWG)

### Document Structure
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page title</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Header level 1</h1>
    <p>A paragraph</p>
    <em>Emphasis - italic</em>
    <strong>Strong - bold</strong>
  </body>
</html>
```

#### Key Elements
- **DOCTYPE** - what kind of page
- **`<html>`** - the main envelope
- **`<head>`** - meta information
  - **`<title>`** - page title
  - **`<meta>`** - meta definitions
- **`<body>`** - page contents

### Attributes
- **Additional values** that configure elements or adjust their behavior
- **Global Attributes**: `class`, `id`
- **Element Specific**: `accept` for `<form>` and `<input>`

### Hyperlinks
```html
<a href="https://example.com" target="_blank">Link Text</a>
```

#### Link Targets
- **`_self`** - default, open in same tab
- **`_blank`** - open in new tab/page
- **`_parent`** - open in parent frame
- **`_top`** - open in full body of window

### Images
```html
<img src="image.jpg" width="100px" alt="Description">
```

#### Key Points
- **`src` attribute** - image source
- **`alt` attribute** - textual replacement (mandatory, crucial for accessibility)
- **Size considerations**: Dimension (width/height - beware of ratio), Resolution (density of pixels)

#### Supported Image Formats
- **APNG** - Good for lossless animation sequences
- **AVIF** - Good for both images and animated images (high performance)
- **GIF** - Good for simple images and animations
- **JPEG** - Good for lossy compression of still images (most popular)
- **PNG** - Good for lossless compression (slightly better quality than JPEG)
- **SVG** - Vector format, scalable at different sizes
- **WebP** - Excellent for both images and animated images

### Interactive Elements (Without JavaScript)
- **Navigation Links**: `<a href="...">` 
- **Area Elements** in image maps
- **Form Elements**: Submission, Input Fields, Buttons, Dropdowns, Radio buttons, Checkboxes, File uploads
- **Media Elements** - Audio/Video controls
- **Modal Dialogs**
- **Tab index navigation**
- **CSS-only interactions**: `:hover` menus, `:target` tabs
- **Tooltips** (using title attribute)
- **Auto-scrolling** with fragment identifiers (#section-id)

## CSS Fundamentals

### Overview
- **Cascading Style Sheets** - language to describe presentation of markup documents
- **Describes how elements should be rendered** on screen, paper, speech, or other media

### Three Ways to Apply CSS

#### 1. Inline
```html
<h1 style="color: red;">The Lists - Our Program</h1>
```

#### 2. Internal
```html
<head>
  <style>
    h1 { color: red; }
  </style>
</head>
```

#### 3. External
```html
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
```

## CSS Specificity

### Definition
**The algorithm used by the browser** to determine which CSS declaration is most relevant to an element

### Selector Weight Categories (Decreasing Specificity)
1. **Inline Style**: `<div style="color:blue">` - **1,0,0,0**
2. **ID**: `#exampleID` - **1,0,0**
3. **Class**: `.exampleClass`, attribute selectors `[type="radio"]`, pseudo-class `:hover` - **0,1,0**
4. **Type**: `p`, `h1`, `div`, pseudo-elements `::before`, `::placeholder` - **0,0,1**

## CSS Box Model

### Components
- **Content** - The rectangle containing all pixels of an element (width and height)
- **Padding** - Space between content and border
- **Border** - Space taken by border pixels
- **Margin** - Space outside the border

### The `<div>` Element
- **Primary wrapper/container element**
- Foundation for layout and styling

## Responsive Web Design

### Viewport Setup
- **Automatically resize** properly defined web pages based on device size

### Responsive vs Non-Responsive Units

#### Non-Responsive Unit
- **`px`** - pixels (fixed size)

#### Responsive Units
- **`em`** - relative to font size
- **`%`** - percentage of parent element
- **`vh`** - relative to 1% of viewport height
- **`vw`** - relative to 1% of viewport width

### Responsive Properties
- **`width`**, **`height`**, **`min-width`**, **`max-width`**
- **Applicable to all elements** using the box model (boxes, images, etc.)

### CSS Float Property
- **Stacks elements side by side** rather than beneath each other
```css
#image { 
  float: right;
  margin: 0 0 5px;
  border: 1px solid #000000;
}
```

## Modern CSS Layouts

### Flexbox Layout (Flexible Box)
- **W3C Recommendation** as of October 2017
- **Efficient layout and space distribution** for dynamic content
- **Direction Agnostic** - unlike traditional block/inline layouts
- **Dynamic Behavior** - automatically adjusts item sizes

```css
{
  display: flex;
  width: 100%;
  height: 100vh;
  align-items: center;
  justify-content: center;
  text-align: center;
}
```

### CSS Grid Layout
- **Two-dimensional layout system** for complex layouts
- **Divides page into rows and columns**

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr 100px; /* 3 columns */
  grid-template-rows: 100px 200px; /* 2 rows */
}
```

### Key Difference
- **Flexbox** = One-dimensional (either row OR column)
- **Grid** = Two-dimensional (rows AND columns simultaneously)

### Using Flexbox and Grid Together
- **Does Grid Replace Flexbox? Not quite.**
- They complement each other for different layout needs

## CSS Variables and Animations

### CSS Variables (Custom Properties)
- **Store values** that you can reuse throughout your stylesheet
- **Think of them as containers** for colors, sizes, or any CSS value

### CSS Animations
- **Gradually change CSS properties over time**
- **Smooth transitions** between different states
- **Benefits**:
  - **Performance** - Hardware accelerated
  - **No Dependencies** - Pure CSS, works everywhere
  - **Declarative** - Describe what you want, CSS handles how
  - **Flexible** - Control timing, direction, repetition

## GitLab Pages Deployment

### Setup Process
1. **Turn on CI/CD setting**
2. **Settings → General → Visibility, project features, permissions → Repository → CI/CD**
3. **Build → Pipelines → New Pipeline**

## Weekly Assignments
- Complete Project #3
- Complete Sprint Review
- All due Monday by 11:59 pm

---

## The Evolution of CSS
- **CSS 1.0 (1996)** - Basic styling
- **CSS 2.0 (1998)** - Positioning
- **CSS 2.1 (2004)** - `!important`
- **CSS3 (2010+)** - Rounded corners
- **Flexbox (2012)** - Flexible layouts
- **CSS Grid (2017)** - Two-dimensional layouts
- **Custom Properties (2018+)** - Variables
- **CSS-in-JS + AI (Future)** - Dynamic styling

*Study tip: Focus on understanding the relationship between HTML structure and CSS styling, as well as how different CSS layout methods (float, flexbox, grid) solve different design challenges.*