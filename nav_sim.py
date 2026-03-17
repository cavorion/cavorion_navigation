import numpy as np
import matplotlib.pyplot as plt

# Initial position
position = np.array([0.0, 0.0])

# Initial direction (unit vector)
direction = np.array([1.0, 0.0])

# Speed
speed = 1.0

# Store trajectory
trajectory = [position.copy()]

for step in range(50):
    # Simulate a "turn" over time
    angle = 0.1  # change this to control turning

    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])

    # Rotate direction
    direction = rotation_matrix @ direction

    # Move spacecraft
    position = position + direction * speed

    trajectory.append(position.copy())

trajectory = np.array(trajectory)

# Plot
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.scatter(trajectory[0, 0], trajectory[0, 1], label="Start")
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], label="End")

plt.title("Cavorion Navigation Prototype v1 (Turning)")
plt.legend()
plt.grid()
plt.show()
