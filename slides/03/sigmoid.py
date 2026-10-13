#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

xs = np.linspace(-4, 4, 100)
ys = 1 / (1 + np.exp(-xs))
ds = ys * (1 - ys)

plt.figure(figsize=(10,3))
plt.plot(xs, ys, label="Sigmoid")
plt.plot(xs, ds, label="Derivative of Sigmoid")
plt.xlabel("x")
plt.xlim(-3.5, 3.5)
plt.ylabel("σ(x)")
plt.yticks(np.arange(0, 1.01, step=0.25))
plt.gca().set_aspect(1)
plt.grid(True)
plt.title("Plot of the Sigmoid Function σ(x)")
plt.legend(loc="upper left")
plt.savefig("sigmoid.svg", transparent=True, bbox_inches="tight")
