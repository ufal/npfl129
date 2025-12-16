#import "ufal.typ": *

#show: ufal-theme.with(
  footer-content: "NPFL129, Practicals 10 - SVMs",
)
#show math.equation.where(block: false): it => math.display(it)
#set par(justify: true, justification-limits: (
  tracking: (min: -0.01em, max: 0.02em)
))
#show figure.caption: body => {
  set text(size: 10pt, fill: muted-color)
  emph(body)
}

#let argmax = {
  math.op("argmax", limits: true)
}
#let argmin = {
  math.op("argmin", limits: true)
}

#title-slide(
  title: "NPFL129, Practicals 10",
  name: "Support Vector Machines",
  subtitle: "",
  author: "Jan Bronec",
  date: "December 4-5, 2025",
  license-type: "cc-by-sa",
  langtech: false,
)[]

#section-slide("Revisiting linear classifiers")

#slide[
  = Recall the simple linear classifiers

  === Perceptron
  #align(center)[
    $f(bold(x)) = "sign"(bold(w) dot bold(x) + b)$
  ]
  - We find $bold(w), b$ with the perceptron learning algorithm.
  #infobox[It doesn't guarantee anything about the decision boundary.]
  #align(center)[
    #image("figures/perceptron_suboptimal.svgz", height: 8em)
  ]
]

#slide[
  = Recall the simple linear classifiers

  === Perceptron
  #align(center)[
    $f(bold(x)) = "sign"(bold(w) dot bold(x) + b)$
  ]
  - We find $bold(w), b$ with the Perceptron algorithm.
  #infobox[It doesn't guarantee anything about the decision boundary.]
  #infobox[It will not converge for linearly non-separable data.]
]



#slide[
  = Recall the simple linear classifiers

  === Logistic regression
  #align(center)[
    $p("Positive" | bold(x); bold(w),b) = sigma(bold(w) dot bold(x) + b)$
  ]
  - We find $bold(w), b$ by optimizing for NLL with SGD:
  #align(center)[
    $bold(w)^*,b^* = argmin_(bold(w), b) 1/N sum_i - log(p(C_i | bold(x)_i; bold(w), b))$
  ]

  - It can handle even non-separable data
  - We can help with separability using polynomial features.

  #infobox[Polynomial features increase the complexity of learning and inference.]
  #infobox[Decision boundary may still be suboptimal.]
]

#slide[
  = Logistic regression
  #infobox[Polynomial features increase the complexity of learning and inference.]
  Consider logistic regression with linear, quadratic, and cubic features computed by feature mapping $phi: RR^D -> RR^(1+D+D^2+D^3)$:

  #align(center)[
    $phi(bold(x)) = vec(1, x_i, dots, x_i x_j, dots, x_i x_j x_k, dots)$ with $i,j,k in {1...D}$
  ]

  For input of dimensionality $D$, one step of SGD takes $cal(O)(D^3)$ per example.
]

#slide[
  = Logistic regression
  #infobox[Decision boundary may still be suboptimal.]
  The decision boundary is easily skewed by an imbalanced dataset.
  #align(center)[
    #image("figures/logistic_no_margins.svgz", height: 12em)
  ]
]

#slide[
  = Logistic regression
  #infobox[Decision boundary may still be suboptimal.]
  Margin = distance from the boundary to the nearest data point
  #align(center)[
    #image("figures/logistic_with_margins.svgz", height: 12em)
  ]
]

#slide[
  = Logistic regression
  #infobox[Decision boundary may still be suboptimal.]
  What we might want instead...
  #align(center)[
    #image("figures/svm_with_margins.svgz", height: 12em)
  ]
]

#slide[
  = Idea
  #set align(center + horizon)

  == Larger margin $approx$ better generalization
]

#slide[
  = SVM primal formulation

  Lets formulate the problem as margin maximization.

  For now, we will assume the following:
  - linearly separable dataset $cal(D) in.rev (bold(x)_i, t_i)$
  - two classes, targets $t_i in {-1, +1}$
  - $y(bold(x)) = bold(w)^T bold(x) + b$

  #figure(
    image("figures/svm_margin.pdf", height: 8em),
    numbering: none,
    caption: [Figure 7.1 of Pattern Recognition and Machine Learning. ]
  )
]

#slide[
  = SVM primal formulation

  Assume we have a decision boundary given by $bold(w)^T bold(x) + b = 0$ that perfectly separates our training data, i.e. $t_i y(bold(x)_i) > 0$ for all $i$.

  The distance of a given point $x_i$ from the decision boundary is:
  $
    d_i = (|bold(w)^T bold(x)_i + b|)/ (||bold(w)||) = (t_i y(bold(x_i))) / (||bold(w)||)
  $

  The margin $m$ is the distance of the point closest to the decision boundary:
  $
    m = min_i d_i = (min_i t_i y(bold(x_i))) / (||bold(w)||)
  $
]

#slide[
  = SVM primal formulation

  Notice that if we multiply the weights and bias by a positive constant $c > 0$:
  $
    bold(w)' = c dot bold(w), b' = c dot b
  $
  we do not change the decision boundary they describe. The values $y'(bold(x)_i) = bold(w)'^T bold(x)_i + b'$ still have the same sign, but their magnitude changes:
  $
    y'(bold(x_i)) = c dot y(bold(x_i))
  $

  We will set $c$ such that $t_i y(bold(x)_i) = 1$ holds for the closest point $x_i$ to the decision boundary.

  In other words $min_i t_i y(bold(x)_i) = 1$, but also:
  $
    t_i y(bold(x)_i) >= 1
  $
]

#slide[
  = SVM primal formulation

  With $min_i t_i y(bold(x)_i) = 1$, we get that the margin is:

  $
    m = (min_i t_i y(bold(x_i))) / (||bold(w)||) = 1 / (||bold(w)||)
  $

  We want to find $bold(w), b$ that maximize the margin and satisfy $t_i y(bold(x)_i) >= 1 #h(0.5em) forall i$:

  #align(center)[
    $bold(w)^*,b^* = argmax_(bold(w), b)1/(||bold(w)||)$
    #h(3em)
    s.t.: #h(0.5em) $t_i y(bold(x)_i) >= 1$
    #h(0.5em) $forall i$
  ]

  Or equivalently...
  #align(center)[
    $bold(w)^*,b^* = argmin_(bold(w), b)1/2||bold(w)||^2$
    #h(3em)
    s.t.: #h(0.5em) $t_i y(bold(x)_i) - 1 >= 0$
    #h(0.5em) $forall i$
  ]

]

#slide[
  = SVM primal formulation

  What we have arrived at:

  #infobox(fill: blue)[
    #set align(center)
    $bold(w)^*,b^* = argmin_(bold(w), b)1/2||bold(w)||^2$
    #h(3em)
    s.t.: #h(0.5em) $t_i y(bold(x)_i) - 1 >= 0$
    #h(0.5em) $forall i$
  ]

  This is called the primal formulation of the SVM learning problem.

  #v(1em)
  Compare it to the formulation of logistic regression for which we used SGD:
  #infobox()[
    #set align(center)
  $bold(w)^*,b^* = argmin_(bold(w), b) 1/N sum_i cal(L)(t_i, y(bold(x)_i))$
  ]

  This time we cannot just use SGD though. We need another tool.
]

#slide[
  = Constrained Optimization - Equality Constraints
  Given a function $f(bold(x))$, we want to find its minimum w.r.t. the input $bold(x)$.
  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 1fr))[
    #enum(numbering: "a)",
      [
        Without any constraints, we investigate the critical points: $nabla_bold(x) f(bold(x)) = 0$
      ],
      [
        #show: later
        We can incorporate $N$ equality constraints $g_i (bold(x)) = 0$ that the solution must satisfy.

        $=>$ We introduce $N$ *Lagrange multipliers* $bold(lambda) in RR^N$, and we form a Lagrangian:
        #align(center)[
          $cal(L)(bold(x), bold(lambda)) = f(bold(x)) - sum_i lambda_i g_i (bold(x)) = f(bold(x)) - bold(lambda)^T g(bold(x))$
        ]
        And again, we investigate its critical points:
        #align(center)[
          $nabla_(bold(x), bold(lambda)) cal(L)(bold(x), bold(lambda)) = 0$
        ]
      ]
    )
  ][
    #figure(
      image("figures/Lagrange_very_simple.svg", height: 12em),
      numbering: none,
      caption: link("https://commons.wikimedia.org/wiki/File:Lagrange_very_simple.svg")
    )
  ]
]

#slide[
  = Constrained Optimization - Inequality Constraints

  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 0.95fr))[
    #list(marker: "c)",
      [
        In our case, we have $N$ inequality constraints $g_i (bold(x)) >= 0$.

        We again start by forming a Lagrangian:

        #align(center)[$cal(L)(bold(x), bold(lambda)) = f(bold(x)) - bold(lambda)^T g(bold(x))$]

        This time we'll investigate only the critical points in $bold(x)$:

        #align(center)[$nabla_(bold(x)) cal(L)(bold(x), bold(lambda)) = 0$]

        Now, there are two cases that can happen for each constraint.

        Consider first a simpler case with a convex function $f(bold(x))$, and a single constraint $g(bold(x)) >= 0$.
      ]
    )
  ][
    #figure(
      image("figures/lagrange_inequalities_cases.svgz", height: 10em),
      numbering: none,
      caption: link("https://upload.wikimedia.org/wikipedia/commons/5/5d/Inequality_constraint_diagram.svg")
    )
  ]
]

#slide[
  = Constrained Optimization - Inequality Constraints

  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 1.1fr))[
    Case 1)

    If the optimum of $f(bold(x))$ lies within the region $g(bold(x)) > 0$, the constraint is said to be *inactive*.

    We would find the optimum even if we'd remove the constrain, i.e. set $lambda = 0$.
  ][
    #figure(
      image("figures/kkt_case_1.svg", height: 18em),
      numbering: none,
      caption: link("https://upload.wikimedia.org/wikipedia/commons/5/5d/Inequality_constraint_diagram.svg")
    )
  ]
]

#slide[
  = Constrained Optimization - Inequality Constraints

  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 1fr))[
    Case 2)

    If the actual optimum is outside of the region, then we are looking for a minimum on the boundary $g(bold(x)) = 0$.
    The constraint is said to be *active*.

    The minimum corresponds to a critical point with $lambda != 0$. Notice that in both cases, $lambda g(bold(x)) = 0$.
  ][
    #figure(
      image("figures/kkt_case_2.svg", height: 18em),
      numbering: none,
      caption: link("https://upload.wikimedia.org/wikipedia/commons/5/5d/Inequality_constraint_diagram.svg")
    )
  ]
]

#slide[
  = Constrained Optimization - Inequality Constraints

  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 1.1fr))[
    Case 2)

    The minimum corresponds to a point on the boundary.

    Notice that in both cases, $lambda g(bold(x)) = 0$.

    This time, the sign of $lambda$ matters.
    We can use the fact, that $nabla g(bold(x))$ on the boundary is oriented *into* the region $g(bold(x)) >= 0$.
    Minimum is attained only when the gradient of $f(bold(x))$ is also oriented *into* the region. We therefore require:

    #align(center)[$nabla f(bold(x)) = lambda nabla g(bold(x))$ for $lambda > 0$]

    Again, notice that in both cases, $lambda >= 0$.
  ][
    #figure(
      image("figures/lagrange_inequalities.svgz", height: 10em),
      numbering: none,
      caption: [Figure E.3 of Pattern Recognition and Machine Learning.]
    )
  ]
]

#slide[
  = Minimization - Inequality Constraints

  *Theorem*: Let $f(bold(x)): RR^D -> RR$ be a function, which has a minimum in $bold(x)^*$ subject to $N$ inequality constraints $g_i (bold(x)) >= 0$. Assume that all $f$ and $g_i$ have continuous partial derivatives, and that $nabla_bold(x) g_i (bold(x)^*) != 0$.

  Then, there exist $bold(lambda) in RR^N$, such that the *Lagrangian function*

  #align(center)[
    $cal(L)(bold(x), bold(lambda)) eq.def f(bold(x)) - bold(lambda)^T g(bold(x))$
  ]

  has zero gradient in $bold(x)^*$, and the following conditions hold $forall i$:

  #align(center)[
    $
      g_i (bold(x)) &>= 0, \
      lambda_i &>= 0, \
      lambda_i g_i (bold(x)) &= 0.
    $
  ]

  These conditions are known as *Karush-Kuhn-Tucker (KKT)* conditions.
]

#slide[
  = Necessary and Sufficient KKT Conditions

  The KKT conditions are *necessary* conditions for a minimum.
  - i.e. the minimum has to satisfy them, but other points can satisfy them as well.

  //#show: later

  However, in the following settings, the conditions are also *sufficient*:
  - we are optimizing a _convex_ function $f(bold(x))$
  - the inequality constraints are continuously differentiable convex functions
  - the equality constraints (if any) are affine functions

  //#show: later

  Our problem satisfies these settings:
  #infobox(fill: blue)[
    #set align(center)
    $bold(w)^*,b^* = argmin_(bold(w), b)1/2||bold(w)||^2$
    #h(3em)
    s.t.: #h(0.5em) $t_i y(bold(x)_i) - 1 >= 0$
    #h(0.5em) $forall i$
  ]
]

#slide[
  = Minimization - Inequality Constraints

  *Lemma* (Lagrangian duality): For a problem that is in the settings from previous slide, if $cal(L(bold(x), bold(lambda))) eq f(bold(x)) - bold(lambda)^T g(bold(x))$ has a minimum in $bold(x)^*$, then:

  #align(center)[
    $bold(lambda)$ fulfills the KKT conditions $<==>$ $cal(L)(bold(x)^*, bold(lambda))$ has a maximum in $bold(lambda)$ subject to $bold(lambda) >= 0$
  ]

  #show: later
  *Proof*:

  #enum(numbering: n => ([], $arrow.r.double)$, $arrow.l.double)$).at(n), [
    We have $bold(lambda)$ s.t. $ g_i (bold(x)^*) >= 0, lambda_i >= 0, lambda_i g_i (bold(x)^*) = 0.$
    - if $g_i (bold(x)^*) = 0$, then $cal(L)$ does not change with changing $lambda_i$
    - if $g_i (bold(x)^*) > 0$, then $lambda_i = 0$ from the KKT cond., which maximizes $cal(L)$ subject to $lambda_i >= 0$
  ], [
    #show: later
    We have a maximum of $cal(L)(bold(x)^*, bold(lambda))$ in $bold(lambda)$ subject to $lambda_i >= 0$.
    - if $g_i (bold(x)^*) < 0$, then increasing $lambda_i$ would increase $cal(L)$ #emoji.lightning
    - if $g_i (bold(x)^*) > 0$, then decreasing $lambda_i$ increases $cal(L)$, so $lambda_i = 0$ #h(8em) #math.square
  ]
  )
]

#slide[
  = Dual formulation derivation

  #infobox(fill: blue)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Problem:
      #align(center)[
      $bold(w)^*,b^* = argmin_(bold(w), b)1/2||bold(w)||^2$
      ]
      Lagrangian:
      #align(center)[
        $cal(L)(bold(w), b, bold(alpha)) = 1/2||bold(w)||^2 - sum_i alpha_i (t_i y(bold(x)_i) - 1)$
      ]
    ][
      KKT conditions:
      #set align(center)
      $
        t_i y(bold(x)_i) - 1 &>= 0 \
        alpha_i &>= 0 \
        alpha_i (t_i y(bold(x)_i) - 1) &= 0
      $
    ]
  ]
]

#slide[
  = Dual formulation derivation
  We have the Lagrangian:
  $
    cal(L)(bold(w), b, bold(alpha)) = 1/2||bold(w)||^2 - sum_i alpha_i (t_i (bold(w)^T bold(x)_i + b) - 1)
  $
  For easier manipulation, let's rewrite it as:
  $
    cal(L)(bold(w), b, bold(alpha)) = 1/2 sum_j w_j^2 - sum_i sum_j alpha_i t_i w_j x_(i,j) - sum_i alpha_i t_i b + sum_i alpha_i
  $
  Then we set these partial derivatives to 0:
  $
    0 = partial/(partial w_j)cal(L) = w_j - sum_i alpha_i t_i x_(i,j) , #h(3em) 0 = partial/(partial b)cal(L) = -sum_i alpha_i t_i
  $
  We get: $w = sum_i alpha_i t_i bold(x)_i$, and $sum_i alpha_i t_i = 0$
]

#slide[
  = Dual formulation derivation
  Substituting $w = sum_i alpha_i t_i bold(x)_i$ back into the Lagrangian:
  $
    cal(L)(bold(w), b, bold(alpha)) = 1/2||bold(w)||^2 - sum_i alpha_i (t_i (bold(w)^T bold(x)_i + b) - 1)
  $
  We get:
  $
    cal(L)(bold(w), b, bold(alpha)) = 1/2 (sum_i alpha_i t_i bold(x)_i)^T (sum_j alpha_j t_j bold(x)_j) - sum_i alpha_i (t_i ((sum_j alpha_j t_j bold(x)_j)^T bold(x)_i + b) - 1)
  $
  This simplifies to:
  $
    cal(L)(bold(w), b, bold(alpha)) = - 1/2 sum_i sum_j alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j - b sum_i alpha_i t_i + sum_i alpha_i
  $
]

#slide[
  $
    cal(L)(bold(w), b, bold(alpha)) = - 1/2 sum_i sum_j alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j - b sum_i alpha_i t_i + sum_i alpha_i
  $

  We know $sum_i alpha_i t_i = 0$, so the $b$ term vanishes:

  $
    cal(L)(bold(alpha)) = sum_i alpha_i - 1/2 sum_i sum_j alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j
  $
]

#slide[
  We know that we can describe $bold(w)$ using the multipliers $bold(alpha)$:
  $
    bold(w) = sum_i alpha_i t_i x_i
  $
  Since the KKT conditions are *sufficient* for our problem,
  we know that finding $bold(alpha)^*$ that satisfy all KKT conditions will be enough to describe the optimal weights:

  $
    bold(w)^* = sum_i alpha^*_i t_i x_i
  $

  With those, we can also express the optimal bias $b^*$,
  $
    b^* = t_s - bold(w)^(*T)x_s
  $
  for any $alpha_s > 0$, because $alpha_s (t_s y(bold(x)_s) - 1) = 0$.


  We must now find $bold(alpha)^*$ that satisfy the KKT conditions. From the *Lemma*, we know that such $bold(alpha)^*$ maximize the Lagrangian $cal(L)(bold(alpha))$ subject to $alpha_i >= 0$. Therefore, we will find them as:

  $
    bold(alpha)^* = argmax_bold(alpha) sum_i alpha_i - 1/2 sum_i sum_j alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j #h(3em) text("s.t.") alpha_i >= 0
  $

  But we have also found the condition $sum_i alpha_i t_i = 0$, which we must satisfy as well.

  We have arrived to a dual problem which is, in a sense, equivalent to our original problem. However, the dual can be solved using quadratic programming.
]

#slide[
  = Dual formulation derivation

  #infobox(fill: blue)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Problem:
      #align(center)[
      $bold(w)^*,b^* = argmin_(bold(w), b)1/2||bold(w)||^2$
      ]
      Lagrangian:
      #align(center)[
        $cal(L)(bold(w), b, bold(alpha)) = 1/2||bold(w)||^2 - sum_i alpha_i (t_i y(bold(x)_i) - 1)$
      ]
    ][
      KKT conditions:
      #set align(center)
      $
        t_i y(bold(x)_i) - 1 &>= 0 \
        alpha_i &>= 0 \
        alpha_i (t_i y(bold(x)_i) - 1) &= 0
      $
    ]
  ]

  #infobox(fill: red)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Dual problem:
      #set align(center)
      $bold(alpha)^* = argmax_(bold(alpha)) sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j$
    ][
      Conditions:
      #set align(center)
      $
        alpha_i &>= 0 \
        sum_i alpha_i t_i &= 0
      $
    ]
  ]
]

#slide[
  = Dual formulation key points
  #infobox(fill: red)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Dual problem:
      #align(center)[
        $bold(alpha)^* = argmax_(bold(alpha)) sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j$
      ]

      Inference: $y(bold(x)) = sum_i alpha_i t_i bold(x)_i^T bold(x) + b$
    ][
      Conditions:
      #set align(center)
      $
        alpha_i &>= 0 \
        sum_i alpha_i t_i &= 0
      $
    ]
  ]

  - Thanks to the lemma, we don't need to explicitly satisfy the KKTs. We know they will be satisfied for $bold(alpha)^*$.
  - From the KKTs, we know that #text(fill: color.green.darken(40%), [$alpha_i (t_i y(bold(x_i)) - 1) = 0$]). For most samples $x_i$, we'll actually have $alpha_i = 0$. Those samples with $alpha_i > 0$ are the *support vectors*, which describe the decision boundary.
]

#slide[
  = Support vectors in a linearly-separable dataset
  #align(center)[
    #image("figures/svm_linear_margins.svgz", height: 19em)
  ]
]

#slide[
  = Dual formulation key points
  #infobox(fill: red)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Dual problem:
      #align(center)[
        $bold(alpha)^* = argmax_(bold(alpha)) sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j$
      ]

      Inference: $y(bold(x)) = sum_i alpha_i t_i bold(x)_i^T bold(x) + b$
    ][
      Conditions:
      #set align(center)
      $
        alpha_i &>= 0 \
        sum_i alpha_i t_i &= 0
      $
    ]
  ]

  - $b = t_s - bold(w)^T bold(x)_s$ for any support vector $bold(x)_s$. Usually a mean over all support vectors is computed for numerical stability.
  #show: later
  - Instead of $bold(w)$, we use the nonzero $alpha_i$ and their support vectors for inference.
  #show: later
  - The feature vectors $bold(x)$ are only used in the scalar products $bold(x)_i^T bold(x)_j$. We can replace them with any *kernel function* $K(bold(x)_i, bold(x)_j)$.
]

#slide[
  = Kernels

  *Definition* A symmetric function $K: RR^D times RR^D -> RR$ is called a positive-definite kernel, if:

  $forall bold(x)_1, ..., bold(x)_n in RR^D, forall c_1, ..., c_n in RR:$

  $
    sum_(i=1)^n sum_(j=1)^n c_i c_j K(bold(x)_i, bold(x)_j) >= 0
  $

  - This definition holds for the skalar product of feature vectors with any mapping $phi$:
  $
    K(bold(x), bold(z)) = phi(bold(x))^T phi(bold(z))
  $
]

#slide[
  = Kernels

  === Other commonly used kernels

  - *Polynomial kernel of degree* $d$
  $
    K(bold(x), bold(z)) = (gamma bold(x)^T bold(z))^d
  $

  #show: later

  - *Polynomial kernel of degree at most* $d$
  $
    K(bold(x), bold(z)) = (gamma bold(x)^T bold(z) + 1)^d
  $

  #show: later

  - *Gaussian Radial basis function (RBF)*
  $
    K(bold(x), bold(z)) = e^(-gamma ||bold(x) - bold(z)||^2)
  $
]

#slide[
  = Dual problem key points
  #infobox(fill: red)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Dual problem:
      #align(center)[
        $bold(alpha)^* = argmax_(bold(alpha)) sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j K(bold(x)_i, bold(x)_j)$
      ]

      Inference: $y(bold(x)) = sum_i alpha_i t_i K(bold(x)_i, bold(x)_j) + b$
    ][
      Conditions:
      #set align(center)
      $
        alpha_i &>= 0 \
        sum_i alpha_i t_i &= 0
      $
    ]
  ]

  #item-by-item()[
    - The kernels are cheaper to compute, than the actual polynomial mappings.
    - The RBF kernel is a function of distance. SVM with the RBF kernel can be viewed as an extended version of the k-nearest neighbors algorithm, selecting only the most significant samples and weights them by similarity.
    - The $alpha_i$ multipliers are given by the data. SVMs are considered to be non-parametric.
  ]

]

