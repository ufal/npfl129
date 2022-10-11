### Assignment: rental_competition
#### Date: Deadline: Oct 24, 7:59 a.m.
#### Points: 3 points+4 bonus

This assignment is a [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2223-winter#competitions). Your goal
is to perform regression on the data from a rental shop.
The train set contains 1000 instances, each instance consists of 12 features,
both integral and real.

The [rental_competition.py](https://github.com/ufal/npfl129/tree/master/labs/02/rental_competition.py)
template shows how to load the training data, downloading it if needed.
Furthermore, it shows how to save a trained estimator and how to load it during
prediction.

The performance of your system is measured using _root mean squared error_
and your goal is to achieve RMSE less than 100. Note that you can use
any number of **generalized linear models** with any regularization to solve
this assignment (but no decision trees, MLPs, …).
