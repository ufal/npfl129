### Assignment: naive_bayes
#### Date: Deadline: Dec 08, 23:59
#### Points: 4 points
#### Examples: naive_bayes_examples

Using the [naive_bayes.py](https://github.com/ufal/npfl129/tree/master/labs/08/naive_bayes.py)
template, implement a naive Bayes classifier (without using the `sklearn` one).
Support all of Gaussian NB, multinomial NB and Bernoulli NB.

#### Examples Start: naive_bayes_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=bernoulli`
```
Test accuracy 93.31%
```
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=multinomial`
```
Test accuracy 94.05%
```
- `python3 naive_bayes.py --classes=3 --naive_bayes_type=gaussian`
```
Test accuracy 97.03%
```
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=bernoulli`
```
Test accuracy 84.32%
```
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=multinomial --alpha=10`
```
Test accuracy 89.66%
```
- `python3 naive_bayes.py --classes=10 --naive_bayes_type=gaussian --alpha=10`
```
Test accuracy 91.32%
```
#### Examples End:
