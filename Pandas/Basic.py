# ==============================================================
# 🛠️  ALL‑IN‑ONE  NumPy + pandas  QUICK‑START SCRIPT
# ==============================================================

import numpy as np
import pandas as pd

# --------------------------------------------------------------
# 1️⃣  NUMPY ESSENTIALS
# --------------------------------------------------------------
print("\n📌 1. NumPy basics\n" + "-"*30)


# Create arrays
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.arange(7, 13)            # [7 8 9 10 11 12]

print("arr1:", arr1)
print("arr2:", arr2)



# Reshape (2 rows, 3 cols)
arr1_2d = arr1.reshape(2, 3)
print("\narr1 reshaped:\n", arr1_2d)

# Vertical / horizontal stacking
v_stacked = np.vstack((arr1, arr2))        # shape (2, 6)
h_stacked = np.hstack((arr1, arr2[:6]))    # shape (12,)

print("\nVertical stack:\n", v_stacked)
print("\nHorizontal stack:\n", h_stacked)

# Basic arithmetic
print("\narr1 * 2:", arr1 * 2)
print("arr1 + arr2[:6]:", arr1 + arr2[:6])          #imp



# --------------------------------------------------------------
# 2️⃣  NUMPY ↔️ PANDAS BRIDGE
# --------------------------------------------------------------


print("\n📌 2. From NumPy to pandas\n" + "-"*30)

# Convert to DataFrame
df_from_np = pd.DataFrame(arr1_2d, columns=['A', 'B', 'C'])
print(df_from_np)

# Back to NumPy
back_to_np = df_from_np.values
print("\nBack to NumPy:\n", back_to_np)

# --------------------------------------------------------------
# 3️⃣  CREATE TWO DATAFRAMES FOR JOIN DEMOS
# --------------------------------------------------------------
print("\n📌 3. Build sample DataFrames\n" + "-"*30)


df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Score': [88, 92]
})

print("df1:\n", df1)
print("\ndf2:\n", df2)

# --------------------------------------------------------------
# 4️⃣  QUICK VIEW / FILTER / SORT
# --------------------------------------------------------------
print("\n📌 4. View, filter, sort\n" + "-"*30)

print("df1.head():\n", df1.head())
print("\nAge > 24:\n", df1[df1['Age'] > 24])
print("\nSorted by Age:\n", df1.sort_values('Age'))

# --------------------------------------------------------------
# 5️⃣  CONCATENATION  (stack rows)
# --------------------------------------------------------------
print("\n📌 5. pd.concat\n" + "-"*30)

concat_df = pd.concat([df1, df1])   # duplicate rows on purpose
print(concat_df)

# --------------------------------------------------------------
# 6️⃣  MERGES / JOINS
# --------------------------------------------------------------
print("\n📌 6. Joins with pd.merge\n" + "-"*30)

inner_join = pd.merge(df1, df2, on='ID')              # default 'inner'
left_join  = pd.merge(df1, df2, on='ID', how='left')  # left outer

print("\nInner join:\n", inner_join)
print("\nLeft  join:\n", left_join)

# --------------------------------------------------------------
# 7️⃣  MISSING‑VALUE HANDLING
# --------------------------------------------------------------
print("\n📌 7. Missing values\n" + "-"*30)

print("Null mask:\n", left_join.isnull())
print("\nFill NaN with 0:\n", left_join.fillna(0))

# --------------------------------------------------------------
# 8️⃣  GROUP‑BY AGGREGATION
# --------------------------------------------------------------
print("\n📌 8. Group‑by\n" + "-"*30)

df1['Gender'] = ['F', 'M', 'M']           # add a column for demo
print(df1.groupby('Gender')['Age'].mean())

# --------------------------------------------------------------
# 9️⃣  SAFE CSV READING  (handles EmptyDataError)
# --------------------------------------------------------------
print("\n📌 9. Safe CSV load\n" + "-"*30)

path = "maybe_empty.csv"   # change to your real file

try:
    safe_df = pd.read_csv(path)
    print(f"Loaded '{path}' successfully:")
    print(safe_df.head())
except pd.errors.EmptyDataError:
    print(f"❌ '{path}' is empty — no columns to parse.")
except FileNotFoundError:
    print(f"❌ '{path}' not found. Check the path.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# --------------------------------------------------------------
# 🔟  EXPORT EXAMPLE (commented out)
# --------------------------------------------------------------
# left_join.to_csv("joined_output.csv", index=False)
# print("\nFile 'joined_output.csv' written to disk.")
