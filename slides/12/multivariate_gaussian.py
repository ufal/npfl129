#!/usr/bin/env python3
# Based on https://scipython.com/blog/visualizing-the-bivariate-gaussian-distribution/
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# Our 2-dimensional distribution will be over variables X and Y
N = 60
X = np.linspace(-3, 3, N)
Y = np.linspace(-2, 4, N)
X, Y = np.meshgrid(X, Y)

def plot(sigma, name):
    # Mean vector and covariance matrix
    mu = np.array([0., 1.])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    # The distribution on the variables X, Y packed into pos.
    Z = scipy.stats.multivariate_normal(mu, sigma).pdf(pos)

    # Create a surface plot and projected filled contour plot under it.
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=2, cstride=2, linewidth=1, antialiased=True, cmap="plasma")
    ax.contourf(X, Y, Z, zdir='z', offset=-0.15, cmap="plasma")

    # Adjust the limits, ticks and view angle
    ax.set_zlim(-0.15,0.2)
    ax.set_zticks(np.linspace(0,0.2,5))
    ax.view_init(19, -21)
    ax.dist = 8

    plt.savefig("multivariate_gaussian_plot_{}.svg".format(name), transparent=True, bbox_inches="tight")

plot(np.eye(2), "eye")
plot([[0.3, 0], [0, 1.5]], "diag")
plot([[1, -0.8], [-0.8, 1]], "full")
