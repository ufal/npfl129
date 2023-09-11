### Assignment: permutation_test
#### Date: Deadline: Feb 12, 23:59
#### Points: 1 point
#### Tests: permutation_test_tests

Given two trained models, perform a random permutation test that the second one
is better than the first one.

Start with the [permutation_test.py](https://github.com/ufal/npfl129/tree/past-2223/labs/13/permutation_test.py)
template. Note that you usually need to perform a lot of resamplings, so you
should make sure your implementation is fast enough.

#### Tests Start: permutation_test_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 permutation_test.py --seed=49 --test_size=0.9 --random_samples=1000`
```
The estimated p-value of the random permutation test: 2.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/permutation_test_1.svgz)
- `python3 permutation_test.py --seed=49 --test_size=0.9 --random_samples=10000`
```
The estimated p-value of the random permutation test: 2.15%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/permutation_test_2.svgz)
- `python3 permutation_test.py --seed=49 --test_size=0.9 --random_samples=100000`
```
The estimated p-value of the random permutation test: 2.16%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/permutation_test_3.svgz)
- `python3 permutation_test.py --seed=33 --test_size=0.95 --random_samples=50000`
```
The estimated p-value of the random permutation test: 10.72%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/permutation_test_4.svgz)
#### Tests End:
