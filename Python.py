# Fibonacci Series using while loop
n = 8
print(f"Fibonacci Series up to {n} terms:")
a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c 
    count += 1
