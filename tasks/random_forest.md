### Assignment: random_forest
#### Date: Deadline: Dec 20, 23:59
#### Points: 3 points
#### Examples: random_forest_examples

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --trees=3 --max_depth=2`
```
Train accuracy: 94.0%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_1.svgz)
- `python3 random_forest.py --trees=3 --bagging --max_depth=2`
```
Train accuracy: 92.5%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_2.svgz)
- `python3 random_forest.py --trees=3 --feature_subsampling=0.5 --max_depth=2`
```
Train accuracy: 95.5%
Test accuracy: 86.7%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_3.svgz)
- `python3 random_forest.py --trees=3 --bagging --feature_subsampling=0.5 --max_depth=2`
```
Train accuracy: 92.5%
Test accuracy: 91.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_4.svgz)
#### Examples End:
