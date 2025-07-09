import numpy as np


# ✅ 2. Create Arrays

a = np.array([1, 2, 3])                      # 1D array
b = np.array([[1, 2], [3, 4]])               # 2D array
c = np.zeros((2, 3))                         # Array of zeros 2by 3
d = np.ones((3, 3))                          # Array of ones  3 by 3
e = np.full((2, 2), 7)                       # Array filled with 7
f = np.eye(3)                                # Identity matrix
g = np.random.rand(2, 3)                     # Random values [0,1)
h = np.random.randint(0, 10, size=(2, 3))    # Random integers

print(a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n")


# ✅ 3. Array Properties

a.shape            # Shape of array
a.ndim             # Number of dimensions
a.dtype            # Data type of elements
a.size             # Total number of elements
a.itemsize         # Size of each element in bytes

print(a.shape,"\n" ,a.ndim,"\n",a.dtype,"\n", a.size,"\n" ,a.itemsize ,"\n" )



# ✅ 4. Reshaping Arrays

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a,"\n")

print(a.reshape(3, 2),"\n")

print(a.flatten() ,"\n")



# ✅ 5. Array Indexing & Slicing

a = np.array([[1, 2, 3], [4, 5, 6]])

a[1, 2]          # Element at row 1, col 2 → 6
a[:, 1]          # All rows, column 1 → [2, 5]
a[0, :]          # First row → [1, 2, 3]
a[1, 0:2]        # Row 1, cols 0 and 1 → [4, 5]



# ✅ 6. Array Operations

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

x + y            # Element-wise addition
x - y            # Element-wise subtraction
x * y            # Element-wise multiplication
x / y            # Element-wise division
np.dot(x, y)     # Dot product

np.sum(x)        # Sum of elements
np.mean(x)       # Mean of elements
np.max(x)        # Maximum value
np.min(x)        # Minimum value
np.std(x)        # Standard deviation



# ✅ 7. Broadcasting

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])

a + b        # b is broadcasted across rows



# ✅ 8. Comparison & Boolean Indexing

a = np.array([1, 2, 3, 4, 5])
a > 2                      # [False, False, True, True, True]
a[a > 2]                  # [3, 4, 5]



# ✅ 9. Useful Functions

np.arange(0, 10, 2)            # [0 2 4 6 8]
np.linspace(0, 1, 5)           # [0.   0.25 0.5  0.75 1.]
np.unique([1, 2, 2, 3])        # [1 2 3]
np.sort([3, 1, 2])             # [1 2 3]
np.concatenate([a, b])         # Join arrays


# ✅ 10. Save and Load Arrays

np.save('my_array.npy', a)       # Save to .npy file
np.load('my_array.npy')          # Load .npy file

np.savetxt('data.txt', a)        # Save to .txt file
np.loadtxt('data.txt')           # Load from .txt

# ✅ 11. Matrix Operations

A = np.array([[1, 2], [3, 4]])

A.T              # Transpose
np.linalg.inv(A) # Inverse
np.linalg.det(A) # Determinant
np.linalg.eig(A) # Eigenvalues and eigenvectors

print(np.linalg.eig(A))



# ✅ 12. Random Functions
np.random.seed(42)              # Set seed for reproducibility
np.random.rand(3)               # 1D array with random floats
np.random.randn(3, 3)           # Normal distribution
np.random.randint(1, 10, 5)     # Random ints between 1 and 9











# ✅ 13. Copy vs View
a = np.array([1, 2, 3])
b = a.view()        # b is a view (changes affect `a`)
c = a.copy()        # c is a deep copy (independent)

b[0] = 100
# a → [100, 2, 3]
# c → [1, 2, 3]






# ✅ 14. Axis Explained
# Axis 0 → rows (vertical)
# Axis 1 → columns (horizontal)

a = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(a, axis=0)   # [5, 7, 9] → column-wise sum
np.sum(a, axis=1)   # [6, 15]   → row-wise sum






# ✅ 15. Stacking Arrays
a = np.array([1, 2])
b = np.array([3, 4])

np.stack((a, b))           # [[1, 2], [3, 4]]
np.hstack((a, b))          # [1, 2, 3, 4] → horizontal stack
np.vstack((a, b))          # [[1, 2], [3, 4]] → vertical stack
np.column_stack((a, b))    # [[1, 3], [2, 4]]





# ✅ 16. Splitting Arrays
a = np.array([[1, 2, 3], [4, 5, 6]])

np.hsplit(a, 3)       # Split into 3 columns
np.vsplit(a, 2)       # Split into 2 rows





# ✅ 17. Masking and Filtering
a = np.array([1, 2, 3, 4, 5])
mask = a > 3
filtered = a[mask]       # [4, 5]






# ✅ 18. Handling NaNs                            
a = np.array([1, 2, np.nan, 4])                    # IMP

np.isnan(a)              # [False, False, True, False]
np.nanmean(a)            # Mean ignoring NaN
np.nan_to_num(a)         # Replace NaN with 0








# ✅ 19. Fancy Indexing
a = np.array([10, 20, 30, 40])
indices = [0, 2]
a[indices]               # [10, 30]







# ✅ 20. Conditional Replacement
a = np.array([1, 2, 3, 4, 5])
np.where(a > 3, 100, a)   # Replace values > 3 with 100 → [1, 2, 3, 100, 100]







