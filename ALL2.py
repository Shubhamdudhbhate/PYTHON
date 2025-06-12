# --- 1. Lists ---
print("--- 1. Lists ---")
my_list = [10, 20, 30, "apple", True, 30]
print(f"Original List: {my_list}")

print(f"Element at index 0: {my_list[0]}")
print(f"Last element: {my_list[-1]}")

print(f"Slice from index 1 to 3 (exclusive): {my_list[1:4]}")
print(f"Slice from beginning to index 2 (exclusive): {my_list[:3]}")
print(f"Slice from index 3 to end: {my_list[3:]}")
print(f"List with step (every 2nd element): {my_list[::2]}")
print(f"Reversed list: {my_list[::-1]}")

my_list[0] = 5
print(f"List after changing index 0: {my_list}")

my_list.append("banana")
print(f"List after append('banana'): {my_list}")

my_list.insert(2, "grape")
print(f"List after insert(2, 'grape'): {my_list}")

my_list.remove(30)
print(f"List after remove(30): {my_list}")

popped_item = my_list.pop()
print(f"Popped item: {popped_item}, List after pop(): {my_list}")

popped_item_at_index = my_list.pop(1)
print(f"Popped item at index 1: {popped_item_at_index}, List after pop(1): {my_list}")

list_numbers = [5, 1, 9, 2, 7]
list_numbers.sort()
print(f"Sorted numbers list: {list_numbers}")

list_numbers.reverse()
print(f"Reversed sorted numbers list: {list_numbers}")

print(f"Length of list: {len(my_list)}")
print(f"Count of 'banana': {my_list.count('banana')}")

squares = [x**2 for x in range(5)]
print(f"Squares using list comprehension: {squares}")

# --- 2. Tuples ---
print("\n--- 2. Tuples ---")
my_tuple = (1, 2, "apple", 3.14, "apple")
print(f"Original Tuple: {my_tuple}")

print(f"Element at index 1: {my_tuple[1]}")

print(f"Slice from index 2 to end: {my_tuple[2:]}")

print(f"Count of 'apple': {my_tuple.count('apple')}")
print(f"Index of 3.14: {my_tuple.index(3.14)}")
print(f"Length of tuple: {len(my_tuple)}")

# --- 3. Dictionaries ---
print("\n--- 3. Dictionaries ---")
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True
}
print(f"Original Dictionary: {my_dict}")

print(f"Name: {my_dict['name']}")
print(f"City (using .get()): {my_dict.get('city', 'Unknown')}")
print(f"Country (using .get() with default): {my_dict.get('country', 'Not specified')}")

my_dict["email"] = "alice@example.com"
print(f"After adding email: {my_dict}")

my_dict["age"] = 31
print(f"After updating age: {my_dict}")

removed_value = my_dict.pop("is_student")
print(f"Removed 'is_student': {removed_value}, Dictionary after pop('is_student'): {my_dict}")

last_item = my_dict.popitem()
print(f"Removed last item: {last_item}, Dictionary after popitem(): {my_dict}")

del my_dict["city"]
print(f"After del 'city': {my_dict}")

print("\nIterating through dictionary keys:")
for key in my_dict:
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

def greet():
    print("Hello from a function!")

greet()

def add(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add(10, 5)
add(b=7, a=3)

def multiply(x, y):
    return x * y

product = multiply(4, 6)
print(f"The product of 4 and 6 is: {product}")

def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome("Charlie")
welcome()

def print_args(*args):
    print("Arbitrary arguments:")
    for arg in args:
        print(arg)

print_args(1, "hello", True, [1, 2])

def print_kwargs(**kwargs):
    print("Arbitrary keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(city="London", population=8.9, landmark="Tower Bridge")

square = lambda x: x * x
print(f"Square of 7 (using lambda): {square(7)}")

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers (using map and lambda): {doubled}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using filter and lambda): {evens}")

# --- 5. Object-Oriented Programming (OOP) ---
print("\n--- 5. Object-Oriented Programming (OOP) ---")

class Animal:
    species = "Animalia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def get_info(self):
        return f"{self.name} is {self.age} years old and belongs to {self.species}."

dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 2)

print(f"Dog's name: {dog.name}")
print(f"Cat's age: {cat.age}")
print(f"Dog's species: {dog.species}")

print(dog.speak())
print(cat.get_info())

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks loudly!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

my_golden = Dog("Max", 4, "Golden Retriever")
print(my_golden.get_info())
print(my_golden.speak())
print(my_golden.fetch())
print(f"Max's breed: {my_golden.breed}")

# --- 6. Conditional Statements ---
print("\n--- 6. Conditional Statements ---")

temperature = 25
if temperature > 30:
    print("It's a hot day!")

grade = 65
if grade >= 60:
    print("You passed the exam.")
else:
    print("You need to study more.")

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

num = 15
if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not positive.")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Person is: {status}")

# --- 7. Loops (All Types) ---
print("\n--- 7. Loops (All Types) ---")

print("\n--- For Loop ---")
print("Iterating over a list (fruits):")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nIterating over a string:")
for char in "Python":
    print(char)

print("\nFor loop with range(5):")
for i in range(5):
    print(i)

print("\nFor loop with range(2, 7):")
for i in range(2, 7):
    print(i)

print("\nFor loop with range(1, 10, 2):")
for i in range(1, 10, 2):
    print(i)

print("\nIterating over dictionary items (for loop):")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print("\nFor loop with 'break':")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\nFor loop with 'continue':")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\nFor loop with 'else' block:")
for i in range(3):
    print(i)
else:
    print("Loop finished without breaking.")

for i in range(5):
    if i == 2:
        pass
    print(i)
else:
    print("Loop finished (even if it had a pass on condition).")

print("\n--- While Loop ---")
count = 0
while count < 3:
    print(f"While loop count: {count}")
    count += 1

print("\nWhile loop with 'break':")
num = 0
while True:
    print(f"Num: {num}")
    num += 1
    if num > 3:
        break

print("\nWhile loop with 'continue':")
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(f"Value of j: {j}")

print("\nWhile loop with 'else' block:")
k = 0
while k < 2:
    print(f"K is: {k}")
    k += 1
else:
    print("While loop finished normally (condition became false).")

m = 0
while m < 5:
    print(f"M is: {m}")
    if m == 2:
        break
    m += 1
else:
    print("This else block will NOT execute if break is hit.")
print("After the while loop (with potential break).")