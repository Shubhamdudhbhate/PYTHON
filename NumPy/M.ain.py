import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Combined trig waves ---

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x) * np.cos(x/2)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='sin(2x)*cos(x/2)')
plt.title('Combined Trigonometric Waves')
plt.legend()
plt.grid()
plt.show()


# --- 2. Polar plot of trig functions ---

theta = np.linspace(0, 2 * np.pi, 400)
r1 = np.abs(np.sin(3 * theta))
r2 = np.abs(np.cos(5 * theta))

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r1, label='|sin(3θ)|')
ax.plot(theta, r2, label='|cos(5θ)|')
ax.set_title('Polar Plot of Trigonometric Functions')
ax.legend()
plt.show()


# --- 3. Animated sine wave ---

fig, ax = plt.subplots()
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

x = np.linspace(0, 4 * np.pi, 1000)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    y = np.sin(x + 0.1 * frame)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=100, init_func=init,
                    blit=True, interval=30)

plt.title('Animated Sine Wave')
plt.show()


# --- 4. 3D wave surface plot ---

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('3D Wave Surface')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
