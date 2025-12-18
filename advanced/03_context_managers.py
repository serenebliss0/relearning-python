"""
Advanced Python Practice: Context Managers

This file covers context managers in Python:
- Using 'with' statement
- Creating custom context managers with __enter__ and __exit__
- Using @contextmanager decorator
- Practical context manager examples
"""

import os
import sys
import time
from contextlib import contextmanager

# ============================================================================
# BASIC CONTEXT MANAGERS (with statement)
# ============================================================================

print("=== Basic Context Managers ===")

# File handling with context manager
print("Writing to a file using 'with':")
with open("temp_context.txt", "w") as file:
    file.write("This file was created using a context manager.\n")
    file.write("It will be automatically closed.\n")

print("File created and automatically closed")

# Read the file
with open("temp_context.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")
print()

# ============================================================================
# CUSTOM CONTEXT MANAGER (Class-based)
# ============================================================================

print("=== Custom Context Manager (Class-based) ===")

class Timer:
    """Context manager to measure execution time"""
    
    def __enter__(self):
        """Called when entering the 'with' block"""
        print("Timer started")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the 'with' block"""
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

# Using the Timer context manager
with Timer():
    print("Doing some work...")
    time.sleep(0.5)
    print("Work completed")
print()

# ============================================================================
# CONTEXT MANAGER WITH RESOURCE MANAGEMENT
# ============================================================================

print("=== Resource Management Context Manager ===")

class DatabaseConnection:
    """Simulate a database connection context manager"""
    
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None
    
    def __enter__(self):
        """Open connection"""
        print(f"Opening connection to {self.database_name}")
        self.connection = f"Connection to {self.database_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection"""
        print(f"Closing connection to {self.database_name}")
        self.connection = None
        return False

# Using the database connection
with DatabaseConnection("my_database") as conn:
    print(f"Using: {conn}")
    print("Executing queries...")
print("Connection automatically closed")
print()

# ============================================================================
# CONTEXT MANAGER WITH DECORATOR
# ============================================================================

print("=== Context Manager with @contextmanager ===")

@contextmanager
def temporary_value(variable_dict, key, temp_value):
    """Temporarily change a dictionary value"""
    original_value = variable_dict.get(key)
    variable_dict[key] = temp_value
    print(f"Changed {key} to {temp_value}")
    
    try:
        yield variable_dict
    finally:
        # Restore original value
        if original_value is None:
            variable_dict.pop(key, None)
        else:
            variable_dict[key] = original_value
        print(f"Restored {key} to {original_value}")

# Using the temporary value context manager
config = {"debug": False, "timeout": 30}
print(f"Original config: {config}")

with temporary_value(config, "debug", True):
    print(f"Inside context: {config}")
    
print(f"After context: {config}")
print()

# ============================================================================
# CONTEXT MANAGER FOR ERROR HANDLING
# ============================================================================

print("=== Context Manager for Error Handling ===")

@contextmanager
def error_handler(error_message="An error occurred"):
    """Context manager to catch and handle errors gracefully"""
    try:
        yield
    except Exception as e:
        print(f"{error_message}: {type(e).__name__} - {e}")

# Using error handler
print("Attempting risky operation:")
with error_handler("Failed to divide"):
    result = 10 / 0  # This will raise ZeroDivisionError

print("Program continues after error")
print()

# ============================================================================
# MULTIPLE CONTEXT MANAGERS
# ============================================================================

print("=== Multiple Context Managers ===")

# Multiple context managers in one 'with' statement
print("Opening two files simultaneously:")
with open("temp_file1.txt", "w") as f1, open("temp_file2.txt", "w") as f2:
    f1.write("Content for file 1\n")
    f2.write("Content for file 2\n")
    print("Both files open and being written to")

print("Both files automatically closed")
print()

# ============================================================================
# CONTEXT MANAGER FOR STATE MANAGEMENT
# ============================================================================

print("=== State Management Context Manager ===")

@contextmanager
def change_directory(path):
    """Temporarily change working directory"""
    original_dir = os.getcwd()
    print(f"Changing directory from {original_dir} to {path}")
    
    try:
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        yield
    finally:
        os.chdir(original_dir)
        print(f"Restored directory to {original_dir}")

# Example usage
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

with change_directory("temp_dir"):
    print(f"Inside context: {os.getcwd()}")

print(f"After context: {os.getcwd()}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a list modification context manager
@contextmanager
def list_transaction(lst):
    """Context manager that allows list rollback on error"""
    backup = lst.copy()
    try:
        yield lst
    except:
        lst.clear()
        lst.extend(backup)
        print("Transaction rolled back")
        raise

my_list = [1, 2, 3]
print(f"\nOriginal list: {my_list}")

try:
    with list_transaction(my_list) as temp_list:
        temp_list.append(4)
        temp_list.append(5)
        print(f"Modified list: {temp_list}")
        raise ValueError("Something went wrong!")
except ValueError:
    pass

print(f"List after rollback: {my_list}")


# Exercise 2: Create a suppression context manager
class SuppressOutput:
    """Context manager to suppress print output"""
    
    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = None
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout
        return False

print("\nBefore suppression:")
print("This will be printed")

# Note: The following demonstrates the concept, but we won't actually suppress
# output here as it would be confusing in the example
print("(Suppression example - would hide output in real use)")


# Exercise 3: Create a timing decorator using context manager
@contextmanager
def timing_context(operation_name):
    """Context manager to time operations"""
    print(f"\nStarting: {operation_name}")
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"Finished: {operation_name} in {elapsed:.4f} seconds")

with timing_context("Data Processing"):
    time.sleep(0.2)
    print("Processing data...")

# Cleanup temporary files
for filename in ["temp_context.txt", "temp_file1.txt", "temp_file2.txt"]:
    try:
        os.remove(filename)
    except:
        pass

print("\n" + "="*50)
print("Practice complete! Temporary files cleaned up.")
print("="*50)
