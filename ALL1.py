# --- 1. Lists ---
print("--- 1. Lists ---")
# Definition: Ordered, changeable, allows duplicate members.
my_list = [10, 20, 30, "apple", True, 30]
print(f"Original List: {my_list}")

# Accessing elements (indexing)
print(f"Element at index 0: {my_list[0]}")
print(f"Last element: {my_list[-1]}")

# Slicing lists
print(f"Slice from index 1 to 3 (exclusive): {my_list[1:4]}")
print(f"Slice from beginning to index 2 (exclusive): {my_list[:3]}")
print(f"Slice from index 3 to end: {my_list[3:]}")
print(f"List with step (every 2nd element): {my_list[::2]}")
print(f"Reversed list: {my_list[::-1]}")


# Modifying lists
my_list[0] = 5  # Change element at index 0
print(f"List after changing index 0: {my_list}")

my_list.append("banana") # Add element to the end
print(f"List after append('banana'): {my_list}")

my_list.insert(2, "grape") # Insert at specific index
print(f"List after insert(2, 'grape'): {my_list}")

my_list.remove(30) # Remove first occurrence of value
print(f"List after remove(30): {my_list}")

popped_item = my_list.pop() # Remove and return last element
print(f"Popped item: {popped_item}, List after pop(): {my_list}")

popped_item_at_index = my_list.pop(1) # Remove and return element at index
print(f"Popped item at index 1: {popped_item_at_index}, List after pop(1): {my_list}")


# Other useful list methods
list_numbers = [5, 1, 9, 2, 7]
list_numbers.sort() # Sorts in-place (ascending by default)
print(f"Sorted numbers list: {list_numbers}")


list_numbers.reverse() # Reverses in-place
print(f"Reversed sorted numbers list: {list_numbers}")

print(f"Length of list: {len(my_list)}")
print(f"Count of 'banana': {my_list.count('banana')}")

# List Comprehension (concise way to create lists)
squares = [x**2 for x in range(5)] # Creates [0, 1, 4, 9, 16]
print(f"Squares using list comprehension: {squares}")


# --- 2. Tuples ---
print("\n--- 2. Tuples ---")
# Definition: Ordered, unchangeable (immutable), allows duplicate members.
my_tuple = (1, 2, "apple", 3.14, "apple")
print(f"Original Tuple: {my_tuple}")

# Accessing elements (indexing) - similar to lists
print(f"Element at index 1: {my_tuple[1]}")

# Slicing tuples - similar to lists
print(f"Slice from index 2 to end: {my_tuple[2:]}")

# Tuples are immutable - uncommenting the line below will cause an error
# my_tuple[0] = 5

# Useful tuple methods
print(f"Count of 'apple': {my_tuple.count('apple')}")
print(f"Index of 3.14: {my_tuple.index(3.14)}")
print(f"Length of tuple: {len(my_tuple)}")


# --- 3. Dictionaries ---
print("\n--- 3. Dictionaries ---")
# Definition: Unordered (as of Python 3.7, insertion order is preserved), changeable,
#              no duplicate keys. Stored as key-value pairs.
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True
}
print(f"Original Dictionary: {my_dict}")

# Accessing values
print(f"Name: {my_dict['name']}")
print(f"City (using .get()): {my_dict.get('city', 'Unknown')}") # .get() is safer, provides default if key not found
print(f"Country (using .get() with default): {my_dict.get('country', 'Not specified')}")

# Adding/Modifying entries
my_dict["email"] = "alice@example.com" # Add new key-value pair
print(f"After adding email: {my_dict}")

my_dict["age"] = 31 # Modify existing value
print(f"After updating age: {my_dict}")

# Removing entries
removed_value = my_dict.pop("is_student") # Remove by key and return value
print(f"Removed 'is_student': {removed_value}, Dictionary after pop('is_student'): {my_dict}")

last_item = my_dict.popitem() # Remove and return the last inserted item (Python 3.7+)
print(f"Removed last item: {last_item}, Dictionary after popitem(): {my_dict}")

del my_dict["city"] # Delete by key
print(f"After del 'city': {my_dict}")

# Iterating through dictionaries
print("\nIterating through dictionary keys:")
for key in my_dict: # By default, iterates over keys
    print(key)

print("\nIterating through dictionary values:")
for value in my_dict.values():
    print(value)

