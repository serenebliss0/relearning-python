"""
Basic Python Practice: Variables and Data Types

This file covers fundamental Python concepts including:
- Variables and assignment
- Basic data types (int, float, str, bool)
- Type checking and conversion
"""

# ============================================================================
# VARIABLES AND ASSIGNMENT
# ============================================================================

# Simple variable assignment
name = "Python Learner"
age = 25
height = 5.9
is_learning = True

print("=== Variables ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Learning: {is_learning}")
print()

# ============================================================================
# DATA TYPES
# ============================================================================

print("=== Data Types ===")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_learning: {type(is_learning)}")
print()

# ============================================================================
# TYPE CONVERSION
# ============================================================================

print("=== Type Conversion ===")
# String to int
string_number = "42"
int_number = int(string_number)
print(f"String '{string_number}' converted to int: {int_number}")

# Int to string
number = 100
string_from_number = str(number)
print(f"Number {number} converted to string: '{string_from_number}'")

# Float to int (truncates)
float_number = 3.14
int_from_float = int(float_number)
print(f"Float {float_number} converted to int: {int_from_float}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create variables for your personal info
# TODO: Fill in your own information
my_name = "Your Name"
my_age = 0
my_favorite_language = "Python"

print(f"My name is {my_name}, I am {my_age} years old, and I love {my_favorite_language}!")

# Exercise 2: Perform some calculations
x = 10
y = 3
sum_result = x + y
difference = x - y
product = x * y
division = x / y
floor_division = x // y
modulo = x % y
power = x ** y

print(f"\n{x} + {y} = {sum_result}")
print(f"{x} - {y} = {difference}")
print(f"{x} * {y} = {product}")
print(f"{x} / {y} = {division}")
print(f"{x} // {y} = {floor_division}")
print(f"{x} % {y} = {modulo}")
print(f"{x} ** {y} = {power}")

# Exercise 3: String operations
greeting = "Hello"
target = "World"
message = greeting + ", " + target + "!"
print(f"\n{message}")
print(f"Message length: {len(message)}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
