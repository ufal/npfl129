### Assignment: linear_regression_features
#### Date: Deadline: Oct 17, 7:59 a.m.
#### Points: 3 points
#### Tests: linear_regression_features_tests

Starting with the
[linear_regression_features.py](https://github.com/ufal/npfl129/tree/past-2324/labs/01/linear_regression_features.py)
template, use `scikit-learn` to train a model of a 1D curve.

Try using a concatenation of features $x^1, x^2, …, x^D$ for $D$ from 1 to
a given range, and report RMSE of every such configuration.

#### Tests Start: linear_regression_features_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 linear_regression_features.py --data_size=10 --test_size=5 --range=6`
```
Maximum feature order 1: 0.74 RMSE
Maximum feature order 2: 1.87 RMSE
Maximum feature order 3: 0.53 RMSE
Maximum feature order 4: 4.52 RMSE
Maximum feature order 5: 1.70 RMSE
Maximum feature order 6: 2.82 RMSE
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_features_1.svgz)

2. `python3 linear_regression_features.py --data_size=30 --test_size=20 --range=9`
```
Maximum feature order 1: 0.56 RMSE
Maximum feature order 2: 1.53 RMSE
Maximum feature order 3: 1.10 RMSE
Maximum feature order 4: 0.28 RMSE
Maximum feature order 5: 1.60 RMSE
Maximum feature order 6: 3.09 RMSE
Maximum feature order 7: 3.92 RMSE
Maximum feature order 8: 65.11 RMSE
Maximum feature order 9: 3886.97 RMSE
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_features_2.svgz)

3. `python3 linear_regression_features.py --data_size=50 --test_size=40 --range=9`
```
Maximum feature order 1: 0.63 RMSE
Maximum feature order 2: 0.73 RMSE
Maximum feature order 3: 0.31 RMSE
Maximum feature order 4: 0.26 RMSE
Maximum feature order 5: 1.22 RMSE
Maximum feature order 6: 0.69 RMSE
Maximum feature order 7: 2.39 RMSE
Maximum feature order 8: 7.28 RMSE
Maximum feature order 9: 201.70 RMSE
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_features_3.svgz)
#### Tests End:
