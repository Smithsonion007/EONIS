import matplotlib.pyplot as plt
import numpy as np

def eonis_visualize(geometry_points, title="EONIS Sacred Geometry"):
    fig, ax = plt.subplots(figsize=(10, 10))
    for i, (x1, y1) in enumerate(geometry_points):
        for j, (x2, y2) in enumerate(geometry_points):
            if i != j:
                ax.plot([x1, x2], [y1, y2], color='blue', alpha=0.3, linewidth=0.5)
        ax.scatter(x1, y1, color='red', s=50, edgecolor='black", label="Encrypted Point" if i == 0 else "")
    theta = np.linspace(0, 4 * np.pi, 1000)
    r = np.exp(theta / (2 * np.pi)) * 0.5
    x_spiral = r * np.cos(theta)
    y_spiral = r * np.sin(theta)
    ax.plot(x_spiral, y_spiral, color='gold', linestyle='--', alpha=0.6, linewidth=2)
    ax.set_xlim(-1e-31, 1e-31)
    ax.set_ylim(-1e-31, 1e-31)
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    plt.title(title)
    plt.show()
