### Assignment: linear_regression_competition
#### Date: Deadline: Oct 20, 23:59
#### Points: 3 points+5 bonus

This assignment is a [competition task](#competitions). Your goal
is to perform linear regression on the data from a rental shop.
The train set contains 1000 instances, each instance consists of 12 features,
both integral and real.

The [linear_regression_competition.py](https://github.com/ufal/npfl129/tree/master/labs/01/linear_regression_competition.py)
template show how to load the
[linear_regression_competition.train.npz](https://github.com/ufal/npfl129/tree/master/labs/01/linear_regression_competition.train.npz)
available in the repository. Furthermore, it shows how to save a trained
estimator, how to load it, and it shows `recodex_predict` method which
is called during ReCodEx evaluation.

The performance of your system is measured using _root mean squared error_
and your goal is to achieve RMSE less than 130. Note that you can use
**any sklearn algorithm** to solve this exercise.
