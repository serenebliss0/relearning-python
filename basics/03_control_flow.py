"""
Basic Python Practice: Control Flow

This file covers control flow structures:
- if/elif/else statements
- for loops
- while loops
- break and continue
"""

# ============================================================================
# IF/ELIF/ELSE STATEMENTS
# ============================================================================

print("=== Conditional Statements ===")

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")
print()

# if/else
temperature = 75
if temperature > 80:
    print("It's hot outside!")
else:
    print("It's comfortable outside")
print()

# if/elif/else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")
print()

# Logical operators
username = "admin"
password = "secret123"
if username == "admin" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid credentials")
print()

# ============================================================================
# FOR LOOPS
# ============================================================================

print("=== For Loops ===")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# Loop through a range
print("Counting to 5:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# Loop with index using enumerate
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
print()

# Loop through a dictionary
person = {"name": "Bob", "age": 25, "city": "Boston"}
for key, value in person.items():
    print(f"{key}: {value}")
print()

# ============================================================================
# WHILE LOOPS
# ============================================================================

print("=== While Loops ===")

# Simple while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print()

# While loop with condition
number = 1
while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    number += 1
print()

# ============================================================================
# BREAK AND CONTINUE
# ============================================================================

print("=== Break and Continue ===")

# Break - exit loop early
print("Finding first number divisible by 7:")
for num in range(1, 20):
    if num % 7 == 0:
        print(f"Found: {num}")
        break
print()

# Continue - skip to next iteration
print("Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print("\n")

# ============================================================================
# LIST COMPREHENSIONS (Bonus!)
# ============================================================================

print("=== List Comprehensions ===")

# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Filter with condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Transform strings
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: FizzBuzz (classic programming exercise)
print("\nFizzBuzz (1-15):")
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print("\n")

# Exercise 2: Find the sum of all even numbers from 1 to 50
sum_even = 0
for num in range(2, 51, 2):
    sum_even += num
print(f"Sum of even numbers 1-50: {sum_even}")

# Exercise 3: Count vowels in a string
text = "Python is awesome"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"\nVowels in '{text}': {vowel_count}")
