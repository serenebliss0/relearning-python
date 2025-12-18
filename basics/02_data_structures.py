"""
Basic Python Practice: Data Structures

This file covers fundamental Python data structures:
- Lists
- Tuples
- Dictionaries
- Sets
"""

# ============================================================================
# LISTS (Mutable, Ordered)
# ============================================================================

print("=== Lists ===")
# Creating lists
fruits = ["apple", "banana", "cherry", "date"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print()

# List operations
fruits.append("elderberry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "apricot")  # Insert at index
print(f"After insert: {fruits}")

fruits.remove("banana")  # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()  # Remove and return last item
print(f"Popped: {popped}, List: {fruits}")
print()

# List slicing
print(f"First 3 fruits: {fruits[:3]}")
print(f"Last 2 fruits: {fruits[-2:]}")
print(f"Every other fruit: {fruits[::2]}")
print()

# ============================================================================
# TUPLES (Immutable, Ordered)
# ============================================================================

print("=== Tuples ===")
# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single_tuple = (42,)  # Note the comma for single element

print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked - x: {x}, y: {y}")
print()

# ============================================================================
# DICTIONARIES (Key-Value Pairs)
# ============================================================================

print("=== Dictionaries ===")
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print()

# Dictionary operations
person["email"] = "alice@example.com"  # Add new key
print(f"After adding email: {person}")

person["age"] = 31  # Update value
print(f"After updating age: {person}")

# Iterate through dictionary
print("\nDictionary items:")
for key, value in person.items():
    print(f"  {key}: {value}")
print()

# ============================================================================
# SETS (Unordered, Unique Elements)
# ============================================================================

print("=== Sets ===")
# Creating sets
colors = {"red", "green", "blue"}
numbers_set = {1, 2, 3, 4, 5}
duplicate_set = {1, 2, 2, 3, 3, 3}  # Duplicates removed

print(f"Colors: {colors}")
print(f"Duplicate set: {duplicate_set}")
print()

# Set operations
colors.add("yellow")
print(f"After add: {colors}")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a shopping list
shopping_list = []
# TODO: Add 5 items to the shopping list
shopping_list.extend(["milk", "bread", "eggs", "butter", "cheese"])
print(f"Shopping list: {shopping_list}")

# Exercise 2: Create a dictionary for a book
book = {
    "title": "Python Fundamentals",
    "author": "John Doe",
    "year": 2023,
    "pages": 350
}
print(f"\nBook: {book['title']} by {book['author']}")

# Exercise 3: Find unique elements
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"\nOriginal: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")
