### Assignment: permutation_test
#### Date: Deadline: Feb 16, 23:59
#### Points: 2 point
#### Tests: permutation_test_tests

Given two trained models, perform a random permutation test that the second one
is better than the first one.

Start with the [permutation_test.py](https://github.com/ufal/npfl129/tree/past-2425/labs/12/permutation_test.py)
template. Note that you usually need to perform a lot of resamplings, so you
should make sure your implementation is fast enough.

#### Tests Start: permutation_test_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 permutation_test.py --seed=47 --test_size=0.9 --random_samples=1000`
```
The estimated p-value of the random permutation test: 3.10%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/permutation_test_1.svgz)

2. `python3 permutation_test.py --seed=47 --test_size=0.9 --random_samples=10000`
```
The estimated p-value of the random permutation test: 2.99%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/permutation_test_2.svgz)

3. `python3 permutation_test.py --seed=47 --test_size=0.9 --random_samples=100000`
```
The estimated p-value of the random permutation test: 3.11%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/permutation_test_3.svgz)

4. `python3 permutation_test.py --seed=55 --test_size=0.95 --random_samples=50000`
```
The estimated p-value of the random permutation test: 6.55%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/permutation_test_4.svgz)
#### Tests End:
