#!/usr/bin/env python3
import argparse

import numpy as np

import sklearn.datasets
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import sklearn.pipeline
import sklearn.preprocessing

parser = argparse.ArgumentParser()
# These arguments will be set appropriately by ReCodEx, even if you change them.
parser.add_argument("--classes", default=10, type=int, help="Number of classes")
parser.add_argument("--plot", default=False, const=True, nargs="?", type=str, help="Plot the predictions")
parser.add_argument("--random_samples", default=1000, type=int, help="Number of random samples")
parser.add_argument("--recodex", default=False, action="store_true", help="Running in ReCodEx")
parser.add_argument("--seed", default=42, type=int, help="Random seed")
parser.add_argument("--test_size", default=0.5, type=lambda x:int(x) if x.isdigit() else float(x), help="Test set size")
# If you add more arguments, ReCodEx will keep them with your default values.

def main(args: argparse.Namespace) -> float:
    # Create a random generator with a given seed
    generator = np.random.RandomState(args.seed)

    # Load the digits dataset
    data = sklearn.datasets.load_digits(n_class=args.classes)

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_size` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        data.data, data.target, test_size=args.test_size, random_state=args.seed)

    # Train a simple linear regression model with polynomial features of order 1 and 2.
    models = []
    for d in [1, 2]:
        models.append(sklearn.pipeline.Pipeline([
            ("features", sklearn.preprocessing.PolynomialFeatures(degree=d)),
            ("estimator", sklearn.linear_model.LogisticRegression(max_iter=2000, random_state=args.seed)),
        ]))
        models[-1].fit(train_data, train_target)

    # TODO: Generate `args.random_samples` test set predictions, every formed
    # by sampling each test set example prediction from either models[0] or models[1],
    # according to a randomly generated assignment:
    #   assignments = generator.choice(2, size=len(test_data), replace=True)
    #
    # Store the accuracies of the `args.random_samples` test set predictions
    # into the `scores`, as percents.
    scores = None

    # TODO: Assuming the null hypothesis that the models have the same performance,
    # perform one-sided random permutation test and estimate its p-value
    # as a ratio of `scores` that are greater or equal to the performance of `models[1]`.
    # Store it in the `p_value` variable as a percentage.
    p_value = None

    # Plot the histograms, confidence intervals and the p-value if requested.
    if args.plot:
        import matplotlib.pyplot as plt
        bin_size = 100 / len(test_data)
        plt.hist(scores, int(round((np.max(scores) - np.min(scores)) / bin_size)),
                 range=(np.min(scores) - bin_size/2, np.max(scores) - bin_size/2),
                 weights=100 * np.ones_like(scores) / len(scores))
        for percentile in [1, 2.5, 5, 25, 50, 75, 95, 97.5, 99]:
            value = np.percentile(scores, percentile)
            color = {1: "#f00", 2.5: "#d60", 5: "#dd0", 25: "#0f0", 50: "#000"}[min(percentile, 100 - percentile)]
            plt.axvline(value, ls="--", color=color, label="{:04.1f}%: {:.2f}".format(percentile, value))
        plt.axvline(second_model, ls="--", color="#f0f", label="{:04.1f}%: {:.2f}".format(p_value, second_model))
        plt.xlabel("Permuted model accuracy")
        plt.ylabel("Frequency [%]")
        plt.legend()
        if args.plot is True: plt.show()
        else: plt.savefig(args.plot, transparent=True, bbox_inches="tight", pad_inches=0)

    return p_value

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    p_value = main(args)
    print("The estimated p-value of the random permutation test: {:.2f}%".format(p_value))
