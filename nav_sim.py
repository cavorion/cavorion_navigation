def figure_04_reference_stars():
    stars = {
        "A": (10, 80),
        "B": (80, 85),
        "C": (50, 20),
    }

    plt.figure(figsize=(8, 6))
    for name, (x, y) in stars.items():
        plt.scatter(x, y, s=120)
        plt.text(x + 2, y + 2, name)

    plt.title("Figure 04 — Reference Stars")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.savefig("outputs/figure-4-reference-stars.png", dpi=150, bbox_inches="tight")
    plt.close()
