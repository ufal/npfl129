#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

xs = np.linspace(-4, 4, 100)
ys = 1 / (1 + np.exp(-xs))
ds = ys * (1 - ys)

plt.plot(xs, 1 / (1 + np.exp(-xs)), label="σ(x)")
plt.plot(xs, 2 / (1 + np.exp(-xs)), label="2σ(x)")
plt.plot(xs, 2 / (1 + np.exp(-xs)) - 1, label="2σ(x) - 1")
plt.plot(xs, 2 / (1 + np.exp(-2*xs)) - 1, label="2σ(2x) - 1 = tanh(x)")
plt.xlabel("x")
plt.xlim(-3.5, 3.5)
plt.ylabel("value")
plt.ylim(-1, 2) #np.arange(-1, 2.25, step=0.25))
plt.gca().set_aspect(1)
plt.grid(True)
plt.title("From Sigmoid Function σ(x) to Tanh")
plt.legend(loc="upper left")
plt.savefig("sigmoid_to_tanh.svg", transparent=True, bbox_inches="tight")
