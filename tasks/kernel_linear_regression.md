### Assignment: kernel_linear_regression
#### Date: Deadline: Nov 21, 7:59 a.m.
#### Points: 5 points
#### Examples: kernel_linear_regression_examples
#### Tests: kernel_linear_regression_tests

Starting with the [kernel_linear_regression.py](https://github.com/ufal/npfl129/tree/past-2223/labs/06/kernel_linear_regression.py),
implement kernel linear regression training using SGD
on the dual formulation. You should support _polynomial_
and _Gaussian_ kernels and also L2 regularization.

#### Examples Start: kernel_linear_regression_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --batch_size=5 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
```
After epoch 10: train RMSE 0.69, test RMSE 0.61
After epoch 20: train RMSE 0.61, test RMSE 0.65
After epoch 30: train RMSE 0.56, test RMSE 0.72
After epoch 40: train RMSE 0.53, test RMSE 0.77
After epoch 50: train RMSE 0.51, test RMSE 0.84
After epoch 60: train RMSE 0.49, test RMSE 0.91
After epoch 70: train RMSE 0.48, test RMSE 0.98
After epoch 80: train RMSE 0.48, test RMSE 1.01
After epoch 90: train RMSE 0.47, test RMSE 1.04
After epoch 100: train RMSE 0.47, test RMSE 1.05
After epoch 110: train RMSE 0.48, test RMSE 1.09
After epoch 120: train RMSE 0.47, test RMSE 1.12
After epoch 130: train RMSE 0.47, test RMSE 1.12
After epoch 140: train RMSE 0.47, test RMSE 1.13
After epoch 150: train RMSE 0.47, test RMSE 1.13
After epoch 160: train RMSE 0.47, test RMSE 1.10
After epoch 170: train RMSE 0.47, test RMSE 1.13
After epoch 180: train RMSE 0.47, test RMSE 1.16
After epoch 190: train RMSE 0.47, test RMSE 1.14
After epoch 200: train RMSE 0.47, test RMSE 1.14
Learned betas -2.28 -1.44 0.55 2.41 1.17 1.48 3.39 2.52 0.96 1.62 0.11 -0.37 -0.20 -2.91 -3.15 ...
Learned bias 0.44076460113546156
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_1.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
After epoch 10: train RMSE 0.63, test RMSE 1.61
After epoch 20: train RMSE 0.54, test RMSE 0.90
After epoch 30: train RMSE 0.49, test RMSE 1.11
After epoch 40: train RMSE 0.46, test RMSE 1.01
After epoch 50: train RMSE 0.47, test RMSE 0.72
After epoch 60: train RMSE 0.44, test RMSE 0.89
After epoch 70: train RMSE 0.46, test RMSE 1.03
After epoch 80: train RMSE 0.41, test RMSE 0.86
After epoch 90: train RMSE 0.44, test RMSE 0.65
After epoch 100: train RMSE 0.51, test RMSE 0.39
After epoch 110: train RMSE 0.39, test RMSE 0.61
After epoch 120: train RMSE 0.43, test RMSE 0.78
After epoch 130: train RMSE 0.36, test RMSE 0.54
After epoch 140: train RMSE 0.36, test RMSE 0.52
After epoch 150: train RMSE 0.40, test RMSE 0.51
After epoch 160: train RMSE 0.36, test RMSE 0.51
After epoch 170: train RMSE 0.34, test RMSE 0.29
After epoch 180: train RMSE 0.31, test RMSE 0.28
After epoch 190: train RMSE 0.31, test RMSE 0.25
After epoch 200: train RMSE 0.38, test RMSE 0.34
Learned betas -5.90 -4.93 0.06 4.67 1.48 2.01 7.45 5.76 2.26 4.14 0.74 0.20 1.17 -5.26 -5.86 ...
Learned bias 0.48895858087675187
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_2.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --kernel_gamma=0.15`
```
After epoch 10: train RMSE 0.80, test RMSE 0.66
After epoch 20: train RMSE 0.77, test RMSE 0.65
After epoch 30: train RMSE 0.76, test RMSE 0.63
After epoch 40: train RMSE 0.77, test RMSE 0.66
After epoch 50: train RMSE 0.75, test RMSE 0.63
After epoch 60: train RMSE 0.74, test RMSE 0.62
After epoch 70: train RMSE 0.72, test RMSE 0.61
After epoch 80: train RMSE 0.71, test RMSE 0.60
After epoch 90: train RMSE 0.72, test RMSE 0.63
After epoch 100: train RMSE 0.69, test RMSE 0.60
After epoch 110: train RMSE 0.73, test RMSE 0.67
After epoch 120: train RMSE 0.72, test RMSE 0.65
After epoch 130: train RMSE 0.70, test RMSE 0.62
After epoch 140: train RMSE 0.66, test RMSE 0.60
After epoch 150: train RMSE 0.67, test RMSE 0.62
After epoch 160: train RMSE 0.66, test RMSE 0.61
After epoch 170: train RMSE 0.64, test RMSE 0.62
After epoch 180: train RMSE 0.64, test RMSE 0.61
After epoch 190: train RMSE 0.63, test RMSE 0.62
After epoch 200: train RMSE 0.64, test RMSE 0.65
Learned betas 3.77 3.44 6.39 9.15 4.53 4.08 7.47 4.30 -0.32 0.70 -3.85 -5.11 -4.98 -11.87 -12.67 ...
Learned bias 0.3756022427815734
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_3.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --l2=0.02`
```
After epoch 10: train RMSE 0.63, test RMSE 1.52
After epoch 20: train RMSE 0.56, test RMSE 0.88
After epoch 30: train RMSE 0.51, test RMSE 1.11
After epoch 40: train RMSE 0.50, test RMSE 1.05
After epoch 50: train RMSE 0.50, test RMSE 0.85
After epoch 60: train RMSE 0.48, test RMSE 1.03
After epoch 70: train RMSE 0.52, test RMSE 1.28
After epoch 80: train RMSE 0.49, test RMSE 1.17
After epoch 90: train RMSE 0.50, test RMSE 0.95
After epoch 100: train RMSE 0.59, test RMSE 0.66
After epoch 110: train RMSE 0.53, test RMSE 1.07
After epoch 120: train RMSE 0.56, test RMSE 1.30
After epoch 130: train RMSE 0.50, test RMSE 1.13
After epoch 140: train RMSE 0.49, test RMSE 1.08
After epoch 150: train RMSE 0.57, test RMSE 1.10
After epoch 160: train RMSE 0.46, test RMSE 0.96
After epoch 170: train RMSE 0.50, test RMSE 0.96
After epoch 180: train RMSE 0.47, test RMSE 1.03
After epoch 190: train RMSE 0.47, test RMSE 1.04
After epoch 200: train RMSE 0.56, test RMSE 0.96
Learned betas -0.65 -0.47 -0.10 0.55 0.39 0.34 0.87 0.60 0.26 0.44 0.05 -0.00 0.05 -0.68 -0.76 ...
Learned bias 0.9258410067869733
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_4.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf`
```
After epoch 10: train RMSE 0.78, test RMSE 0.66
After epoch 20: train RMSE 0.74, test RMSE 0.61
After epoch 30: train RMSE 0.71, test RMSE 0.58
After epoch 40: train RMSE 0.67, test RMSE 0.54
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
After epoch 180: train RMSE 0.42, test RMSE 0.49
After epoch 190: train RMSE 0.41, test RMSE 0.50
After epoch 200: train RMSE 0.40, test RMSE 0.50
Learned betas 0.65 0.59 1.17 1.72 0.86 0.82 1.61 1.04 0.21 0.47 -0.31 -0.56 -0.46 -1.77 -1.88 ...
Learned bias 0.6512539914766637
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
After epoch 120: train RMSE 0.72, test RMSE 0.60
After epoch 130: train RMSE 0.72, test RMSE 0.59
After epoch 140: train RMSE 0.71, test RMSE 0.58
After epoch 150: train RMSE 0.70, test RMSE 0.58
After epoch 160: train RMSE 0.70, test RMSE 0.57
After epoch 170: train RMSE 0.69, test RMSE 0.57
After epoch 180: train RMSE 0.69, test RMSE 0.56
After epoch 190: train RMSE 0.68, test RMSE 0.56
After epoch 200: train RMSE 0.68, test RMSE 0.56
Learned betas 1.45 1.28 1.74 2.17 1.18 1.01 1.67 0.98 0.03 0.19 -0.69 -1.02 -0.99 -2.36 -2.50 ...
Learned bias 0.6326715226190537
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_6.svgz)
- `python3 kernel_linear_regression.py --batch_size=2 --kernel=rbf --kernel_gamma=5`
```
After epoch 10: train RMSE 0.65, test RMSE 0.55
After epoch 20: train RMSE 0.52, test RMSE 0.40
After epoch 30: train RMSE 0.43, test RMSE 0.30
After epoch 40: train RMSE 0.36, test RMSE 0.22
After epoch 50: train RMSE 0.31, test RMSE 0.17
After epoch 60: train RMSE 0.27, test RMSE 0.15
After epoch 70: train RMSE 0.25, test RMSE 0.13
After epoch 80: train RMSE 0.24, test RMSE 0.13
After epoch 90: train RMSE 0.23, test RMSE 0.14
After epoch 100: train RMSE 0.22, test RMSE 0.15
After epoch 110: train RMSE 0.22, test RMSE 0.15
After epoch 120: train RMSE 0.22, test RMSE 0.16
After epoch 130: train RMSE 0.21, test RMSE 0.16
After epoch 140: train RMSE 0.21, test RMSE 0.17
After epoch 150: train RMSE 0.21, test RMSE 0.17
After epoch 160: train RMSE 0.21, test RMSE 0.17
After epoch 170: train RMSE 0.21, test RMSE 0.17
After epoch 180: train RMSE 0.21, test RMSE 0.17
After epoch 190: train RMSE 0.21, test RMSE 0.18
After epoch 200: train RMSE 0.21, test RMSE 0.18
Learned betas 0.21 0.08 0.29 0.51 0.06 0.05 0.49 0.27 -0.06 0.18 -0.09 -0.10 0.06 -0.49 -0.45 ...
Learned bias 0.7290386122306763
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
After epoch 100: train RMSE 0.19, test RMSE 0.16
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
Learned betas 0.61 0.03 0.28 0.67 -0.21 -0.21 0.69 0.28 -0.32 0.25 -0.17 -0.06 0.41 -0.59 -0.48 ...
Learned bias 0.8351544798239042
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
Learned betas 0.35 0.11 0.22 0.38 -0.02 -0.03 0.35 0.16 -0.11 0.12 -0.09 -0.06 0.12 -0.34 -0.30 ...
Learned bias 0.9187854392321663
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_9.svgz)
#### Examples End:
#### Tests Start: kernel_linear_regression_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=5 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
```
After epoch 10: train RMSE 0.69, test RMSE 0.61
After epoch 20: train RMSE 0.61, test RMSE 0.65
Learned betas 0.11 0.11 0.25 0.37 0.17 0.16 0.29 0.17 -0.02 0.02 -0.14 -0.20 -0.18 -0.45 -0.49 ...
Learned bias 0.4388019915399849
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
```
After epoch 10: train RMSE 0.63, test RMSE 1.61
After epoch 20: train RMSE 0.54, test RMSE 0.90
Learned betas -0.81 -0.58 0.20 0.62 0.23 0.44 0.78 0.71 0.27 0.40 -0.00 0.06 -0.03 -0.63 -0.73 ...
Learned bias 0.44409714525206545
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --kernel_gamma=0.15`
```
After epoch 10: train RMSE 0.80, test RMSE 0.66
After epoch 20: train RMSE 0.77, test RMSE 0.65
Learned betas 0.71 0.61 0.87 1.13 0.57 0.45 0.71 0.40 -0.09 -0.04 -0.50 -0.62 -0.64 -1.23 -1.38 ...
Learned bias 0.39859934926020046
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05 --l2=0.02`
```
After epoch 10: train RMSE 0.63, test RMSE 1.52
After epoch 20: train RMSE 0.56, test RMSE 0.88
Learned betas -0.48 -0.32 0.13 0.38 0.13 0.28 0.49 0.44 0.16 0.24 -0.02 0.03 -0.04 -0.42 -0.47 ...
Learned bias 0.6096489059733282
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf`
```
After epoch 10: train RMSE 0.78, test RMSE 0.66
After epoch 20: train RMSE 0.74, test RMSE 0.61
Learned betas 0.21 0.19 0.24 0.27 0.17 0.14 0.20 0.13 0.03 0.04 -0.05 -0.08 -0.08 -0.22 -0.24 ...
Learned bias 0.6111050342939267
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
```
After epoch 10: train RMSE 0.81, test RMSE 0.69
After epoch 20: train RMSE 0.80, test RMSE 0.67
Learned betas 0.22 0.20 0.24 0.27 0.17 0.14 0.20 0.13 0.02 0.03 -0.06 -0.10 -0.09 -0.23 -0.25 ...
Learned bias 0.5619981553157737
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=2 --kernel=rbf --kernel_gamma=5`
```
After epoch 10: train RMSE 0.65, test RMSE 0.55
After epoch 20: train RMSE 0.52, test RMSE 0.40
Learned betas 0.11 0.10 0.12 0.13 0.08 0.07 0.11 0.07 0.03 0.03 -0.01 -0.02 -0.02 -0.08 -0.09 ...
Learned bias 0.7126228629963139
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=50`
```
After epoch 10: train RMSE 0.52, test RMSE 0.44
After epoch 20: train RMSE 0.36, test RMSE 0.29
Learned betas 0.19 0.15 0.18 0.21 0.11 0.09 0.16 0.10 0.02 0.05 -0.02 -0.04 -0.02 -0.14 -0.15 ...
Learned bias 0.843378438496468
```
- `python3 kernel_linear_regression.py --epochs=20 --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
```
After epoch 10: train RMSE 0.54, test RMSE 0.45
After epoch 20: train RMSE 0.39, test RMSE 0.32
Learned betas 0.17 0.14 0.16 0.19 0.10 0.08 0.15 0.10 0.02 0.05 -0.02 -0.04 -0.02 -0.13 -0.14 ...
Learned bias 0.8566622017610405
```
#### Tests End:
