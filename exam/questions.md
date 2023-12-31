#### Questions@:, Lecture 1 Questions

- Explain why we need separate train and test data? What is generalization and
  how the concept relates to underfitting and overfitting? [10]

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
  non-negative). [20]

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

- Prove that decision regions of a multiclass logistic regression convex. [10]

- Considering a single-layer MLP with $D$ input neurons, $H$ hidden
  neurons, $K$ output neurons, hidden activation $f$, and output activation $a$,
  list its parameters (including their size) and write down how the output
  is computed. [10]

- List the definitions of frequently used MLP output layer activations (the ones
  producing parameters of a Bernoulli distribution and a categorical distribution).
  Then write down three commonly used hidden layer activations (sigmoid, tanh,
  ReLU). [10]

#### Questions@:, Lecture 5 Questions
- Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer
  with $H$ units and a softmax output layer with $K$ units, write down the
  explicit formulas of the gradient of all the MLP parameters (two weight matrices and
  two bias vectors), assuming input $\boldsymbol x$, target $t$, and negative log
  likelihood loss. [20]

- Formulate the Universal approximation theorem. [10]

- How do we search for a minimum of a function
  $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to equality
  constraints $g_1(\boldsymbol x)=0, \ldots, g_m(\boldsymbol x)=0$? [10]

- Prove which categorical distribution with $N$ classes has maximum
  entropy. [10]

- Consider derivation of softmax using maximum entropy principle, assuming
  we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D,
  t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the
  searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the
  Lagrangian to be minimized. [20]

- Define precision (including true positives and others), recall, $F_1$ score,
  and $F_\beta$ score (we stated several formulations for $F_1$ and $F_\beta$
  scores; any one of them will do). [10]

- Explain the difference between micro-averaged and macro-averaged $F_1$ scores. [10]

- Explain (using examples) why accuracy is not a suitable metric for unbalanced
  target classes, e.g., for a diagnostic test for a contagious disease. [5]

### Questions@:, Lecture 6 Questions
- Explain how is the TF-IDF weight of a given document-term pair computed. [5]

- Define conditional entropy, mutual information, write down the relation
  between them, and finally prove that mutual information is zero
  if and only if the two random variables are independent (you do not
  need to prove statements about $D_\textrm{KL}$). [10]

- Show that TF-IDF terms can be considered portions of suitable mutual
  information. [10]

- Explain the concept of word embedding in the context of MLP and how it
  relates to representation learning. [5]

- Describe the skip-gram model trained using negative sampling. [10]

- How would you proceed to train a part-of-speech tagger (i.e., you want to
  assign each word with its part of speech) if you only could use pre-trained
  word embeddings and MLP classifier? [5]

### Questions@:, Lecture 7 Questions
- Describe $k$-nearest neighbors prediction, both for regression and
  classification. Define $L_p$ norm and describe uniform, inverse,
  and softmax weighting. [10]

- Show that $L^2$-regularization can be obtained from a suitable prior
  by Bayesian inference (from the MAP estimate). [10]

- Write down how $p(C_k | \boldsymbol x)$ is approximated in a Naive Bayes
  classifier, explicitly state the Naive Bayes assumption, and show how is the
  prediction performed. [10]

- Considering a Gaussian naive Bayes, describe how are $p(x_d | C_k)$ modeled
  (what distribution and which parameters does it have) and how we estimate it
  during fitting. [10]

- Considering a Bernoulli naive Bayes, describe how are $p(x_d | C_k)$ modeled
  (what distribution and which parameters does it have) and how we estimate it
  during fitting. [10]

### Questions@:, Lecture 8 Questions

- Prove that independent discrete random variables are uncorrelated. [10]

- Write down the definition of covariance and Pearson correlation coefficient
  $\rho$, including its range. [10]

- Explain how are the Spearman's rank correlation coefficient and the Kendall
  rank correlation coefficient computed (no need to describe the Pearson
  correlation coefficient). [10]

- Describe setups where a correlation coefficient might be a good
  evaluation metric. [5]

- Describe under what circumstance correlation can be used to assess validity
  of evaluation metrics. [5]

- Define Cohen's $\kappa$ and explain what is used for when preparing data for
  machine learning. [10]

- Considering an averaging ensemble of $M$ models, prove the relation between
  the average mean squared error of the ensemble and the average error of the
  individual models, assuming the model errors have zero means and are
  uncorrelated. [20]

- Explain knowledge distillation: what it is used for, describe how it is done.
  [10]

### Questions@:, Lecture 9 Questions

- In a regression decision tree, state what values are kept in internal nodes,
  define the squared error criterion and describe how is a leaf split during
  training (without discussing splitting constraints). [10]

- In a $K$-class classification decision tree, state what values are kept in
  internal nodes, define the Gini index and describe how is a node split during
  training (without discussing splitting constraints). [10]

- In a $K$-class classification decision tree, state what values are kept in
  internal nodes, define the entropy criterion and describe how is a node split during
  training (without discussing splitting constraints). [10]

- For binary classification, derive the Gini index from a squared error loss. [20]

- For $K$-class classification, derive the entropy criterion from a non-averaged
  NLL loss. [20]

- Describe how is a random forest trained (including bagging and a random subset
  of features) and how is prediction performed for regression and classification. [10]

#### Questions@:, Lecture 10 Questions
- Write down the loss function which we optimize in gradient boosted decision
  trees during the construction of $t^\mathrm{th}$ tree. Then define $g_i$
  and $h_i$ and show the value $w_\mathcal{T}$ of optimal prediction in node
  $\mathcal{T}$ and the criterion used during node splitting. [20]

- For a $K$-class classification, describe how to perform prediction with
  a gradient boosted decision tree trained for $T$ time steps (how the
  individual trees perform prediction and how are the $K \cdot T$ trees
  combined to produce the predicted categorical distribution). [10]

- What type of data are gradient boosted decision trees good for as opposed to
  multilayer perceptron? Explain the intuition why it is the case. [5]

#### Questions@:, Lecture 11 Questions
- Formulate SVD decomposition of matrix $\boldsymbol X$, describe properties of
  individual parts of the decomposition. Explain what the reduced version of
  SVD is. [10]

- Formulate the Eckart-Young theorem. [10]

- Explain how to compute the PCA of dimension $M$ using the SVD decomposition of
  a data matrix $\boldsymbol X$, and why it works. [10]

- Given a data matrix $\boldsymbol X$, write down the algorithm for computing
  the PCA of dimension $M$ using the power iteration algorithm. [20]

- Describe the K-means algorithm, including the `kmeans++` initialization. [20]

#### Questions@:, Lecture 12 Questions
- Considering statistical hypothesis testing, define type I errors and type II
  errors (in terms of the null hypothesis). Finally, define what a significance
  level is. [10]

- Explain what a test statistic and a p-value are. [10]

- Write down the steps of a statistical hypothesis test, including a definition
  of a p-value. [10]

- Explain the differences between a one-sample test, two-sample test, and
  a paired test. [10]

- When considering multiple comparison problem, define the family-wise
  error rate, and prove the Bonferroni correction, which allows
  limiting the family-wise error rate by a given $\alpha$. [10]

- For a trained model and a given test set with $N$ examples and metric $E$,
  write how to estimate 95\% confidence intervals using bootstrap resampling.
  [10]

- For two trained models and a given test set with $N$ examples and metric $E$,
  explain how to perform a paired bootstrap test that the first model is better
  than the other. [10]

- For two trained models and a given test set with $N$ examples and metric $E$,
  explain how to perform a random permutation test that the first model is better
  than the other with a significance level $\alpha$. [10]
