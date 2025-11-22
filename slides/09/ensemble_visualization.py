#!/usr/bin/env python3
import argparse
import cmath

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--models", default=7, type=int, help="Number of models")
parser.add_argument("--output", type=str, help="Output file path")
parser.add_argument("--runs", default=1, type=int, help="Number of runs")
parser.add_argument("--seed", default=42, type=int, help="Random seed")
parser.add_argument("--skip", default=0, type=int, help="Skip that many runs")
args = parser.parse_args()

np.random.seed(args.seed)
xs, ys = [[] for _ in range(args.runs)], [[] for _ in range(args.runs)]
rs, ps = [[] for _ in range(args.runs)], [[] for _ in range(args.runs)]

fig = plt.figure(figsize=(2*args.models, 2))
for i in range(1, args.models + 1):
    for run in range(args.runs):
        x, y = None, None
        while x is None or x * x + y * y > 1:
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
        x, y = x * 0.95, y * 0.95
        xs[run].append(x)
        ys[run].append(y)

        r, p = cmath.polar(x + y * 1j)
        rs[run].append(r)
        ps[run].append(p)

    ers, eps = [], []
    for run in range(args.runs):
        r, p = cmath.polar(np.mean(xs[run]) + np.mean(ys[run]) * 1j)
        ers.append(r)
        eps.append(p)

    ax = fig.add_subplot(1, args.models, i, polar=True)
    ax.scatter(np.ravel(ps[args.skip:]), np.ravel(rs[args.skip:]), color="r", marker="o", s=60, zorder=2)
    ax.scatter(eps[args.skip:], ers[args.skip:], color="b", marker="*", s=60, zorder=3)
    ax.set_ylim(0, 1)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
plt.tight_layout(pad=0)

if args.output:
    plt.savefig(args.output, transparent=True, bbox_inches="tight")
else:
    plt.show()
