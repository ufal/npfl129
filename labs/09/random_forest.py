#!/usr/bin/env python3
import argparse

import numpy as np
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

parser = argparse.ArgumentParser()
# These arguments will be set appropriately by ReCodEx, even if you change them.
parser.add_argument("--bootstrapping", default=False, action="store_true", help="Perform data bootstrapping")
parser.add_argument("--feature_subsampling", default=1, type=float, help="What fraction of features to subsample")
parser.add_argument("--max_depth", default=None, type=int, help="Maximum decision tree depth")
parser.add_argument("--recodex", default=False, action="store_true", help="Running in ReCodEx")
parser.add_argument("--seed", default=42, type=int, help="Random seed")
parser.add_argument("--test_size", default=42, type=lambda x:int(x) if x.isdigit() else float(x), help="Test set size")
parser.add_argument("--trees", default=1, type=int, help="Number of trees in the forest")
# If you add more arguments, ReCodEx will keep them with your default values.

def main(args):
    # Use the wine dataset
    data, target = sklearn.datasets.load_wine(return_X_y=True)

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_size` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        data, target, test_size=args.test_size, random_state=args.seed)

    # TODO: Create a random forest on the trainining data.
    #
    # For determinism, create a generator
    #   generator = np.random.RandomState(args.seed)
    # at the beginning and then use this instance for all random number generation.
    #
    # Use a simplified decision tree from the `decision_tree` assignment. The
    # tree needs to support only the `entropy` criterion and `max_depth` constraint.
    # When splitting nodes, proceed in the depth-first order, splitting all nodes
    # in left subtrees before nodes in right subtrees.
    #
    # Additionally, implement:
    # - feature subsampling: when searching for the best split, try only
    #   a subset of features. When splitting a node, start by generating
    #   a feature mask using
    #     generator.uniform(size=number_of_features) <= feature_subsampling
    #   which gives a boolean value for every feature, with `True` meaning the
    #   feature is used during best split search, and `False` it is not.
    #   (When feature_subsampling == 1, all features are used.)
    #
    # - train a random forest consisting of `args.trees` decision trees
    #
    # - if `args.bootstrapping` is set, right before training a decision tree,
    #   create a bootstrap sample of the training data using the following indices
    #     indices = generator.randint(len(train_data), size=len(train_data))
    #   and if `args.bootstrapping` is not set, use the original training data.
    #
    # During prediction, use voting to find the most frequent class for a given
    # input, choosing the one with smallest class index in case of a tie.

    # TODO: Finally, measure the training and testing accuracy.
    train_accuracy = None
    test_accuracy = None

    return train_accuracy, test_accuracy

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    train_accuracy, test_accuracy = main(args)

    print("Train accuracy: {:.1f}%".format(100 * train_accuracy))
    print("Test accuracy: {:.1f}%".format(100 * test_accuracy))
