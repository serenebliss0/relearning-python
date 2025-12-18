"""
Intermediate Python Practice: File Handling

This file covers file operations in Python:
- Reading from files
- Writing to files
- Working with context managers
- Different file modes
- JSON file handling
"""

import os
import json

# ============================================================================
# WRITING TO FILES
# ============================================================================

print("=== Writing to Files ===")

# Create a sample directory for practice files
os.makedirs("temp_files", exist_ok=True)

# Write to a file
with open("temp_files/sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is easy!\n")

print("Created and wrote to 'temp_files/sample.txt'")
print()

# ============================================================================
# READING FROM FILES
# ============================================================================

print("=== Reading from Files ===")

# Read entire file
with open("temp_files/sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Read line by line
with open("temp_files/sample.txt", "r") as file:
    print("Reading line by line:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")
print()

# ============================================================================
# APPENDING TO FILES
# ============================================================================

print("=== Appending to Files ===")

# Append to existing file
with open("temp_files/sample.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("Another appended line.\n")

# Read the updated file
with open("temp_files/sample.txt", "r") as file:
    print("Updated file content:")
    print(file.read())
print()

# ============================================================================
# WORKING WITH JSON
# ============================================================================

print("=== Working with JSON ===")

# Create Python data structure
person_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_active": True
}

# Write JSON to file
with open("temp_files/person.json", "w") as file:
    json.dump(person_data, file, indent=2)

print("Created 'temp_files/person.json'")

# Read JSON from file
with open("temp_files/person.json", "r") as file:
    loaded_data = json.load(file)
    print("\nLoaded JSON data:")
    print(f"Name: {loaded_data['name']}")
    print(f"Age: {loaded_data['age']}")
    print(f"Skills: {', '.join(loaded_data['skills'])}")
print()

# ============================================================================
# FILE EXISTENCE AND INFORMATION
# ============================================================================

print("=== File Information ===")

filename = "temp_files/sample.txt"
if os.path.exists(filename):
    print(f"File '{filename}' exists")
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes")
else:
    print(f"File '{filename}' does not exist")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a simple log file
def write_log(message, filename="temp_files/log.txt"):
    """Append a timestamped message to a log file"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

write_log("Application started")
write_log("User logged in")
write_log("Data processed successfully")

print("Created log file:")
with open("temp_files/log.txt", "r") as file:
    print(file.read())


# Exercise 2: Read and count words in a file
def count_words(filename):
    """Count words in a file"""
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)

word_count = count_words("temp_files/sample.txt")
print(f"Word count in sample.txt: {word_count}")


# Exercise 3: Save and load a list of tasks
tasks = [
    {"id": 1, "task": "Learn Python basics", "completed": True},
    {"id": 2, "task": "Practice file handling", "completed": True},
    {"id": 3, "task": "Build a project", "completed": False}
]

# Save tasks
with open("temp_files/tasks.json", "w") as file:
    json.dump(tasks, file, indent=2)

# Load tasks
with open("temp_files/tasks.json", "r") as file:
    loaded_tasks = json.load(file)
    print("\nTask List:")
    for task in loaded_tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"  [{status}] {task['task']}")

# Cleanup instruction
print("\n" + "="*50)
print("Note: Practice files created in 'temp_files/' directory")
print("You can safely delete this directory after practice")
print("="*50)
