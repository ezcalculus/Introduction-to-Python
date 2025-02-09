import matplotlib.pyplot as plt
import numpy as np

# Setup canvas
fig, ax = plt.subplots(figsize=(8, 4))

# Create crystalline regions (rectangles)
for i in range(3):  # Number of crystalline regions
    for j in range(5):  # Number of rectangles in a crystalline region
        ax.add_patch(plt.Rectangle((j * 0.5 + i * 3, 0.5), 0.4, 1, color="blue", alpha=0.7))

# Create amorphous regions (random curves)
x_amorphous = np.linspace(-0.5, 15, 300)
y_amorphous = 0.5 + 0.2 * np.sin(10 * x_amorphous) + 0.05 * np.random.randn(300)
ax.plot(x_amorphous, y_amorphous, color="red", linewidth=1.5, alpha=0.8)

# Labels and styling
ax.set_xlim(-1, 16)
ax.set_ylim(0, 2)
ax.axis("off")
ax.set_title("Semi-Crystalline Polymer Structure", fontsize=14)

# Show the diagram
plt.show()
