- **Linear Regression**
  Define the linear regression model, error function used, and derive
  an algorithm which can analytically find the best fit. Also
  describe an extension with L2 regularization (error function and
  an algorithm).

- **Gradient Descent**
  Describe gradient descent, its variants (GD, SGD, minibatch SGD),
  and derive minibatch SGD algorithm for fitting L2 regularized
  linear regression.

- **Perceptron**
  Formulate binary classification, perceptron algorithm,
  its SGD formulation (i.e., which loss gives rise to the algorithm)

- **Information Theory, MLE**
  Define self-information, entropy, cross-entropy and Kullback-Leibler
  divergence. Prove Gibbs inequality, i.e., that cross-entropy is larger or
  equal to entropy. Finally describe maximum likelihood estimation,
  as minimizing NLL, cross-entropy and KL divergence.

- **Maximum Likelihood Estimation, MSE**
  Describe maximum likelihood estimation, as minimizing NLL, cross-entropy and
  KL divergence. Define mean squared error and show how it can be derived
  using MLE.

- **Logistic Regression, SGD**
  Formulate binary classification and logistic regression model including the
  sigmoid function. Describe what a logit is. Finally, write down a training
  algorithm based on SGD and explicitly compute the gradient of the loss function.

- **Multiclass Logistic Regression, SGD**
  Formulate multiclass classification and multiclass logistic regression model
  including the softmax function. Describe what a logit is. Finally, write down
  a training algorithm based on SGD and explicitly compute the gradient of the
  loss function.

- **Multiclass Logistic Regression, Decision Regions**
  Formulate multiclass classification and multiclass logistic regression model
  including the softmax function. Describe what a logit is. Write down
  a training algorithm based on SGD. Finally, show that decision regions
  of the multiclass logistic regression are singly connected and convex.

- **Multilayer Perceptron, SGD**
  Formulate multiclass classification and multilayer perceptron model,
  including hidden activation functions ($\sigma$, tanh, ReLU) and
  output activation functions (linear, $\sigma$, softmax). Write down
  a training algorithm based on SGD.

- **Multilayer Perceptron, Universal Approximation Theorem**
  Formulate multiclass classification and multilayer perceptron model,
  including hidden activation functions ($\sigma$, tanh, ReLU) and
  output activation functions (linear, $\sigma$, softmax). Formulate
  the Universal approximation theorem.

- **Kernelized Linear Regression**
  Formulate what a kernel is, and describe polynomial kernel and Gaussian
  kernel. Formulate linear regression using kernels and derive a dual formulation
  of the training algorithm (either as full GD or SGD) and write down how
  predictions are made.

- **Hard-Margin Support Vector Machines**
  Formulate what a kernel is, and describe polynomial kernel and Gaussian
  kernel. Formulate kernelized hard-margin support vector machines
  and write down the dual formulation of the problem (the loss to minimize
  and constraints to fulfil). Describe what a support vector is
  and how a prediction can be made using the support vectors only. Finally,
  describe the one-versus-rest and one-versus-one schemes for extending
  the binary SVM classification to a multiclass one.

- **Soft-Margin Support Vector Machines**
  Describe what a kernel is, and describe polynomial kernel and Gaussian kernel.
  Formulate kernelized soft-margin support vector machines and write down the
  dual formulation of the problem (the loss to minimize and constraints to
  fulfil). Finally, describe what a support vector is, which input examples are
  support vectors, and how a prediction can be made using the support vectors
  only.

- **Sequential Minimization Optimization Algorithm**
  Formulate kernelized soft-margin support vector machines and write down
  the dual formulation of the problem (the loss to minimize and constraints to
  fulfil). Describe the KKT conditions of the solution and formulate
  the SMO algorithm (to the level of $\textit{AlgorithmSketch}$ section of the slides;
  the $\textit{UpdateRules}$ section of the slides is not required)

- **Decision Trees**
  Describe a decision tree, and formulate an algorithm to fit a decision tree
  using a Gini criterion and entropy criterion. Show that the Gini criterion
  corresponds to MSE loss and that entropy criterion corresponds to NLL.
  Finally describe the maximum tree depth and maximum number of leaf nodes
  constraints and how can they be implemented.

- **Random Forests**
  Describe a decision tree, and formulate an algorithm to fit a decision tree
  using a Gini criterion and entropy criterion. Then, define random forests
  model, describe bagging and random subset of features procedure, and show
  a training procedure for random forests.

- **Gradient Boosting**
  Formulate gradient boosting decision trees, show how prediction is made,
  derive the loss using second-order Taylor expansion, show optimal weight
  for a node and the resulting splitting criterion. Finally, formulate
  the training algorithm.

- **Naive Bayes**
  Derive the generic naive Bayes classifier – formulation and prediction. Then,
  describe Gaussian NB, multinomial NB and Bernoulli NB variants.

- **K-Means**
  Describe clustering and derive the K-Means algorithm – formulate the loss it
  minimizes and show that the algorithm converges to its local minimum.

- **Gaussian Mixture**
  Describe clustering, formulate multinomial Gaussian distribution and write
  down the Gaussian mixture model and the training algorithm.
