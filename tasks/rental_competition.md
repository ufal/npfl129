### Assignment: rental_competition
#### Date: Deadline: Oct 21, 22:00
#### Points: 3 points+4 bonus

This assignment is a [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2425-winter#competitions).
Your goal is to perform regression on the data from a bike rental shop.
The train set contains 1000 instances, each instance consists of 12 features,
both integral and real.

The [rental_competition.py](https://github.com/ufal/npfl129/tree/master/labs/02/rental_competition.py)
template shows how to load the training data, downloading it if needed.
Furthermore, it shows how to save a trained estimator and how to load it during
prediction.

The performance of your system is measured using _root mean squared error_
and your goal is to achieve RMSE less than 100. Note that you can use
any number of **generalized linear models from sklearn** to solve
this assignment (but no other ML models like decision trees, MLPs, …; however,
you can use any supporting methods like pre/post-processing, data manipulation,
evaluation, cross-validation, …).
