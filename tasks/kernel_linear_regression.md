### Assignment: kernel_linear_regression
#### Date: Deadline: Nov 22, 23:59
#### Points: 5 points
#### Examples: kernel_linear_regression_examples
#### Tests: kernel_linear_regression_tests

Starting with the [kernel_linear_regression.py](https://github.com/ufal/npfl129/tree/master/labs/06/kernel_linear_regression.py),
implement kernel linear regression training using SGD
on the dual formulation. You should support _polynomial_
and _Gaussian_ kernels and also L2 regularization.

#### Examples Start: kernel_linear_regression_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
```
Iteration 10, train RMSE 0.59, test RMSE 1.10
Iteration 20, train RMSE 0.48, test RMSE 0.98
Iteration 30, train RMSE 0.51, test RMSE 1.15
Iteration 40, train RMSE 0.49, test RMSE 1.13
Iteration 50, train RMSE 0.47, test RMSE 1.10
Iteration 60, train RMSE 0.48, test RMSE 1.23
Iteration 70, train RMSE 0.49, test RMSE 1.29
Iteration 80, train RMSE 0.48, test RMSE 1.24
Iteration 90, train RMSE 0.47, test RMSE 1.12
Iteration 100, train RMSE 0.49, test RMSE 1.02
Iteration 110, train RMSE 0.52, test RMSE 1.22
Iteration 120, train RMSE 0.53, test RMSE 1.37
Iteration 130, train RMSE 0.50, test RMSE 1.28
Iteration 140, train RMSE 0.49, test RMSE 1.25
Iteration 150, train RMSE 0.53, test RMSE 1.19
Iteration 160, train RMSE 0.49, test RMSE 1.02
Iteration 170, train RMSE 0.51, test RMSE 1.12
Iteration 180, train RMSE 0.48, test RMSE 1.24
Iteration 190, train RMSE 0.47, test RMSE 1.13
Iteration 200, train RMSE 0.48, test RMSE 1.12
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_1.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
Iteration 10, train RMSE 0.61, test RMSE 1.59
Iteration 20, train RMSE 0.52, test RMSE 0.92
Iteration 30, train RMSE 0.48, test RMSE 1.08
Iteration 40, train RMSE 0.45, test RMSE 1.01
Iteration 50, train RMSE 0.47, test RMSE 0.71
Iteration 60, train RMSE 0.43, test RMSE 0.89
Iteration 70, train RMSE 0.45, test RMSE 1.01
Iteration 80, train RMSE 0.41, test RMSE 0.86
Iteration 90, train RMSE 0.43, test RMSE 0.63
Iteration 100, train RMSE 0.50, test RMSE 0.38
Iteration 110, train RMSE 0.38, test RMSE 0.60
Iteration 120, train RMSE 0.43, test RMSE 0.79
Iteration 130, train RMSE 0.36, test RMSE 0.56
Iteration 140, train RMSE 0.36, test RMSE 0.53
Iteration 150, train RMSE 0.39, test RMSE 0.50
Iteration 160, train RMSE 0.36, test RMSE 0.49
Iteration 170, train RMSE 0.35, test RMSE 0.29
Iteration 180, train RMSE 0.31, test RMSE 0.29
Iteration 190, train RMSE 0.31, test RMSE 0.24
Iteration 200, train RMSE 0.37, test RMSE 0.34
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_2.svgz)
- `python3 kernel_linear_regression.py --batch_size=5 --kernel=poly --kernel_degree=5 --learning_rate=0.1`
```
Iteration 10, train RMSE 0.52, test RMSE 1.20
Iteration 20, train RMSE 0.48, test RMSE 1.01
Iteration 30, train RMSE 0.49, test RMSE 1.09
Iteration 40, train RMSE 0.47, test RMSE 1.05
Iteration 50, train RMSE 0.47, test RMSE 0.96
Iteration 60, train RMSE 0.47, test RMSE 1.16
Iteration 70, train RMSE 0.45, test RMSE 1.12
Iteration 80, train RMSE 0.44, test RMSE 1.02
Iteration 90, train RMSE 0.45, test RMSE 0.87
Iteration 100, train RMSE 0.43, test RMSE 0.86
Iteration 110, train RMSE 0.44, test RMSE 0.95
Iteration 120, train RMSE 0.44, test RMSE 1.04
Iteration 130, train RMSE 0.43, test RMSE 0.96
Iteration 140, train RMSE 0.42, test RMSE 0.91
Iteration 150, train RMSE 0.44, test RMSE 0.79
Iteration 160, train RMSE 0.43, test RMSE 0.64
Iteration 170, train RMSE 0.42, test RMSE 0.72
Iteration 180, train RMSE 0.41, test RMSE 0.86
Iteration 190, train RMSE 0.39, test RMSE 0.69
Iteration 200, train RMSE 0.39, test RMSE 0.70
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_3.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf`
```
Iteration 10, train RMSE 0.78, test RMSE 0.66
Iteration 20, train RMSE 0.74, test RMSE 0.61
Iteration 30, train RMSE 0.71, test RMSE 0.58
Iteration 40, train RMSE 0.67, test RMSE 0.54
Iteration 50, train RMSE 0.64, test RMSE 0.52
Iteration 60, train RMSE 0.62, test RMSE 0.50
Iteration 70, train RMSE 0.59, test RMSE 0.48
Iteration 80, train RMSE 0.57, test RMSE 0.47
Iteration 90, train RMSE 0.55, test RMSE 0.46
Iteration 100, train RMSE 0.53, test RMSE 0.45
Iteration 110, train RMSE 0.51, test RMSE 0.45
Iteration 120, train RMSE 0.49, test RMSE 0.45
Iteration 130, train RMSE 0.48, test RMSE 0.45
Iteration 140, train RMSE 0.46, test RMSE 0.46
Iteration 150, train RMSE 0.45, test RMSE 0.46
Iteration 160, train RMSE 0.44, test RMSE 0.47
Iteration 170, train RMSE 0.43, test RMSE 0.48
Iteration 180, train RMSE 0.42, test RMSE 0.49
Iteration 190, train RMSE 0.41, test RMSE 0.49
Iteration 200, train RMSE 0.40, test RMSE 0.50
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_4.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
```
Iteration 10, train RMSE 0.80, test RMSE 0.69
Iteration 20, train RMSE 0.79, test RMSE 0.67
Iteration 30, train RMSE 0.79, test RMSE 0.66
Iteration 40, train RMSE 0.78, test RMSE 0.65
Iteration 50, train RMSE 0.77, test RMSE 0.64
Iteration 60, train RMSE 0.76, test RMSE 0.64
Iteration 70, train RMSE 0.76, test RMSE 0.63
Iteration 80, train RMSE 0.75, test RMSE 0.62
Iteration 90, train RMSE 0.74, test RMSE 0.61
Iteration 100, train RMSE 0.74, test RMSE 0.61
Iteration 110, train RMSE 0.73, test RMSE 0.60
Iteration 120, train RMSE 0.72, test RMSE 0.59
Iteration 130, train RMSE 0.72, test RMSE 0.59
Iteration 140, train RMSE 0.71, test RMSE 0.58
Iteration 150, train RMSE 0.71, test RMSE 0.58
Iteration 160, train RMSE 0.70, test RMSE 0.57
Iteration 170, train RMSE 0.69, test RMSE 0.57
Iteration 180, train RMSE 0.69, test RMSE 0.56
Iteration 190, train RMSE 0.68, test RMSE 0.56
Iteration 200, train RMSE 0.68, test RMSE 0.56
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_5.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=5`
```
Iteration 10, train RMSE 0.52, test RMSE 0.40
Iteration 20, train RMSE 0.36, test RMSE 0.22
Iteration 30, train RMSE 0.27, test RMSE 0.14
Iteration 40, train RMSE 0.24, test RMSE 0.13
Iteration 50, train RMSE 0.22, test RMSE 0.14
Iteration 60, train RMSE 0.22, test RMSE 0.16
Iteration 70, train RMSE 0.21, test RMSE 0.16
Iteration 80, train RMSE 0.21, test RMSE 0.17
Iteration 90, train RMSE 0.21, test RMSE 0.17
Iteration 100, train RMSE 0.21, test RMSE 0.17
Iteration 110, train RMSE 0.21, test RMSE 0.18
Iteration 120, train RMSE 0.21, test RMSE 0.18
Iteration 130, train RMSE 0.21, test RMSE 0.18
Iteration 140, train RMSE 0.21, test RMSE 0.18
Iteration 150, train RMSE 0.21, test RMSE 0.18
Iteration 160, train RMSE 0.21, test RMSE 0.18
Iteration 170, train RMSE 0.21, test RMSE 0.17
Iteration 180, train RMSE 0.21, test RMSE 0.17
Iteration 190, train RMSE 0.21, test RMSE 0.17
Iteration 200, train RMSE 0.21, test RMSE 0.17
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_6.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50`
```
Iteration 10, train RMSE 0.52, test RMSE 0.44
Iteration 20, train RMSE 0.36, test RMSE 0.28
Iteration 30, train RMSE 0.27, test RMSE 0.21
Iteration 40, train RMSE 0.23, test RMSE 0.17
Iteration 50, train RMSE 0.21, test RMSE 0.16
Iteration 60, train RMSE 0.21, test RMSE 0.16
Iteration 70, train RMSE 0.20, test RMSE 0.16
Iteration 80, train RMSE 0.20, test RMSE 0.16
Iteration 90, train RMSE 0.20, test RMSE 0.16
Iteration 100, train RMSE 0.20, test RMSE 0.15
Iteration 110, train RMSE 0.19, test RMSE 0.15
Iteration 120, train RMSE 0.19, test RMSE 0.15
Iteration 130, train RMSE 0.19, test RMSE 0.15
Iteration 140, train RMSE 0.19, test RMSE 0.15
Iteration 150, train RMSE 0.19, test RMSE 0.15
Iteration 160, train RMSE 0.19, test RMSE 0.15
Iteration 170, train RMSE 0.19, test RMSE 0.15
Iteration 180, train RMSE 0.19, test RMSE 0.15
Iteration 190, train RMSE 0.19, test RMSE 0.15
Iteration 200, train RMSE 0.19, test RMSE 0.15
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_7.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
```
Iteration 10, train RMSE 0.54, test RMSE 0.45
Iteration 20, train RMSE 0.39, test RMSE 0.31
Iteration 30, train RMSE 0.32, test RMSE 0.25
Iteration 40, train RMSE 0.28, test RMSE 0.21
Iteration 50, train RMSE 0.26, test RMSE 0.20
Iteration 60, train RMSE 0.25, test RMSE 0.19
Iteration 70, train RMSE 0.25, test RMSE 0.18
Iteration 80, train RMSE 0.24, test RMSE 0.18
Iteration 90, train RMSE 0.24, test RMSE 0.18
Iteration 100, train RMSE 0.24, test RMSE 0.17
Iteration 110, train RMSE 0.24, test RMSE 0.17
Iteration 120, train RMSE 0.24, test RMSE 0.17
Iteration 130, train RMSE 0.24, test RMSE 0.17
Iteration 140, train RMSE 0.24, test RMSE 0.17
Iteration 150, train RMSE 0.24, test RMSE 0.17
Iteration 160, train RMSE 0.24, test RMSE 0.17
Iteration 170, train RMSE 0.24, test RMSE 0.17
Iteration 180, train RMSE 0.24, test RMSE 0.17
Iteration 190, train RMSE 0.24, test RMSE 0.17
Iteration 200, train RMSE 0.24, test RMSE 0.17
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kernel_linear_regression_8.svgz)
#### Examples End:
#### Tests Start: kernel_linear_regression_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
```
Iteration 10, train RMSE 0.59, test RMSE 1.10
Iteration 20, train RMSE 0.48, test RMSE 0.98
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
Iteration 10, train RMSE 0.61, test RMSE 1.59
Iteration 20, train RMSE 0.52, test RMSE 0.92
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=5 --kernel=poly --kernel_degree=5 --learning_rate=0.1`
```
Iteration 10, train RMSE 0.52, test RMSE 1.20
Iteration 20, train RMSE 0.48, test RMSE 1.01
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=rbf`
```
Iteration 10, train RMSE 0.78, test RMSE 0.66
Iteration 20, train RMSE 0.74, test RMSE 0.61
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
```
Iteration 10, train RMSE 0.80, test RMSE 0.69
Iteration 20, train RMSE 0.79, test RMSE 0.67
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=rbf --kernel_gamma=5`
```
Iteration 10, train RMSE 0.52, test RMSE 0.40
Iteration 20, train RMSE 0.36, test RMSE 0.22
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=rbf --kernel_gamma=50`
```
Iteration 10, train RMSE 0.52, test RMSE 0.44
Iteration 20, train RMSE 0.36, test RMSE 0.28
```
- `python3 kernel_linear_regression.py --iterations=20 --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
```
Iteration 10, train RMSE 0.54, test RMSE 0.45
Iteration 20, train RMSE 0.39, test RMSE 0.31
```
#### Tests End:
