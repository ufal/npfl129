#### Questions@:, Lecture 1 Questions

1. Explain how reinforcement learning differs from supervised and unsupervised learning in terms of the type of input the learning algorithms use to improve model performance. [5]

1. Explain why we need separate training and test data. What is generalization, and how does the concept relate to underfitting and overfitting? [10]

1. Define the prediction function of a *linear regression* model and write down $L^2$-regularized mean squared error loss. [10]

1. Starting from the unregularized sum of squares error of a linear regression model, show how the explicit solution can be obtained, assuming $\boldsymbol X^T \boldsymbol X$ is invertible. [10]

#### Questions@:, Lecture 2 Questions

1. Describe standard gradient descent and compare it to stochastic (i.e., online) gradient descent and minibatch stochastic gradient descent. Explain what it is used for in machine learning. [10]

1. Explain possible intuitions behind $L^2$ regularization. [5]

1. Explain the difference between hyperparameters and parameters. [5]

1. Write an $L^2$-regularized minibatch SGD algorithm for training a *linear regression* model, including the explicit formulas (i.e, formulas you would need to code it with `numpy`) of the loss function and its gradient. [10]

1. Does the SGD algorithm for *linear regression* always find the best solution on the training data? If yes, explain under what conditions it happens; if not, explain why it is not guaranteed to converge. What properties of the error function does this depend on? [10]

1. After training a model with SGD, you ended up with a low training error and a high test error. Using the learning curves, explain what might have happened and what steps you might take to prevent this from happening. [10]

1. You were given a fixed training set and a fixed test set, and you are supposed to report model performance on that test set. You need to decide what hyperparameters to use. How will you proceed and why? [10]

1. What methods can be used to normalize feature values? Explain why it is useful. [5]

#### Questions@:, Lecture 3 Questions

1. Define binary classification, write down the perceptron algorithm, and show how a prediction is made for a given data instance $\boldsymbol x$. [10]

1. For discrete random variables, define entropy, cross-entropy, and Kullback-Leibler divergence, and prove the Gibbs inequality (i.e., that KL divergence is non-negative). [20]

1. Explain the notion of likelihood in machine learning. What likelihood are we estimating, and why do we do it? [10]

1. Describe maximum likelihood estimation as minimizing NLL, cross-entropy, and KL divergence and explain whether they differ or are the same and why. [20]

1. Provide an intuitive justification for why cross-entropy is a good optimization objective in machine learning. What distributions do we compare in cross-entropy? Why is it good when the cross-entropy is low? [5]

1. Considering the binary *logistic regression* model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the explicit formula for the sigmoid function). [10]

1. Write down an $L^2$-regularized minibatch SGD algorithm for training a binary *logistic regression* model, including the explicit formulas (i.e., formulas you would need to code it in `numpy`) of the loss function and its gradient (saying just $\nabla$ is not enough). [20]

#### Questions@:, Lecture 4 Questions

1. Define mean squared error and show how it can be derived using MLE. What assumptions do we make during such derivation? [10]

1. Considering $K$-class logistic regression model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the formula for the softmax function). [10]

1. Explain the relationship between the sigmoid function and softmax. [5]

1. Show that the softmax function is invariant towards constant shift. [5]

1. Write down an $L^2$-regularized minibatch SGD algorithm for training a $K$-class logistic regression model, including the explicit formulas (i.e., formulas you would use to code it in `numpy`) of the loss function and its gradient. [20]

1. Prove that decision regions of a multiclass logistic regression are convex. [10]

1. Considering a single-layer MLP with $D$ input neurons, $H$ hidden neurons, $K$ output neurons, hidden activation $f$, and output activation $a$, list its parameters (including their size) and write down how the output is computed. [10]

1. List the definitions of frequently used MLP output layer activations (the ones producing parameters of a Bernoulli distribution and a categorical distribution). Then, write down three commonly used hidden layer activations (sigmoid, tanh, ReLU). Explain why identity is not a suitable activation for hidden layers. [10]

#### Questions@:, Lecture 5 Questions

1. Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer with $H$ units, and a softmax output layer with $K$ units, write down the explicit formulas (i.e., formulas you would use to code it in `numpy`) of the gradient of the loss function with respect to all the MLP parameters (two weight matrices and two bias vectors), assuming input $\boldsymbol x$, target $t$, and negative log likelihood loss. [20]

1. Formulate the computation of MLP as a computation graph. What do the nodes and the edges of the graph represent? Explain how such a graph can be used to compute the gradients of the parameters in the back-propagation algorithm. [10]

1. Formulate the Universal approximation theorem and explain in words what it says about multi-layer perceptron. [10]

1. How do we search for a minimum of a function $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to equality constraints $g_1(\boldsymbol x)=0, \ldots, g_m(\boldsymbol x)=0$? [10]

1. Prove which categorical distribution with $N$ classes has maximum entropy. [10]

1. Consider derivation of softmax using maximum entropy principle, assuming we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D, t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the Lagrangian to be minimized. Explain in words what is the interpretation of the conditions. [20]

1. Define precision (including true positives and others), recall, $F_1$ score, and $F_\beta$ score (we stated several formulations for $F_1$ and $F_\beta$ scores; any one of them will do). [10]

1. Explain the difference between micro-averaged and macro-averaged $F_1$ scores. Under what circumstances do we use them? [10]

1. Explain (using examples) why accuracy is not a suitable metric for unbalanced target classes, e.g., for a diagnostic test for a contagious disease. [5]

#### Questions@:, Lecture 6 Questions

1. Explain how the TF-IDF weight of a given document-term pair is computed. [5]

1. What is Zipf's law? Explain how it can be used to provide intuitive justification for using the logarithm when computing IDF. [5]

1. Define conditional entropy and mutual information, write down the relation between them, and finally prove that mutual information is zero if and only if the two random variables are independent (you do not need to prove statements about $D_\textrm{KL}$). [10]

1. Show that TF-IDF terms can be considered portions of suitable mutual information. [10]

1. Explain the concept of word embedding in the context of MLP and how it relates to representation learning. [5]

1. Describe the skip-gram model trained using negative sampling. What is it used for? What are the input and output of the algorithm? [10]

1. How would you train a part-of-speech tagger (i.e., you want to assign each word to its part of speech) if you could only use labeled data, pre-trained word embeddings and MLP classifier? [5]

#### Questions@:, Lecture 7 Questions

1. Describe the prediction of $k$ nearest neighbors, both for regression and classification. Define $L_p$ norm and describe uniform, inverse, and softmax weighting. [10]

1. Show that $L^2$-regularization can be obtained from a suitable prior by Bayesian inference (from the MAP estimate). [10]

1. Write down how $p(C_k | \boldsymbol x)$ is approximated in a Naive Bayes classifier, explicitly state the Naive Bayes assumption, and show how the prediction is performed. [10]

1. Considering a Gaussian Naive Bayes, describe how probabilities $p(x_d | C_k)$ are modeled (what distribution and which parameters it has) and how we estimate it during fitting. [10]

1. Considering a Bernoulli Naive Bayes, describe how probabilities $p(x_d | C_k)$ are modeled (what distribution and which parameters it has) and how we estimate it during fitting. [10]

1. What measures can we take to prevent numeric instabilities in the Naive Bayes classifier, particularly if the probability density is too high in Gaussian Naive Bayes and there are zero probabilities in Bernoulli Naive Bayes? [10]

1. What is the difference between discriminative and (classical) generative models? [5]

#### Questions@:, Lecture 8 Questions

1. Prove that independent discrete random variables are uncorrelated. [10]

1. Write down the definition of covariance and Pearson correlation coefficient $\rho$, including its range. [10]

1. Explain how Spearman's rank correlation coefficient and Kendall's rank correlation coefficient are computed (there is no need to describe the Pearson correlation coefficient). [10]

1. Describe setups where a correlation coefficient might be a good model evaluation metric. [5]

1. Describe under what circumstance correlation can be used to assess the validity of evaluation metrics. [5]

1. Define Cohen's $\kappa$ (including the definition of the respective probabilities) and explain what it is used for when collecting data for machine learning. [10]

1. Assuming you have collected data for classification by letting people annotate data instances. How do you estimate a reasonable range for classifier performance? [5]

1. Considering an averaging ensemble of $M$ models, prove the relation between the average mean squared error of the ensemble and the average error of the individual models, assuming the model errors have zero means and are uncorrelated. Use a formula to explain what uncorrelated errors mean in this context. [20]

1. Explain knowledge distillation: what it is used for, describe how it is done. What is the loss function? How does it differ from standard training? [10]

#### Questions@:, Lecture 9 Questions

1. In a regression decision tree, state what values are kept in internal nodes, define the squared error criterion, and describe how a leaf is split during training (without discussing splitting constraints). [10]

1. Explain the CART algorithm for constructing a decision tree. Explain the relationship between the loss function that is optimized during the decision tree construction and the splitting criterion that is during the node splitting. [10]

1. In a $K$-class classification decision tree, state what values are kept in internal nodes, define the Gini index, and describe how a node is split during training (without discussing splitting constraints). [10]

1. In a $K$-class classification decision tree, state what values are kept in internal nodes, define the entropy criterion, and describe how a node is split during training (without discussing splitting constraints). [10]

1. For binary classification using decision trees, derive the Gini index from a squared error loss. [20]

1. For $K$-class classification using decision trees, derive the entropy criterion from a non-averaged NLL loss. [20]

1. Describe how a random forest is trained (including bagging and a random subset of features) and how prediction is performed for regression and classification. [10]

#### Questions@:, Lecture 10 Questions

1. Explain the main differences between random forests and gradient-boosted decision trees. [5]

1. Explain the intuition for second-order optimization using Newton's root-finding method or Taylor expansions. [10]

1. Write down the loss function that we optimize in gradient-boosted decision trees while constructing $t^\mathrm{th}$ tree. Then, define $g_i$ and $h_i$ and show the value $w_\mathcal{T}$ of optimal prediction in node $\mathcal{T}$ and the criterion used during node splitting. [20]

1. For a $K$-class classification, describe how to perform prediction with a gradient boosted decision tree trained for $T$ time steps (how the individual trees perform prediction and how are the $K \cdot T$ trees combined to produce the predicted categorical distribution). [10]

1. What type of data are gradient boosted decision trees suitable for as opposed to multilayer perceptron? Explain the intuition why it is the case. [5]

#### Questions@:, Lecture 11 Questions

1. Formulate SVD decomposition of matrix $\boldsymbol X$, describe properties of individual parts of the decomposition. Explain what the reduced version of SVD is. [10]

1. Formulate the Eckart-Young theorem. Provide an interpretation of what the theorem says and why it is useful. [10]

1. Given a data matrix $\boldsymbol X$, explain how to compute the PCA of dimension M using the SVD decomposition. Explain the why it works. [10]

1. Given a data matrix $\boldsymbol X$, write down the algorithm for computing the PCA of dimension $M$ using the power iteration algorithm. [20]

1. List at least two applications of SVD or PCA. [5]

1. Describe the $K$-means algorithm, including the `kmeans++` initialization. What is it used for? What is the loss function that the algorithm optimizes? What can you say about the algorithm convergence? [20]

1. Name at least two clustering algorithms. What is their main principle? How do they differ? [10]

#### Questions@:, Lecture 12 Questions

1. Considering statistical hypothesis testing, define type I errors and type II errors (in terms of the null hypothesis). Finally, define what a significance level is. [10]

1. Explain what a test statistic and a p-value are. [10]

1. Write down the steps of a statistical hypothesis test, including a definition of a p-value. [10]

1. Explain the differences between a one-sample test, a two-sample test, and a paired test. [10]

1. When considering the multiple comparison problem, define the family-wise error rate and prove the Bonferroni correction, which allows limiting the family-wise error rate by a given $\alpha$. [10]

1. For a trained model and a given test set with $N$ examples and metric $E$, write how to estimate 95\% confidence intervals using bootstrap resampling. [10]

1. For two trained models and a given test set with $N$ examples and metric $E$, explain how to perform a paired bootstrap test that the first model is better than the other. [10]

1. For two trained models and a given test set with $N$ examples and metric $E$, explain how to perform a random permutation test that the first model is better than the other with a significance level $\alpha$. What is the null hypothesis here? How do to compute the $p$-value? [10]

#### Questions@:, Lecture 13 Questions

1. Explain the difference between deontological and utilitarian ethics. List examples of how these theoretical frameworks can be applied in machine learning ethics. [10]

1. List at least two potential ethical problems related to data collection. [5]

1. List at least two potential ethical problems that can originate in model evaluation. [5]

1. List at least one example of an ethical problem that can originate in model design or model development. [5]

1. Under what circumstances could train-test mismatch be an ethical problem? [5]
