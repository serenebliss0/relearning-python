"""
Advanced Python Practice: Generators

This file covers generators in Python:
- Generator functions with yield
- Generator expressions
- Benefits of generators (memory efficiency)
- Practical generator examples
"""

import sys

# ============================================================================
# BASIC GENERATORS
# ============================================================================

print("=== Basic Generators ===")

def simple_generator():
    """A simple generator that yields three values"""
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3

# Using the generator
gen = simple_generator()
print(f"Created generator: {gen}")

for value in gen:
    print(f"Received: {value}")
print()

# ============================================================================
# GENERATOR VS LIST (MEMORY COMPARISON)
# ============================================================================

print("=== Generator vs List Memory Comparison ===")

def get_list(n):
    """Return a list of numbers (stores all in memory)"""
    return [x for x in range(n)]

def get_generator(n):
    """Return a generator of numbers (generates on-the-fly)"""
    for x in range(n):
        yield x

# Compare memory usage
list_obj = get_list(1000)
gen_obj = get_generator(1000)

print(f"List size: {sys.getsizeof(list_obj)} bytes")
print(f"Generator size: {sys.getsizeof(gen_obj)} bytes")
print()

# ============================================================================
# INFINITE GENERATORS
# ============================================================================

print("=== Infinite Generators ===")

def infinite_sequence():
    """Generator that produces infinite sequence"""
    num = 0
    while True:
        yield num
        num += 1

# Use infinite generator (with a limit)
gen = infinite_sequence()
print("First 10 numbers from infinite sequence:")
for i in range(10):
    print(next(gen), end=" ")
print("\n")

# ============================================================================
# GENERATOR EXPRESSIONS
# ============================================================================

print("=== Generator Expressions ===")

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(10)]
print(f"List comprehension: {squares_list}")

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))
print(f"Generator expression: {squares_gen}")
print(f"Values: {list(squares_gen)}")
print()

# ============================================================================
# FIBONACCI GENERATOR
# ============================================================================

print("=== Fibonacci Generator ===")

def fibonacci():
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib_gen = fibonacci()
fib_numbers = [next(fib_gen) for _ in range(10)]
print(f"First 10 Fibonacci numbers: {fib_numbers}")
print()

# ============================================================================
# GENERATOR WITH SEND METHOD
# ============================================================================

print("=== Generator with Send Method ===")

def counter_generator():
    """Generator that accepts values via send()"""
    count = 0
    while True:
        increment = yield count
        if increment is not None:
            count += increment
        else:
            count += 1

gen = counter_generator()
print(f"Initial: {next(gen)}")
print(f"Next: {next(gen)}")
print(f"Send 5: {gen.send(5)}")
print(f"Next: {next(gen)}")
print(f"Send 10: {gen.send(10)}")
print()

# ============================================================================
# FILE READING GENERATOR
# ============================================================================

print("=== File Reading Generator ===")

def read_lines(filename):
    """Generator to read file line by line (memory efficient)"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return

# Example (will work if file exists)
print("Attempting to read file using generator...")
for line in read_lines("example.txt"):
    print(line)
print("(No file found - that's okay for this example)")
print()

# ============================================================================
# PRACTICAL GENERATORS
# ============================================================================

print("=== Practical Generators ===")

def batch_data(data, batch_size):
    """Generator to yield data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Process data in batches
data = list(range(1, 21))
print(f"Original data: {data}")
print("\nProcessing in batches of 5:")
for batch_num, batch in enumerate(batch_data(data, 5), 1):
    print(f"Batch {batch_num}: {batch}")
print()

# ============================================================================
# GENERATOR PIPELINE
# ============================================================================

print("=== Generator Pipeline ===")

def numbers(n):
    """Generate numbers from 0 to n"""
    for i in range(n):
        yield i

def square(nums):
    """Square each number"""
    for num in nums:
        yield num ** 2

def even_only(nums):
    """Filter even numbers only"""
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators together
pipeline = even_only(square(numbers(10)))
result = list(pipeline)
print("Pipeline: numbers(10) -> square -> even_only")
print(f"Result: {result}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a prime number generator
def prime_generator():
    """Generate prime numbers"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("\nFirst 15 prime numbers:")
prime_gen = prime_generator()
primes = [next(prime_gen) for _ in range(15)]
print(primes)


# Exercise 2: Create a range generator with step
def custom_range(start, stop, step=1):
    """Custom range generator"""
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step

print("\nCustom range(0, 10, 2):")
print(list(custom_range(0, 10, 2)))

print("\nCustom range(10, 0, -2):")
print(list(custom_range(10, 0, -2)))


# Exercise 3: Create a running average generator
def running_average():
    """Calculate running average of sent numbers"""
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        if value is not None:
            total += value
            count += 1

print("\nRunning average:")
avg_gen = running_average()
next(avg_gen)  # Prime the generator
print(f"After 10: {avg_gen.send(10)}")
print(f"After 20: {avg_gen.send(20)}")
print(f"After 30: {avg_gen.send(30)}")
