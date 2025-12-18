"""
Intermediate Python Practice: Functions

This file covers functions in Python:
- Function definition and calling
- Parameters and arguments
- Return values
- Default arguments
- *args and **kwargs
- Lambda functions
"""

# ============================================================================
# BASIC FUNCTIONS
# ============================================================================

print("=== Basic Functions ===")

def greet():
    """Simple function with no parameters"""
    print("Hello, World!")

greet()
print()


def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
print()


def add_numbers(a, b):
    """Function with return value"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

# ============================================================================
# DEFAULT ARGUMENTS
# ============================================================================

print("=== Default Arguments ===")

def greet_with_title(name, title="Friend"):
    """Function with default parameter"""
    return f"Hello, {title} {name}!"

print(greet_with_title("Alice"))
print(greet_with_title("Bob", "Mr."))
print()

# ============================================================================
# MULTIPLE RETURN VALUES
# ============================================================================

print("=== Multiple Return Values ===")

def calculate_stats(numbers):
    """Function returning multiple values"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return total, count, average

nums = [10, 20, 30, 40, 50]
sum_val, count_val, avg_val = calculate_stats(nums)
print(f"Numbers: {nums}")
print(f"Sum: {sum_val}, Count: {count_val}, Average: {avg_val}")
print()

# ============================================================================
# *ARGS AND **KWARGS
# ============================================================================

print("=== *args and **kwargs ===")

def sum_all(*args):
    """Function that accepts variable number of arguments"""
    return sum(args)

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50): {sum_all(10, 20, 30, 40, 50)}")
print()


def print_info(**kwargs):
    """Function that accepts variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Person info:")
print_info(name="Alice", age=30, city="New York")
print()


def flexible_function(*args, **kwargs):
    """Function that accepts both *args and **kwargs"""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function(1, 2, 3, name="Bob", age=25)
print()

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================

print("=== Lambda Functions ===")

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
print()

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================

print("=== Higher-Order Functions ===")

def apply_operation(numbers, operation):
    """Function that takes another function as parameter"""
    return [operation(n) for n in numbers]

def double(x):
    return x * 2

def triple(x):
    return x * 3

nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
print(f"Doubled: {apply_operation(nums, double)}")
print(f"Tripled: {apply_operation(nums, triple)}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a function to check if a number is prime
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime numbers from 1 to 20:")
primes = [n for n in range(1, 21) if is_prime(n)]
print(primes)


# Exercise 2: Create a function to reverse a string
def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

original = "Python"
reversed_text = reverse_string(original)
print(f"\nOriginal: {original}, Reversed: {reversed_text}")


# Exercise 3: Create a function to find the factorial
def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}")
