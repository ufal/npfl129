### Assignment: linear_regression_sgd
#### Date: Deadline: Oct 24, 7:59 a.m.
#### Points: 4 points
#### Tests: linear_regression_sgd_tests

Starting with the [linear_regression_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/02/linear_regression_sgd.py),
implement minibatch SGD for linear regression and compare the results to an
explicit linear regression solver.

#### Tests Start: linear_regression_sgd_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 90.96, explicit 91.38
Learned weights: 3.94 7.52 0.08 30.82 -1.72 -1.13 -1.98 6.29 1.98 -10.60 -13.84 -4.31 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_1.svgz)
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.1`
```
Test RMSE: SGD 90.73, explicit 91.38
Learned weights: 1.94 8.31 1.22 33.18 -3.74 -3.64 -2.46 5.19 1.72 -12.40 -14.08 -2.28 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_2.svgz)
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.001`
```
Test RMSE: SGD 108.66, explicit 91.38
Learned weights: 2.79 2.19 -0.06 14.16 -1.07 0.97 0.78 4.62 0.79 -4.62 -7.37 -3.07 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_3.svgz)
- `python3 linear_regression_sgd.py --batch_size=1  --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 90.73, explicit 91.38
Learned weights: 1.94 8.31 1.22 33.18 -3.74 -3.64 -2.46 5.19 1.72 -12.40 -14.08 -2.28 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_4.svgz)
- `python3 linear_regression_sgd.py --batch_size=50 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 99.74, explicit 91.38
Learned weights: 3.99 3.67 -0.20 20.79 -1.29 1.37 0.47 6.54 1.54 -6.95 -10.65 -4.50 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_5.svgz)
- `python3 linear_regression_sgd.py --batch_size=50 --epochs=500 --learning_rate=0.01`
```
Test RMSE: SGD 90.67, explicit 91.38
Learned weights: 3.20 8.00 0.57 32.21 -2.49 -2.45 -2.28 5.57 1.69 -11.47 -14.00 -3.44 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_6.svgz)
- `python3 linear_regression_sgd.py --batch_size=50 --epochs=500 --learning_rate=0.01 --l2=0.1`
```
Test RMSE: SGD 90.71, explicit 91.38
Learned weights: 3.40 7.36 0.32 30.21 -2.14 -1.68 -1.88 5.79 1.72 -10.84 -13.45 -3.73 ...
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/linear_regression_sgd_7.svgz)
#### Tests End:
