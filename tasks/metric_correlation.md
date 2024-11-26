### Assignment: metric_correlation
#### Date: Deadline: Dec 9, 22:00
#### Points: 3 points
#### Tests: metric_correlation_tests

Using the [metric_correlation.py](https://github.com/ufal/npfl129/tree/master/labs/08/metric_correlation.py)
template, find a $\beta$ for which $F_\beta$ score correlates
best with human ratings.

We use an aritificial dataset, which for every sentence contains:
- the number of edits that must be performed for every sentence,
- the number of edits proposed by a model,
- the number of correct edits proposed by a model,
- human rating of the sentence.

Using bootstrap resampling, compute the mean human rating and $F_\beta$ score
for each sampled dataset and then manually compute the Pearson correlation
for betas between 0 and 2, and return the most correlating beta.

#### Tests Start: metric_correlation_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 metric_correlation.py --bootstrap_samples=100 --data_size=1000`
```
Best correlation of 0.711 was found for beta 0.79
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/metric_correlation_1.svgz)

2. `python3 metric_correlation.py --bootstrap_samples=100 --data_size=2000`
```
Best correlation of 0.726 was found for beta 0.63
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/metric_correlation_2.svgz)

3. `python3 metric_correlation.py --bootstrap_samples=200 --data_size=2000`
```
Best correlation of 0.676 was found for beta 0.61
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2425/tasks/figures/metric_correlation_3.svgz)
#### Tests End:
