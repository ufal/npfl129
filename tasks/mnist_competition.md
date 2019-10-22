### Assignment: mnist_competition
#### Date: Deadline: Nov 10, 23:59
#### Points: 6 points+6 bonus

This assignment is a [competition task](#competitions). Your goal
is to perform 10-class classification on the well-known
[MNIST](http://yann.lecun.com/exdb/mnist/) dataset.
The train set contains 60k images, each consisting of $28×28$ pixels with values
in $\{0, 1, …, 255\}$. Evaluation is performed on 10k test images.

The [mnist_competition.py](https://github.com/ufal/npfl129/tree/master/labs/03/mnist_competition.py)
template shows how to load the `mnist.train.npz` training data, downloading it
if needed. Furthermore, the template shows how to save a _compressed_ trained
estimator and how to load it in `recodex_predict` method.

The performance of your system is measured using _accuracy_ and your goal is to
achieve at least 94%. Note that you can use **any sklearn algorithm** to solve
this exercise.
