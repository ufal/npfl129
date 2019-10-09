#!/usr/bin/env python3
import argparse

import numpy as np

import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Load the data to train["data"] and train["target"]
    train = np.load("linear_regression_competition.train.npz")
    train = {entry: train[entry] for entry in train}

    # TODO: Import the `pickle` package.
    # import pickle

    # TODO: Open file `model.pkl` for binary write access. Make sure the file
    # is not open in text mode, otherwise `pickle` will fail to serialize the
    # model.Use `pickle.dump` to save the model in the opened file.
    # with open("model.pkl", "wb") as f:
    #     pickle.dump(model, f)

    # TODO: To load the model, again open `model.pkl` for binary read access.
    # Then use `pickle.load` to deserialize the model from the stored binary
    # data.
    # with open("model.pkl", "rb") as f:
    #     depickle = pickle.load(f)
