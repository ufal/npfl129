### Assignment: gradient_boosting
#### Date: Deadline: Dec 19, 7:59 a.m.
#### Points: 6 points
#### Tests: gradient_boosting_tests

Using the [gradient_boosting.py](https://github.com/ufal/npfl129/tree/master/labs/10/gradient_boosting.py)
template, train gradient boosted decision tree forest for classification.

#### Tests Start: gradient_boosting_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=1 --learning_rate=0.3`
```
Using 1 trees, train accuracy: 95.5%, test accuracy: 91.1%
Using 2 trees, train accuracy: 95.5%, test accuracy: 86.7%
Using 3 trees, train accuracy: 97.7%, test accuracy: 91.1%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gradient_boosting_1.svgz)
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=2 --learning_rate=0.3 --seed=599`
```
Using 1 trees, train accuracy: 99.2%, test accuracy: 91.1%
Using 2 trees, train accuracy: 99.2%, test accuracy: 91.1%
Using 3 trees, train accuracy: 99.2%, test accuracy: 95.6%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gradient_boosting_2.svgz)
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=2 --l2=0.5 --learning_rate=0.3 --seed=488`
```
Using 1 trees, train accuracy: 97.0%, test accuracy: 95.6%
Using 2 trees, train accuracy: 98.5%, test accuracy: 97.8%
Using 3 trees, train accuracy: 99.2%, test accuracy: 97.8%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gradient_boosting_3.svgz)
- `python3 gradient_boosting.py --dataset=digits --trees=3 --max_depth=2 --learning_rate=0.5`
```
Using 1 trees, train accuracy: 79.1%, test accuracy: 76.9%
Using 2 trees, train accuracy: 85.7%, test accuracy: 84.4%
Using 3 trees, train accuracy: 91.3%, test accuracy: 87.8%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gradient_boosting_4.svgz)
- `python3 gradient_boosting.py --dataset=breast_cancer --trees=3 --max_depth=2 --learning_rate=0.5 --seed=45`
```
Using 1 trees, train accuracy: 94.6%, test accuracy: 90.2%
Using 2 trees, train accuracy: 96.9%, test accuracy: 95.1%
Using 3 trees, train accuracy: 96.9%, test accuracy: 93.7%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/gradient_boosting_5.svgz)
#### Tests End:
