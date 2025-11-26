### Assignment: random_forest
#### Date: Deadline: Dec 10, 22:00
#### Points: 3 points
#### Tests: random_forest_tests
#### Examples: random_forest_examples

Using the [random_forest.py](https://github.com/ufal/npfl129/tree/master/labs/09/random_forest.py)
template, train a random forest, which is a collection of decision trees trained
with dataset bagging and random feature subsampling.

#### Tests Start: random_forest_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 random_forest.py --dataset=digits --trees=10 --max_depth=3 --seed=73`
```
Train accuracy: 56.3%
Test accuracy: 51.6%
```

2. `python3 random_forest.py --dataset=digits --trees=10 --bagging --max_depth=3 --seed=73`
```
Train accuracy: 73.1%
Test accuracy: 70.7%
```

3. `python3 random_forest.py --dataset=digits --trees=10 --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 77.2%
Test accuracy: 74.4%
```

4. `python3 random_forest.py --dataset=digits --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 74.4%
Test accuracy: 74.0%
```

5. `python3 random_forest.py --dataset=wine --trees=10 --max_depth=3 --seed=73`
```
Train accuracy: 97.0%
Test accuracy: 80.0%
```

6. `python3 random_forest.py --dataset=wine --trees=10 --bagging --max_depth=3 --seed=73`
```
Train accuracy: 99.2%
Test accuracy: 97.8%
```

7. `python3 random_forest.py --dataset=breast_cancer --trees=10 --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 98.6%
Test accuracy: 95.8%
```

8. `python3 random_forest.py --dataset=breast_cancer --trees=10 --bagging --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 98.4%
Test accuracy: 97.9%
```
#### Tests End:
#### Examples Start: random_forest_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

- `python3 random_forest.py --dataset=wine --trees=3 --max_depth=3 --seed=73`
```
Train accuracy: 97.0%
Test accuracy: 80.0%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2526/tasks/figures/random_forest_1.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --bagging --max_depth=3 --seed=73`
```
Train accuracy: 94.7%
Test accuracy: 88.9%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2526/tasks/figures/random_forest_2.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 98.5%
Test accuracy: 97.8%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2526/tasks/figures/random_forest_3.svgz)

- `python3 random_forest.py --dataset=wine --trees=3 --bagging --feature_subsampling=0.5 --max_depth=3 --seed=73`
```
Train accuracy: 95.5%
Test accuracy: 86.7%
```
![Example visualization](//ufal.mff.cuni.cz/~courses/npfl129/2526/tasks/figures/random_forest_4.svgz)
#### Examples End:
