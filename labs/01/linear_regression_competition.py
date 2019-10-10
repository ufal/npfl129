#!/usr/bin/env python3
import argparse
import pickle

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

    # TODO: Train the model

    # TODO: The trained model needs to be saved. All sklear models can
    # be serialized and deserialized using the standard `pickle` module.
    #
    # To save a model, open a target file for binary access, and use
    # `pickle.dump` to save the model to the opened file:
    # with open(output_model_path, "wb") as model_file:
    #       pickle.dump(model, model_file)
    #
    # To load the model, again open the model file for binary read access.
    # Then use `pickle.load` to deserialize the model from the stored binary
    # data:
    # with open(model_path, "rb") as model_file:
    #     model = pickle.load(model_file)
