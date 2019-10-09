#!/usr/bin/env python3
import argparse

import numpy as np
import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--plot", default=False, action="store_true", help="Plot the results")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--test_size", default=50, type=int, help="Test size to use")
    args = parser.parse_args()

    # Load Boston housing dataset
    dataset = sklearn.datasets.load_boston()

    # TODO: Split the dataset randomly to train and test using
    # `sklearn.model_selection.train_test_split`, with
    # `test_size=args.test_size` and `random_state=args.seed`.

    # TODO: Using sklearn.linear_model.Ridge, fit the train set using
    # L2 regularization, employing lambdas from 0 to 100 with a step size 0.1.
    # For every model, compute the root mean squared error
    # (sklearn.metrics.mean_squared_error may come handy) and print out
    # the lambda producing lowest test error.
    best_lambda = None
    best_rmse = None

    with open("linear_regression_l2.out", "w") as output_file:
        print("{:.1f}, {:.2f}".format(best_lambda, best_rmse), file=output_file)

    if args.plot:
        # TODO: This block is not part of ReCodEx submission, so you
        # will get points even without it. However, it is useful to
        # learn to visualize the results.

        # If you collect used lambdas to `lambdas` and their respective
        # results to `rmses`, the following lines will plot the result
        # if you add `--plot` argument.
        import matplotlib.pyplot as plt
        plt.plot(lambdas, rmses)
        plt.show()
