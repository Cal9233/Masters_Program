# CSC 6303 Week 4 Study Notes: JavaScript and Perl

## Overview
This week covers two scripting languages: JavaScript (for web development) and Perl 5 (for system administration and text processing).

---

## Part 1: JavaScript

### History and Purpose
- **Created**: 1995 at Netscape
- **Purpose**: Add interactivity and logic to web pages
- **Not related to Java** - only shares the name and procedural language inspiration from Algol and C
- Originally designed as an "ad hoc language" for the World Wide Web

### Web Technology Stack
- **HTML** = Structure (content and markup)
- **CSS** = Presentation (styling and layout)
- **JavaScript** = Interactivity & Logic (dynamic behavior)

### Internet vs WWW Analogy
- **Internet** = The whole library system (buildings, wires, computers)
- **WWW** = The bookshelves with books (websites)
- **Website** = A book with many pages (HTML documents)
- **Hyperlinks** = Bookmarks that jump to other pages
- **CSS** = The book's design (fonts, colors, layout)
- **JavaScript** = The magic ink that makes pages interactive

### Program Structure
- **Common patterns**: Scripts, embedded functions, functions to call
- **Less common**: Classes with methods
- **Syntax**: C-like with curly braces `{}` and semicolons `;`

### Basic JavaScript Commands

#### Variables
```javascript
let name = "John Adams";        // String
let age = 90;                   // Number
let isPresident = true;         // Boolean
let occupations = [             // Array
    1758, 'Lawyer',
    1774, 'Politician',
    1778, 'Diplomat'
];
let president = {               // Object
    name: "John Adams",
    age: 61,
    inauguration: 1797
};
```

**Key Points**:
- Declaration needed (`let` or `var`)
- Untyped and implicit allocation
- Integers have limited precision, BigInt for larger numbers
- Arrays can hold mixed types (similar to Python lists)

#### Functions
```javascript
function sumMinMax(a, b) {
    let sum = a + b;
    let min, max;
    if (a < b) {
        min = a;
        max = b;
    } else {
        min = b;
        max = a;
    }
    return [sum, min, max];
}
```

**Key Points**:
- Functions are untyped
- Parameters passed by value except for non-primitives (objects, dates, arrays)
- Single return value (can be array or object)

#### Decision Structures
- **if-else if-else**: Standard conditional logic
- **switch-case-default**: For multiple conditions
- **Conditional operator**: `condition ? value1 : value2`

#### Loops
```javascript
// For loop
for (let i = 0; i < 10; i++) {
    alert(i);
}

// While loop
let i = 0;
while (i < 10) {
    alert(i);
    i++;
}

// Do-while loop
let i = -1;
do {
    i++;
    alert(i);
} while (i < 10);
```

### Object-Oriented Concepts in JavaScript

#### Basic Objects (Native Data Type)
```javascript
let animal = {
    name: 'Animal',
    sayName: function() {
        console.log(this.name);
    }
};

// Object creation and inheritance
let dog = Object.create(animal);
dog.name = 'Dog';
dog.sound = function() {
    console.log('Woof!');
};
```

#### Classes (More Structured Approach)
```javascript
class President {
    constructor(name, age, inauguration) {
        this.name = name;
        this._age = age;  // Convention for "private"
        this._inauguration = inauguration;
    }
    
    getAge() { 
        return this._age; 
    }
}
```

**Key Points**:
- Encapsulation: Use `_` convention or `#privateField` for true privacy
- JavaScript offers inheritance through object creation
- Enables polymorphism without full class structure

### JavaScript in HTML/CSS

#### Basic HTML Structure
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <style>
        /* CSS styles */
    </style>
</head>
<body>
    <h1>Header</h1>
    <p>Paragraph</p>
    <button onclick="myFunction()">Click Me</button>
    <script>
        function myFunction() {
            // JavaScript code
        }
    </script>
</body>
</html>
```

#### Key HTML Elements for JavaScript
- `<script>`: Defines JavaScript functions
- `<button>`: Creates clickable buttons
- `<input>`: Creates input fields (type="text", type="number")
- `<label>`: Text labels
- `.innerHTML`: Property to change element content

#### Development Options
**Online interpreters**:
- Programiz
- JDoodle
- W3Schools

---

## Part 2: Perl 5

### History and Purpose
- **Created**: 1987 by Unisys
- **Became stable**: Turn of the century
- **Known as**: "Hacking language" for system programmers (creative problem-solving)
- **Split**: Perl 5 (ongoing) and Perl 6/Raku (2019)
- **Uses**: System administration, network programming, text processing, GUIs

### Program Structure
- **Common patterns**: Several packages, mostly subroutines (functions), scripts
- **Less common**: Classes
- **Syntax**: C-like with curly braces `{}` and semicolons `;`

### Basic Perl Commands

#### Variables and Data Types
```perl
$name = "John Adams";           # Scalar (string/number)
$age = 90;                      # Scalar (number)

