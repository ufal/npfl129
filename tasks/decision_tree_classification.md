### Assignment: decision_tree_classification
#### Date: Deadline: Dec 08, 23:59
#### Points: 8 points
#### Examples: decision_tree_classification_examples

Starting with the [decision_tree_classification.py](https://github.com/ufal/npfl129/tree/master/labs/06/decision_tree_classification.py),
implement construction of a classification decision tree, supporting both
`gini` and `entropy` criteria, and `max_depth`, `min_to_split` and `max_leaves`
constraints.

In this assignment, you will get partial points during ReCodEx evaluation,
depending on which argument values your solution support.

#### Examples Start: decision_tree_classification_examples
- `--criterion=gini --max_depth=2 --seed=42`
```
Train acc: 94.1%
Test acc: 85.7%
```
[Decision tree visualization](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/decision_tree_classification_1.svg)
- `--criterion=gini --min_to_split=49 --seed=42`
```
Train acc: 97.8%
Test acc: 95.2%
```
[Decision tree visualization](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/decision_tree_classification_2.svg)
- `--criterion=gini --max_leaves=4 --seed=42`
```
Train acc: 97.1%
Test acc: 95.2%
```
[Decision tree visualization](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/decision_tree_classification_3.svg)
- `--criterion=entropy --max_leaves=5 --seed=42`
```
Train acc: 97.8%
Test acc: 88.1%
```
[Decision tree visualization](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/decision_tree_classification_4.svg)
#### Examples End:
