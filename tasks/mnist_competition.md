### Assignment: mnist_competition
#### Date: Deadline: Nov 7, 7:59 a.m.
#### Points: 4 points+5 bonus

This assignment is a [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2324-winter#competitions). Your goal
is to perform 10-class classification on the well-known
[MNIST](http://yann.lecun.com/exdb/mnist/) dataset.
The train set contains 60k images, each consisting of $28×28$ pixels with values
in $\{0, 1, …, 255\}$. Evaluation is performed on 10k test images.
You can find a simple online demo of a trained classifier
[here](https://ufal.mff.cuni.cz/~courses/npfl129/2324/demos/mnist_web.html).

The [mnist_competition.py](https://github.com/ufal/npfl129/tree/master/labs/04/mnist_competition.py)
template shows how to load training data, downloading it if needed.
Furthermore, it shows how to save a trained estimator and how to load it during
prediction.

The performance of your system is measured using _accuracy_ of correctly
predicted examples and your goal is to achieve at least 97% accuracy.
Note that you can use **any sklearn algorithm** to solve this exercise
(and of course anything you implement yourself).