print("\nIterating through dictionary items (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print(f"Length of dictionary: {len(my_dict)}")


# --- 4. Functions ---
print("\n--- 4. Functions ---")

# Simple function with no arguments and no return value
def greet():
    print("Hello from a function!")

greet() # Calling the function

# Function with arguments
def add(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add(10, 5) # Calling with positional arguments
add(b=7, a=3) # Calling with keyword arguments

# Function with a return value
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print(f"The product of 4 and 6 is: {product}")



# Function with default argument values
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome("Charlie")
welcome() # Uses default "Guest"


# Function with arbitrary arguments (*args)
def print_args(*args):
    print("Arbitrary arguments:")
    for arg in args:
        print(arg)

print_args(1, "hello", True, [1, 2])

# Function with arbitrary keyword arguments (**kwargs)
def print_kwargs(**kwargs):
    print("Arbitrary keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(city="London", population=8.9, landmark="Tower Bridge")

# Lambda Functions (anonymous functions)
# Definition: Small, anonymous functions defined with the `lambda` keyword.
#             Can take any number of arguments, but can only have one expression.

square = lambda x: x * x
print(f"Square of 7 (using lambda): {square(7)}")



# Using lambda with higher-order functions (e.g., map, filter)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers (using map and lambda): {doubled}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using filter and lambda): {evens}")


# --- 5. Object-Oriented Programming (OOP) ---
print("\n--- 5. Object-Oriented Programming (OOP) ---")

# Class Definition
class Animal:
    # Class attribute (shared by all instances of the class)
    kingdom = "Animalia"

    # Constructor method (__init__) - called when an object is created
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method (operates on an instance of the class)
    def speak(self):
        return f"{self.name} makes a sound."

    def get_info(self):
        return f"{self.name} is {self.age} years old and belongs to {self.kingdom}."

# Creating objects (instances) of the Animal class
dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 2)

print(f"Dog's name: {dog.name}")
print(f"Cat's age: {cat.age}")
print(f"Dog's kingdom: {dog.kingdom}") # Accessing class attribute via instance

print(dog.speak())
print(cat.get_info())

# Inheritance: Creating a new class that inherits from an existing class
class Dog(Animal): # Dog inherits from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age) # Call the parent class's constructor
        self.breed = breed # New instance attribute for Dog

    # Overriding a parent method
    def speak(self):
        return f"{self.name} barks loudly!"

    # New method specific to Dog class
    def fetch(self):
        return f"{self.name} is fetching the ball!"

my_golden = Dog("Max", 4, "Golden Retriever")
print(my_golden.get_info()) # Inherited method
print(my_golden.speak())    # Overridden method
print(my_golden.fetch())    # New method
print(f"Max's breed: {my_golden.breed}")


# --- 6. Conditional Statements ---
print("\n--- 6. Conditional Statements ---")

# if statement
temperature = 25
if temperature > 30:
    print("It's a hot day!")

# if-else statement
grade = 65
if grade >= 60:
    print("You passed the exam.")
else:
    print("You need to study more.")

# if-elif-else statement (Ladder)
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
num = 15
if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not positive.")

# Ternary Operator (Conditional Expressions) - concise if-else for single line
age =  78
status = "Adult" if age >= 18 else "Minor"
print(f"Person is: {status}")


# --- 7. Loops (All Types) ---
print("\n--- 7. Loops (All Types) ---")

# 7.1. For Loop
print("\n--- For Loop ---")
# Iterating over a list
print("Iterating over a list (fruits):")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
print("\nIterating over a string:")
for char in "Python":
    print(char)

# Iterating with range()
# range(stop) - Generates numbers from 0 up to (but not including) stop
print("\nFor loop with range(5):")
for i in range(5): # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) - Generates numbers from start up to (but not including) stop
print("\nFor loop with range(2, 7):")
for i in range(2, 7): # 2, 3, 4, 5, 6
    print(i)

# range(start, stop, step) - Generates numbers from start up to stop, with a specified step
print("\nFor loop with range(1, 10, 2):")
for i in range(1, 10, 2): # 1, 3, 5, 7, 9
    print(i)

# Iterating over a dictionary (keys, values, items) - already shown in dictionary section
print("\nIterating over dictionary items (for loop):")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# For loop with 'break' (exits the loop entirely)
print("\nFor loop with 'break':")
for i in range(10):
    if i == 5:
        break # Exit loop when i is 5
    print(i)

# For loop with 'continue' (skips current iteration, continues with next)
print("\nFor loop with 'continue':")
for i in range(5):
    if i == 2:
        continue # Skip printing when i is 2
    print(i)

# For loop with 'else' block (executes if loop completes without a 'break')
print("\nFor loop with 'else' block:")
for i in range(3):
    print(i)
else:
    print("Loop finished without breaking.")

for i in range(5):
    if i == 2:
        # break # If uncommented, 'else' block won't execute
        pass # To show that 'else' executes if no break
    print(i)
else:
    print("Loop finished (even if it had a pass on condition).")



# 7.2. While Loop
print("\n--- While Loop ---")
# Definition: Repeats a block of code as long as a condition is True.
count = 0
while count < 3:
    print(f"While loop count: {count}")
    count += 1 # Increment count to eventually make the condition False

# While loop with 'break'
print("\nWhile loop with 'break':")
num = 0
while True: # Infinite loop condition
    print(f"Num: {num}")
    num += 1
    if num > 3:
        break # Exit loop when num is greater than 3

# While loop with 'continue'
print("\nWhile loop with 'continue':")
j = 0
while j < 5:
    j += 1 # Increment first, so 0 isn't skipped if it was the condition
    if j == 3:
        continue # Skip printing when j is 3
    print(f"Value of j: {j}")

# While loop with 'else' block (executes if loop condition becomes False, not by break)
print("\nWhile loop with 'else' block:")
k = 0
while k < 2:
    print(f"K is: {k}")
    k += 1
else:
    print("While loop finished normally (condition became false).")

# Example where 'else' doesn't execute (due to break)
m = 0
while m < 5:
    print(f"M is: {m}")
    if m == 2:
        break
    m += 1
else:
    print("This else block will NOT execute if break is hit.")

    
print("After the while loop (with potential break).")