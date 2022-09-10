### Assignment: random_forest
#### Date: Deadline: Dec 20, 23:59
#### Points: 3 points
#### Examples: random_forest_examples
#### Tests: random_forest_tests

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/past-2122/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --dataset=wine --trees=3 --max_depth=3 --seed=74`
```
Train accuracy: 98.5%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_1.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --bagging --max_depth=3 --seed=74`
```
Train accuracy: 100.0%
Test accuracy: 91.1%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_2.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --feature_subsampling=0.5 --max_depth=3 --seed=74`
```
Train accuracy: 99.2%
Test accuracy: 95.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_3.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --bagging --feature_subsampling=0.5 --max_depth=3 --seed=74`
```
Train accuracy: 97.7%
Test accuracy: 93.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/random_forest_4.svgz)
#### Examples End:
#### Tests Start: random_forest_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --dataset=digits --trees=5 --max_depth=3`
```
Train accuracy: 54.4%
Test accuracy: 50.4%
```
- `python3 random_forest.py --dataset=digits --trees=5 --bagging --max_depth=3`
```
Train accuracy: 67.9%
Test accuracy: 68.4%
```
- `python3 random_forest.py --dataset=digits --trees=5 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 62.1%
Test accuracy: 61.3%
```
- `python3 random_forest.py --dataset=digits --trees=5 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 68.5%
Test accuracy: 69.6%
```
#### Tests End:
