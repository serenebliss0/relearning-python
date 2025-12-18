# Intermediate Python 🌿

Ready to level up? This section covers the core concepts that make you a proficient Python developer.

## Files in This Section

### 01_functions.py
**Topics Covered:**
- Function definition and calling
- Parameters and return values
- Default arguments
- `*args` and `**kwargs`
- Lambda functions
- Higher-order functions
- Recursion

**Key Concepts:**
- Functions make code reusable and organized
- `*args` for variable positional arguments
- `**kwargs` for variable keyword arguments
- Lambda functions for simple, one-line functions
- Functions are first-class objects in Python

**Run it:** `python 01_functions.py`

### 02_classes_oop.py
**Topics Covered:**
- Classes and objects
- Constructor (`__init__`)
- Instance vs class variables
- Instance vs class methods
- Inheritance
- Special methods (`__str__`, `__repr__`, `__len__`, `__eq__`)

**Key Concepts:**
- OOP helps organize complex programs
- `self` refers to the instance
- Inheritance allows code reuse
- Special methods enable Python's built-in operations
- `super()` calls parent class methods

**Run it:** `python 02_classes_oop.py`

### 03_file_handling.py
**Topics Covered:**
- Reading from files
- Writing to files
- Appending to files
- Context managers (`with` statement)
- JSON file handling
- File existence and information

**Key Concepts:**
- Always use `with` for file operations (automatic cleanup)
- Different modes: 'r' (read), 'w' (write), 'a' (append)
- JSON for structured data storage
- `os` module for file operations
- Exception handling for missing files

**Run it:** `python 03_file_handling.py`

## Learning Path

1. **Functions First**: Master functions before moving to classes
2. **OOP Next**: Understand object-oriented programming concepts
3. **File Handling**: Learn to persist data
4. **Combine**: Use all three concepts together in projects

## Project Ideas to Practice

### Beginner Projects
1. **Password Generator**: Function-based tool with options
2. **Grade Calculator**: Class to manage student grades
3. **Contact Book**: Save/load contacts to/from JSON file

### Intermediate Projects
1. **Bank Account Simulator**: Classes with file persistence
2. **Simple Blog**: Posts stored in files with CRUD operations
3. **Task Manager**: Complete app with functions, classes, and file I/O

### Challenge Projects
1. **Library Management System**: Books, members, borrowing (OOP)
2. **Budget Tracker**: Track income/expenses with reporting
3. **Simple Database**: Build a JSON-based database with queries

## Common Patterns

### The Function Pattern
```python
def process_data(data):
    """Process and return data"""
    # validate
    # transform
    # return
    return processed_data
```

### The Class Pattern
```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def method(self):
        return self.value
```

### The File Pattern
```python
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed
```

## Key Skills to Master

- [ ] Write functions with different parameter types
- [ ] Create classes with methods and properties
- [ ] Use inheritance effectively
- [ ] Read and write to files safely
- [ ] Work with JSON data
- [ ] Understand when to use functions vs classes
- [ ] Handle file-related errors

## Tips for This Level

1. **Think in abstractions**: What should be a function? A class?
2. **DRY principle**: Don't Repeat Yourself - use functions!
3. **SOLID principles**: Learn these for better OOP
4. **Test your code**: Write small tests as you go
5. **Document**: Add docstrings to functions and classes

## Moving to Advanced

Before moving to the advanced section, make sure you can:
- Write clean, well-documented functions
- Create classes with multiple methods
- Use inheritance to extend functionality
- Handle files and errors gracefully
- Combine all these concepts in a project

## Debugging Tips

- Use `print()` statements liberally
- Use Python's debugger: `import pdb; pdb.set_trace()`
- Read stack traces from bottom to top
- Check that files exist before trying to open them
- Verify data types match expectations

---

**Remember**: This is where Python gets really powerful. Take time to understand these concepts deeply! 💪
