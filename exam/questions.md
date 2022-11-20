#### Questions@:, Lecture 1 Questions
- Define prediction function of a linear regression model and write down
  $L^2$-regularized mean squared error loss. [5]

- Starting from unregularized sum of squares error of a linear regression model,
  show how the explicit solution can be obtained, assuming
  $\boldsymbol X^T \boldsymbol X$ is regular. [10]

#### Questions@:, Lecture 2 Questions
- Define expectation $\mathbb{E}[f(x)]$ and variance $\operatorname{Var}(f(x))$
  of a discrete random variable. Then define the bias of an estimator and show that
  estimating an expectation using a single sample is unbiased. [5]

- Describe standard gradient descent and compare it to stochastic (i.e., online) gradient
  descent and minibatch stochastic gradient descent. [5]

- Formulate conditions on the sequence of learning rates used in SGD to converge
  to optimum almost surely. [5]

- Write an $L^2$-regularized minibatch SGD algorithm for training a linear
  regression model, including the explicit formulas of the loss function and
  its gradient. [5]

#### Questions@:, Lecture 3 Questions
- Define binary classification, write down the perceptron algorithm and show
  how a prediction is made for a given example. [5]

- Show that the perceptron algorithm is an instance of stochastic gradient
  descent. Why are the learning rates not needed (i.e., why are the predictions
  of a trained model the same for all positive learning rates)? [5]

- For discrete random variables, define entropy, cross-entropy, Kullback-Leibler
  divergence, and prove the Gibbs inequality (i.e., that KL divergence is
  non-negative). [5]

- Define data distribution, empirical data distribution and likelihood. [5]

- Describe maximum likelihood estimation, as minimizing NLL, cross-entropy and
  KL divergence. [10]

- Considering binary logistic regression model, write down its parameters
  (including their size) and explain how prediction is performed (including the
  formula for the sigmoid function). Describe how we can interpret the outputs
  of the linear part of the model as logits. [5]

- Write down an $L^2$-regularized minibatch SGD algorithm for training a
  binary logistic regression model, including the explicit formulas of the
  loss function and its gradient. [10]

#### Questions@:, Lecture 4 Questions
- Define mean squared error and show how it can be derived using MLE. [5]

- Considering $K$-class logistic regression model, write down its parameters
  (including their size) and explain how prediction is performed (including the
  formula for the softmax function). Describe how we can interpret the outputs
  of the linear part of the model as logits. [5]

- Write down an $L^2$-regularized minibatch SGD algorithm for training
  a $K$-class logistic regression model, including the explicit formulas of the
  loss function and its gradient. [10]

- Prove why are decision regions of a multiclass logistic regression convex. [5]

- Considering a single-layer MLP with $D$ input neurons, $H$ hidden
  neurons, $K$ output neurons, hidden activation $f$ and output activation $a$,
  list its parameters (including their size) and write down how the output
  is computed. [5]

- List the definitions of frequently used MLP output layer activations (the ones
  producing parameters of a Bernoulli distribution and a categorical distribution).
  Then write down three commonly used hidden layer activations (sigmoid, tanh,
  ReLU). [5]

- Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer
  with $H$ units and a softmax output layer with $K$ units, write down the
  formulas of the gradient of all the MLP parameters (two weight matrices and
  two bias vectors), assuming input $\boldsymbol x$, target $t$ and negative log
  likelihood loss. [10]

- Formulate the Universal approximation theorem. [5]

#### Questions@:, Lecture 5 Questions
- How do we search for a minimum of a function
  $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to equality
  constraints $g_1(\boldsymbol x)=0, \ldots, g_m(\boldsymbol x)=0$? [5]

- Prove which categorical distribution with $N$ classes has maximum
  entropy. [5]

- Consider derivation of softmax using maximum entropy principle, assuming
  we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D,
  t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the
  searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the
  Lagrangian to be maximized. [10]

- Define precision (including true positives and others), recall, $F_1$ score,
  and $F_\beta$ score (we stated several formulations for $F_1$ and $F_\beta$
  scores; any one of them will do). [5]

- Explain the difference between micro-averaged and macro-averaged $F_1$ scores. [5]

- Describe k-nearest neighbors prediction, both for regression and
  classification. Define $L_p$ norm and describe uniform, inverse, 
  and softmax weighting. [5]

#### Questions@:, Lecture 6 Questions
- Define a kernel based on a feature map $\varphi: \mathbb{R}^D \rightarrow \mathbb{R}^F$,
  and write down the formulas for (1) a polynomial kernel of degree $d$, (2)
  a polynomial kernel of degree at most $d$, (3) an RBF kernel. [5]

- Define a kernel and write down the mini-batch SGD training algorithm of dual
  formulation of kernel linear regression (including the update for the bias).
  Then describe how are predictions for unseen data made. [10]

- Derive the primary formulation of hard-margin SVM (the value to minimize,
  the constraints to fulfill) as a maximum-margin classifier (i.e., start by
  margin maximization). [5]

- How do we search for a minimum of a function
  $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to an inequality
  constraint $g(\boldsymbol x) \ge 0$? Formulate both the variant with KKT
  conditions and the variant with the $\lambda$ maximization, and prove that they
  are equivalent. [10]

- Starting from primary hard-margin SVM formulation, derive the dual formulation
  (the Lagrangian $\mathcal{L}$ in the form used for training, the required
  conditions, the KKT conditions of the solution, and how is the prediction
  performed). [10]

- Considering hard-margin SVM, define what is a support vector, and how are
  predictions performed for unseen data. [5]

#### Questions@:, Lecture 7 Questions
- Write down the primary formulation of soft-margin SVM using the slack
  variables (the value to minimize, the constraints to fulfill). [5]

- Starting from primary soft-margin SVM formulation, derive the dual formulation
  (the Lagrangian $\mathcal{L}$ in the form used for training, the required
  conditions, the KKT conditions of the solution, and how is prediction
  performed). [10]

- Write down the primary formulation of soft-margin SVM using the hinge
  loss. [5]

- Describe the high-level overview of the SMO algorithm (the test whether
  the KKT conditions hold, how do we select the $a_i$ and $a_j$ to update,
  what is the goal of updating the $a_i$ and $a_j$, how do we detect
  convergence; but without the update of $a_i$, $a_j$, $b$ themselves). [5]

- Describe the part of the SMO algorithm which updates $a_i$ and $a_j$ to
  maximize the Lagrangian. If you explain how the update is derived (so that if
  I followed the instructions, I would come up with the update rules), you do
  not need to write explicit formulas. [10]

- Describe the part of the SMO algorithm which updates $b$ to maximize the
  Lagrangian. If you explain how the update is derived (so that if I followed
  the instructions, I would come up with two $b$ candidates and a rule to
  utilize them), you do not need to write explicit formulas. [10]

- Describe the one-versus-one and one-versus-rest schemes of constructing
  a $K$-class classifier by combining multiple binary classifiers. [5]

#### Questions@:, Lecture 8 Questions
- Explain how is the TF-IDF weight of a given document-term pair computed. [5]

- Define conditional entropy, mutual information, write down the relation
  between them, and finally prove that mutual information is zero
  if and only if the two random variables are independent (you do not
  need to prove statements about $D_\textrm{KL}$). [5]

- Show that TF-IDF terms can be considered portions of suitable mutual
  information. [5]

- Show that $L^2$-regularization can be obtained from a suitable prior
  by Bayesian inference (from the MAP estimate). [5]

- Write down how $p(C_k | \boldsymbol x)$ is approximated in a Naive Bayes
  classifier, explicitly state the Naive Bayes assumption, and show how
  prediction is performed. [5]

- Considering a Gaussian naive Bayes, describe how are $p(x_d | C_k)$ modeled
  (what distribution and which parameters does it have) and how we estimate it
  during fitting. [5]

- Considering a Multinomial naive Bayes, describe how are
  $p(\boldsymbol x | C_k)$ modeled (what distribution and which parameters does
  it have) and how we estimate it during fitting. [5]

- Considering a Bernoulli naive Bayes, describe how are $p(x_d | C_k)$ modeled
  (what distribution and which parameters does it have) and how we estimate it
  during fitting. [5]

- Describe the difference between a generative and a discriminative model,
  the strengths of these models, and explain why is logistic regression
  and multinomial/Bernoulli naive Bayes called a generative-discriminative pair.
  [5]
