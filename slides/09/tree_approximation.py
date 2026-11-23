#!/usr/bin/env python3
"""Piecewise-constant approximation of a smooth function by trees of growing depth."""
import matplotlib.pyplot as plt
import numpy as np


def fit_tree(xs, ts, depth):
    """Greedily fit a 1-D regression tree minimizing the sum of squares, return (borders, values)."""
    if depth == 0 or len(xs) < 2 or np.allclose(ts, ts[0]):
        return [], [ts.mean()]

    best, best_loss = None, np.sum((ts - ts.mean()) ** 2)
    for i in range(1, len(xs)):
        left, right = ts[:i], ts[i:]
        loss = np.sum((left - left.mean()) ** 2) + np.sum((right - right.mean()) ** 2)
        if loss < best_loss:
            best, best_loss = i, loss
    if best is None:
        return [], [ts.mean()]

    threshold = (xs[best - 1] + xs[best]) / 2
    l_borders, l_values = fit_tree(xs[:best], ts[:best], depth - 1)
    r_borders, r_values = fit_tree(xs[best:], ts[best:], depth - 1)
    return l_borders + [threshold] + r_borders, l_values + r_values


generator = np.random.RandomState(7)
xs = np.sort(generator.uniform(0, 1, size=100))
target = lambda x: np.sin(2 * np.pi * x)
ts = target(xs) + generator.normal(0, 0.1, size=xs.shape)
grid = np.linspace(0, 1, 500)

for depth in [1, 2, 3, 6]:
    borders, values = fit_tree(xs, ts, depth)
    edges = np.concatenate([[0], borders, [1]])

    plt.figure(figsize=(4.2, 3.4))
    plt.plot(grid, target(grid), color="lightgray", lw=4, label="$f(x)$", zorder=1)
    plt.scatter(xs, ts, s=6, color="darkgray", zorder=2)
    for i, value in enumerate(values):
        plt.plot([edges[i], edges[i + 1]], [value, value], color="tab:red", lw=2.5, zorder=3,
                 label="tree" if i == 0 else None)
    for border in borders:
        plt.axvline(border, color="tab:blue", lw=0.8, ls=":", zorder=0)
    plt.title(f"depth {depth}: {len(values)} leaves")
    plt.ylim(-1.6, 1.6)
    plt.xlabel("$x$")
    plt.legend(loc="upper right", fontsize="small")
    plt.savefig(f"tree_approximation{depth}.svg", transparent=True, bbox_inches="tight")
    plt.close()
