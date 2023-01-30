import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Create a figure and an axes object
fig, ax = plt.subplots()

# Set the axes limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the theta angle at 0
theta = 0

# Create a scatter plot of a circle
circle = ax.scatter(0, 0, c="b", s=100)

# Define the update function that will be called on each frame
def update(frame):
    global theta
    # Increment the theta angle
    theta += 1
    
    # Compute the x and y coordinates of the circle
    x = np.cos(theta)
    y = np.sin(theta)
    
    # Update the coordinates of the circle
    circle.set_offsets([x, y])
    
    # Return the circle object
    return circle,

# Create the animation object
anim = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 360), interval=20)

# Show the animation
plt.show()