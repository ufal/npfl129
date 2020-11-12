#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-2, 2, 50)
ys = np.linspace(-2, 2, 50)
cs = np.array([[0, -1], [-1, 1], [1, 1]])

def rbf(x, z, gamma):
    return np.exp(-gamma * np.linalg.norm(x - z))

for gamma, ax in zip([1, 2, 0.5], plt.subplots(ncols=3)[1]):
    k = np.zeros((len(ys), len(xs), 3))
    for y in range(len(ys)):
        for x in range(len(xs)):
            for c in range(len(cs)):
                k[y, x, c] = rbf([ys[y], xs[x]], cs[c], gamma)
    ax.set_aspect(1)
    ax.set_title("RBF kernel, γ={}".format(gamma))
    ax.imshow(k, extent=[min(xs), max(xs), min(ys), max(ys)])
plt.savefig("rbf_kernel.svg", transparent=True, bbox_inches="tight")
