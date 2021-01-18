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

- Show that the perceptron algorithm is an instance of a stochastic gradient
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
  compute the results. [5]

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
  we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D,
  t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the
  searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the
  Lagrangian to be maximized. [10]

- Define precision, recall, $F_1$ score and $F_\beta$ score (we stated several
  formulations for $F_1$ and $F_\beta$ scores; any of them will do). [5]

- Explain the difference between micro-averaged and macro-averaged $F_1$ score. [5]

- Describe k-nearest neighbors prediction, both for regression and
  classification. Define $L_p$ norm and describe uniform, inverse
  and softmax weighting. [5]

####Questions@: ,Lecture 6 Questions
- Define a kernel based on a feature map $\varphi$, and write down the formulae
  for (1) a polynomial kernel of degree $d$, (2) a polynomial kernel of degree
  at most $d$, (3) an RBF kernel. [5]

- Define a kernel and write down the mini-batch SGD training algorithm of dual
  formulation of kernel linear regression. Then, describe how predictions for
  unseen data are made. [10]

- Derive the primary formulation of hard-margin SVM (the value to minimize,
  the constraints to fulfil) as a maximum-margin classifier. [5]

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

####Questions@: ,Lecture 8 Questions
- Write down how is a Nyström approximation of an RBF kernel constructed. [10]

- Describe how is a trained Nyström approximation of an RBF kernel applied
  to input data. [5]

- Explain how is the TF-IDF weight of a given term computed. [5]

- Write down how is $p(C_k | \boldsymbol x)$ approximated in a Naive Bayes
  classifier, and explicitly state the Naive Bayes assumption. [5]

- Describe how are $p(x_i | C_k)$ modelled and estimated in Gaussian NB
  classifier. [5]

- Describe how are $p(x_i | C_k)$ modelled and estimated in Multinomial NB
  classifier. [5]

- Describe how are $p(x_i | C_k)$ modelled and estimated in Bernoulli NB
  classifier. [5]

####Questions@: ,Lecture 9 Questions
- Write down the definition of covariance and Pearson covariation coefficient.
  [5]

- Prove that independent variables are uncorrelated. [5]

- Explain how are the Spearman's rank correlation coefficient and the Kendall
  rank correlation coefficient computed. [5]

- Considering an averaging ensemble of $M$ models, prove the relation of the
  average mean squared error of the ensemble to the average error of the
  individual models, assuming the model errors have zero mean and are
  uncorrelated. [10]

- In a regression decision tree, define the squared error criterion and
  describe how a node is split during training. [5]

- In a classification decision tree, define the Gini index and
  describe how a node is split during training. [5]

- In a classification decision tree, define the entropy criterion and
  describe how a node is split during training. [5]

- For binary classification, derive Gini index from squared error loss. [10]

- For $k$-class classification, derive entropy criterion from non-averaged NLL loss. [10]

- Describe how is a random forest trained (including bagging and random subset
  of features) and how is prediction performed for regression and classification. [10]

####Questions@: ,Lecture 10 Questions
- For a $k$-class classification, describe how to perform prediction with
  a gradient boosting decision tree trained for $T$ timestamps. [5]

- Write down the loss function which we optimize in gradient boosting decision
  tree during the construction of $t^\mathrm{th}$ tree. Then define $g_i$
  and $h_i$ and show the value $w_\mathcal{T}$ of optimal prediction in node
  $\mathcal{T}$. [10]

- Write down the loss function which we optimize in gradient boosting decision
  tree during the construction of $t^\mathrm{th}$ tree. Then define $g_i$
  and $h_i$ and the criterion used during node splitting. [10]

- How is the learning rate used during training and prediction of a gradient
  boosting decision tree? [5]

- Considering a $k$-class classification, describe which individual trees are
  created during gradient boosted decision tree training, in which order they
  are constructed and what per-example loss is used for training every one of
  them (without describing the training process of the individual trees
  themselves). [5]

####Questions@: ,Lecture 11 Questions
- When discovering the first principal component, write the value of the
  variance we aim to maximize, both without and with the covariance matrix
  (and define the covariance matrix). [5]

- When discovering the first $M$ principal components, write the value of the
  reconstruction loss we aim to minimize, both without and with the covariance
  matrix (and define the covariance matrix). [5]

- Write down the result of whitening (sphering) the data matrix $\boldsymbol X$.
  [5]

- Explain how to compute the first $M$ principal components using the SVD
  decomposition of the data matrix $\boldsymbol X$. [5]

- Write down the algorithm of computing the first $M$ principal components
  of the data matrix $\boldsymbol X$ using the power iteration algorithm. [10]

- Describe the K-means algorithm. [10]

- Define the multivariate Gaussian distribution of dimension $D$. [5]

- Show how to sample from a multivariate Gaussian distribution
  $\mathcal{N}(\boldsymbol \mu, \boldsymbol \Sigma)$ with a full covariance
  matrix, by using random samples from $\mathcal{N}(0, \boldsymbol I)$
  distribution. [5]

- Describe the constant surfaces of a multivariate Gaussian distribution with
  (1) $\sigma^2 \boldsymbol I$ covariation, (2) a diagonal covariation matrix,
  (3) a full covariation matrix. [5]

####Questions@: ,Lecture 12 Questions
- Considering a Gaussian mixture with $K$ cluster, explain how we represent
  the individual clusters and write down the likelihood of an example
  $\boldsymbol x$ for a given Gaussian mixture. [5]

- Write down the log likelihood of a dataset for a given Gaussian mixture. [5]

- Considering the algorithm for Gaussian mixture clustering, write down the
  E step (how to compute the responsibilities) and the M step (how to update
  the means, covariances and priors of the individual clusters). [10]

- Write down the MSE loss of a regression problem, and formulate the
  bias-variance trade-off, i.e., the decomposition of expected MSE loss
  (with respect to a randomly sampled test set) into bias, variance and
  irreducible error terms. [10]

####Questions@: ,Lecture 13 Questions
- Considering statistical hypothesis testing, define type I errors, type II
  errors and significance level. [5]

- Explain what a test statistic and a p-value are. [5]

- Write down the steps of a statistical hypothesis test. [10]

- Explain the differences between a one-sample test, two-sample test and
  a paired test. [5]

- When considering multiple comparison problem, define the family-wise
  error rate, and formulate the Bonferroni correction, which allows
  to limit the family-wise error rate by a given $\alpha$. [5]

- For a trained model and a given test set, write how to estimate
  95\% confidence intervals using bootstrap resampling. [10]

- For two trained models, explain how to perform a paired bootstrap
  test that the first model is better with a significance level $\alpha$. [10]
