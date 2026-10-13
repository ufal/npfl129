#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

xs = np.linspace(-5, 5, 100)
ys1 = scipy.stats.norm.pdf(xs, loc=0, scale=1)
ys2 = scipy.stats.norm.pdf(xs, loc=0, scale=4)

plt.figure(figsize=(6,4))
plt.plot(xs, ys1, label="Low entropy")
plt.plot(xs, ys2, label="High entropy")
plt.xlabel("x")
plt.ylabel("probability density")
plt.title("PDF of a Normal Distribution")
plt.legend(loc="upper right")
plt.grid(True)
plt.savefig("entropy_example.svg", transparent=True, bbox_inches="tight")
