### Assignment: isnt_it_ironic
#### Date: Deadline: ~~Dec 06~~ Dec 13, 23:59
#### Points: 5 points+5 bonus

The goal of the `isnt_it_ironic` [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2122-winter#competitions) is to learn to
classify given text as ironic or not.

The [isnt_it_ironic.py](https://github.com/ufal/npfl129/tree/master/labs/08/isnt_it_ironic.py)
template shows how to load the training data, downloading it if needed.
Please note that the data are provided only for the purpose of this class
and you cannot use them in any other way.

Each instance is a string of an English tweet. The texts have
already been tokenized and tokens are separated by exactly one space.
The performance of your solution will be evaluated using
F1-score with [sklearn.metrics.f1_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
and if you surpass at least **58.5%**, you will obtain 5 points.
Note that you can use **any sklearn algorithm** to solve this exercise
(or anything you implement yourselves).

You might find
[TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html)
or
[TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
useful.
