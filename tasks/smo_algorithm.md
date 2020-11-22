### Assignment: smo_algorithm
#### Date: Deadline: Dec 1, 23:59
#### Points: 7 points
#### Examples: smo_algorithm_examples

Using the [smo_algorithm.py](https://github.com/ufal/npfl129/tree/master/labs/07/smo_algorithm.py)
template, implement the SMO algorithm for binary classification
using dual formulation of soft-margin SVM. The template contains
more detailed instructions.
#### Examples Start: smo_algorithm_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=1`
```
Iteration 100, train acc 88.0%, test acc 83.0%
Training finished after iteration 140, train acc 88.0%, test acc 83.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/smo_algorithm_1.svgz)
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=3`
```
Iteration 100, train acc 89.0%, test acc 89.0%
Iteration 200, train acc 91.0%, test acc 86.0%
Iteration 300, train acc 90.0%, test acc 86.0%
Iteration 400, train acc 91.0%, test acc 84.0%
Iteration 500, train acc 88.0%, test acc 86.0%
Iteration 600, train acc 91.0%, test acc 86.0%
Iteration 700, train acc 91.0%, test acc 86.0%
Iteration 800, train acc 90.0%, test acc 86.0%
Iteration 900, train acc 91.0%, test acc 85.0%
Training finished after iteration 1000, train acc 91.0%, test acc 85.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/smo_algorithm_2.svgz)
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=3 --C=5`
```
Iteration 100, train acc 85.0%, test acc 82.0%
Iteration 200, train acc 83.0%, test acc 83.0%
Iteration 300, train acc 84.0%, test acc 83.0%
Iteration 400, train acc 66.0%, test acc 71.0%
Iteration 500, train acc 89.0%, test acc 89.0%
Iteration 600, train acc 91.0%, test acc 89.0%
Iteration 700, train acc 89.0%, test acc 90.0%
Iteration 800, train acc 89.0%, test acc 89.0%
Iteration 900, train acc 54.0%, test acc 60.0%
Training finished after iteration 1000, train acc 90.0%, test acc 88.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/smo_algorithm_3.svgz)
- `python3 smo_algorithm.py --kernel=rbf --kernel_gamma=1`
```
Iteration 100, train acc 92.0%, test acc 84.0%
Iteration 200, train acc 92.0%, test acc 84.0%
Training finished after iteration 217, train acc 92.0%, test acc 84.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/smo_algorithm_4.svgz)
- `python3 smo_algorithm.py --kernel=rbf --kernel_gamma=0.1`
```
Training finished after iteration 87, train acc 88.0%, test acc 84.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/smo_algorithm_5.svgz)
#### Examples End:
