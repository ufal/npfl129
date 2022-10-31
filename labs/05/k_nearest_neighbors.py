#!/usr/bin/env python3
import argparse
import os
import sys
import urllib.request

import numpy as np
import sklearn.metrics
import sklearn.model_selection
import sklearn.preprocessing


parser = argparse.ArgumentParser()
# These arguments will be set appropriately by ReCodEx, even if you change them.
parser.add_argument("--k", default=1, type=int, help="K nearest neighbors to consider")
parser.add_argument("--p", default=2, type=int, help="Use L_p as distance metric")
parser.add_argument("--plot", default=False, const=True, nargs="?", type=str, help="Plot the predictions")
parser.add_argument("--recodex", default=False, action="store_true", help="Running in ReCodEx")
parser.add_argument("--seed", default=42, type=int, help="Random seed")
parser.add_argument("--test_size", default=1000, type=int, help="Test set size")
parser.add_argument("--train_size", default=1000, type=int, help="Train set size")
parser.add_argument("--weights", default="uniform", type=str, help="Weighting to use (uniform/inverse/softmax)")
# If you add more arguments, ReCodEx will keep them with your default values.


class MNIST:
    """MNIST Dataset.

    The train set contains 60000 images of handwritten digits. The data
    contain 28*28=784 values in the range 0-255, the targets are numbers 0-9.
    """
    def __init__(self,
                 name="mnist.train.npz",
                 data_size=None,
                 url="https://ufal.mff.cuni.cz/~straka/courses/npfl129/2223/datasets/"):
        if not os.path.exists(name):
            print("Downloading dataset {}...".format(name), file=sys.stderr)
            urllib.request.urlretrieve(url + name, filename=name)

        # Load the dataset, i.e., `data` and optionally `target`.
        dataset = np.load(name)
        for key, value in dataset.items():
            setattr(self, key, value[:data_size])
        self.data = self.data.reshape([-1, 28*28]).astype(float)


def main(args: argparse.Namespace) -> float:
    # Load MNIST data, scale it to [0, 1] and split it to train and test.
    mnist = MNIST(data_size=args.train_size + args.test_size)
    mnist.data = sklearn.preprocessing.MinMaxScaler().fit_transform(mnist.data)
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        mnist.data, mnist.target, test_size=args.test_size, random_state=args.seed)

    # TODO: Generate `test_predictions` with classes predicted for `test_data`.
    #
    # Find `args.k` nearest neighbors, choosing the ones with the smallest train_data
    # indices in case of ties. Use the most frequent class (optionally weighted
    # by a given scheme described below) as prediction, choosing the one with the
    # smallest class index when there are multiple classes with the same frequency.
    #
    # Use L_p norm for a given p (either 1, 2 or 3) to measure distances.
    #
    # The weighting can be:
    # - "uniform": all nearest neighbors have the same weight
    # - "inverse": `1/distances` is used as weights
    # - "softmax": `softmax(-distances)` is used as weights
    #
    # If you want to plot misclassified examples, you also need to fill `test_neighbors`
    # with indices of nearest neighbors; but it is not needed for passing in ReCodEx.
    test_predictions = ...

    accuracy = sklearn.metrics.accuracy_score(test_target, test_predictions)

    if args.plot:
        import matplotlib.pyplot as plt
        examples = [[] for _ in range(10)]
        for i in range(len(test_predictions)):
            if test_predictions[i] != test_target[i] and not examples[test_target[i]]:
                examples[test_target[i]] = [test_data[i], *train_data[test_neighbors[i]]]
        examples = [[img.reshape(28, 28) for img in example] for example in examples if example]
        examples = [[example[0]] + [np.zeros_like(example[0])] + example[1:] for example in examples]
        plt.imshow(np.concatenate([np.concatenate(example, axis=1) for example in examples], axis=0), cmap="gray")
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show() if args.plot is True else plt.savefig(args.plot, transparent=True, bbox_inches="tight")

    return accuracy


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    accuracy = main(args)
    print("K-nn accuracy for {} nearest neighbors, L_{} metric, {} weights: {:.2f}%".format(
        args.k, args.p, args.weights, 100 * accuracy))
