#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("gold", type=str, help="Gold data")
    parser.add_argument("system", type=str, help="System data")
    args = parser.parse_args()

    with open(args.gold, "r", encoding="utf-8") as gold_file:
        gold = [line.rstrip("\n").split() for line in gold_file.readlines()]

    with open(args.system, "r", encoding="utf-8") as system_file:
        system = [line.rstrip("\n").split() for line in system_file.readlines()]

    tokens, correct = 0, 0
    assert len(gold) == len(system), "The gold and system files need to have the same number of lines"
    for i in range(len(gold)):
        assert len(gold[i]) == len(system[i]), "Each line in gold and system files must have the same number of tokens"
        for j in range(len(gold[i])):
            tokens += 1
            correct += gold[i][j] == system[i][j]

    print("Accuracy: {:.2f}".format(100 * correct / tokens))
