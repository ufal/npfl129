### Assignment: random_forest
#### Date: Deadline: Dec 15, 23:59
#### Points: 3 points
#### Examples: random_forest_examples

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 random_forest.py --trees=3 --max_depth=2 --seed=46`
```
Train accuracy: 93.4%
Test accuracy: 83.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/random_forest_1.svgz)
- `python3 random_forest.py --trees=3 --bootstrapping --max_depth=2 --seed=46`
```
Train accuracy: 97.1%
Test accuracy: 88.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/random_forest_2.svgz)
- `python3 random_forest.py --trees=3 --feature_subsampling=0.5 --max_depth=2 --seed=46`
```
Train accuracy: 97.1%
Test accuracy: 85.7%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/random_forest_3.svgz)
- `python3 random_forest.py --trees=3 --bootstrapping --feature_subsampling=0.5 --max_depth=2 --seed=46`
```
Train accuracy: 98.5%
Test accuracy: 90.5%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/random_forest_4.svgz)
#### Examples End:
