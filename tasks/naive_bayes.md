### Assignment: naive_bayes
#### Date: Deadline: Dec 5, 7:59 a.m.
#### Points: 3 points
#### Tests: naive_bayes_tests

Using the [naive_bayes.py](https://github.com/ufal/npfl129/tree/past-2223/labs/08/naive_bayes.py)
template, implement a naive Bayes classifier (without using the
`sklearn.naive_bayes` module in any way). Support all of Gaussian NB,
multinomial NB and Bernoulli NB.

#### Tests Start: naive_bayes_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=bernoulli --seed=72`
```
Test accuracy 95.17%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_1.svgz)
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=multinomial --seed=72`
```
Test accuracy 93.68%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_2.svgz)
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=gaussian --seed=72`
```
Test accuracy 95.54%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_3.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli --seed=72`
```
Test accuracy 89.21%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_4.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli --alpha=10 --seed=72`
```
Test accuracy 88.54%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_5.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=multinomial --alpha=10 --seed=53`
```
Test accuracy 90.77%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_6.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=gaussian --alpha=10 --seed=72`
```
Test accuracy 92.10%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/naive_bayes_7.svgz)
#### Tests End:
