### Assignment: kernel_linear_regression
#### Date: Deadline: Nov 21, 7:59 a.m.
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
After epoch 10: train RMSE 0.62, test RMSE 1.07
After epoch 20: train RMSE 0.51, test RMSE 0.96
After epoch 30: train RMSE 0.54, test RMSE 1.16
After epoch 40: train RMSE 0.51, test RMSE 1.12
After epoch 50: train RMSE 0.47, test RMSE 1.12
After epoch 60: train RMSE 0.50, test RMSE 1.22
After epoch 70: train RMSE 0.50, test RMSE 1.29
After epoch 80: train RMSE 0.47, test RMSE 1.23
After epoch 90: train RMSE 0.48, test RMSE 1.12
After epoch 100: train RMSE 0.49, test RMSE 1.02
After epoch 110: train RMSE 0.56, test RMSE 1.24
After epoch 120: train RMSE 0.54, test RMSE 1.35
After epoch 130: train RMSE 0.53, test RMSE 1.28
After epoch 140: train RMSE 0.50, test RMSE 1.24
After epoch 150: train RMSE 0.57, test RMSE 1.20
After epoch 160: train RMSE 0.49, test RMSE 1.02
After epoch 170: train RMSE 0.50, test RMSE 1.12
After epoch 180: train RMSE 0.48, test RMSE 1.22
After epoch 190: train RMSE 0.47, test RMSE 1.14
After epoch 200: train RMSE 0.49, test RMSE 1.10
Learned betas -15.61 -10.44 0.22 9.84 5.67 7.16 16.56 12.84 6.20 9.09 1.92 0.39 1.48 -10.78 -12.60 ...
Learned bias 0.508105605626597
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_1.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
After epoch 10: train RMSE 0.62, test RMSE 1.59
After epoch 20: train RMSE 0.53, test RMSE 0.91
After epoch 30: train RMSE 0.50, test RMSE 1.11
After epoch 40: train RMSE 0.46, test RMSE 1.01
After epoch 50: train RMSE 0.46, test RMSE 0.74
After epoch 60: train RMSE 0.44, test RMSE 0.91
After epoch 70: train RMSE 0.45, test RMSE 1.03
After epoch 80: train RMSE 0.41, test RMSE 0.87
After epoch 90: train RMSE 0.44, test RMSE 0.65
After epoch 100: train RMSE 0.50, test RMSE 0.39
After epoch 110: train RMSE 0.40, test RMSE 0.64
After epoch 120: train RMSE 0.43, test RMSE 0.80
After epoch 130: train RMSE 0.37, test RMSE 0.58
After epoch 140: train RMSE 0.37, test RMSE 0.54
After epoch 150: train RMSE 0.41, test RMSE 0.53
After epoch 160: train RMSE 0.36, test RMSE 0.50
After epoch 170: train RMSE 0.35, test RMSE 0.31
After epoch 180: train RMSE 0.32, test RMSE 0.31
After epoch 190: train RMSE 0.31, test RMSE 0.26
After epoch 200: train RMSE 0.38, test RMSE 0.33
Learned betas -5.74 -4.70 0.07 4.47 1.47 2.00 7.15 5.52 2.18 3.97 0.72 0.19 1.09 -5.04 -5.61 ...
Learned bias 0.49826947783955583
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_2.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --kernel_gamma=0.15`
```
After epoch 10: train RMSE 0.80, test RMSE 0.66
After epoch 20: train RMSE 0.78, test RMSE 0.65
After epoch 30: train RMSE 0.76, test RMSE 0.63
After epoch 40: train RMSE 0.78, test RMSE 0.66
After epoch 50: train RMSE 0.75, test RMSE 0.63
After epoch 60: train RMSE 0.74, test RMSE 0.63
After epoch 70: train RMSE 0.72, test RMSE 0.61
After epoch 80: train RMSE 0.71, test RMSE 0.60
After epoch 90: train RMSE 0.72, test RMSE 0.63
After epoch 100: train RMSE 0.70, test RMSE 0.60
After epoch 110: train RMSE 0.74, test RMSE 0.66
After epoch 120: train RMSE 0.72, test RMSE 0.65
After epoch 130: train RMSE 0.70, test RMSE 0.62
After epoch 140: train RMSE 0.67, test RMSE 0.59
After epoch 150: train RMSE 0.67, test RMSE 0.61
After epoch 160: train RMSE 0.66, test RMSE 0.61
After epoch 170: train RMSE 0.65, test RMSE 0.61
After epoch 180: train RMSE 0.64, test RMSE 0.60
After epoch 190: train RMSE 0.64, test RMSE 0.62
After epoch 200: train RMSE 0.64, test RMSE 0.65
Learned betas 3.71 3.37 6.14 8.73 4.32 3.87 7.08 4.06 -0.34 0.62 -3.70 -4.91 -4.79 -11.33 -12.09 ...
Learned bias 0.385092447610249
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_3.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --l2=0.02`
```
After epoch 10: train RMSE 0.62, test RMSE 1.50
After epoch 20: train RMSE 0.55, test RMSE 0.88
After epoch 30: train RMSE 0.51, test RMSE 1.10
After epoch 40: train RMSE 0.50, test RMSE 1.04
After epoch 50: train RMSE 0.50, test RMSE 0.85
After epoch 60: train RMSE 0.48, test RMSE 1.03
After epoch 70: train RMSE 0.52, test RMSE 1.26
After epoch 80: train RMSE 0.49, test RMSE 1.15
After epoch 90: train RMSE 0.49, test RMSE 0.94
After epoch 100: train RMSE 0.57, test RMSE 0.68
After epoch 110: train RMSE 0.53, test RMSE 1.07
After epoch 120: train RMSE 0.55, test RMSE 1.29
After epoch 130: train RMSE 0.50, test RMSE 1.14
After epoch 140: train RMSE 0.49, test RMSE 1.07
After epoch 150: train RMSE 0.57, test RMSE 1.09
After epoch 160: train RMSE 0.47, test RMSE 0.93
After epoch 170: train RMSE 0.50, test RMSE 0.96
After epoch 180: train RMSE 0.47, test RMSE 1.04
After epoch 190: train RMSE 0.47, test RMSE 1.03
After epoch 200: train RMSE 0.54, test RMSE 0.96
Learned betas -0.61 -0.45 -0.08 0.53 0.37 0.32 0.83 0.57 0.24 0.42 0.05 -0.01 0.04 -0.65 -0.72 ...
Learned bias 0.9235402057573058
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_4.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf`
```
After epoch 10: train RMSE 0.78, test RMSE 0.66
After epoch 20: train RMSE 0.74, test RMSE 0.62
After epoch 30: train RMSE 0.71, test RMSE 0.58
After epoch 40: train RMSE 0.67, test RMSE 0.55
After epoch 50: train RMSE 0.64, test RMSE 0.52
After epoch 60: train RMSE 0.62, test RMSE 0.50
After epoch 70: train RMSE 0.59, test RMSE 0.48
After epoch 80: train RMSE 0.57, test RMSE 0.47
After epoch 90: train RMSE 0.55, test RMSE 0.46
After epoch 100: train RMSE 0.53, test RMSE 0.45
After epoch 110: train RMSE 0.51, test RMSE 0.45
After epoch 120: train RMSE 0.49, test RMSE 0.45
After epoch 130: train RMSE 0.48, test RMSE 0.45
After epoch 140: train RMSE 0.46, test RMSE 0.46
After epoch 150: train RMSE 0.45, test RMSE 0.46
After epoch 160: train RMSE 0.44, test RMSE 0.47
After epoch 170: train RMSE 0.43, test RMSE 0.48
After epoch 180: train RMSE 0.42, test RMSE 0.48
After epoch 190: train RMSE 0.41, test RMSE 0.49
After epoch 200: train RMSE 0.40, test RMSE 0.50
Learned betas 0.65 0.59 1.16 1.71 0.86 0.81 1.60 1.03 0.20 0.47 -0.31 -0.56 -0.46 -1.76 -1.86 ...
Learned bias 0.6533387254029029
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_5.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
```
After epoch 10: train RMSE 0.81, test RMSE 0.69
After epoch 20: train RMSE 0.80, test RMSE 0.67
After epoch 30: train RMSE 0.79, test RMSE 0.66
After epoch 40: train RMSE 0.78, test RMSE 0.65
After epoch 50: train RMSE 0.77, test RMSE 0.64
After epoch 60: train RMSE 0.77, test RMSE 0.64
After epoch 70: train RMSE 0.76, test RMSE 0.63
After epoch 80: train RMSE 0.75, test RMSE 0.62
After epoch 90: train RMSE 0.74, test RMSE 0.61
After epoch 100: train RMSE 0.74, test RMSE 0.61
After epoch 110: train RMSE 0.73, test RMSE 0.60
After epoch 120: train RMSE 0.73, test RMSE 0.60
After epoch 130: train RMSE 0.72, test RMSE 0.59
After epoch 140: train RMSE 0.71, test RMSE 0.58
After epoch 150: train RMSE 0.71, test RMSE 0.58
After epoch 160: train RMSE 0.70, test RMSE 0.57
After epoch 170: train RMSE 0.69, test RMSE 0.57
After epoch 180: train RMSE 0.69, test RMSE 0.56
After epoch 190: train RMSE 0.68, test RMSE 0.56
After epoch 200: train RMSE 0.68, test RMSE 0.56
Learned betas 1.44 1.27 1.73 2.15 1.17 1.00 1.66 0.97 0.03 0.19 -0.68 -1.01 -0.98 -2.34 -2.48 ...
Learned bias 0.6349201284266073
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_6.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=5`
```
After epoch 10: train RMSE 0.52, test RMSE 0.40
After epoch 20: train RMSE 0.36, test RMSE 0.22
After epoch 30: train RMSE 0.28, test RMSE 0.15
After epoch 40: train RMSE 0.24, test RMSE 0.14
After epoch 50: train RMSE 0.22, test RMSE 0.15
After epoch 60: train RMSE 0.22, test RMSE 0.16
After epoch 70: train RMSE 0.21, test RMSE 0.16
After epoch 80: train RMSE 0.21, test RMSE 0.17
After epoch 90: train RMSE 0.21, test RMSE 0.18
After epoch 100: train RMSE 0.21, test RMSE 0.18
After epoch 110: train RMSE 0.21, test RMSE 0.18
After epoch 120: train RMSE 0.21, test RMSE 0.18
After epoch 130: train RMSE 0.21, test RMSE 0.18
After epoch 140: train RMSE 0.21, test RMSE 0.18
After epoch 150: train RMSE 0.21, test RMSE 0.18
After epoch 160: train RMSE 0.21, test RMSE 0.18
After epoch 170: train RMSE 0.21, test RMSE 0.18
After epoch 180: train RMSE 0.21, test RMSE 0.18
After epoch 190: train RMSE 0.21, test RMSE 0.18
After epoch 200: train RMSE 0.21, test RMSE 0.18
Learned betas 0.16 -0.11 0.32 0.77 -0.10 -0.10 0.81 0.41 -0.19 0.33 -0.16 -0.13 0.24 -0.82 -0.72 ...
Learned bias 0.7233374435314919
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_7.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50`
```
After epoch 10: train RMSE 0.52, test RMSE 0.44
After epoch 20: train RMSE 0.36, test RMSE 0.29
After epoch 30: train RMSE 0.27, test RMSE 0.21
After epoch 40: train RMSE 0.23, test RMSE 0.18
After epoch 50: train RMSE 0.21, test RMSE 0.17
After epoch 60: train RMSE 0.20, test RMSE 0.17
After epoch 70: train RMSE 0.20, test RMSE 0.16
After epoch 80: train RMSE 0.20, test RMSE 0.16
After epoch 90: train RMSE 0.20, test RMSE 0.16
After epoch 100: train RMSE 0.20, test RMSE 0.16
After epoch 110: train RMSE 0.19, test RMSE 0.16
After epoch 120: train RMSE 0.19, test RMSE 0.16
After epoch 130: train RMSE 0.19, test RMSE 0.16
After epoch 140: train RMSE 0.19, test RMSE 0.16
After epoch 150: train RMSE 0.19, test RMSE 0.16
After epoch 160: train RMSE 0.19, test RMSE 0.16
After epoch 170: train RMSE 0.19, test RMSE 0.16
After epoch 180: train RMSE 0.19, test RMSE 0.16
After epoch 190: train RMSE 0.19, test RMSE 0.16
After epoch 200: train RMSE 0.19, test RMSE 0.16
Learned betas 0.60 0.04 0.28 0.67 -0.21 -0.21 0.69 0.28 -0.31 0.25 -0.17 -0.06 0.41 -0.58 -0.48 ...
Learned bias 0.8361226793231809
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_8.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
```
After epoch 10: train RMSE 0.54, test RMSE 0.45
After epoch 20: train RMSE 0.39, test RMSE 0.32
After epoch 30: train RMSE 0.32, test RMSE 0.25
After epoch 40: train RMSE 0.28, test RMSE 0.22
After epoch 50: train RMSE 0.26, test RMSE 0.20
After epoch 60: train RMSE 0.25, test RMSE 0.19
After epoch 70: train RMSE 0.25, test RMSE 0.18
After epoch 80: train RMSE 0.24, test RMSE 0.18
After epoch 90: train RMSE 0.24, test RMSE 0.18
After epoch 100: train RMSE 0.24, test RMSE 0.18
After epoch 110: train RMSE 0.24, test RMSE 0.18
After epoch 120: train RMSE 0.24, test RMSE 0.18
After epoch 130: train RMSE 0.24, test RMSE 0.17
After epoch 140: train RMSE 0.24, test RMSE 0.17
After epoch 150: train RMSE 0.24, test RMSE 0.17
After epoch 160: train RMSE 0.24, test RMSE 0.17
After epoch 170: train RMSE 0.24, test RMSE 0.17
After epoch 180: train RMSE 0.24, test RMSE 0.17
After epoch 190: train RMSE 0.24, test RMSE 0.17
After epoch 200: train RMSE 0.24, test RMSE 0.17
Learned betas 0.35 0.12 0.22 0.38 -0.01 -0.03 0.35 0.16 -0.11 0.12 -0.09 -0.06 0.12 -0.33 -0.30 ...
Learned bias 0.9189943209387189
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_9.svgz)
#### Examples End:
#### Tests Start: kernel_linear_regression_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
```
After epoch 10: train RMSE 0.62, test RMSE 1.07
After epoch 20: train RMSE 0.51, test RMSE 0.96
Learned betas -0.64 -0.36 0.57 1.37 0.65 0.81 1.39 1.08 0.27 0.45 -0.32 -0.32 -0.41 -1.43 -1.72 ...
Learned bias 0.4077383039526549
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
After epoch 10: train RMSE 0.62, test RMSE 1.59
After epoch 20: train RMSE 0.53, test RMSE 0.91
Learned betas -0.77 -0.54 0.19 0.59 0.22 0.42 0.75 0.68 0.25 0.38 -0.00 0.05 -0.03 -0.60 -0.70 ...
Learned bias 0.4546544361118512
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --kernel_gamma=0.15`
```
After epoch 10: train RMSE 0.80, test RMSE 0.66
After epoch 20: train RMSE 0.78, test RMSE 0.65
Learned betas 0.68 0.59 0.83 1.07 0.54 0.43 0.67 0.38 -0.09 -0.03 -0.48 -0.59 -0.61 -1.17 -1.31 ...
Learned bias 0.4111906185199331
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --l2=0.02`
```
After epoch 10: train RMSE 0.62, test RMSE 1.50
After epoch 20: train RMSE 0.55, test RMSE 0.88
Learned betas -0.45 -0.30 0.12 0.36 0.13 0.26 0.47 0.41 0.15 0.22 -0.02 0.02 -0.04 -0.40 -0.45 ...
Learned bias 0.6187601705172338
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf`
```
After epoch 10: train RMSE 0.78, test RMSE 0.66
After epoch 20: train RMSE 0.74, test RMSE 0.62
Learned betas 0.21 0.19 0.23 0.27 0.17 0.14 0.20 0.13 0.03 0.04 -0.05 -0.08 -0.08 -0.22 -0.24 ...
Learned bias 0.6131012801218498
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
```
After epoch 10: train RMSE 0.81, test RMSE 0.69
After epoch 20: train RMSE 0.80, test RMSE 0.67
Learned betas 0.22 0.19 0.24 0.27 0.17 0.14 0.20 0.12 0.02 0.03 -0.06 -0.09 -0.09 -0.23 -0.25 ...
Learned bias 0.5641037711361468
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=5`
```
After epoch 10: train RMSE 0.52, test RMSE 0.40
After epoch 20: train RMSE 0.36, test RMSE 0.22
Learned betas 0.16 0.14 0.18 0.22 0.12 0.10 0.17 0.11 0.03 0.05 -0.02 -0.04 -0.03 -0.15 -0.16 ...
Learned bias 0.7219215265350089
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=50`
```
After epoch 10: train RMSE 0.52, test RMSE 0.44
After epoch 20: train RMSE 0.36, test RMSE 0.29
Learned betas 0.19 0.15 0.18 0.21 0.11 0.09 0.16 0.10 0.02 0.05 -0.02 -0.04 -0.02 -0.14 -0.15 ...
Learned bias 0.8442484226378268
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
```
After epoch 10: train RMSE 0.54, test RMSE 0.45
After epoch 20: train RMSE 0.39, test RMSE 0.32
Learned betas 0.17 0.13 0.16 0.19 0.10 0.08 0.15 0.09 0.02 0.05 -0.02 -0.04 -0.02 -0.13 -0.14 ...
Learned bias 0.8574226518868522
```
#### Tests End:
