### Assignment: decision_tree
#### Date: Deadline: Dec 15, 23:59
#### Points: 4 points
#### Examples: decision_tree_examples

Starting with the [decision_tree.py](https://github.com/ufal/npfl129/tree/master/labs/09/decision_tree.py),
implement construction of a classification decision tree, supporting both
`gini` and `entropy` criteria, and `max_depth`, `min_to_split` and `max_leaves`
constraints.

In this assignment, you will get partial points during ReCodEx evaluation,
depending on which argument values your solution support.

#### Examples Start: decision_tree_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 decision_tree.py --criterion=gini --min_to_split=50 --seed=91`
```
Train accuracy: 92.6%
Test accuracy: 88.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_1.svgz)
- `python3 decision_tree.py --criterion=gini --max_depth=2 --seed=91`
```
Train accuracy: 93.4%
Test accuracy: 88.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_2.svgz)
- `python3 decision_tree.py --criterion=gini --max_leaves=4 --seed=91`
```
Train accuracy: 97.8%
Test accuracy: 92.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_3.svgz)
- `python3 decision_tree.py --criterion=gini --min_to_split=42 --max_leaves=5 --seed=91`
```
Train accuracy: 98.5%
Test accuracy: 92.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_4.svgz)
- `python3 decision_tree.py --criterion=entropy --min_to_split=55 --seed=97`
```
Train accuracy: 94.1%
Test accuracy: 78.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_5.svgz)
- `python3 decision_tree.py --criterion=entropy --max_depth=2 --seed=97`
```
Train accuracy: 94.9%
Test accuracy: 81.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_6.svgz)
- `python3 decision_tree.py --criterion=entropy --max_leaves=4 --seed=97`
```
Train accuracy: 98.5%
Test accuracy: 88.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_7.svgz)
- `python3 decision_tree.py --criterion=entropy --min_to_split=40 --max_leaves=6 --seed=97`
```
Train accuracy: 99.3%
Test accuracy: 90.5%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/decision_tree_8.svgz)
#### Examples End:
