import numpy as np
import matplotlib.pyplot as plt


def figure_01_linear_motion():
    x = [0, 50]
    y = [0, 25]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.scatter([x[0]], [y[0]], label="Start")
    plt.scatter([x[-1]], [y[-1]], label="End")
    plt.title("Cavorion Navigation Prototype v0")
    plt.legend()
    plt.grid(True)
    plt.savefig("outputs/figure-01-linear-motion.png", dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    figure_01_linear_motion()

