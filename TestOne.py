import matplotlib.pyplot as plt

# Create a square of a specific color
color = 'red'  # You can change this to any valid color name or specify a color in various ways
size = 100     # Size of the square in pixels

fig, ax = plt.subplots()
ax.set_facecolor(color)
ax.set_xlim([0, size])
ax.set_ylim([0, size])
ax.set_aspect('equal', 'box')

plt.axis('off')  # Turn off axis labels and ticks
plt.show()
