### Assignment: smo_algorithm
#### Date: Deadline: Dec 15, 23:59
#### Points: 7 points
#### Examples: smo_algorithm_examples

**<span class="text-danger">The comments in the template were changed on Dec 08.</span>**

Using the [smo_algorithm.py](https://github.com/ufal/npfl129/tree/master/labs/07/smo_algorithm.py)
template, implement the SMO algorithm for binary classification
using dual formulation of soft-margin SVM.

#### Examples Start: smo_algorithm_examples
**<span class="text-danger">The example outputs were changed on Dec 07.</span>**

- `--C 1 --kernel linear --tolerance 0.0001 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 75.0%, test acc 67.0%
Train acc 70.0%, test acc 62.0%
Train acc 53.3%, test acc 55.0%
Train acc 56.7%, test acc 55.0%
Train acc 85.0%, test acc 77.0%
...
Train acc 85.0%, test acc 74.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_1.svg)
- `--C 1 --kernel rbf --kernel_gamma=1 --tolerance 0.0001 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 70.0%, test acc 56.0%
Train acc 91.7%, test acc 80.0%
Train acc 91.7%, test acc 82.0%
Train acc 91.7%, test acc 78.0%
Train acc 95.0%, test acc 74.0%
...
Train acc 93.3%, test acc 75.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_2.svg)
- `--C 1 --kernel rbf --kernel_gamma=0.1 --tolerance 0.0001 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 86.7%, test acc 76.0%
Train acc 80.0%, test acc 73.0%
Train acc 83.3%, test acc 75.0%
Train acc 81.7%, test acc 79.0%
Train acc 85.0%, test acc 73.0%
...
Train acc 85.0%, test acc 75.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_3.svg)
- `--C 1 --kernel poly --kernel_degree=3 --kernel_gamma=1 --tolerance 0.0001 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 73.3%, test acc 62.0%
Train acc 51.7%, test acc 51.0%
Train acc 63.3%, test acc 60.0%
Train acc 66.7%, test acc 63.0%
Train acc 85.0%, test acc 73.0%
...
Train acc 88.3%, test acc 73.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_4.svg)
- `--C 5 --kernel poly --kernel_degree=3 --kernel_gamma=1 --tolerance 0.0001 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 73.3%, test acc 62.0%
Train acc 51.7%, test acc 51.0%
Train acc 63.3%, test acc 60.0%
Train acc 66.7%, test acc 63.0%
Train acc 65.0%, test acc 62.0%
...
Train acc 91.7%, test acc 74.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_5.svg)
- `--C 1 --kernel poly --kernel_degree=3 --kernel_gamma=1 --tolerance 0.01 --examples 160 --num_passes 5 --seed 007 --test_ratio 0.625`
```
Train acc 86.7%, test acc 73.0%
Train acc 56.7%, test acc 66.0%
Train acc 66.7%, test acc 63.0%
Train acc 70.0%, test acc 56.0%
Train acc 68.3%, test acc 73.0%
...
Train acc 78.3%, test acc 68.0%
```
![Decision tree visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/smo_algorithm_6.svg)
#### Examples End:
