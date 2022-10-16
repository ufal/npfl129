#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 1, 100)
ys = xs * (1 - xs)

plt.figure(figsize=(8,4))
plt.plot(xs, ys)
plt.xlabel("φ")
plt.ylabel("variance")
plt.yticks(np.arange(0, 0.3, step=0.05))
plt.gca().set_aspect(1)
plt.grid(True)
plt.title("Bernoulli Variance")
plt.savefig("bernoulli_variance.svg", transparent=True, bbox_inches="tight")
