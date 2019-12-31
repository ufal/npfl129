#!/usr/bin/env python3
import argparse

import numpy as np

import matplotlib.patches
import matplotlib.pyplot as plt
import sklearn.datasets

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clusters", default=3, type=int, help="Number of clusters")
    parser.add_argument("--examples", default=200, type=int, help="Number of examples")
    parser.add_argument("--iterations", default=20, type=int, help="Number of kmeans iterations to perfom")
    parser.add_argument("--plot", default=False, action="store_true", help="Plot the results")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Generate artificial data
    data, target = sklearn.datasets.make_blobs(n_samples=args.examples, centers=args.clusters, n_features=2, random_state=args.seed)

    # Start by using the first `args.clusters` samples as the cluster representations,
    # identiy matrices as covariances and uniform distribution as the mixing coefficients.
    means = data[:args.clusters].copy()
    covs = np.stack([np.identity(data.shape[1])] * args.clusters)
    mixing_coefs = np.array([1 / args.clusters] * args.clusters)

    # TODO: Run `args.iterations` of the gaussian mixture fitting algorithm
    for iteration in range(args.iterations):
        # TODO: Evaluate responsibilities

        # TODO: Update cluster means, covariances and mixing coefficients.

        # TODO: Compute and print negative log likelihood of the current model.
        print("Loss after iteration {}: {:.1f}".format(
            iteration + 1,
            loss
        ))

    # Plot the points and fitted clusters as ellipses.
    if args.plot:
        colors = np.concatenate([[[1,0,0], [0,1,0], [0,0,1]],
                                 np.random.RandomState(4).uniform(size=[args.clusters, 3])], axis=0)[:-3]

        plt.gca().set_aspect(1)
        plt.scatter(data[:, 0], data[:, 1])
        for c in range(args.clusters):
            eigvalues, eigvectors = np.linalg.eigh(covs[c])
            ellipse = matplotlib.patches.Ellipse(
                xy=means[c], width=4*np.sqrt(eigvalues[0]), height=4*np.sqrt(eigvalues[1]),
                angle=np.rad2deg(np.arctan2(*eigvectors[0, ::-1])))
            ellipse.set_color(colors[c])
            ellipse.set_alpha(0.4)
            plt.gca().add_artist(ellipse)
        plt.show()
