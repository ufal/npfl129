### Assignment: random_forest
#### Date: Deadline: Dec 20, 23:59
#### Points: 3 points
#### Examples: random_forest_examples

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --trees=3 --max_depth=2 --seed=74`
```
Train accuracy: 92.5%
Test accuracy: 80.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_1.svgz)
- `python3 random_forest.py --trees=3 --bagging --max_depth=2 --seed=74`
```
Train accuracy: 97.0%
Test accuracy: 84.4%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_2.svgz)
- `python3 random_forest.py --trees=3 --feature_subsampling=0.5 --max_depth=2 --seed=74`
```
Train accuracy: 94.7%
Test accuracy: 95.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_3.svgz)
- `python3 random_forest.py --trees=3 --bagging --feature_subsampling=0.5 --max_depth=2 --seed=74`
```
Train accuracy: 97.0%
Test accuracy: 93.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_4.svgz)
#### Examples End:
