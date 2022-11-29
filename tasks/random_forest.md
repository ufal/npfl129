### Assignment: random_forest
#### Date: Deadline: Dec 12, 7:59 a.m.
#### Points: 3 points
#### Examples: random_forest_examples
#### Tests: random_forest_tests

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --dataset=wine --trees=3 --max_depth=3`
```
Train accuracy: 99.2%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/random_forest_1.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --bagging --max_depth=3`
```
Train accuracy: 97.7%
Test accuracy: 95.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/random_forest_2.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 97.7%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/random_forest_3.svgz)
- `python3 random_forest.py --dataset=wine --trees=3 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 99.2%
Test accuracy: 95.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/random_forest_4.svgz)
#### Examples End:
#### Tests Start: random_forest_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 random_forest.py --dataset=digits --trees=10 --max_depth=3`
```
Train accuracy: 54.4%
Test accuracy: 50.4%
```
- `python3 random_forest.py --dataset=digits --trees=10 --bagging --max_depth=3`
```
Train accuracy: 72.8%
Test accuracy: 72.2%
```
- `python3 random_forest.py --dataset=digits --trees=10 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 64.3%
Test accuracy: 62.7%
```
- `python3 random_forest.py --dataset=digits --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 73.5%
Test accuracy: 75.6%
```
- `python3 random_forest.py --dataset=wine --trees=10 --max_depth=3`
```
Train accuracy: 99.2%
Test accuracy: 88.9%
```
- `python3 random_forest.py --dataset=wine --trees=10 --bagging --max_depth=3`
```
Train accuracy: 100.0%
Test accuracy: 97.8%
```
- `python3 random_forest.py --dataset=breast_cancer --trees=10 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 97.9%
Test accuracy: 95.1%
```
- `python3 random_forest.py --dataset=breast_cancer --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 98.6%
Test accuracy: 95.1%
```
#### Tests End:
