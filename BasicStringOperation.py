import re 

s = "Shubham is a good"

print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

print("__________________________________________________________________________________")


print(s.replace("good", "bad"))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.split())
print(s.split(" "))
print(s.find("good"))
print(s.index("good"))
print(s.count("o"))
print(s.startswith("Shubham"))
print(s.endswith("good"))
print(re.findall(r"\b\w{4}\b", s))  # Find all words with exactly 4 characters
print(re.sub(r"\b\w{4}\b", "****", s))  # Replace all 4-character words with ****

print("__________________________________________________________________________________")


print(s.isalnum())  # Check if all characters are alphanumeric
print(s.isalpha())  # Check if all characters are alphabetic
print(s.isdigit())  # Check if all characters are digits
print(s.islower())  # Check if all characters are lowercase 
print(s.isupper())  # Check if all characters are uppercase
print(s.isspace())  # Check if all characters are whitespace
print(s.isprintable())  # Check if all characters are printable


print("__________________________________________________________________________________")


print(s.center(30, '*'))  # Center the string with '*' padding
print(s.ljust(30, '-'))  # Left justify the string with '-' padding
print(s.rjust(30, '='))  # Right justify the string with '=' padding
print(s.zfill(30))  # Pad the string with zeros on the left to fill to 30 characters


print("__________________________________________________________________________________")


print(s.expandtabs(4))  # Replace tabs with spaces (4 spaces per tab)
print(s.removeprefix("Shubham "))  # Remove the prefix "Shubham "
print(s.removesuffix(" good"))  # Remove the suffix " good"     
print(s.partition("good"))  # Split the string at the first occurrence of "good"
print(s.rpartition("good"))  # Split the string at the last occurrence of "good
print(s.splitlines())  # Split the string into lines (not applicable here, but useful for multiline strings)
print(s.join(["Hello", "World"]))  # Join a list of strings with the original string as a separator

print("__________________________________________________________________________________")

s = "Hello, {name}! Welcome to the world of {lang}."
p = "Hello, {}! Welcome to the world of  Java."
print(s.translate(str.maketrans("aeiou", "12345")))  # Translate vowels to numbers
print(s.casefold())  # Casefold the string for case-insensitive comparisons 
print(p.format("Shubham"))  # Format the string with a placeholder 
print(s.format_map({"name": "Shubham", "lang": "Python"})) # Format the string using a mapping  


print("__________________________________________________________________________________")

s = "Hello, World!"

print(s.find("World"))
print(s.rfind("l"))
print(s.index("Hello"))
print(s.rindex("l"))