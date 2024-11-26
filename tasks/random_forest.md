### Assignment: random_forest
#### Date: Deadline: Dec 9, 22:00
#### Points: 3 points
#### Tests: random_forest_tests
#### Examples: random_forest_examples

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Tests Start: random_forest_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 random_forest.py --dataset=digits --trees=10 --max_depth=3`
```
Train accuracy: 56.6%
Test accuracy: 55.8%
```

2. `python3 random_forest.py --dataset=digits --trees=10 --bagging --max_depth=3`
```
Train accuracy: 71.5%
Test accuracy: 71.8%
```

3. `python3 random_forest.py --dataset=digits --trees=10 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 69.0%
Test accuracy: 67.6%
```

4. `python3 random_forest.py --dataset=digits --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 76.6%
Test accuracy: 76.9%
```

5. `python3 random_forest.py --dataset=wine --trees=10 --max_depth=3`
```
Train accuracy: 98.5%
Test accuracy: 91.1%
```

6. `python3 random_forest.py --dataset=wine --trees=10 --bagging --max_depth=3`
```
Train accuracy: 98.5%
Test accuracy: 93.3%
```

7. `python3 random_forest.py --dataset=breast_cancer --trees=10 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 98.6%
Test accuracy: 97.9%
```

8. `python3 random_forest.py --dataset=breast_cancer --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 96.9%
Test accuracy: 96.5%
```
#### Tests End:
#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

- `python3 random_forest.py --dataset=wine --trees=3 --max_depth=3`
```
Train accuracy: 98.5%
Test accuracy: 91.1%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/random_forest_1.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --bagging --max_depth=3`
```
Train accuracy: 97.0%
Test accuracy: 93.3%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/random_forest_2.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 100.0%
Test accuracy: 97.8%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/random_forest_3.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --bagging --feature_subsampling=0.5 --max_depth=3`
```
Train accuracy: 98.5%
Test accuracy: 91.1%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/random_forest_4.svgz)
#### Examples End:
