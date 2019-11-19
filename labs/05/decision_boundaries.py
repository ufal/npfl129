#!/usr/bin/env python3
import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection
import sklearn.neural_network
import sklearn.svm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--C", default=1, type=float, help="C parameter of SVM")
    parser.add_argument("--examples", default=200, type=int, help="Number of examples")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--test_ratio", default=0.5, type=float, help="Test set size ratio")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Generate an artifical regression dataset
    data, target = sklearn.datasets.make_classification(
        n_samples=args.examples, n_features=2, n_informative=2, n_redundant=0, random_state=args.seed)

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_ratio` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        data, target, test_size=args.test_ratio, random_state=args.seed)

    xs = np.linspace(np.min(data[:, 0] - .5), np.max(data[:, 0] + .5), 500)
    ys = np.linspace(np.min(data[:, 1] - .5), np.max(data[:, 1] + .5), 500)
    grid = np.array([[x, y] for y in ys for x in xs])
    def plot(ax, model, title):
        try:
            predictions = model.predict_proba(grid)[:, 1].reshape([len(xs), len(ys)])
        except:
            predictions = model.predict(grid).reshape([len(xs), len(ys)])
        ax.contourf(xs, ys, predictions, levels=40, cmap=plt.cm.RdBu, alpha=0.7)
        ax.contour(xs, ys, predictions, levels=[0.25, 0.5, 0.75], colors="k")
        ax.scatter(train_data[:, 0], train_data[:, 1], c=train_target, marker="P", label="train", cmap=plt.cm.RdBu)
        ax.scatter(test_data[:, 0], test_data[:, 1], c=test_target, label="test", cmap=plt.cm.RdBu)
        ax.legend(loc="upper right")
        ax.set_title("{}, acc {:.1f}%".format(title, 100 * sklearn.metrics.accuracy_score(test_target, model.predict(test_data))))

    methods = [
        [("SVM Linear SVM", sklearn.svm.SVC(kernel="linear").fit(train_data, train_target)),
         ("SVM Poly3", sklearn.svm.SVC(C=args.C, kernel="poly", degree=3, coef0=1, gamma="scale").fit(train_data, train_target)),
         ("SVM RBF", sklearn.svm.SVC(C=args.C, kernel="rbf", gamma="scale").fit(train_data, train_target))],
        [("Logistic Regression", sklearn.linear_model.LogisticRegression(solver="lbfgs").fit(train_data, train_target)),
         ("MLP Hidden 50 ReLU", sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(50,), max_iter=99999).fit(train_data, train_target)),
         ("MLP Hidden 200 ReLU", sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(200,), max_iter=99999).fit(train_data, train_target))]
    ]

    _, axs = plt.subplots(nrows=len(methods), ncols=len(methods[0]))
    for row_axs, row_methods in zip(axs, methods):
        for ax, (title, predictions) in zip(row_axs, row_methods):
            plot(ax, predictions, title)
    plt.show()
