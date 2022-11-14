### Assignment: smo_algorithm
#### Date: Deadline: Nov 28, 7:59 a.m.
#### Points: 7 points
#### Examples: smo_algorithm_examples
#### Tests: smo_algorithm_tests

Using the [smo_algorithm.py](https://github.com/ufal/npfl129/tree/master/labs/07/smo_algorithm.py)
template, implement the SMO algorithm for binary classification
using dual formulation of soft-margin SVM. The template contains
more detailed instructions.

#### Examples Start: smo_algorithm_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=1`
```
Iteration 100, train acc 88.0%, test acc 83.0%
Done, iteration 140, support vectors 41, train acc 88.0%, test acc 83.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_1.svgz)
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=3`
```
Iteration 100, train acc 89.0%, test acc 88.0%
Iteration 200, train acc 91.0%, test acc 86.0%
Iteration 300, train acc 86.0%, test acc 77.0%
Iteration 400, train acc 91.0%, test acc 84.0%
Iteration 500, train acc 88.0%, test acc 86.0%
Iteration 600, train acc 91.0%, test acc 86.0%
Iteration 700, train acc 91.0%, test acc 86.0%
Iteration 800, train acc 90.0%, test acc 86.0%
Iteration 900, train acc 91.0%, test acc 86.0%
Done, iteration 1000, support vectors 39, train acc 91.0%, test acc 86.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_2.svgz)
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=3 --C=5`
```
Iteration 100, train acc 85.0%, test acc 82.0%
Iteration 200, train acc 83.0%, test acc 83.0%
Iteration 300, train acc 84.0%, test acc 85.0%
Iteration 400, train acc 63.0%, test acc 66.0%
Iteration 500, train acc 89.0%, test acc 89.0%
Iteration 600, train acc 91.0%, test acc 89.0%
Iteration 700, train acc 89.0%, test acc 90.0%
Iteration 800, train acc 89.0%, test acc 89.0%
Iteration 900, train acc 55.0%, test acc 60.0%
Done, iteration 1000, support vectors 49, train acc 91.0%, test acc 88.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_3.svgz)
- `python3 smo_algorithm.py --kernel=poly --kernel_degree=3 --kernel_gamma=2`
```
Iteration 100, train acc 85.0%, test acc 84.0%
Iteration 200, train acc 84.0%, test acc 85.0%
Iteration 300, train acc 83.0%, test acc 84.0%
Iteration 400, train acc 55.0%, test acc 60.0%
Iteration 500, train acc 89.0%, test acc 87.0%
Iteration 600, train acc 91.0%, test acc 88.0%
Iteration 700, train acc 89.0%, test acc 90.0%
Iteration 800, train acc 89.0%, test acc 89.0%
Iteration 900, train acc 56.0%, test acc 61.0%
Done, iteration 1000, support vectors 51, train acc 90.0%, test acc 90.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_4.svgz)
- `python3 smo_algorithm.py --kernel=rbf --kernel_gamma=1`
```
Iteration 100, train acc 92.0%, test acc 84.0%
Iteration 200, train acc 92.0%, test acc 84.0%
Iteration 300, train acc 92.0%, test acc 84.0%
Iteration 400, train acc 92.0%, test acc 84.0%
Done, iteration 483, support vectors 53, train acc 92.0%, test acc 84.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_5.svgz)
- `python3 smo_algorithm.py --kernel=rbf --kernel_gamma=0.1`
```
Done, iteration 87, support vectors 51, train acc 88.0%, test acc 85.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/smo_algorithm_6.svgz)
#### Examples End:
#### Tests Start: smo_algorithm_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 smo_algorithm.py --max_iterations=20 --kernel=poly --kernel_degree=1`
```
Done, iteration 20, support vectors 48, train acc 84.0%, test acc 86.0%
```
- `python3 smo_algorithm.py --max_iterations=20 --kernel=poly --kernel_degree=3`
```
Done, iteration 20, support vectors 70, train acc 85.0%, test acc 84.0%
```
- `python3 smo_algorithm.py --max_iterations=20 --kernel=poly --kernel_degree=3 --C=5`
```
Done, iteration 20, support vectors 78, train acc 87.0%, test acc 86.0%
```
- `python3 smo_algorithm.py --max_iterations=20 --kernel=poly --kernel_degree=3 --kernel_gamma=2`
```
Done, iteration 20, support vectors 77, train acc 86.0%, test acc 84.0%
```
- `python3 smo_algorithm.py --max_iterations=20 --kernel=rbf --kernel_gamma=1`
```
Done, iteration 20, support vectors 67, train acc 92.0%, test acc 84.0%
```
- `python3 smo_algorithm.py --max_iterations=20 --kernel=rbf --kernel_gamma=0.1`
```
Done, iteration 20, support vectors 53, train acc 85.0%, test acc 84.0%
```
#### Tests End:
