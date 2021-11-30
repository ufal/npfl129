### Assignment: decision_tree
#### Date: Deadline: Dec 20, 23:59
#### Points: 4 points
#### Examples: decision_tree_examples

Starting with the [decision_tree.py](https://github.com/ufal/npfl129/tree/master/labs/09/decision_tree.py),
manually implement construction of a classification decision tree, supporting both
`gini` and `entropy` criteria, and `max_depth`, `min_to_split` and `max_leaves`
constraints.

In this assignment, you will get partial points during ReCodEx evaluation,
depending on which argument values your solution support.

#### Examples Start: decision_tree_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 decision_tree.py --criterion=gini --min_to_split=50`
```
Train accuracy: 93.2%
Test accuracy: 84.4%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_1.svgz)
- `python3 decision_tree.py --criterion=gini --max_depth=2`
```
Train accuracy: 94.0%
Test accuracy: 84.4%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_2.svgz)
- `python3 decision_tree.py --criterion=gini --max_leaves=4`
```
Train accuracy: 97.7%
Test accuracy: 93.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_3.svgz)
- `python3 decision_tree.py --criterion=gini --min_to_split=40 --max_leaves=4`
```
Train accuracy: 97.7%
Test accuracy: 93.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_4.svgz)
- `python3 decision_tree.py --criterion=entropy --min_to_split=55`
```
Train accuracy: 91.0%
Test accuracy: 86.7%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_5.svgz)
- `python3 decision_tree.py --criterion=entropy --max_depth=2`
```
Train accuracy: 94.0%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_6.svgz)
- `python3 decision_tree.py --criterion=entropy --max_leaves=4`
```
Train accuracy: 94.7%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_7.svgz)
- `python3 decision_tree.py --criterion=entropy --min_to_split=45 --max_depth=2`
```
Train accuracy: 91.0%
Test accuracy: 86.7%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/decision_tree_8.svgz)
#### Examples End:
