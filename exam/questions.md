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