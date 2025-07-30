"""
Matplotlib Basics — Examples 1‑10
---------------------------------
Run as: python matplotlib_basics_1-10.py
Each block is self‑contained and shows its own window.
"""

import matplotlib.pyplot as plt
import numpy as np

# ---------- 1. Importing Matplotlib ----------
# (Already done above)

# ---------- 2. Line Plot ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.title("2. Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()

# ---------- 3. Bar Chart ----------
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

plt.figure()
plt.bar(categories, values, color='orange')
plt.title("3. Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ---------- 4. Scatter Plot ----------
x = [1, 2, 3, 4, 5]
y = [5, 15, 7, 10, 12]

plt.figure()
plt.scatter(x, y, color='red')
plt.title("4. Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# ---------- 5. Pie Chart ----------
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [20, 30, 25, 25]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)  #autopct='%1.1f%%'	Automatically prints the percentage on each slice with 1 decimal place.
plt.title("5. Pie Chart")
plt.axis('equal')  # Keep it circular
plt.show()





# ---------- 6. Histogram ----------
data = np.random.randn(1000)    # generates 1,000 samples from a standard normal

plt.figure()                          # plt.figure(figsize=(w, h))  (width and height).
plt.hist(data, bins=30, color='purple', edgecolor='black')       #bins=30 divides the data range into 30 equal‑width intervals.
plt.title(" Histogram ")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()




#

# ---------- 7. Multiple Lines in One Graph ----------
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [5, 15, 20, 25]

plt.figure()
plt.plot(x, y1, label='Line 1', color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label='Line 2', color='green', marker='x')
plt.title('7. Two Lines on Same Graph')
plt.xlabel('X‑Axis')
plt.ylabel('Y‑Axis')
plt.legend()
plt.grid(True)
plt.show()

# ---------- 8. Subplots (Two graphs side by side) ----------

#This creates a 4 × 4 grid, like:

# [ 1 ][ 2 ][ 3 ][ 4 ]
# [ 5 ][ 6 ][ 7 ][ 8 ]
# [ 9 ][10 ][11 ][12 ]
# [13 ][14 ][15 ][16 ]



x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)  # (rows, cols, index)
plt.plot(x, y)
plt.title("8a. Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("8b. Bar Chart")

plt.tight_layout()   #	Adjusts spacing to prevent text/axis overlapping
plt.show()




# ---------- 9. Styled Line Plot ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y, color='magenta', marker='s', linestyle='dotted', linewidth=2)
plt.title("9. Styled Line Plot")
plt.show()

# ---------- 10. Saving the Plot to a File ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.title("10. Saved Plot")
plt.savefig("saved_plot.png")   # Saves to the working directory
plt.show()

print("All 10 examples executed. Check 'saved_plot.png' for the saved image.")




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates

# ---------- 11. Multiple Line Plots using Loop ----------
x = [1, 2, 3, 4]
ys = [[10, 20, 25, 30], [5, 15, 20, 25], [7, 18, 22, 29]]
labels = ['Line A', 'Line B', 'Line C']

plt.figure()
for y, label in zip(ys, labels):
    plt.plot(x, y, label=label)

plt.title("11. Multiple Lines with Loop")
plt.legend()
plt.show()

# ---------- 12. Annotations ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.annotate('Max Point', xy=(4, 30), xytext=(3, 29),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("12. Annotated Point")
plt.show()





# ---------- 13. Fill Between Two Lines ----------
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5

plt.figure()
plt.plot(x, y1, label='Lower')
plt.plot(x, y2, label='Upper')
plt.fill_between(x, y1, y2, color='skyblue', alpha=0.3)   # opicity  0.3
plt.title("13. Fill Between Lines")
plt.legend()
plt.show()

# ---------- 14. Grid Styling ----------
x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

plt.figure()
plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("14. Grid Styled Plot")
plt.show()

# ---------- 15. Custom Tick Marks ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.xticks([1, 2, 3, 4], ['One', 'Two', 'Three', 'Four'])
plt.yticks([10, 20, 30], ['Low', 'Medium', 'High'])
plt.title("15. Custom Tick Labels")
plt.show()

# ---------- 16. Horizontal & Vertical Lines ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.axhline(y=20, color='red', linestyle='--')
plt.axvline(x=2, color='green', linestyle='--')
plt.title("16. Horizontal and Vertical Reference Lines")
plt.show()

# ---------- 17. Box Plot ----------                                            @@@@@ IMP
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure()
plt.boxplot(data)
plt.title("17. Box Plot")
plt.show()




# ---------- 18. Error Bars ----------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
errors = [1.5, 2.0, 1.0, 2.5]

plt.figure()
plt.errorbar(x, y, yerr=errors, fmt='-o', capsize=5)
plt.title("18. Error Bars")
plt.show()

# ---------- 19. Plot with Date Axis ----------
dates = [datetime.datetime(2025, 7, i+1) for i in range(5)]
values = [10, 12, 13, 15, 14]

plt.figure()
plt.plot(dates, values)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.gcf().autofmt_xdate()
plt.title("19. Date-Based Plot")
plt.show()

# ---------- 20. Plot from CSV File ----------
# First, create a sample CSV file (optional)
df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 25, 30]})
df.to_csv('data.csv', index=False)








# Now read and plot from CSV
data = pd.read_csv('data.csv')

plt.figure()
plt.plot(data['x'], data['y'])
plt.title("20. Plot from CSV")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()




days = [1, 2, 3, 4, 5]
sleep = [7, 8, 6, 7, 8]
study = [2, 3, 4, 3, 2]

plt.stackplot(days, sleep, study, labels=['Sleep', 'Study'], colors=['#add8e6', '#90ee90'])
plt.legend()
plt.title("Daily Routine")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()






x = np.linspace(0, 10, 10)
y = np.sin(x)

plt.stem(x, y)
plt.title("Stem Plot")
plt.show()










x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 2, 3, 4]

plt.plot(x, y1, 'r--', label='Squared')   # red dashed line
plt.plot(x, y2, 'g:', label='Linear')     # green dotted line
plt.legend()
plt.title("Line Styles")
plt.show()






import pandas as pd
import matplotlib.pyplot as plt

# Create sample data and save to CSV (you can skip this if you already have a CSV)
data = {'Year': [2020, 2021, 2022, 2023],
        'Sales': [250, 300, 400, 450]}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)

# Read and plot
df = pd.read_csv('sales.csv')
plt.plot(df['Year'], df['Sales'], marker='o')
plt.title("Sales Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.show()



data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, patch_artist=True, labels=['Std=1', 'Std=2', 'Std=3'],
            boxprops=dict(facecolor='lightblue'))
plt.title("Box Plot")
plt.show()



x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.axhline(y=20, color='red', linestyle='--')   # Horizontal line
plt.axvline(x=2, color='blue', linestyle=':')    # Vertical line
plt.axhspan(20, 25, color='yellow', alpha=0.2)   # Horizontal shaded area
plt.axvspan(2, 3, color='green', alpha=0.2)      # Vertical shaded area
plt.title("Lines and Spans")
plt.show()
