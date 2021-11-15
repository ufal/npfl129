#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

xs = np.linspace(-2, 2, 401)

plt.figure(figsize=(7,5))
plt.plot(xs, xs < 0, label="Misclassification Error", zorder=11)
plt.plot(xs, 0.5 * (xs - 1) ** 2, label="Mean Squared Error", zorder=12)
plt.plot(xs, np.log (1 + np.exp(-xs)), label="Sigmoid NLL", zorder=13)
plt.plot(xs, np.maximum(0, 1 - xs), label="Hinge Loss", zorder=14)
plt.plot(xs, np.maximum(0, - xs), label="Perceptron Loss", zorder=13)
plt.xlabel("t⋅y")
plt.xlim(-2, 2)
plt.ylabel("L(t⋅y)")
plt.ylim(0, 3)
plt.gca().set_aspect(1)
plt.grid(True)
plt.title("Comparison of binary losses with {-1,1} targets")
plt.legend(loc="upper right")
plt.savefig("binary_losses.svg", transparent=True, bbox_inches="tight")
