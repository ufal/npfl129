#!/usr/bin/env python3
import argparse

import numpy as np
import scipy.stats

import sklearn.datasets

parser = argparse.ArgumentParser()
# These arguments will be set appropriately by ReCodEx, even if you change them.
parser.add_argument("--clusters", default=3, type=int, help="Number of clusters")
parser.add_argument("--examples", default=200, type=int, help="Number of examples")
parser.add_argument("--init", default="random", type=str, help="Initialization (random/kmeans++)")
parser.add_argument("--iterations", default=10, type=int, help="Number of kmeans iterations to perfom")
parser.add_argument("--plot", default=False, const=True, nargs="?", type=str, help="Plot the predictions")
parser.add_argument("--recodex", default=False, action="store_true", help="Running in ReCodEx")
parser.add_argument("--seed", default=42, type=int, help="Random seed")
# If you add more arguments, ReCodEx will keep them with your default values.

def plot(
    args: argparse.Namespace, iteration: int, data: np.ndarray,
    r: np.ndarray, means: np.ndarray, covs: np.ndarray, colors: np.ndarray,
) -> None:
    import matplotlib.patches
    import matplotlib.pyplot as plt

    if args.plot is not True:
        if not plt.gcf().get_axes(): plt.figure(figsize=(4*2, 5*6))
        plt.subplot(6, 2, 1 + len(plt.gcf().get_axes()))
    plt.title("MoG Initialization" if not iteration else
              "MoG After Iteration {}".format(iteration))
    plt.gca().set_aspect(1)
    plt.scatter(data[:, 0], data[:, 1], c=r.T @ colors if r is not None else "k")
    for c in range(args.clusters):
        eigvalues, eigvectors = np.linalg.eigh(covs[c])

        ellipse = matplotlib.patches.Ellipse(
            xy=means[c], width=4*np.sqrt(eigvalues[0]), height=4*np.sqrt(eigvalues[1]),
            angle=np.rad2deg(np.arctan2(*eigvectors[0, ::-1])))
        ellipse.set_color(colors[c])
        ellipse.set_alpha(0.3)
        plt.gca().add_artist(ellipse)
    if args.plot is True: plt.show()
    else: plt.savefig(args.plot, transparent=True, bbox_inches="tight")

def main(args: argparse.Namespace) -> np.ndarray:
    # Create a random generator with a given seed
    generator = np.random.RandomState(args.seed)

    # Generate artificial data
    data, target = sklearn.datasets.make_blobs(
        n_samples=args.examples, centers=args.clusters, n_features=2, random_state=args.seed)

    # TODO(kmeans): Initialize `means` with shape [args.clusters, data.shape[1]] as follows:
    # - if args.init == "random", use K random data points with the indices returned by
    #     generator.choice(len(data), size=args.clusters, replace=False)
    # - if args.init == "kmeans++", generate the first cluster index by
    #     generator.randint(len(data))
    #   and then iteratively sample the rest of the cluster indices proportionally to
    #   the square of their distances to their closest cluster using
    #     generator.choice(unused_points_indices, p=square_distances / np.sum(square_distances))
    #   Use the `np.linalg.norm` to measure the distances.
    means = None

    # TODO: Initialize the cluster covariances in the variable `covs` of
    # shape [args.clusters, data.shape[1], data.shape[1]] as identity matrices.
    covs = None

    # TODO: Initialize the prior distribution `mixing_coefs` as a uniform distribution.
    mixing_coefs = None

    if args.plot:
        colors = np.concatenate([[[1,0,0], [0,1,0], [0,0,1]],
                                 np.random.RandomState(4).uniform(size=[args.clusters, 3])], axis=0)[:-3]
        plot(args, 0, data, None, means, covs, colors)

    # Run `args.iterations` of the gaussian mixture fitting algorithm
    losses = []
    for iteration in range(args.iterations):
        # TODO: Evaluate responsibilities. You can use
        # `scipy.stats.multivariate_normal` to calculate PDF of
        # a multivariate Gaussian distribution.

        # TODO: Update cluster `means`, `covs` and `mixing_coefs`.

        # TODO: Compute the negative log-likelihood of the current model to `loss`.
        loss = None

        # Append the current `loss` to `losses`.
        losses.append(loss)

        if args.plot:
            # If you want the plotting code to work, `r` must have shape [args.clusters, data.shape[0]].
            plot(args, 1 + iteration, data, r, means, covs, colors)

    return losses

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    losses = main(args)

    for iteration, loss in enumerate(losses):
        print("Loss after iteration {}: {:.1f}".format(iteration + 1, loss))
