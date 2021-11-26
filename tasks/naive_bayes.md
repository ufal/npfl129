### Assignment: naive_bayes
#### Date: Deadline: ~~Dec 06~~ Dec 13, 23:59
#### Points: 3 points
#### Tests: naive_bayes_tests

Using the [naive_bayes.py](https://github.com/ufal/npfl129/tree/master/labs/08/naive_bayes.py)
template, implement a naive Bayes classifier (without using the
`sklearn.naive_bayes` module in any way). Support all of Gaussian NB,
multinomial NB and Bernoulli NB.

#### Tests Start: naive_bayes_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=bernoulli`
```
Test accuracy 95.17%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_1.svgz)
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=multinomial`
```
Test accuracy 94.05%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_2.svgz)
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=gaussian`
```
Test accuracy 97.03%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_3.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli`
```
Test accuracy 88.32%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_4.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli --alpha=10`
```
Test accuracy 87.76%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_5.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=multinomial --alpha=10`
```
Test accuracy 89.66%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_6.svgz)
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=gaussian --alpha=10 --seed=41`
```
Test accuracy 91.55%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/naive_bayes_7.svgz)
#### Tests End:
