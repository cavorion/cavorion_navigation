def figure_02_position_grid():
    x = np.linspace(0, 100, 11)
    y = np.linspace(0, 100, 11)

    plt.figure(figsize=(8, 6))
    for xi in x:
        plt.axvline(xi, color="gray", linewidth=0.5, alpha=0.5)
    for yi in y:
        plt.axhline(yi, color="gray", linewidth=0.5, alpha=0.5)

    plt.scatter([42], [58], s=80)
    plt.title("Figure 02 — Position Grid")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(False)
    plt.savefig("outputs/figure-2-position-grid.png", dpi=150, bbox_inches="tight")
    plt.close()
    
if __name__ == "__main__":
    figure_01_linear_motion()
    figure_02_position_grid()
