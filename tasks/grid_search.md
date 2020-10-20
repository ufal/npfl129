### Assignment: grid_search
#### Date: Deadline: Nov 03, 23:59
#### Points: 3 points
#### Examples: grid_search_examples

Starting with [grid_search.py](https://github.com/ufal/npfl129/tree/master/labs/03/grid_search.py)
template, perform a hyperparameter grid search, evaluating hyperparameter performance
using a stratified k-fold crossvalidation, and finally evaluate a model
trained with best hyparparameters on all training data. The easiest way is
to utilize `sklearn.model_selection.GridSearchCV`.

#### Examples Start: grid_search_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 grid_search.py --test_size=0.5`
```
Rank: 11 Cross-val: 86.7% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 1    
Rank:  5 Cross-val: 92.7% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 2    
Rank: 11 Cross-val: 86.7% lr__C: 0.01  lr__solver: sag   polynomial__degree: 1    
Rank:  5 Cross-val: 92.7% lr__C: 0.01  lr__solver: sag   polynomial__degree: 2    
Rank:  7 Cross-val: 90.8% lr__C: 1     lr__solver: lbfgs polynomial__degree: 1    
Rank:  3 Cross-val: 96.8% lr__C: 1     lr__solver: lbfgs polynomial__degree: 2    
Rank:  7 Cross-val: 90.8% lr__C: 1     lr__solver: sag   polynomial__degree: 1    
Rank:  4 Cross-val: 96.8% lr__C: 1     lr__solver: sag   polynomial__degree: 2    
Rank: 10 Cross-val: 90.1% lr__C: 100   lr__solver: lbfgs polynomial__degree: 1    
Rank:  1 Cross-val: 97.2% lr__C: 100   lr__solver: lbfgs polynomial__degree: 2    
Rank:  9 Cross-val: 90.5% lr__C: 100   lr__solver: sag   polynomial__degree: 1    
Rank:  2 Cross-val: 97.0% lr__C: 100   lr__solver: sag   polynomial__degree: 2    
Test accuracy: 98.33
```
- `python3 grid_search.py --test_size=0.7`
```
Rank: 11 Cross-val: 87.9% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 1    
Rank:  5 Cross-val: 91.8% lr__C: 0.01  lr__solver: lbfgs polynomial__degree: 2    
Rank: 11 Cross-val: 87.9% lr__C: 0.01  lr__solver: sag   polynomial__degree: 1    
Rank:  5 Cross-val: 91.8% lr__C: 0.01  lr__solver: sag   polynomial__degree: 2    
Rank:  7 Cross-val: 91.3% lr__C: 1     lr__solver: lbfgs polynomial__degree: 1    
Rank:  3 Cross-val: 95.9% lr__C: 1     lr__solver: lbfgs polynomial__degree: 2    
Rank:  7 Cross-val: 91.3% lr__C: 1     lr__solver: sag   polynomial__degree: 1    
Rank:  4 Cross-val: 95.7% lr__C: 1     lr__solver: sag   polynomial__degree: 2    
Rank: 10 Cross-val: 89.2% lr__C: 100   lr__solver: lbfgs polynomial__degree: 1    
Rank:  1 Cross-val: 96.5% lr__C: 100   lr__solver: lbfgs polynomial__degree: 2    
Rank:  9 Cross-val: 89.2% lr__C: 100   lr__solver: sag   polynomial__degree: 1    
Rank:  2 Cross-val: 96.1% lr__C: 100   lr__solver: sag   polynomial__degree: 2    
Test accuracy: 96.98
```
#### Examples End:
