#### Questions@:, Lecture 1 Questions

- Explain why we need separate train and test data? What is generalization and
  how the concept relates to underfitting and overfitting? [10]
  the concept relates to underfitting and overfitting? [10]

- Define prediction function of a linear regression model and write down
  $L^2$-regularized mean squared error loss. [10]

- Starting from unregularized sum of squares error of a linear regression model,
  show how the explicit solution can be obtained, assuming
  $\boldsymbol X^T \boldsymbol X$ is regular. [20]

#### Questions@:, Lecture 2 Questions

- Describe standard gradient descent and compare it to stochastic (i.e.,
  online) gradient descent and minibatch stochastic gradient descent. [10]

- Write an $L^2$-regularized minibatch SGD algorithm for training a linear
  regression model, including the explicit formulas of the loss function and
  its gradient. [10]

- Does the SGD algorithm for linear regression always find the best solution on
  the training data? If yes, explain under what conditions it happens, if not
  explain why it is not guaranteed to converge. [20]

- After training a model with SGD, you ended up with a low training error and
  a high test error. Using the learning curves, explain what might have happen
  and what steps you might take to prevent this from happening. [10]

- You were provided with a fixed training set and a fixed test set and you are
  supposed to report model performance on that test set. You need to decide
  what hyperparameters to use. How will you proceed and why? [5]

- What method can be used for normalizing feature values? Explain why it is
  useful. [5]
