### Assignment: linear_regression_sgd
#### Date: Deadline: Oct 24, 7:59 a.m.
#### Points: 4 points
#### Tests: linear_regression_sgd_tests

Starting with the [linear_regression_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/02/linear_regression_sgd.py),
implement minibatch SGD for linear regression and compare the results to an
explicit linear regression solver.

#### Tests Start: linear_regression_sgd_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 114.118, explicit 115.6
Learned weights: 6.864 6.907 -1.208 -2.252 -1.464 -13.323 13.909 4.883 -11.468 -0.229 37.803 -5.191 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_1.svgz)

2. `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.1`
```
Test RMSE: SGD 111.395, explicit 115.6
Learned weights: 11.559 12.428 -1.529 -2.236 -1.575 -8.868 18.842 3.882 -7.175 -1.373 38.918 -6.522 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_2.svgz)

3. `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.001`
```
Test RMSE: SGD 151.210, explicit 115.6
Learned weights: 1.885 -0.580 -0.386 0.389 -1.745 -6.994 6.787 3.019 -8.013 0.353 15.712 -3.322 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_3.svgz)

4. `python3 linear_regression_sgd.py --batch_size=1  --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 111.395, explicit 115.6
Learned weights: 11.559 12.429 -1.529 -2.236 -1.574 -8.868 18.843 3.882 -7.174 -1.373 38.917 -6.522 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_4.svgz)

5. `python3 linear_regression_sgd.py --batch_size=50 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 136.015, explicit 115.6
Learned weights: 2.940 0.504 -0.555 0.143 -2.088 -10.664 9.146 4.607 -11.620 0.129 24.294 -4.089 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_5.svgz)

6. `python3 linear_regression_sgd.py --batch_size=50 --epochs=500 --learning_rate=0.01`
```
Test RMSE: SGD 111.914, explicit 115.6
Learned weights: 9.360 9.428 -1.333 -2.646 -1.379 -11.248 16.352 4.153 -9.041 -0.755 38.872 -5.881 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_6.svgz)

7. `python3 linear_regression_sgd.py --batch_size=50 --epochs=500 --learning_rate=0.01 --l2=0.1`
```
Test RMSE: SGD 113.521, explicit 115.6
Learned weights: 8.013 7.818 -1.227 -2.234 -1.491 -11.592 14.863 4.343 -9.807 -0.575 36.745 -5.487 ...
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/linear_regression_sgd_7.svgz)
#### Tests End:
