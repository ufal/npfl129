### Assignment: miniaturization
#### Date: Deadline: Dec 1, 22:00
#### Points: 3 points+4 bonus

This assignment is a [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2627-winter#competitions).
Your goal is to reach at least 99% accuracy on the
[MNIST](http://yann.lecun.com/exdb/mnist/) dataset using the **smallest possible
submission**. The total size of your submission, i.e., the sum of sizes of all
submitted files (source code included), must be at most **1 MiB**. Competition
points are awarded according to this size, which ReCodEx shows in the logs (the
accuracy of your solution does not affect the competition points, as long as it
is at least 99%, so unlike in other competitions, it is not hidden).

The [miniaturization.py](https://github.com/ufal/npfl129/tree/master/labs/08/miniaturization.py)
template shows how to load training data, downloading it if needed.
Furthermore, it shows how to save a trained estimator and how to load it during
prediction. Finally, it includes a class `MLPFullDistributionClassifier`, which
modifies `MLPClassifier` to support full categorical distributions on input,
i.e., each label is a distribution over the predicted classes. Such a classifier
might be useful for example for knowledge distillation.

You can use **any sklearn/numpy/scipy algorithm** to solve this assignment
(and of course anything you implement yourself). You can also use the
`mnist_competition` reference solution in this competition.
