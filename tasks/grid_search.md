### Assignment: grid_search
#### Date: Deadline: Oct 29, 22:00
#### Points: 2 points
#### Tests: grid_search_tests
#### Examples: grid_search_examples

Starting with [grid_search.py](https://github.com/ufal/npfl129/tree/master/labs/03/grid_search.py)
template, perform a hyperparameter grid search, evaluating hyperparameter performance
using a stratified k-fold crossvalidation, and finally evaluate a model
trained with best hyperparameters on all training data. The easiest way is
to utilize `sklearn.model_selection.GridSearchCV`.

#### Tests Start: grid_search_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 grid_search.py --test_size=0.5`
```
Test accuracy: 98.11%
```

2. `python3 grid_search.py --test_size=0.7`
```
Test accuracy: 96.26%
```
#### Tests End:
#### Examples Start: grid_search_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

- `python3 grid_search.py --test_size=0.5`
```
Rank: 11 Cross-val: 86.7% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 1
Rank:  5 Cross-val: 92.7% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 2
Rank: 11 Cross-val: 86.7% lr__C: 0.01  lr__solver: sag   polynomial__degree: 1
Rank:  5 Cross-val: 92.7% lr__C: 0.01  lr__solver: sag   polynomial__degree: 2
Rank:  7 Cross-val: 91.0% lr__C: 1     lr__solver: lbfgs polynomial__degree: 1
Rank:  2 Cross-val: 96.8% lr__C: 1     lr__solver: lbfgs polynomial__degree: 2
Rank:  8 Cross-val: 90.8% lr__C: 1     lr__solver: sag   polynomial__degree: 1
Rank:  3 Cross-val: 96.8% lr__C: 1     lr__solver: sag   polynomial__degree: 2
Rank: 10 Cross-val: 90.1% lr__C: 100   lr__solver: lbfgs polynomial__degree: 1
Rank:  4 Cross-val: 96.4% lr__C: 100   lr__solver: lbfgs polynomial__degree: 2
Rank:  9 Cross-val: 90.5% lr__C: 100   lr__solver: sag   polynomial__degree: 1
Rank:  1 Cross-val: 97.0% lr__C: 100   lr__solver: sag   polynomial__degree: 2
Test accuracy: 98.11%
```

- `python3 grid_search.py --test_size=0.7`
```
Rank: 11 Cross-val: 87.9% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 1
Rank:  5 Cross-val: 91.8% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 2
Rank: 11 Cross-val: 87.9% lr__C: 0.01  lr__solver: sag   polynomial__degree: 1
Rank:  5 Cross-val: 91.8% lr__C: 0.01  lr__solver: sag   polynomial__degree: 2
Rank:  7 Cross-val: 91.5% lr__C: 1     lr__solver: lbfgs polynomial__degree: 1
Rank:  2 Cross-val: 95.9% lr__C: 1     lr__solver: lbfgs polynomial__degree: 2
Rank:  8 Cross-val: 91.3% lr__C: 1     lr__solver: sag   polynomial__degree: 1
Rank:  3 Cross-val: 95.7% lr__C: 1     lr__solver: sag   polynomial__degree: 2
Rank:  9 Cross-val: 89.4% lr__C: 100   lr__solver: lbfgs polynomial__degree: 1
Rank:  4 Cross-val: 95.2% lr__C: 100   lr__solver: lbfgs polynomial__degree: 2
Rank: 10 Cross-val: 89.2% lr__C: 100   lr__solver: sag   polynomial__degree: 1
Rank:  1 Cross-val: 96.1% lr__C: 100   lr__solver: sag   polynomial__degree: 2
Test accuracy: 96.26%
```
#### Examples End:
