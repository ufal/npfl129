### Questions@:, Lecture 1 Questions

- Explain how reinforcement learning differs from supervised and unsupervised learning in terms of the type of input the learning algorithms use to improve model performance. [5]

- Explain why we need separate training and test data. What is generalization, and how does the concept relate to underfitting and overfitting? [10]

- Define the prediction function of a linear regression model and write down $L^2$-regularized mean squared error loss. [10]

- Starting from the unregularized sum of squares error of a linear regression model, show how the explicit solution can be obtained, assuming $\boldsymbol X^T \boldsymbol X$ is invertible. [10]

#### Questions@:, Lecture 2 Questions

- Describe standard gradient descent and compare it to stochastic (i.e., online) gradient descent and minibatch stochastic gradient descent. Explain what it is used for in machine learning. [10]

- Explain possible intuitions behind $L^2$ regularization. [5]

- Explain the difference between hyperparameters and parameters. [5]

- Write an $L^2$-regularized minibatch SGD algorithm for training a *linear regression* model, including the explicit formulas (i.e, formulas you would need to code it with `numpy`) of the loss function and its gradient. [10]

- Does the SGD algorithm for *linear regression* always find the best solution on the training data? If yes, explain under what conditions it happens; if not, explain why it is not guaranteed to converge. What properties of the error function does this depend on? [10]

- After training a model with SGD, you ended up with a low training error and a high test error. Using the learning curves, explain what might have happened and what steps you might take to prevent this from happening. [10]

- You were given a fixed training set and a fixed test set, and you are supposed to report model performance on that test set. You need to decide what hyperparameters to use. How will you proceed and why? [10]

- What methods can be used to normalize feature values? Explain why it is useful. [5]

#### Questions@:, Lecture 3 Questions

- Define binary classification, write down the perceptron algorithm, and show how a prediction is made for a given data instance $\boldsymbol x$. [10]

- For discrete random variables, define entropy, cross-entropy, and Kullback-Leibler divergence, and prove the Gibbs inequality (i.e., that KL divergence is non-negative). [20]

- Explain the notion of likelihood in maximum likelihood estimation. What likelihood are we estimating in machine learning, and why do we do it? [5]

- Describe maximum likelihood estimation as minimizing NLL, cross-entropy, and KL divergence and explain whether they differ or are the same and why. [20]

- Provide an intuitive justification for why cross-entropy is a good optimization objective in machine learning. What distributions do we compare in cross-entropy? Why is it good when the cross-entropy is low? [5]

- Considering the binary logistic regression model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the explicit formula for the sigmoid function). [10]

- Write down an $L^2$-regularized minibatch SGD algorithm for training a binary *logistic regression* model, including the explicit formulas (i.e., formulas you would need to code it in `numpy`) of the loss function and its gradient (saying just $\grad$ is not enough). [20]

#### Questions@:, Lecture 4 Questions

- Define mean squared error and show how it can be derived using MLE. What assuptions do we make during such derivation? [10]

- Considering $K$-class logistic regression model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the formula for the softmax function). [10]

- Explain the relationship between the sigmoid function and softmax. [5]

- Show that the softmax function is invariant towards constant shift. [5]

- Write down an $L^2$-regularized minibatch SGD algorithm for training a $K$-class logistic regression model, including the explicit formulas (i.e., formulas you would to code it in `numpy`) of the loss function and its gradient. [20]

- Prove that decision regions of a multiclass logistic regression are convex. [10]

- Considering a single-layer MLP with $D$ input neurons, $H$ hidden neurons, $K$ output neurons, hidden activation $f$, and output activation $a$, list its parameters (including their size) and write down how the output is computed. [10]

- List the definitions of frequently used MLP output layer activations (the ones producing parameters of a Bernoulli distribution and a categorical distribution). Then write down three commonly used hidden layer activations (sigmoid, tanh, ReLU). Explain why identity is not a suitable activation for hidden layers. [10]

#### Questions@:, Lecture 5 Questions

- Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer with $H$ units and a softmax output layer with $K$ units, write down the explicit formulas (i.e., formulas you would to code it in `numpy`) of the gradient of all the MLP parameters (two weight matrices and two bias vectors), assuming input $\boldsymbol x$, target $t$, and negative log likelihood loss. [20]

- Formulate the computation of MLP as a computation graph. Explain how such a graph can be used to compute the gradients of the parameters in the back-propagation algorithm. [10]

- Formulate the Universal approximation theorem and explain in words what it says about multi-layer perceptron. [10]

- How do we search for a minimum of a function $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to equality constraints $g_1(\boldsymbol x)=0, \ldots, g_m(\boldsymbol x)=0$? [10]

- Prove which categorical distribution with $N$ classes has maximum entropy. [10]

- Consider derivation of softmax using maximum entropy principle, assuming we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D, t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the Lagrangian to be minimized. Explain in words what is the interpretation of the conditions. [20]

- Define precision (including true positives and others), recall, $F_1$ score, and $F_\beta$ score (we stated several formulations for $F_1$ and $F_\beta$ scores; any one of them will do). [10]

- Explain the difference between micro-averaged and macro-averaged $F_1$ scores. List few examples when you would use them. [10]

- Explain (using examples) why accuracy is not a suitable metric for unbalanced target classes, e.g., for a diagnostic test for a contagious disease. [5]
