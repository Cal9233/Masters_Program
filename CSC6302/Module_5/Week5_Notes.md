# CSC 6302 Database Principles - Week 5 Study Notes

## Course Timeline

### Future Projects Schedule
- **This week (Week 5)**: Adding View Layer
- **Next week (Week 6)**: Final project written plan
- **Week 7**: Final project database implementation
- **Week 8**: Final project GUI application

## Project 4 Feedback

### Key Issues Identified
1. **Config & Connections**: Need better configuration management for database connections
2. **Too much copying of sample program**: Should create more original code rather than copying examples
3. **Database relationship issues**: New vessel/passenger combinations weren't properly added to database
   - Need to add vessels and passengers separately first
   - Or implement code in add trips function to create them if they don't exist

## MVC Architecture Review

### Model-View-Controller Pattern

#### View Layer Key Responsibilities
- **Data Presentation**: Formatting and displaying data retrieved from model layer in way that is understandable and useful to users
- **User Interaction**: Providing user interface components (buttons, forms, menus) that allow users to interact with application
- **Input Validation**: Ensuring user input is valid and providing immediate feedback on errors or issues
- **User Experience Design**: Creating responsive and intuitive interface that enhances user engagement and satisfaction

#### Complete MVC Structure
- **View**: User interface and presentation layer
- **Controller**: Server that manages communication between Model and View
- **Model**: Contains both Business Logic and Data Access components
  - **Business Logic**: Application rules and workflow management
  - **Data Access**: Database interaction and data management

## Department Store Analogy

This analogy helps understand the three-layer architecture:

### View Layer (Department Shelves)
- Department shelves where merchandise is displayed
- Customers pick from available merchandise
- Goods are ready to buy, easy to see, attractively displayed

### Business Logic Layer (Store Manager)
- Manager making decisions about what to buy, when, and where to put it in store
- Manager putting in orders to shipping/receiving department based on customer requests
- Sometimes frequent predefined orders, sometimes special orders

### Data Access Layer (Shipping/Receiving Department)
- Takes orders from manager and translates them into purchase orders for supplier
- When order comes back, takes items off truck, unpacks them, removes plastic
- Stages items for Manager who then directs them to proper shelves

## Common Python GUI Frameworks

### Desktop GUI Options

#### Tkinter
- Standard GUI toolkit for Python
- Comes bundled with most Python installations
- Good for basic desktop applications

#### PyQt
- Set of Python bindings for Qt application framework
- Powerful and allows cross-platform applications with rich graphical interfaces
- Professional-grade applications

#### Toga
- Open-source, cross-platform GUI toolkit
- Part of BeeWare project
- Create native applications for Windows, macOS, Linux, iOS, and Android using single codebase
- Provides simple and consistent API across all platforms

#### PySimpleGUI
- Uses lists to organize layouts
- Good alternative if having trouble with widget-heavy models
- Simplified approach to GUI development

### Web Framework Option

#### Flask
- Lightweight and flexible web framework for Python
- Designed for building web applications and APIs
- Serves HTML, JavaScript, and CSS
- Good for web-based user interfaces

## Widgets and GUI Structure

### Widget Concept
Widgets are building blocks of GUI applications. Think of them as a nest or tree of content:

```
Main Window
|--------- Frame 1
    |-------- Button 1
    |-------- Button 2
|--------- Frame 2
    |-------- Entry Box 1
    |-------- Entry Box 2
|--------- Frame 3
    |-------- Results Display Area
```

### Hierarchical Organization
- **Main Window**: Top-level container
- **Frames**: Organizational containers for grouping related elements
- **Widgets**: Individual interface elements (buttons, text boxes, labels)
- **Nested Structure**: Allows for complex, organized layouts

## Sample Implementation Example

### Goal: Get all students taught by George Feeny

#### View Layer Implementation
```python
# Create interface including text boxes to enter teacher name
window = tk.Tk()
fnamebox = tk.Entry(...); fname_value = "George"
lnamebox = tk.Entry(...); lname_value = "Feeny"

# Define button to get information from text boxes and do business logic
btn = tk.Button(window, text="Submit", 
    command=lambda: BLL.getStudents(fname_value.get(), lname_value.get()))

# Define method to display results
def showResults(results):
    for x in results:
        tk.Label(window, x)
```

#### Business Logic Layer (BLL)
```python
# Create function that takes information from view and packages it for DAL
def getStudents(fname, lname):
    View.message(f"Searching for {fname} {lname}")
    View.showResults(DAL.getDBStudents(fname, lname))
```

#### Data Access Layer (DAL)
```python
# Define function to get students
def getDBStudents(fname, lname):
    cursor.execute(f"CALL getStudents(getTeacherId({fname},{lname}))")
```

#### Database Layer
```sql
-- Create & call Functions & Stored Procedures
CREATE getTeacherId(fname VARCHAR(20), name VARCHAR(20));
CREATE getStudents(teacherId INT);
CALL getStudents(getTeacherId("George", "Feeny"));
```

## Real-World Example: Chewy.com

The presentation showed Chewy.com as an example of effective front-end design, demonstrating:
- Clear order summary presentation
- User-friendly input validation (promo code functionality)
- Consistent interface design across different states
- Professional error handling and user feedback

## Project 5 Requirements

### Objective
Add a view layer that allows users to:
- Add passengers
- Add vessels  
- Add trips

### Key Implementation Points
- Must implement proper MVC architecture
- View layer should handle user interface and input validation
- Business logic should manage workflow and rules
- Data access layer should handle all database interactions
- Follow the hierarchical structure demonstrated in examples

### Best Practices
- Avoid copying sample programs extensively
- Implement proper configuration management
- Handle database relationships correctly
- Ensure proper separation of concerns between layers
- Include appropriate error handling and user feedback