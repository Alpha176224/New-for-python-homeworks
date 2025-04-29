import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Task 1: Basic Plotting
x1 = np.linspace(-10, 10, 400)
y1 = x1**2 - 4*x1 + 4
plt.figure()
plt.plot(x1, y1)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.grid(True)
plt.savefig("task1_basic_plot.png")

# Task 2: Sine and Cosine Plot
x2 = np.linspace(0, 2 * np.pi, 400)
y2_sin = np.sin(x2)
y2_cos = np.cos(x2)
plt.figure()
plt.plot(x2, y2_sin, 'r--', label='sin(x)')
plt.plot(x2, y2_cos, 'b-o', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid(True)
plt.savefig("task2_sine_cosine.png")

# Task 3: Subplots
x3 = np.linspace(-2, 2, 400)
x3_log = np.linspace(0, 5, 400)
fig3, axs = plt.subplots(2, 2)
axs[0, 0].plot(x3, x3**3, 'm')
axs[0, 0].set_title("f(x) = x^3")
axs[0, 1].plot(x3, np.sin(x3), 'g')
axs[0, 1].set_title("f(x) = sin(x)")
axs[1, 0].plot(x3, np.exp(x3), 'c')
axs[1, 0].set_title("f(x) = exp(x)")
axs[1, 1].plot(x3_log, np.log(x3_log + 1), 'orange')
axs[1, 1].set_title("f(x) = log(x+1)")
for ax in axs.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
plt.tight_layout()
plt.savefig("task3_subplots.png")

# Task 4: Scatter Plot
x4 = np.random.uniform(0, 10, 100)
y4 = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x4, y4, c='purple', marker='x')
plt.title("Random 2D Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("task4_scatter.png")

# Task 5: Histogram
data5 = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data5, bins=30, alpha=0.7, color='steelblue')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("task5_histogram.png")

# Task 6: 3D Plotting
fig6 = plt.figure()
ax6 = fig6.add_subplot(111, projection='3d')
x6 = np.linspace(-5, 5, 100)
y6 = np.linspace(-5, 5, 100)
x6, y6 = np.meshgrid(x6, y6)
z6 = np.cos(x6**2 + y6**2)
surf = ax6.plot_surface(x6, y6, z6, cmap='viridis')
fig6.colorbar(surf)
ax6.set_title("3D Surface Plot: f(x, y) = cos(x² + y²)")
ax6.set_xlabel("x")
ax6.set_ylabel("y")
ax6.set_zlabel("f(x, y)")
plt.savefig("task6_3d_surface.png")

# Task 7: Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'green', 'blue', 'orange', 'purple']
plt.figure()
plt.bar(products, sales, color=colors)
plt.title("Sales Data for Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.savefig("task7_bar_chart.png")

# Task 8: Stacked Bar Chart
periods = ['T1', 'T2', 'T3', 'T4']
cat_a = np.array([5, 7, 6, 8])
cat_b = np.array([3, 6, 5, 4])
cat_c = np.array([4, 2, 3, 5])
plt.figure()
plt.bar(periods, cat_a, label='Category A', color='skyblue')
plt.bar(periods, cat_b, bottom=cat_a, label='Category B', color='salmon')
plt.bar(periods, cat_c, bottom=cat_a+cat_b, label='Category C', color='lightgreen')
plt.title("Stacked Bar Chart")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend()
plt.savefig("task8_stacked_bar_chart.png")
