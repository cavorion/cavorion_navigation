def figure_05_trilateration():
    stars = [(10, 80), (80, 85), (50, 20)]
    craft = (42, 58)

    plt.figure(figsize=(8, 6))
    for sx, sy in stars:
        plt.scatter(sx, sy, s=100)
        radius = np.sqrt((craft[0] - sx) ** 2 + (craft[1] - sy) ** 2)
        circle = plt.Circle((sx, sy), radius, fill=False, alpha=0.5)
        plt.gca().add_patch(circle)

    plt.scatter(craft[0], craft[1], s=120, label="Estimated Position")
    plt.title("Figure 05 — Trilateration")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    plt.grid(True)
    plt.savefig("outputs/figure-5-trilateration.png", dpi=150, bbox_inches="tight")
    plt.close()