#slide[
  = RBF Kernel support vectors in a non-linear dataset
  #align(center)[
    #image("figures/svm_nonlinear.svgz", height: 19em)
  ]
]

#slide[
  = Overfitting
  SVMs with RBF kernel can technically #text(fill: green.darken(30%))[separate] any dataset. This typically causes overfitting on noise.
  #align(center)[
    #figure(
      image("figures/classification_overfitting.svgz", height: 13em),
      numbering: none,
      caption: link("https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg")
    )
  ]
]

#slide[
  = Allowing SVMs to make mistakes $=>$ Soft-margin SVMs

  #toolbox.side-by-side(gutter: 1em, columns: (2fr, 0.9fr))[
    Until now, we assumed the data do be linearly separable, and allowed points to only be outside the margin.

    We will now relax this condition, and allow points to be *in the margin*, or even on the *wrong side* of the decision boundary.

    We introduce *slack variables* $xi_i >= 0$ for each training instance $i$.
  ][
    #figure(
      image("figures/svm_softmargin.pdf", height: 10em),
      numbering: none,
      caption: [Figure 7.3 of Pettern Recognition and Machine Learning]
    )
  ]

  We will define them such that $xi_i = 0$ signifies a point outside of the margin, $xi_i in (0, 1)$ for a point inside the margin, $xi_i = 1$ for a point on the decision boundary, and $xi_i > 1$ for the wrong side of the boundary. We want $sum_i xi_i$ to be minimal.
]

#slide[
  = Soft-margin SVM derivation

  #infobox(fill: blue)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.9fr, 1fr))[
      Problem:
      #align(center)[
      $bold(w)^*,b^* = argmin_(bold(w), b, bold(xi))1/2||bold(w)||^2 + C sum_i xi_i$
      ]
      Lagrangian:
      #align(center)[#scale(90%, reflow:true)[
        $cal(L) = 1/2||bold(w)||^2 + C sum_i xi_i - sum_i alpha_i (t_i y(bold(x)_i) + xi_i - 1) - sum_i beta_i xi_i$
      ]]
    ][
      KKT conditions:
      #set align(center)
      $
        t_i y(bold(x)_i) + xi_i - 1 >= 0, xi_i &>= 0  \
        alpha_i (t_i y(bold(x)_i) + xi_i - 1) = 0, alpha_i &>= 0 \
        beta_i xi_i = 0, beta_i &>= 0
      $
    ]
  ]
]

#slide[
  = Soft-margin SVM derivation
  We perform the same procedure as before with the Lagrangian:
  $
    cal(L)(bold(w), b, bold(xi), bold(alpha), bold(beta))  = 1/2||bold(w)||^2 + C sum_i xi_i - sum_i alpha_i (t_i y(bold(x)_i) + xi_i - 1) - sum_i beta_i xi_i
  $
  This time we also compute the partial derivative w.r.t. $xi_i$:
  $
    partial/(partial xi_i)cal(L) = C - alpha_i - beta_i = 0
  $
  Again, substituting everything back into the Lagrangian we obtain:

  $
    cal(L) = sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j + sum_i xi_i (C - alpha_i - beta_i)
  $

  Since $C - alpha_i - beta_i = 0$, the last sum is also equal to 0.
]

#slide[
  = Soft-margin SVM derivation
  We have arrived to the exact same expression as before, which we now must maximize:

  $
    bold(alpha)^* = argmax_bold(alpha) sum_i alpha_i - 1/2 sum_i sum_j alpha_i alpha_j t_i t_j bold(x_i)^T bold(x)_j #h(3em) text("s.t.") alpha_i >= 0, #h(1em)sum_i alpha_i t_i = 0
  $

  But this time, we also have $C - alpha_i - beta_i = 0$, i.e.:
  $
    alpha_i = C - beta_i
  $
  Since $beta_i >= 0$ from the KKT, we get:
  $
    alpha_i <= C
  $
  Our actual constraints are therefore:
  $
    C >= alpha_i >= 0, #h(1em)sum_i alpha_i t_i = 0
  $
]

#slide[
  = Soft-margin SVM derivation

  #infobox(fill: blue)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.9fr, 1fr))[
      Problem:
      #align(center)[
      $bold(w)^*,b^* = argmin_(bold(w), b, bold(xi))1/2||bold(w)||^2 + C sum_i xi_i$
      ]
      Lagrangian:
      #align(center)[#scale(90%, reflow:true)[
        $cal(L) = 1/2||bold(w)||^2 + C sum_i xi_i - sum_i alpha_i (t_i y(bold(x)_i) + xi_i - 1) - sum_i beta_i xi_i$
      ]]
    ][
      KKT conditions:
      #set align(center)
      $
        t_i y(bold(x)_i) + xi_i - 1 >= 0, xi_i &>= 0  \
        alpha_i (t_i y(bold(x)_i) + xi_i - 1) = 0, alpha_i &>= 0 \
        beta_i xi_i = 0, beta_i &>= 0
      $
    ]
  ]

  #infobox(fill: red)[
    #toolbox.side-by-side(gutter: 1em, columns: (1.5fr, 1fr))[
      Dual problem:
      #set align(center)
      $bold(alpha)^* = argmax_(bold(alpha)) sum_i alpha_i - 1/2sum_(i,j)alpha_i alpha_j t_i t_j bold(x)_i^T bold(x)_j$
    ][
      Conditions:
      #set align(center)
      $
        C >= alpha_i &>= 0 \
        sum_i alpha_i t_i &= 0
      $
    ]
  ]
]

#slide[
  = Soft-margin SVM with RBF kernel
  ```python
  svm_classifier = sklearn.svm.SVC(kernel='rbf', C=10)
  ```
  #align(center)[
    #image("figures/svm_nonlinear_2.svgz", height: 15em)
  ]
]

#slide[
  = SGD-like Formulation of Soft-Margin SVM
  Note that the slack variables can be written as:
  #align(center)[$xi_i = max(0, 1-t_i y(bold(x)_i))$]

  So, we can reformulate the soft-margin objective with the *hinge loss*:
  #align(center)[$cal(L)_text("hinge")(t, y) = max(0, 1-t y)$]

  to:
  #infobox(fill: blue)[
    #set align(center)
    $bold(w)^*,b^* = argmin_(bold(w), b) C sum_i cal(L)_text("hinge")(t_i, y(bold(x_i))) + 1/2||bold(w)||^2$
  ]

  Which is analogous to a regularized loss, similar to logistic regression with $L_2$ norm:
  #infobox()[
    #set align(center)
  $bold(w)^*,b^* = argmin_(bold(w), b) 1/N sum_i cal(L)_text("NLL")(t_i, y(bold(x)_i)) + 1/2||bold(w)||^2$
  ]
]

#slide[
  = Hinge-loss regression trained by SGD
  #align(center)[
    #image("figures/hinge_sgd_decision_boundary.svgz", height: 18em)
  ]
]

#slide[
  = Primal versus Dual Formulation
  Assume we have a dataset with $N$ training examples, each with $D$ features. We use a feature map $phi$ to generate $F$ features.

  #set align(center)
  #set table(
    fill: (x, y) =>
      if y == 0 {ufal-orange.lighten(20%)}
      else if calc.div-euclid(y, 2) * 2 == y {gray.lighten(70%)}
  )

  #table(
  columns: 3,
  [], [Primal formulation], [Dual formulation],
  [Parameters], [$F$], [$N$],
  [Model size], [$F$], [$s dot F$ for $s$ support vectors],
  [Usual training time], [$Theta(e dot N dot F)$ for $e$ epochs], [between $Omega(N D)$ and $cal(O)(N^2 D)$],
  [Inference time], [$Theta(F)$], $Theta(s dot D)$
  )
]

#summary-slide(
  title: "Today's Lecture Objectives",
  subtitle: "NPFL129, Practicals 10 - SVMs",
)[
  After this lecture, you should be able to:
  - explain the soft-margin SVM dual derivation
  - know that something called "Karush-Kuhn-Tucker" conditions exists for constraint optimization
  - be familiar with "kernels" and their advantages over feature maps
]
