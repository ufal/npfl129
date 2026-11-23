#!/usr/bin/env python3
"""Linear regions of a ReLU network: every unit cuts the input space by a hyperplane."""
import matplotlib.pyplot as plt
import numpy as np

generator = np.random.RandomState(11)
units = 8
ws = generator.normal(0, 1, size=(units, 2))
ws /= np.linalg.norm(ws, axis=1, keepdims=True)
bs = generator.uniform(-0.6, 0.6, size=units)

grid = np.linspace(-1, 1, 801)
xs, ys = np.meshgrid(grid, grid)
points = np.stack([xs, ys], axis=-1)

for used in [1, 3, 8]:
    activations = (points @ ws[:used].T + bs[:used]) > 0
    codes = (activations * (2 ** np.arange(used))).sum(-1)
    unique = np.unique(codes)
    # Map each activation pattern to a pastel color.
    colors = plt.get_cmap("tab20")((np.arange(len(unique)) * 7) % 20)
    lookup = np.zeros(codes.max() + 1, dtype=int)
    lookup[unique] = np.arange(len(unique))

    plt.figure(figsize=(3.6, 3.6))
    plt.imshow(colors[lookup[codes]], origin="lower", extent=(-1, 1, -1, 1), alpha=0.55,
               interpolation="nearest")
    for w, b in zip(ws[:used], bs[:used]):
        if abs(w[1]) > abs(w[0]):
            plt.plot(grid, -(w[0] * grid + b) / w[1], color="black", lw=1.2)
        else:
            plt.plot(-(w[1] * grid + b) / w[0], grid, color="black", lw=1.2)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"{used} ReLU unit{'s' if used > 1 else ''}: {len(unique)} linear regions")
    plt.savefig(f"relu_regions{used}.svg", transparent=True, bbox_inches="tight")
    plt.close()
