### Assignment: kernel_linear_regression
#### Date: Deadline: Nov 21, 7:59 a.m.
#### Points: 5 points
#### Examples: kernel_linear_regression_examples

Starting with the [kernel_linear_regression.py](https://github.com/ufal/npfl129/tree/master/labs/06/kernel_linear_regression.py),
implement kernel linear regression training using SGD
on the dual formulation. You should support _polynomial_
and _Gaussian_ kernels and also L2 regularization.

#### Examples Start: kernel_linear_regression_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=3 --learning_rate=0.1`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_1.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=poly --kernel_degree=5 --learning_rate=0.05`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_2.svgz)
- `python3 kernel_linear_regression.py --batch_size=5 --kernel=poly --kernel_degree=5 --learning_rate=0.1`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_3.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_4.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=0.5`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_5.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=5`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_6.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_7.svgz)
- `python3 kernel_linear_regression.py --batch_size=1 --kernel=rbf --kernel_gamma=50 --l2=0.02`
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/kernel_linear_regression_8.svgz)
#### Examples End:
