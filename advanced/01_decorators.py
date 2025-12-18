"""
Advanced Python Practice: Decorators

This file covers decorators in Python:
- Function decorators
- Decorators with arguments
- Class decorators
- Multiple decorators
- Practical decorator examples
"""

import time
import functools

# ============================================================================
# BASIC DECORATORS
# ============================================================================

print("=== Basic Decorators ===")

def simple_decorator(func):
    """A simple decorator that prints before and after function call"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
print()

# ============================================================================
# DECORATORS WITH ARGUMENTS
# ============================================================================

print("=== Decorators with Arguments ===")

def decorator_with_args(func):
    """Decorator that works with function arguments"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result1 = add(5, 3)
result2 = greet("Alice", greeting="Hi")
print()

# ============================================================================
# TIMING DECORATOR
# ============================================================================

print("=== Timing Decorator ===")

def timing_decorator(func):
    """Decorator to measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Simulate a slow function"""
    time.sleep(0.1)
    return "Done!"

result = slow_function()
print()

# ============================================================================
# CACHING DECORATOR
# ============================================================================

print("=== Caching Decorator ===")

def memoize(func):
    """Decorator to cache function results"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            print(f"Computing {func.__name__}{args}")
            cache[args] = func(*args)
        else:
            print(f"Using cached result for {func.__name__}{args}")
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    """Calculate fibonacci number (inefficient without caching)"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Calculating fibonacci(5):")
result = fibonacci(5)
print(f"Result: {result}")
print("\nCalculating fibonacci(5) again:")
result = fibonacci(5)
print(f"Result: {result}")
print()

# ============================================================================
# DECORATOR WITH PARAMETERS
# ============================================================================

print("=== Decorator with Parameters ===")

def repeat(times):
    """Decorator factory that repeats function calls"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Bob")
print()

# ============================================================================
# MULTIPLE DECORATORS
# ============================================================================

print("=== Multiple Decorators ===")

def bold(func):
    """Wrap output in bold markers"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "**" + func(*args, **kwargs) + "**"
    return wrapper

def italic(func):
    """Wrap output in italic markers"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "_" + func(*args, **kwargs) + "_"
    return wrapper

@bold
@italic
def get_text():
    return "Hello, World"

print(get_text())
print()

# ============================================================================
# CLASS DECORATORS
# ============================================================================

print("=== Class Decorators ===")

def add_str_method(cls):
    """Decorator to add a custom __str__ method to a class"""
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.__class__.__str__ = lambda self: f"{cls.__name__} instance"
    
    cls.__init__ = new_init
    return cls

@add_str_method
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person)
print()

# ============================================================================
# PRACTICAL DECORATORS
# ============================================================================

print("=== Practical Decorators ===")

def validate_positive(func):
    """Decorator to validate that all arguments are positive"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"All arguments must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

try:
    print(f"Area (5, 10): {calculate_area(5, 10)}")
    print(f"Area (-5, 10): {calculate_area(-5, 10)}")  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a debug decorator
def debug(func):
    """Decorator that prints debug information"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"DEBUG: Calling {func.__name__}")
        print(f"DEBUG: Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"DEBUG: {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def multiply(x, y):
    return x * y

print("\nUsing debug decorator:")
multiply(4, 5)


# Exercise 2: Create a counter decorator
def count_calls(func):
    """Decorator to count function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def process_data():
    return "Data processed"

print("\nUsing counter decorator:")
process_data()
process_data()
process_data()
