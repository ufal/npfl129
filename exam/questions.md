####Questions@: ,Lecture 1 Questions
- Define prediction function of a linear regression model and write down
  $L_2$-regularized mean squared error loss. [5]

- Starting from unregularized sum of squares error of a linear regression model,
  show how the explicit solution can be obtained, assuming
  $\boldsymbol X^T \boldsymbol X$ is regular. [10]

####Questions@: ,Lecture 2 Questions
- Define expectation and variance of a random variable. Then define bias of
  an estimator and show that estimating an expectation using a simple sample
  is unbiased. [5]

- Describe gradient descent and compare it to stochastic (i.e., online) gradient
  descent and minibatch stochastic gradient descent. [5]

- Formulate conditions on the sequence of learning rates used in SGD to convert
  to optimum almost surely. [5]

- Write an $L_2$-regularized minibatch SGD algorithm for training a linear
  regression model, including the explicit formulae of the loss function and
  its gradient. [5]

####Questions@: ,Lecture 3 Questions
- Define binary classification, write down the perceptron algorithm and show
  how a prediction is made for a given example. [5]

- Show that the perceptron algorithm an instance of a stochastic gradient
  descent. Why are the learning rates not needed? [5]

- Define entropy, cross-entropy, Kullback-Leibler divergence, and prove
  the Gibbs inequality (i.e., that KL divergence is non-negative). [5]

- Describe maximum likelihood estimation, as minimizing NLL, cross-entropy and
  KL divergence. [5]

- Describe (binary) logistic regression model including the sigmoid function.
  Describe how we can interpret the model outputs as logits. [5]

- Write down an $L_2$-regularized minibatch SGD algorithm for training a
  (binary) logistic regression model, including the explicit formulae of the
  loss function and its gradient. [10]

####Questions@: ,Lecture 4 Questions
- Define mean squared error and show how it can be derived using MLE. [5]

- Describe multiclass logistic regression model including the softmax function.
  Describe how we can interpret the model outputs as logits. [5]

- Write down an $L_2$-regularized minibatch SGD algorithm for training a
  multiclass logistic regression model, including the explicit formulae of the
  loss function and its gradient. [10]

- Describe how does a single-layer MLP with $i$ input neurons, $h$ hidden
  neurons, $o$ output neurons, hidden activation $f$ and output activation $a$
  computes the results. [5]

- List the definitions of frequently used MLP output layer activations (the ones
  producing parameters of a Bernoulli distribution and a categorical distribution).
  Then write down three commonly used hidden layer activations (sigmoid, tanh,
  ReLU), including their partial derivatives. [5]

- Considering a single-layer MLP with $i$ input neurons, a ReLU hidden layer
  with $h$ units and softmax output layer with $o$ units, write down explicit
  formulae of the gradient of all the MLP parameters (two weight matrices and
  two bias vectors), assuming input $\boldsymbol x$, target $t$ and negative log
  likelihood loss. [10]

- Formulate the Universal approximation theorem. [5]

####Questions@: ,Lecture 5 Questions
- Consider derivation of softmax using maximum entropy principle, assuming
  we have a dataset of $N$ examples $(x_i, t_i), x_i ∈ ℝ^D, t_i ∈ \{1, 2, …, K\}$.
  Formulate the three conditions we impose on the searched $π: ℝ^D → ℝ^K$, and
  write down the Lagrangian to be maximized. [10]

- Define precision, recall, $F_1$ score and $F_β$ score. [5]

- Explain the difference between micro-averaged and macro-averaged $F_1$ score. [5]

- Describe k-nearest neighbors prediction, both for regression and
  classification. Define $L_p$ norm and describe uniform, inverse
  and softmax weighting. [5]

####Questions@: ,Lecture 6 Questions
- Define a kernel based on a feature map $φ$, and write down the formulae for
  (1) a polynomial kernel of degree $d$, (2) a polynomial kernel of degree at
  most $d$, (3) an RBF kernel. [5]

- Define a kernel and write down the mini-batch SGD training algorithm of dual
  formulation of kernel linear regression. Then, describe how predictions for
  unseen data are made. [10]

- Derive the primary formulation of hard-margin SVM (the value to minimize,
  the constrains to fulfil) as a maximum-margin classifier. [5]

- Starting from primary hard-margin SVM formulation, derive the dual formulation
  (the Lagrangian L, the required conditions, the KKT conditions). [10]

- Starting from dual formulation of hard-margin SVM, define what
  a support vector is, and how predictions are performed for unseen data. [5]

####Questions@: ,Lecture 7 Questions
- Write down the primary formulation of soft-margin SVM using the slack
  variables (the value to minimize, the constraints to fulfil). [5]

- Starting from primary soft-margin SVM formulation, derive the dual formulation
  (the Lagrangian L, the required conditions, the KKT conditions). [10]

- Write down the primary formulation of soft-margin SVM using the hinge
  loss. [5]

- Describe high-level overview of the SMO algorithm (without the update rules
  for $a_i$, $a_j$ and $b$). [10]

- Describe the part of the SMO algorithm which updates $a_i$ and $a_j$ to
  maximize the Lagrangian. [10]

- Describe the part of the SMO algorithm which updates $b$ to maximize the
  Lagrangian. [10]

- Describe the one-versus-one and one-versus-rest schemes of constructing
  a $K$-class classifier by combining multiple binary classifiers. [5]
