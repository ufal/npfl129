### Assignment: linear_regression_features
#### Date: Deadline: Oct 20, 23:59
#### Points: 3 points
#### Examples: linear_regression_features_examples

Starting with the
[linear_regression_features.py](https://github.com/ufal/npfl129/tree/master/labs/01/linear_regression_features.py)
template, use `scikit-learn` to train a model of a 1D curve.

Try using features $x^1, x^2, …, x^D$ for $D$ from 1 to a given range, and
report RMSE of every such configuration.

#### Examples Start: linear_regression_features_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 linear_regression_features.py --data_size=10 --test_size=5 --range=5`
```
Maximum feature order 1: 0.74 RMSE
Maximum feature order 2: 1.87 RMSE
Maximum feature order 3: 0.53 RMSE
Maximum feature order 4: 4.52 RMSE
Maximum feature order 5: 1.70 RMSE
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_features_1.svgz)
- `python3 linear_regression_features.py --data_size=50 --test_size=40 --range=9`
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
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_features_2.svgz)
#### Examples End:
