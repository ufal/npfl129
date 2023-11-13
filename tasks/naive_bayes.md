### Assignment: naive_bayes
#### Date: Deadline: Nov 28, 7:59 a.m.
#### Points: 3 points
#### Tests: naive_bayes_tests

Using the [naive_bayes.py](https://github.com/ufal/npfl129/tree/master/labs/07/naive_bayes.py)
template, implement a naive Bayes classifier (without using the
`sklearn.naive_bayes` module in any way). Support all of Gaussian NB,
multinomial NB and Bernoulli NB.

#### Tests Start: naive_bayes_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 naive_bayes.py --classes=3 --naive_bayes_type=bernoulli`
```
Test accuracy 95.17%, log probability -4933.45
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_1.svgz)

2. `python3 naive_bayes.py --classes=3 --naive_bayes_type=multinomial`
```
Test accuracy 93.68%, log probability -300352.40
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_2.svgz)

3. `python3 naive_bayes.py --classes=3 --naive_bayes_type=gaussian`
```
Test accuracy 95.54%, log probability -31895.82
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_3.svgz)

4. `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli`
```
Test accuracy 89.21%, log probability -18342.14
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_4.svgz)

5. `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli --alpha=10`
```
Test accuracy 88.54%, log probability -20829.42
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_5.svgz)

6. `python3 naive_bayes.py --classes=10 --naive_bayes_type=multinomial --alpha=10`
```
Test accuracy 90.32%, log probability -1006524.57
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_6.svgz)

7. `python3 naive_bayes.py --classes=10 --naive_bayes_type=gaussian --alpha=10`
```
Test accuracy 92.10%, log probability -149703.75
```
![Test visualization](//ufal.mff.cuni.cz/~courses/npfl129/2324/tasks/figures/naive_bayes_7.svgz)
#### Tests End:
