### Assignment: isnt_it_ironic
#### Date: Deadline: Dec 15, 23:59
#### Points: 7 points+7 bonus

The goal of the `isnt_it_ironic` competition is to learn to classify given
texts as ironic or not.

The [isnt_it_ironic.py](https://github.com/ufal/npfl129/tree/master/labs/07/isnt_it_ironic.py)
template shows how to load the training data, downloading it if needed,
it shows how to save a compressed trained estimator and how to load it in
`recodex_predict` method.

The data are a list of strings, each representing one text. The texts has
already been tokenized and tokens are separated by exactly one space.
The performance of your solution will be evaluated using
[F1 score](https://en.wikipedia.org/wiki/F1_score) with
[`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
and if you surpass at least **55%**, you will obtain 7 points.
Note that you can use **any sklearn algorithm** to solve this exercise
(or anything you implement by yourself).
