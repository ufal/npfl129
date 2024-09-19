### Assignment: bootstrap_resampling
#### Date: Deadline: Feb 18, 23:59
#### Points: 3 points
#### Tests: bootstrap_resampling_tests

Given two trained models, compute their 95% confidence intervals using bootstrap
resampling. Then, estimate the probability that the second one is better than
the first one using a paired bootstrap test.

Start with the [bootstrap_resampling.py](https://github.com/ufal/npfl129/tree/past-2324/labs/12/bootstrap_resampling.py)
template. Note that you usually need to perform a lot of the bootstrap
resamplings, so you should make sure your implementation is fast enough.

#### Tests Start: bootstrap_resampling_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 bootstrap_resampling.py --seed=47 --test_size=0.9 --bootstrap_samples=1000`
```
Confidence intervals of the two models:
- [91.41% .. 93.88%]
- [91.96% .. 94.38%]
The estimated probability that the null hypothesis holds: 2.10%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/bootstrap_resampling_1.svgz)

2. `python3 bootstrap_resampling.py --seed=47 --test_size=0.9 --bootstrap_samples=10000`
```
Confidence intervals of the two models:
- [91.35% .. 93.88%]
- [91.97% .. 94.38%]
The estimated probability that the null hypothesis holds: 2.40%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/bootstrap_resampling_2.svgz)

3. `python3 bootstrap_resampling.py --seed=47 --test_size=0.9 --bootstrap_samples=100000`
```
Confidence intervals of the two models:
- [91.35% .. 93.88%]
- [91.97% .. 94.38%]
The estimated probability that the null hypothesis holds: 2.21%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/bootstrap_resampling_3.svgz)

4. `python3 bootstrap_resampling.py --seed=55 --test_size=0.95 --bootstrap_samples=50000`
```
Confidence intervals of the two models:
- [84.72% .. 88.00%]
- [85.30% .. 88.52%]
The estimated probability that the null hypothesis holds: 5.47%
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/bootstrap_resampling_4.svgz)
#### Tests End:
