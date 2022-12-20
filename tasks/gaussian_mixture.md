### Assignment: gaussian_mixture
#### Date: Deadline: Feb 12, 23:59
#### Points: 5 points
#### Tests: gaussian_mixture_tests

Cluster given input by fitting a Gaussian mixture using the
[gaussian_mixture.py](https://github.com/ufal/npfl129/tree/master/labs/12/gaussian_mixture.py)
template. Use full covariances and compute the negative log-likelihood
of the model after every iteration of the EM algorithm.

#### Tests Start: gaussian_mixture_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 gaussian_mixture.py --examples=112 --clusters=4 --iterations=5 --init=random`
```
Loss after iteration 1: 546.2
Loss after iteration 2: 524.1
Loss after iteration 3: 502.9
Loss after iteration 4: 471.1
Loss after iteration 5: 463.5
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gaussian_mixture_1.svgz)
- `python3 gaussian_mixture.py --examples=112 --clusters=4 --iterations=3 --init=kmeans++`
```
Loss after iteration 1: 458.5
Loss after iteration 2: 458.5
Loss after iteration 3: 458.5
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gaussian_mixture_2.svgz)
- `python3 gaussian_mixture.py --examples=120 --clusters=5 --iterations=11 --init=random`
```
Loss after iteration 1: 526.2
Loss after iteration 2: 520.9
Loss after iteration 3: 517.5
Loss after iteration 4: 517.2
Loss after iteration 5: 517.1
Loss after iteration 6: 517.0
Loss after iteration 7: 517.0
Loss after iteration 8: 517.0
Loss after iteration 9: 516.9
Loss after iteration 10: 516.9
Loss after iteration 11: 516.9
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gaussian_mixture_3.svgz)
- `python3 gaussian_mixture.py --examples=120 --clusters=5 --iterations=5 --init=kmeans++`
```
Loss after iteration 1: 516.5
Loss after iteration 2: 513.7
Loss after iteration 3: 508.8
Loss after iteration 4: 505.4
Loss after iteration 5: 504.5
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gaussian_mixture_4.svgz)
#### Tests End:
