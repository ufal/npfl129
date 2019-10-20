### Assignment: binary_classification_competition
#### Date: Deadline: Nov 03, 23:59
#### Points: 4 points+5 bonus

This assignment is a [competition task](#competitions). Your goal
is to perform binary classification on the data from contract approval.
The train set contains 20k instances, each instance consists of 14 features,
both integral and categorical. Evaluation is performed on 15k examples.

The [binary_competition_competition.py](https://github.com/ufal/npfl129/tree/master/labs/02/binary_competition_competition.py)
template shows how to load the `binary_classification_competition.train.csv.xz`
training data, downloading it if needed. Note that the input is in
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format and we load
it using [pandas](https://pandas.pydata.org/) as a
[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html),
which is a two-dimensional heterogeneous array with labeled columns.
Furthermore, the template shows how to save a _compressed_ trained
estimator and how to load it in `recodex_predict` method.

The performance of your system is measured using _accuracy_
and your goal is to achieve at least 83%. Note that you can use
**any sklearn algorithm** to solve this exercise, except for
**AdaBoost** and **gradient boosting**.
