#!/usr/bin/env python3
import argparse

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--beta", default=1.0, type=float, help="Harmonic mean beta")
parser.add_argument("--mean", default="harmonic", type=str, help="Mean type")
parser.add_argument("--output", type=str, help="Output file path")
parser.add_argument("--tangents", default=False, action="store_true", help="Draw tangents")
args = parser.parse_args()


def mean_arithmetic(p, r): return (p + r) / 2
def mean_geometric(p, r): return (p * r) ** 0.5
def mean_harmonic(p, r): return (1 + args.beta**2) * p * r / (args.beta**2 * p + r or 1)

ps = np.linspace(0, 1, 50)
rs = np.linspace(0, 1, 50)
fs = [[globals()["mean_{}".format(args.mean)](p, r) for p in ps] for r in rs]

levels = [0.25, 0.5, 0.75]
colors = ["#0aa", "#0a0", "#00a"]

cmap = plt.contourf(ps, rs, fs, levels=21, cmap="plasma")
cbar = plt.colorbar(cmap, ticks=[0] + levels + [1])
for label, color in zip(cbar.ax.get_yticklabels(), ["#000"] + colors + ["#000"]):
    label.set_color(color)
plt.contour(ps, rs, fs, levels=levels, colors=colors)

if args.tangents:
    for level, color in zip(levels, colors):
        p = level * (1 + args.beta) / (1 + args.beta**2)
        r = args.beta * p
        plt.axline((p, r), slope=-1, color=color, ls="dashed")
        plt.plot((0, p), (r, r), color=color, ls="dotted", lw=1)
        plt.plot((p, p), (0, r), color=color, ls="dotted", lw=1)
    plt.axline((0, 0), slope=args.beta, color="#000")

plt.gca().minorticks_on()
plt.gca().set_aspect(1)
plt.xlabel("precision")
plt.ylabel("recall")
plt.title("Precision-recall $\\mathbf{{{}}}$ mean{}".format(args.mean, ", $\\beta={}$".format(args.beta) if args.tangents else ""))

if args.output:
    plt.savefig(args.output, transparent=True, bbox_inches="tight")
else:
    plt.show()
