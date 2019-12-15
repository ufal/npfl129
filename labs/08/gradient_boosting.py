#!/usr/bin/env python3
import argparse

import numpy as np
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

class DecisionTree:
    class Node:
        def __init__(self, instances, prediction):
            self.is_leaf = True
            self.instances = instances
            self.prediction = prediction

        def split(self, feature, value, left, right):
            self.is_leaf = False
            self.feature = feature
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, max_depth, min_to_split):
        self._max_depth = max_depth
        self._min_to_split = min_to_split

    def fit(self, data, targets):
        self._data = data
        self._targets = targets

        self._root = self._create_leaf(np.arange(len(self._data)))
        self._split_recursively(self._root, 0)

        return self

    def predict(self, data):
        results = np.zeros(len(data), dtype=np.int32)
        for i in range(len(data)):
            node = self._root
            while not node.is_leaf:
                node = node.left if data[i][node.feature] <= node.value else node.right
            results[i] = node.prediction

        return results

    def _split_recursively(self, node, depth):
        if not self._can_split(node, depth):
            return

        feature, value, left, right = self._best_split(node)
        node.split(feature, value, self._create_leaf(left), self._create_leaf(right))
        self._split_recursively(node.left, depth + 1)
        self._split_recursively(node.right, depth + 1)

    def _can_split(self, node, depth):
        return (
            (self._max_depth is None or depth < self._max_depth) and
            len(node.instances) >= self._min_to_split and
            not np.array_equiv(self._targets[node.instances], node.prediction) and
            not np.array_equiv(self._data[node.instances], self._data[node.instances[0]])
        )

    def _best_split(self, node):
        best_criterion = None
        for feature in range(self._data.shape[1]):
            node_features = self._data[node.instances, feature]
            separators = np.unique(node_features)
            for i in range(len(separators) - 1):
                value = (separators[i] + separators[i + 1]) / 2
                left, right = node.instances[node_features <= value], node.instances[node_features > value]
                criterion = self._criterion(left) + self._criterion(right)
                if best_criterion is None or criterion < best_criterion:
                    best_criterion, best_feature, best_value, best_left, best_right = \
                        criterion, feature, value, left, right

        return best_feature, best_value, best_left, best_right

    def _criterion(self, instances):
        # We use Gini index
        bins = np.bincount(self._targets[instances])
        return np.sum(bins * (1 - bins / len(instances)))

    def _create_leaf(self, instances):
        # Create a new leaf, together with its prediction (the most frequent class)
        return self.Node(instances, np.argmax(np.bincount(self._targets[instances])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--l2", default=0, type=float, help="L2 regularization factor")
    parser.add_argument("--learning_rate", default=1, type=float, help="Learning rate")
    parser.add_argument("--max_depth", default=None, type=int, help="Maximum decision tree depth")
    parser.add_argument("--min_to_split", default=2, type=int, help="Minimum examples required to split")
    parser.add_argument("--n_estimators", default=1, type=int, help="Number of trees in the forest")
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

    classes = np.max(target) + 1

    # TODO: Create a gradient boosted trees on the classification training data.
    #
    # Notably, train for `args.n_estimators` iteration. During iteration `t`:
    # - the goal is to train `classes` regression trees, each predicting
    #   raw weight for the corresponding class.
    # - compute the current predictions `y(x_i)` for every training example `i` as
    #     y_raw(x_i)_c = \sum_{i=1}^{t-1} trees_from_iteration_i_for_class_c.predict(x_i)
    #     y_prob(x_i) = softmax(y_raw(x_i))
    # - loss in iteration `t` is
    #     L = (\sum_i NLL(target_i, y_prob(x_i))) + 1/2 * args.l2 * (sum of all weights)
    # - for every class `c`:
    #   - start by computing `g_i` and `h_i` for every training example `i`;
    #     the `g_i` is the first derivative of NLL(target_i_c, y_prob(x_i)_c) with respect
    #     to y_prob(x_i)_c, and the `h_i` is the second derivative fo the same.
    #   - then, create a decision tree, where the criterion function is the above loss L,
    #     so the optimum prediction for a given node T with training examples I_T is
    #       w_T = - (\sum_{i \in I_T} g_i) / (args.l2 + sum_{i \in I_T} h_i)
    #     and the value of the loss with the above prediction is
    #       c_GB = - 1/2 (\sum_{i \in I_T} g_i)^2 / (args.l2 + sum_{i \in I_T} h_i)
    #
    # To perform a prediction, analogically compute the y_raw for all trees, and return
    # the class with the highest value (and the smallest class if there is a tie).

    # TODO: Finally, measure the training and testing accuracy.
    print("Train acc: {:.1f}%".format(100 * train_accuracy))
    print("Test acc: {:.1f}%".format(100 * test_accuracy))
