### Assignment: bootstrap_resampling
#### Date: Deadline: Feb 12, 23:59
#### Points: 3 points
#### Tests: bootstrap_resampling_tests

Given two trained models, compute their 95% confidence intervals using bootstrap
resampling. Then, estimate the probability that the second one is better than
the first one using a paired bootstrap test.

Start with the [bootstrap_resampling.py](https://github.com/ufal/npfl129/tree/master/labs/13/bootstrap_resampling.py)
template. Note that you usually need to perform a lot of the bootstrap
resamplings, so you should make sure your implementation is fast enough.

#### Tests Start: bootstrap_resampling_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=1000`
```
Confidence intervals of the two models:
- [90.23% .. 93.02%]
- [90.98% .. 93.63%]
The estimated probability that the null hypothesis hold: 1.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/bootstrap_resampling_1.svgz)
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=10000`
```
Confidence intervals of the two models:
- [90.30% .. 93.02%]
- [91.10% .. 93.70%]
The estimated probability that the null hypothesis hold: 1.71%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/bootstrap_resampling_2.svgz)
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=100000`
```
Confidence intervals of the two models:
- [90.30% .. 92.95%]
- [91.10% .. 93.70%]
The estimated probability that the null hypothesis hold: 1.62%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/bootstrap_resampling_3.svgz)
- `python3 bootstrap_resampling.py --seed=33 --test_size=0.95 --bootstrap_samples=50000`
```
Confidence intervals of the two models:
- [87.18% .. 90.16%]
- [87.65% .. 90.63%]
The estimated probability that the null hypothesis hold: 8.94%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/bootstrap_resampling_4.svgz)
#### Tests End:
