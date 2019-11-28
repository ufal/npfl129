### Assignment: kernelized_linear_regression
#### Date: Deadline: Dec 01, 23:59
#### Points: 5 points
#### Examples: kernelized_linear_regression_examples

Starting with the [kernelized_linear_regression.py](https://github.com/ufal/npfl129/tree/master/labs/05/kernelized_linear_regression.py),
implement kernelized linear regression training using SGD
on the dual formulation. You should support _polynomial_
and _Gaussian_ kernels and also L2 regularization. More details
are present in the template.

#Examples Start: kernelized_linear_regression_examples
- `--examples=50 --kernel=rbf --kernel_gamma=1 --iterations=5 --l2=0 --learning_rate=0.05 --seed 42`
```
Iteration 1, train RMSE 0.80, test RMSE 0.68
Iteration 2, train RMSE 0.78, test RMSE 0.66
Iteration 3, train RMSE 0.76, test RMSE 0.63
Iteration 4, train RMSE 0.74, test RMSE 0.61
Iteration 5, train RMSE 0.72, test RMSE 0.59
```
- `--examples=50 --kernel=rbf --kernel_gamma=2 --iterations=5 --l2=0 --learning_rate=0.05 --seed 42`
```
Iteration 1, train RMSE 0.75, test RMSE 0.63
Iteration 2, train RMSE 0.68, test RMSE 0.56
Iteration 3, train RMSE 0.62, test RMSE 0.49
Iteration 4, train RMSE 0.57, test RMSE 0.44
Iteration 5, train RMSE 0.53, test RMSE 0.40
```
- `--examples=50 --kernel=rbf --kernel_gamma=1 --iterations=5 --l2=2.0 --learning_rate=0.05 --seed 42`
```
Iteration 1, train RMSE 0.80, test RMSE 0.68
Iteration 2, train RMSE 0.78, test RMSE 0.66
Iteration 3, train RMSE 0.76, test RMSE 0.64
Iteration 4, train RMSE 0.75, test RMSE 0.62
Iteration 5, train RMSE 0.74, test RMSE 0.61
```
- `--examples=50 --kernel=poly --kernel_gamma=1 --iterations=5 --l2=0 --learning_rate=0.01 --seed 42`
```
Iteration 1, train RMSE 0.75, test RMSE 0.82
Iteration 2, train RMSE 0.70, test RMSE 0.59
Iteration 3, train RMSE 0.66, test RMSE 0.74
Iteration 4, train RMSE 0.63, test RMSE 0.64
Iteration 5, train RMSE 0.61, test RMSE 0.74
```
#Examples End:
