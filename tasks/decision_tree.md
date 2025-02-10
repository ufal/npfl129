### Assignment: decision_tree
#### Date: Deadline: Dec 9, 22:00
#### Points: 4 points
#### Tests: decision_tree_tests
#### Examples: decision_tree_examples

Starting with the [decision_tree.py](https://github.com/ufal/npfl129/tree/master/labs/09/decision_tree.py),
manually implement construction of a classification decision tree, supporting both
`gini` and `entropy` criteria, and `max_depth`, `min_to_split` and `max_leaves`
constraints.

We recommend using object-oriented programming to implement the decision tree
classifier; if you are not familiar with it, now is a good time to go through
some tutorials. Regarding the API of your decision tree implementation, you can
take inspiration from scikit-learn itself.

#### Tests Start: decision_tree_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 decision_tree.py --dataset=digits --criterion=gini --min_to_split=250`
```
Train accuracy: 60.7%
Test accuracy: 59.6%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_1.svgz)

2. `python3 decision_tree.py --dataset=digits --criterion=gini --max_depth=3`
```
Train accuracy: 41.1%
Test accuracy: 38.0%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_2.svgz)

3. `python3 decision_tree.py --dataset=digits --criterion=gini --max_leaves=8`
```
Train accuracy: 60.1%
Test accuracy: 57.1%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_3.svgz)

4. `python3 decision_tree.py --dataset=digits --criterion=gini --min_to_split=220 --max_leaves=8`
```
Train accuracy: 60.7%
Test accuracy: 59.6%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_4.svgz)

5. `python3 decision_tree.py --dataset=digits --criterion=entropy --min_to_split=420`
```
Train accuracy: 42.4%
Test accuracy: 40.2%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_5.svgz)

6. `python3 decision_tree.py --dataset=breast_cancer --criterion=entropy --max_depth=3 --seed=44`
```
Train accuracy: 94.8%
Test accuracy: 93.7%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_6.svgz)

7. `python3 decision_tree.py --dataset=digits --criterion=entropy --max_leaves=7`
```
Train accuracy: 53.2%
Test accuracy: 51.6%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_7.svgz)

8. `python3 decision_tree.py --dataset=breast_cancer --criterion=entropy --min_to_split=55 --max_depth=3 --seed=44`
```
Train accuracy: 94.4%
Test accuracy: 93.7%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_8.svgz)
#### Tests End:
#### Examples Start: decision_tree_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

- `python3 decision_tree.py --dataset=iris --max_depth=3`
```
Train accuracy: 95.5%
Test accuracy: 100.0%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_dtreeviz_1.svgz)

- `python3 decision_tree.py --dataset=wine --criterion=entropy --min_to_split=20 --seed=44`
```
Train accuracy: 97.7%
Test accuracy: 91.1%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_dtreeviz_2.svgz)

- `python3 decision_tree.py --dataset=breast_cancer --criterion=entropy --max_depth=3 --seed=44`
```
Train accuracy: 94.8%
Test accuracy: 93.7%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/decision_tree_dtreeviz_3.svgz)
#### Examples End:
