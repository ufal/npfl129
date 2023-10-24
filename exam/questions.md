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

#### Questions@:, Lecture 3 Questions
- Define binary classification, write down the perceptron algorithm and show
  how a prediction is made for a given example. [10]

- For discrete random variables, define entropy, cross-entropy, Kullback-Leibler
  divergence, and prove the Gibbs inequality (i.e., that KL divergence is
  non-negative). [10]

- Explain the notion of likelihood in maximum likelihood estimation. [5]

- Describe maximum likelihood estimation, as minimizing NLL, cross-entropy, and
  KL divergence. [20]

- Considering binary logistic regression model, write down its parameters
  (including their size) and explain how prediction is performed (including the
  formula for the sigmoid function). Describe how we can interpret the outputs
  of the linear part of the model as logits. [10]

- Write down an $L^2$-regularized minibatch SGD algorithm for training a
  binary logistic regression model, including the explicit formulas of the
  loss function and its gradient. [20]

#### Questions@:, Lecture 4 Questions
- Define mean squared error and show how it can be derived using MLE. [10]

- Considering $K$-class logistic regression model, write down its parameters
  (including their size) and explain how prediction is performed (including the
  formula for the softmax function). Describe how we can interpret the outputs
  of the linear part of the model as logits. [10]

- Explain the relationship between the sigmoid function and softmax. [5]

- Write down an $L^2$-regularized minibatch SGD algorithm for training
  a $K$-class logistic regression model, including the explicit formulas of the
  loss function and its gradient. [20]

- Prove why are decision regions of a multiclass logistic regression convex. [10]

- Considering a single-layer MLP with $D$ input neurons, $H$ hidden
  neurons, $K$ output neurons, hidden activation $f$, and output activation $a$,
  list its parameters (including their size) and write down how the output
  is computed. [10]

- List the definitions of frequently used MLP output layer activations (the ones
  producing parameters of a Bernoulli distribution and a categorical distribution).
  Then write down three commonly used hidden layer activations (sigmoid, tanh,
  ReLU). [10]

#### Questions@:, Lecture 5 Questions
- List the definitions of frequently used MLP output layer activations (the ones
  producing parameters of a Bernoulli distribution and a categorical distribution).
  Then write down three commonly used hidden layer activations (sigmoid, tanh,
  ReLU). [10]

- Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer
  with $H$ units and a softmax output layer with $K$ units, write down the
  explicit formulas of the gradient of all the MLP parameters (two weight matrices and
  two bias vectors), assuming input $\boldsymbol x$, target $t$, and negative log
  likelihood loss. [20]

- Formulate the Universal approximation theorem. [10]