# ✅ 21. Math & Trig Functions                           
a = np.array([0, np.pi / 2, np.pi])
np.sin(a)              # [0.0, 1.0, 0.0]
np.log([1, np.e , np.e**2])      # [0.0, 1.0,2.0]
np.exp([0, 1,2])         # [1.0, 2.718..., 4....]






# ✅ 22. Memory Efficiency
a = np.array([1, 2, 3], dtype=np.int8)       # Smaller type = less memory
b = np.array([1.0, 2.0, 3.0], dtype=np.float64)





# ✅ 23. Flatten vs Ravel

a = np.array([[1, 2], [3, 4]])

a.flatten()      # Returns a copy → [1, 2, 3, 4]  	New array
a.ravel()        # Returns a view → [1, 2, 3, 4]    Same memory





# ✅ 24. Matrix Multiplication           
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)           # Matrix multiplication
A @ B                  # Shorthand for dot product   for higher dimension


# ✅ 25. Broadcasting Rules Summary
# Shapes must be compatible:
# (3, 1) + (1, 4) → (3, 4)

a = np.array([[1], [2], [3]])  # shape: (3,1)
b = np.array([10, 20, 30, 40]) # shape: (4,)
c = a + b                      # shape: (3,4)

print (c)



# ✅ 26. Generate Special Sequences

np.identity(4)                  # 4x4 Identity matrix
np.diag([1, 2, 3])              # Diagonal matrix
np.tile([1, 2], (3,2 ))         # Repeat pattern → [[1,2],[1,2],[1,2]]   3 by 2  

print(np.tile([1, 2], (3,3)))
                                 





# ✅ 27. Clip and Clamp

a = np.array([1, 5, 10, 15])
np.clip(a, 3, 10)       # [3, 5, 10, 10] → Clamp between 3 and 10    
print(np.clip(a, 3, 10))   


# If element < 3, it becomes 3
# If element > 10, it becomes 10
# Else, it stays unchanged









# ✅ 28. Counting & Binning

a = np.array([1, 1, 2, 3, 3, 3])
np.unique(a, return_counts=True)     # ([1, 2, 3], [2, 1, 3])   
unique_vals, counts = np.unique(a, return_counts=True)
print(unique_vals)   # [1 2 3]       sort the array
print(counts)        # [2 1 3]    gives frequency




# ✅ 29. argmax() and argmin() — Index of max/min value

a = np.array([3, 7, 2, 9])
print(np.argmax(a))   # Index of max → 3
print(np.argmin(a))   # Index of min → 2







# ✅ 30. argsort() — Indices that would sort the array

a = np.array([3, 1, 4])
print(np.argsort(a))   # [1, 0, 2] → positions of sorted values




# ✅ 31. any() and all()

a = np.array([0, 1, 2])
print(np.any(a))     # True → At least one non-zero
print(np.all(a))     # False → Not all non-zero









# ✅ 32. reshape() with -1 (auto-infer dimension)          

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(2, -1))   # → [[1 2 3], [4 5 6]]    -1 means auto row or col








# ✅ 33. astype() — Convert data type

a = np.array([1.5, 2.3])
b = a.astype(int)     # [1, 2]
c = a.astype(float)     # [5, 3]

print(a,"\n",b,"\n",c,"\n")






# ✅ 34. cumsum() and cumprod() — Cumulative Sum/Product

a = np.array([1, 2, 3,4,5])
print(np.cumsum(a))   # [1, 3, 6,10,15]
print(np.cumprod(a))  # [1, 2, 6,24,120]







# ✅ 35. setdiff1d(), intersect1d() — Set Operations              

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print(np.setdiff1d(a, b))     # [1]     a-b
print(np.intersect1d(a, b))   # [2 3]   a&b




# ✅ 36. clip() with min & max arrays               

x = np.array([5, 15, 25])
min_vals = np.array([0, 10, 20])
max_vals = np.array([10, 20, 30])
print(np.clip(x, min_vals, max_vals))  # [5 15 25]


# Values below min → become min
# Values above max → become max
# Values within range → stay same




# ✅ 37. round(), floor(), ceil()

x = np.array([1.3, 2.7, 3.5])
y = np.array([1.7, 2.5, 3.5])

print(np.round(x))  # [1. 3. 4.]
print(np.floor(x))  # [1. 2. 3.] 
print(np.ceil(x))   # [2. 3. 4.]

print(np.round(y))  # [1. 3. 4.]
print(np.floor(y))  # [1. 2. 3.]
print(np.ceil(y))   # [2. 3. 4.]





# 🔹 38. np.meshgrid() — Create coordinate grids (for 3D plotting, surface plots)

x = np.array([1, 2, 3])     # Co-ordinate system  x: x-axis  and y: y-axis
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
# X → [[1 2 3]
#       [1 2 3]]
# Y → [[4 4 4]
#       [5 5 5]]


# 🔹 43. np.array_equal() — Compare if two arrays are exactly the same 

a = np.array([1, 2])
b = np.array([1, 2])
np.array_equal(a, b)   # True



# 🔹 45. np.delete(), np.insert(), np.append()

a = np.array([1, 2, 3])

np.append(a, 4)          # → [1, 2, 3, 4]
np.insert(a, 1, 100)     # → [1, 100, 2, 3]
np.delete(a, 0)          # → [2, 3]