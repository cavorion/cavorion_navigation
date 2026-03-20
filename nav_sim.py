def figure_03_linear_motion():
    t = np.linspace(0, 10, 100)
    x = 5 * t
    y = 2.5 * t

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=2)
    plt.scatter(x[0], y[0], label="Start")
    plt.scatter(x[-1], y[-1], label="End")
    plt.title("Figure 03 — Linear Motion Progression")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.grid(True)
    plt.savefig("outputs/figure-3-linear-motion.png", dpi=150, bbox_inches="tight")
    plt.close()
