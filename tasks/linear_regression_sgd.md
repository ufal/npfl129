### Assignment: linear_regression_sgd
#### Date: Deadline: Oct 27, 23:59
#### Points: 5 points
#### Examples: linear_regression_sgd_examples

Starting with the [linear_regression_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/02/linear_regression_sgd.py),
implement minibatch SGD for linear regression and compare the results to an
explicit linear regression solver.

#### Examples Start: linear_regression_sgd_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 88.98, explicit 91.51
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_sgd_1.svgz)
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.1`
```
Test RMSE: SGD 88.80, explicit 91.51
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_sgd_2.svgz)
- `python3 linear_regression_sgd.py --batch_size=10 --epochs=50 --learning_rate=0.001`
```
Test RMSE: SGD 106.51, explicit 91.51
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_sgd_3.svgz)
- `python3 linear_regression_sgd.py --batch_size=1  --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 88.80, explicit 91.51
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_sgd_4.svgz)
- `python3 linear_regression_sgd.py --batch_size=50 --epochs=50 --learning_rate=0.01`
```
Test RMSE: SGD 97.63, explicit 91.51
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/linear_regression_sgd_5.svgz)
#### Examples End:
