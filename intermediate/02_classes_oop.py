"""
Intermediate Python Practice: Classes and Object-Oriented Programming

This file covers OOP concepts in Python:
- Classes and objects
- Constructors (__init__)
- Instance variables and methods
- Class variables and methods
- Inheritance
- Special methods
"""

# ============================================================================
# BASIC CLASSES
# ============================================================================

print("=== Basic Classes ===")

class Dog:
    """Simple class representing a dog"""
    
    def __init__(self, name, age):
        """Constructor to initialize a dog"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Method to make the dog bark"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Method to get dog information"""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog1.get_info())
print(dog2.bark())
print(dog2.get_info())
print()

# ============================================================================
# CLASS VARIABLES AND METHODS
# ============================================================================

print("=== Class Variables and Methods ===")

class Circle:
    """Class demonstrating class variables and methods"""
    
    # Class variable (shared by all instances)
    pi = 3.14159
    
    def __init__(self, radius):
        """Instance variable (unique to each instance)"""
        self.radius = radius
    
    def area(self):
        """Calculate area of the circle"""
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference of the circle"""
        return 2 * Circle.pi * self.radius
    
    @classmethod
    def from_diameter(cls, diameter):
        """Class method to create a Circle from diameter"""
        return cls(diameter / 2)

circle1 = Circle(5)
print(f"Circle with radius 5:")
print(f"  Area: {circle1.area():.2f}")
print(f"  Circumference: {circle1.circumference():.2f}")

circle2 = Circle.from_diameter(10)
print(f"\nCircle from diameter 10:")
print(f"  Radius: {circle2.radius}")
print(f"  Area: {circle2.area():.2f}")
print()

# ============================================================================
# INHERITANCE
# ============================================================================

print("=== Inheritance ===")

class Animal:
    """Base class for animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Call parent constructor
        self.color = color
    
    def make_sound(self):
        """Override parent method"""
        return "Meow!"
    
    def purr(self):
        """Cat-specific method"""
        return f"{self.name} is purring"


class Bird(Animal):
    """Bird class inheriting from Animal"""
    
    def __init__(self, name, can_fly):
        super().__init__(name, "Bird")
        self.can_fly = can_fly
    
    def make_sound(self):
        return "Chirp!"

# Create instances
cat = Cat("Whiskers", "orange")
bird = Bird("Tweety", True)

print(cat.info())
print(cat.make_sound())
print(cat.purr())
print()

print(bird.info())
print(bird.make_sound())
print(f"Can fly: {bird.can_fly}")
print()

# ============================================================================
# SPECIAL METHODS (MAGIC METHODS)
# ============================================================================

print("=== Special Methods ===")

class Book:
    """Class demonstrating special methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return length (number of pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Check equality based on title and author"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("Python Basics", "John Doe", 250)
book2 = Book("Python Basics", "John Doe", 250)
book3 = Book("Advanced Python", "Jane Smith", 350)

print(book1)  # Uses __str__
print(repr(book1))  # Uses __repr__
print(f"Pages: {len(book1)}")  # Uses __len__
print(f"book1 == book2: {book1 == book2}")  # Uses __eq__
print(f"book1 == book3: {book1 == book3}")
print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("=== Practice Exercises ===")

# Exercise 1: Create a BankAccount class
class BankAccount:
    """Bank account with deposit and withdrawal"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"

account = BankAccount("Alice", 100)
print(f"\n{account}")
print(account.deposit(50))
print(account.withdraw(30))
print(account)


# Exercise 2: Create a Rectangle class
class Rectangle:
    """Rectangle with area and perimeter calculations"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

rect = Rectangle(5, 10)
print(f"\n{rect}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
