#!/usr/bin/env python3
import argparse
import os
import urllib.request
import sys
import zipfile

import numpy as np
import scipy.stats

import sklearn.feature_extraction.text
import sklearn.metrics
import sklearn.model_selection

class Dataset:
    def __init__(self,
                 name="isnt_it_ironic.train.zip",
                 url="https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/"):
        if not os.path.exists(name):
            print("Downloading dataset {}...".format(name), file=sys.stderr)
            urllib.request.urlretrieve(url + name, filename=name)

        # Load the dataset and split it into `data` and `target`.
        self.data = []
        self.target = []

        with zipfile.ZipFile(name, "r") as dataset_file:
            with dataset_file.open(name.replace(".zip", ".txt"), "r") as train_file:
                for line in train_file:
                    label, text = line.decode("utf-8").rstrip("\n").split("\t")
                    self.data.append(text)
                    self.target.append(int(label))
        self.target = np.array(self.target, np.int32)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", default=1, type=float, help="Smoothing parameter for Bernoulli and Multinomial NB")
    parser.add_argument("--gaussian_var_epsilon", default=1e-9, type=float, help="Gaussian smoothing factor")
    parser.add_argument("--naive_bayes_type", default="gaussian", type=str, help="NB type to use")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--test_ratio", default=0.5, type=float, help="Test set size ratio")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Load the dataset, downloading it if required
    dataset = Dataset()

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_ratio` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        dataset.data, dataset.target, stratify=dataset.target, test_size=args.test_ratio, random_state=args.seed)

    # Use TFIDF as the text representation
    tfidf = sklearn.feature_extraction.text.TfidfVectorizer(analyzer="word", lowercase=True, strip_accents="unicode")
    train_data = tfidf.fit_transform(train_data).toarray()
    test_data = tfidf.transform(test_data).toarray()

    # Get number of classes
    classes = np.max(train_target) + 1

    # TODO: Fit the naive Bayes classifier on the train data.
    #
    # The naive_bayes_type can be one of:
    # - gaussian: Fit Gaussian NB, by estimating mean and variance of the input
    #   features. For variance estimation use
    #     1/N * \sum_x (x - mean)^2
    #   and additionally increase all estimated variances by
    #     args.gaussian_var_epsilon * maximum variance of any feature in the whole train data
    #   You can use `scikit.stats.norm` to compute probability density function of
    #   Gaussian distribution.
    # - multinomial: Multinomial NB with smoothing factor args.alpha
    # - bernoulli: Bernoulli NB with smoothing factor args.alpha

    # TODO: Predict the test data classes and print out test accuracy.
    print("Test accuracy {:.2f}%".format(100 * test_accuracy))