@occupations_date = (           # Array
    1758, "Lawyer",
    1774, "Politician", 
    1778, "Diplomat"
);

%president = (                  # Hash (key-value pairs)
    name => "John Adams",
    age => 61,
    inauguration => 1797
);

$potus2 = \%president;          # Reference
print $potus2->{name};          # Prints "John Adams"
```

**Variable Prefixes**:
- `$` = Scalars (numbers and strings)
- `@` = Arrays
- `%` = Hashes (associative arrays)
- `\` = References
- `$_` = Default scalar variable

#### Subroutines
```perl
sub sumMaxMin {
    my ($a, $b) = @_;
    my $sum = $a + $b;
    my ($min, $max);
    if ($a < $b) {
        $min = $a;
        $max = $b;
    } else {
        $min = $b;
        $max = $a;
    }
    return ($sum, $min, $max);
}
```

**Key Points**:
- Subroutines are untyped
- Parameters passed by reference (default) or by value (user choice)
- Multiple return values supported
- No subroutine overload

#### Decision Structures
- **if-elsif-else**: Standard conditional
- **unless-elsif-else**: Negative conditional
- **given-when-default**: Pattern matching
- **Conditional operator**: Same as other languages

#### Loops
```perl
# For loop
for ($i = 0; $i < 10; $i++) {
    print "$i\n";
}

# Foreach loop
@arr = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
foreach $arr (@arr) {
    print "$arr\n";
}

# While loop
$count = 0;
while ($count < 10) {
    print "$count\n";
    $count++;
}

# Do-while loop
do {
    print "$count\n";
    $count++;
} while ($count < 10);

# Until loop
until ($count >= 10) {
    print "$count\n";
    $count++;
}
```

**Loop Control**:
- `last` = equivalent to `break` in C
- `next` = equivalent to `continue` in C

### Object-Oriented Concepts in Perl

#### Similarities to Python
- Not required
- Subclasses for inheritance
- Methods and constructors
- Instance variables

#### Differences from Python
- **Encapsulation**: No true encapsulation; privacy by convention only
- **Polymorphism**: Flexible subroutine references
- **Classes**: Implicitly defined as packages (namespaces with subroutines)
- Python classes are explicitly defined and more structured

#### Example OO Code
```perl
package Animal;
sub new {
    my ($class) = @_;
    my $self = {};
    bless $self, $class;
    return $self;
}

package Dog;
use base 'Animal';
sub new {
    my ($class) = @_;
    my $self = $class->SUPER::new();
    $self->{breed} = 'Unknown';
    bless $self, $class;
    return $self;
}
```

---

## Development Tools

### JavaScript
- **Browser**: Built-in JavaScript engine
- **Online**: Programiz, JDoodle, W3Schools
- **IDE**: VS Code, any text editor

### Perl
- **Installation**: Less likely pre-installed than JavaScript
- **Online**: JDoodle
- **IDE**: VS Code, any text editor

---

## Important Standards and Testing

### Web Standards
- **W3C**: Defines HTML, CSS standards
- **ECMA**: JavaScript standards
- **Browser compatibility**: Always test on multiple browsers
- **Error handling**: Browsers tolerate mistakes differently

---

## Key Concepts to Remember

### JavaScript
1. Created for web interactivity, now a full programming language
2. Part of the HTML/CSS/JS web technology stack
3. Object-oriented features added later
4. Can be embedded in HTML or in separate .js files
5. Mobile web development focuses on efficiency and responsiveness

### Perl
1. Mature scripting language with significant legacy code
2. Excellent for text processing and system administration
3. Flexible syntax with multiple ways to accomplish tasks
4. OO features available but not as structured as Java/C++
5. Future development focuses on Perl 7

### Both Languages
1. Started as scripting languages for small tasks (like Python)
2. Evolved into full programming languages
3. Untyped variables and functions
4. C-like syntax with curly braces
5. Cross-platform compatibility