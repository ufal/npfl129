### Assignment: miniaturization
#### Date: Deadline: Dec 5, 7:59 a.m.
#### Points: 2 points+4 bonus

This assignment is a [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2324-winter#competitions).
Your goal is to submit the **smallest model** achieving at least 99%
accuracy on the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset.
The total size of your submission must be at most **1 MiB**, and the competition
points will be awarded according to the size of your submission, which ReCodEx
shows in the logs (the accuracy of your solution does not affect the competition
points, as long as it is at least 99%, and is therefore not hidden as usual).

The [miniaturization.py](https://github.com/ufal/npfl129/tree/past-2324/labs/08/miniaturization.py)
template shows how to load training data, downloading it if needed.
Furthermore, it shows how to save a trained estimator and how to load it during
prediction. Finally, it includes a class `MLPFullDistributionClassifier`, which
modifies `MLPClassifier` to support full categorical distributions on input,
i.e., each label is a distribution over the predicted classes. Such a classifier
might be useful for example for knowledge distillation.

You can use **any sklearn/numpy/scipy algorithm** to solve this exercise
(and of course anything you implement yourself).
