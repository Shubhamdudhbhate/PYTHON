import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Trigonometric functions
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
y_cot = 1 / np.tan(x)
y_sec = 1 / np.cos(x)
y_csc = 1 / np.sin(x)

# Set up subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle('Trigonometric Function Graphs', fontsize=16)

# Plot each trigonometric function
axs[0, 0].plot(x, y_sin, label='sin(x)', color='blue')
axs[0, 0].set_title('Sine')
axs[0, 0].grid()

axs[0, 1].plot(x, y_cos, label='cos(x)', color='green')
axs[0, 1].set_title('Cosine')
axs[0, 1].grid()

axs[1, 0].plot(x, y_tan, label='tan(x)', color='orange')
axs[1, 0].set_title('Tangent')
axs[1, 0].set_ylim(-10, 10)
axs[1, 0].grid()

axs[1, 1].plot(x, y_cot, label='cot(x)', color='purple')
axs[1, 1].set_title('Cotangent')
axs[1, 1].set_ylim(-10, 10)
axs[1, 1].grid()

axs[2, 0].plot(x, y_sec, label='sec(x)', color='red')
axs[2, 0].set_title('Secant')
axs[2, 0].set_ylim(-10, 10)
axs[2, 0].grid()

axs[2, 1].plot(x, y_csc, label='csc(x)', color='brown')
axs[2, 1].set_title('Cosecant')
axs[2, 1].set_ylim(-10, 10)
axs[2, 1].grid()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# ---------------------------
# Sample Bar Graph
# ---------------------------

labels = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 36]

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='skyblue')
plt.title('Sample Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()
