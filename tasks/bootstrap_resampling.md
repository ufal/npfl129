### Assignment: bootstrap_resampling
#### Date: Deadline: Feb 28, 23:59
#### Points: 3 points
#### Examples: bootstrap_resampling_examples

Given two trained models, compute their 95% confidence intervals using bootstrap
resampling. Then, perform a paired bootstrap test that the second one is better
than the first one.

Start with the [bootstrap_resampling.py](https://github.com/ufal/npfl129/tree/past-2021/labs/13/bootstrap_resampling.py)
template. Note that you usually need to perform a lot of the bootstrap
resamplings, so you should make sure your implementation is fast enough.

#### Examples Start: bootstrap_resampling_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=1000`
```
Confidence intervals of the two models:
- [90.23% .. 93.02%]
- [90.98% .. 93.63%]
The p-value of the test: 1.40%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/bootstrap_resampling_1.svgz)
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=10000`
```
Confidence intervals of the two models:
- [90.30% .. 93.02%]
- [91.10% .. 93.70%]
The p-value of the test: 1.71%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/bootstrap_resampling_2.svgz)
- `python3 bootstrap_resampling.py --seed=49 --test_size=0.9 --bootstrap_samples=100000`
```
Confidence intervals of the two models:
- [90.30% .. 92.95%]
- [91.10% .. 93.70%]
The p-value of the test: 1.62%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/bootstrap_resampling_3.svgz)
- `python3 bootstrap_resampling.py --seed=85 --test_size=0.95 --bootstrap_samples=50000`
```
Confidence intervals of the two models:
- [86.83% .. 89.87%]
- [87.18% .. 90.16%]
The p-value of the test: 15.63%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/bootstrap_resampling_4.svgz)
#### Examples End:
