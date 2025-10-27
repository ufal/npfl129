#### Questions@:, Lecture 1 Questions

1. Explain how reinforcement learning differs from supervised and unsupervised learning in terms of the type of input the learning algorithms use to improve model performance. [5]

1. Explain why we need separate training and test data. What is generalization, and how does the concept relate to underfitting and overfitting? [10]

1. Define the three key components of Mitchell's definition of machine learning (Task $T$, Performance measure $P$, and Experience $E$). Give a concrete example for each component in the context of email spam classification. [10]

1. Explain the difference between classification and regression tasks. For each task type, provide: (a) the mathematical representation of the target variable, (b) a real-world example, and (c) one appropriate evaluation metric. [10]

1. Define the prediction function of a *linear regression* model and write down $L^2$-regularized mean squared error loss. [10]

1. Starting from the unregularized sum of squares error of a linear regression model, show how the explicit solution can be obtained, assuming $\boldsymbol X^T \boldsymbol X$ is invertible. [10]

#### Questions@:, Lecture 2 Questions

1. Describe standard gradient descent and compare it to stochastic (i.e., online) gradient descent and minibatch stochastic gradient descent. Explain what it is used for in machine learning. [10]

1. Explain the relationship between model capacity and overfitting/underfitting. How does increasing polynomial degree in linear regression affect model capacity, and what are the consequences? [10]

1. Explain possible intuitions behind $L^2$ regularization. [5]

1. Explain the difference between hyperparameters and parameters. [5]

1. Write an $L^2$-regularized minibatch SGD algorithm for training a *linear regression* model, including the explicit formulas (i.e, formulas you would need to code it with `numpy`) of the loss function and its gradient. [10]

1. Does the SGD algorithm for *linear regression* always find the best solution on the training data? If yes, explain under what conditions it happens; if not, explain why it is not guaranteed to converge. What properties of the error function does this depend on? [10]

1. After training a model with SGD, you ended up with a low training error and a high test error. Using the learning curves, explain what might have happened and what steps you might take to prevent this from happening. [10]

1. You were given a fixed training set and a fixed test set, and you are supposed to report model performance on that test set. You need to decide what hyperparameters to use. How will you proceed and why? [10]

1. What methods can be used to normalize feature values? Explain why it is useful. [5]

1. You have a dataset with a categorical feature “color” with values {“red”, “green”, “blue”}. Explain why using integer encoding (`red=0`, `green=1`, `blue=2`) is problematic for linear regression. How would encode such feature instead? [10]

#### Questions@:, Lecture 3 Questions

1. Define binary classification, write down the perceptron algorithm, and show how a prediction is made for a given data instance $\boldsymbol x$. [10]

1. Explain what it means for a dataset to be linearly separable. Give an example of a simple 2D dataset that is *not* linearly separable and explain why the perceptron algorithm would fail on it. [10]

1. For discrete random variables, define entropy, cross-entropy, and Kullback-Leibler divergence, and prove the Gibbs inequality (i.e., that KL divergence is non-negative). [20]

1. Explain the notion of likelihood in machine learning. What likelihood are we estimating, and why do we do it? [10]

1. Describe maximum likelihood estimation as minimizing NLL, cross-entropy, and KL divergence and explain whether they differ or are the same and why. [20]

1. Provide an intuitive justification for why cross-entropy is a good optimization objective in machine learning. What distributions do we compare in cross-entropy? Why is it good when the cross-entropy is low? [5]

1. Considering the binary *logistic regression* model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the explicit formula for the sigmoid function). [10]

1. Write down an $L^2$-regularized minibatch SGD algorithm for training a binary *logistic regression* model, including the explicit formulas (i.e., formulas you would need to code it in `numpy`) of the loss function and its gradient (saying just $\nabla$ is not enough). [20]

1. Compare and contrast perceptron and logistic regression by discussing: (a) what each algorithm optimizes, (b) whether each provides probability estimates, (c) whether each is guaranteed to converge, and (d) the quality of solutions each finds. [10]

1. Explain in intuitive terms why we use the logarithm when working with likelihoods in machine learning. What are the computational and optimization advantages of using negative log-likelihood instead of directly maximizing the likelihood? [5]

#### Questions@:, Lecture 4 Questions

1. Define mean squared error and show how it can be derived using MLE. What assumptions do we make during such derivation? [10]

1. Considering $K$-class logistic regression model, write down its parameters (including their size) and explain how we decide what classes the input data belong to (including the formula for the softmax function). [10]

1. Explain the relationship between the sigmoid function and softmax. [5]

1. Show that the softmax function is invariant towards constant shift. [5]

1. Write down an $L^2$-regularized minibatch SGD algorithm for training a $K$-class logistic regression model, including the explicit formulas (i.e., formulas you would use to code it in `numpy`) of the loss function and its gradient. [20]

1. Prove that decision regions of a multiclass logistic regression are convex. [10]

1. Considering a single-layer MLP with $D$ input neurons, $H$ hidden neurons, $K$ output neurons, hidden activation $f$, and output activation $a$, list its parameters (including their size) and write down how the output is computed. [10]

1. List the definitions of frequently used MLP output layer activations (the ones producing parameters of a Bernoulli distribution and a categorical distribution). Then, write down three commonly used hidden layer activations (sigmoid, tanh, ReLU). Explain why identity is not a suitable activation for hidden layers. [10]

1. Explain the role of initialization in training MLPs. Why is it problematic to initialize all weights to zero? What is a common strategy for random initialization, and why does it typically scale with the input dimension? [10]

1. You have trained two models on the same dataset: (1) logistic regression and (2) a multilayer perceptron with one hidden layer of 100 neurons. The MLP achieves 95% training accuracy while logistic regression achieves 85%. However, both achieve 84% test accuracy. Interpret these results and explain what they suggest about the models and the data. [5]

1. You are supposed to train an MLP for regression that has several numeric features as the input. How would you preprocess them? Specifically, would you use polynomial features? Explain your decision. [5]

#### Questions@:, Lecture 5 Questions

1. Considering a single-layer MLP with $D$ input neurons, a ReLU hidden layer with $H$ units, and a softmax output layer with $K$ units, write down the explicit formulas (i.e., formulas you would use to code it in `numpy`) for the forward pass through the MLP. [10]

1. Compute the partial derivative of $-\log \operatorname{softmax}(\boldsymbol{z})$ with respect to $\boldsymbol{z}$. Explain how this computation is used when training MLP. [20]

1. Formulate the computation of MLP as a computation graph. What do the nodes and the edges of the graph represent? Explain how such a graph can be used to compute the gradients of the parameters in the back-propagation algorithm. [10]

1. Explain the concept of dropout as a regularization technique for MLPs. How does it work during training versus at test time, and what is the intuition behind why it improves generalization? [10]

1. Formulate the Universal approximation theorem and explain in words what it says about multi-layer perceptron. [10]

1. How do we search for a minimum of a function $f(\boldsymbol x): \mathbb{R}^D \rightarrow \mathbb{R}$ subject to equality constraints $g_1(\boldsymbol x)=0, \ldots, g_m(\boldsymbol x)=0$? [10]

1. Prove which categorical distribution with $N$ classes has maximum entropy. [10]

1. Consider derivation of softmax using maximum entropy principle, assuming we have a dataset of $N$ examples $(x_i, t_i), x_i \in \mathbb{R}^D, t_i \in \{1, 2, \ldots, K\}$. Formulate the three conditions we impose on the searched $\pi: \mathbb{R}^D \rightarrow \mathbb{R}^K$, and write down the Lagrangian to be minimized. Explain in words what is the interpretation of the conditions. [20]

1. Define precision (including true positives and others), recall, $F_1$ score, and $F_\beta$ score (we stated several formulations for $F_1$ and $F_\beta$ scores; any one of them will do). [10]

1. Explain the difference between micro-averaged and macro-averaged $F_1$ scores. Under what circumstances do we use them? [10]

1. Explain (using examples) why accuracy is not a suitable metric for unbalanced target classes, e.g., for a diagnostic test for a contagious disease. [5]
