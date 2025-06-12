f = open("demo.txt", "w")
f.write("Hello\nI am Shubham from VJTI.\nI am Sujit from IITB.")
f.close()




print("1.\nNEXT:::")




f = open("demo.txt", "r")
print(f.read())
f.close()

print("\nNEXT:::")


f = open("demo.txt", "r")
print(f.readline())  # Line 1
print(f.readline())  # Line 2
print(f.readline())  # Line 3
f.close()

print("2.\nNEXT:::")

f = open("demo.txt", "r")
lines = f.readlines()
print(lines)
f.close()

print("3.\nNEXT:::")


f = open("demo.txt", "r+")
f.write("Shubham is coder")  # Overwrites from beginning
f.seek(0)
print(f.read())
f.close()


print("4.\nNEXT:::")


f = open("demo.txt", "a")
f.write("\nI love Python programming.")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()

print("5.\nNEXT:::")

f = open("sd.txt", "w+")
f.write("New content here")
f.seek(0)  # Move to start
print(f.read())
f.close()



print("6.\nNEXT:::")


f = open("demo.txt", "a+")
f.write("\nThis is the a+ mode.")
f.seek(0)
print(f.read())
f.close()







print("7.\nNEXT:::")



f = open("demo.txt", "a+")
f.write("\nThis is the a+ mode.")
f.seek(0)
print(f.read())
f.close()

print("8.\nNEXT:::")


with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())


print("9.\nNEXT:::")


f = open("demo.txt", "r")
print("Pointer at:", f.tell())      # ➤ 0
print("Reading:", f.read(10))       # ➤ Reads first 10 characters
print("Pointer now:", f.tell())     # ➤ 10
f.seek(0)                           # ➤ Go back to start
print("After seek:", f.read(10))    # ➤ Again reads first 10
f.close()


print("10.\nNEXT:::")


import os

if os.path.exists("demo.txt"):
    print("File exists.")
else:
    print("File does not exist.")

    print("11.\nNEXT:::")

try:
    f = open("nonexistent.txt", "r")
    print(f.read())#HHHHHHHHHHHHHHHHHHHHHHHHHH
    f.close()
except FileNotFoundError:
    print("File not found.")

    print("12.\nNEXT:::")



print("13.\nNEXT:::")

f = open("newfile.txt", "w")
lines = ["Line 1\n", "Line 2\n", "Line 3\n","HELLO SHUBHAM\n"]
f.writelines(lines)
f.close()


# Reading back
f = open("newfile.txt", "r")
print(f.read())
f.close()




print("14.\nNEXT:::")

f = open("demo.txt", "r")
data = f.read()
lines = data.splitlines() #  split into lines
words = data.split()   #  split into Words
chars = len(data)     # counts characters

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)
f.close()




print("15.\nNEXT:::")

f1 = open("demo.txt", "r")
f2 = open("copy.txt", "w")
for lin in f1:
    f2.write(lin)
f1.close()
f2.close()




print("16.\nNEXT:::")

import os

if os.path.exists("copy.txt"):
    os.remove("copy.txt")
    print("File deleted.")
else:
    print("File does not exist.")





print("17.\nNEXT:::")

with open("demo.txt", "a") as f:
# f.open("demo.txt","a")
   f.writelines(["\nNew Line 1", "\nNew Line 2"])







print("18.\nNEXT:::")

import os

file_path = "C:/Users/Lenovo/Desktop/image.jpg"

if os.path.exists(file_path):
   try:
     with open("C:/Users/Lenovo/Desktop/image.jpg", "rb") as f:
        data = f.read(20)
        print("Read success:", data)
   except PermissionError:
    print("❌ Permission denied. Try using a copy or running as admin.")


else:
    print("❌ File not found:", file_path)





print("19.\nNEXT:::")

import os

file_path = "C:/Users/Lenovo/Desktop/image.jpg"

if os.path.exists(file_path):
   with open("sample.txt", "wb") as f:
    f.write(b"Binary test content")

   with open("sample.txt", "rb") as f:
    print(f.read())



else:
    print("❌ File not found:", file_path)

