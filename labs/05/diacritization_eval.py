#!/usr/bin/env python3

def accuracy(gold, system):
    assert len(gold) == len(system), "The gold and system outputs must have same length: {} vs {}.".format(len(gold), len(system))
    gold, system = gold.split(), system.split()
    assert len(gold) == len(system), "The gold and system outputs must have same number of tokens: {} vs {}.".format(len(gold), len(system))

    tokens, correct = 0, 0
    for gold_token, system_token in zip(gold, system):
        tokens += 1
        correct += gold_token == system_token

    return correct / tokens

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
