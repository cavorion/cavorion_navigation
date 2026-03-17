import numpy as np
import matplotlib.pyplot as plt

# Initial position (x, y)
position = np.array([0.0, 0.0])

# Velocity (direction + speed)
velocity = np.array([1.0, 0.5])

# Store trajectory
trajectory = [position.copy()]

# Simulate movement
for _ in range(50):
    position = position + velocity
    trajectory.append(position.copy())

trajectory = np.array(trajectory)

# Plot
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.scatter(trajectory[0, 0], trajectory[0, 1], label="Start")
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], label="End")

plt.title("Cavorion Navigation Prototype v0")
plt.legend()
plt.grid()
plt.show()
