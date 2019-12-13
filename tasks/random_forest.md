### Assignment: random_forest
#### Date: Deadline: Jan 05, 23:59
#### Points: 3 points
#### Examples: random_forest_example

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/08/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_example
- `--n_estimators=3 --max_depth=2 --seed=42`
```
Train acc: 94.1%
Test acc: 85.7%
```
![Random forest visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/random_forest_1.svg)
- `--bootstrapping --n_estimators=3 --max_depth=2 --seed=42`
```
Train acc: 89.0%
Test acc: 88.1%
```
![Random forest visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/random_forest_2.svg)
- `--feature_subsampling 0.5 --n_estimators=3 --max_depth=2 --seed=42`
```
Train acc: 94.1%
Test acc: 90.5%
```
![Random forest visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/random_forest_3.svg)
- `--bootstrapping --feature_subsampling 0.5 --n_estimators=3 --max_depth=2 --seed=42`
```
Train acc: 90.4%
Test acc: 92.9%
```
![Random forest visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/random_forest_4.svg)
#### Examples End:
