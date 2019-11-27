#!/usr/bin/env python3
import argparse
import sys

import numpy as np
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--criterion", default="gini", type=str, help="Criterion to use; either `gini` or `entropy`")
    parser.add_argument("--max_depth", default=None, type=int, help="Maximum decision tree depth")
    parser.add_argument("--min_to_split", default=2, type=int, help="Minimum examples required to split")
    parser.add_argument("--max_leaves", default=None, type=int, help="Maximum number of leaf nodes")
    parser.add_argument("--plot", default=False, action="store_true", help="Plot progress")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--test_size", default=42, type=int, help="Test set size")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Use the digits dataset
    data, target = sklearn.datasets.load_wine(return_X_y=True)

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_size` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        data, target, stratify=target, test_size=args.test_size, random_state=args.seed)

    # TODO: Create a decision tree on the trainining data.
    #
    # For each node, predict the most frequent class (and the one with smallest
    # index if there are several such classes).
    #
    # - When `args.max_leaves` is None, use recursive (left descendants first, then
    #   right descendants) approach, splitting every node if `args.max_depth`
    #   and `args.min_to_split` constraints are valid. When splitting, consider
    #   the features in sequential order, then for each feature consider all
    #   possible split points ordered in ascending value, and perform the
    #   first encountered split descreasing the criterion the most.
    # - When `args.max_leaves` is not None, always split a node where the
    #   overall criterion value decreases the most (c_left + c_right - c_node).
    #   If there are several such nodes, choose the one which was created sooner.

    # TODO: Finally, measure the training and testing accuracy.
    print("Train acc: {:.1f}%".format(100 * train_accuracy))
    print("Test acc: {:.1f}%".format(100 * test_accuracy))
