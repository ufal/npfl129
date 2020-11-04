#!/usr/bin/env python3

def accuracy(gold, system):
    assert isinstance(gold, str) and isinstance(system, str), "The gold and system outputs must be strings"
    gold, system = gold.split(), system.split()
    assert len(gold) == len(system), "The gold and system outputs must have same number of words: {} vs {}.".format(len(gold), len(system))

    words, correct = 0, 0
    for gold_token, system_token in zip(gold, system):
        words += 1
        correct += gold_token == system_token

    return correct / words

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("gold", type=str, help="Gold data")
    parser.add_argument("system", type=str, help="System data")
    args = parser.parse_args()

    with open(args.gold, "r", encoding="utf-8") as gold_file:
        gold = gold_file.read()

    with open(args.system, "r", encoding="utf-8") as system_file:
        system = system_file.read()

    score = accuracy(gold, system)

    print("Accuracy: {:.2f}".format(100 * score))
