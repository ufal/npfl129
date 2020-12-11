### Assignment: gradient_boosting
#### Date: Deadline: Jan 05, 23:59
#### Points: 6 points
#### Examples: gradient_boosting_examples

Using the [gradient_boosting.py](https://github.com/ufal/npfl129/tree/master/labs/10/gradient_boosting.py)
template, train gradient boosted decision tree forest for classification.

#### Examples Start: gradient_boosting_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=1 --learning_rate=0.3`
```
Using 1 trees, train accuracy: 91.2%, test accuracy: 73.8%
Using 2 trees, train accuracy: 96.3%, test accuracy: 90.5%
Using 3 trees, train accuracy: 97.1%, test accuracy: 95.2%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/gradient_boosting_1.svgz)
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=2 --learning_rate=0.3`
```
Using 1 trees, train accuracy: 97.1%, test accuracy: 83.3%
Using 2 trees, train accuracy: 97.1%, test accuracy: 90.5%
Using 3 trees, train accuracy: 98.5%, test accuracy: 97.6%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/gradient_boosting_2.svgz)
- `python3 gradient_boosting.py --dataset=wine --trees=3 --max_depth=2 --l2=0.5 --learning_rate=0.3`
```
Using 1 trees, train accuracy: 96.3%, test accuracy: 83.3%
Using 2 trees, train accuracy: 98.5%, test accuracy: 97.6%
Using 3 trees, train accuracy: 98.5%, test accuracy: 100.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/gradient_boosting_3.svgz)
- `python3 gradient_boosting.py --dataset=digits --trees=3 --max_depth=2 --learning_rate=0.5`
```
Using 1 trees, train accuracy: 79.4%, test accuracy: 76.2%
Using 2 trees, train accuracy: 86.8%, test accuracy: 81.0%
Using 3 trees, train accuracy: 90.3%, test accuracy: 83.3%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/gradient_boosting_4.svgz)
- `python3 gradient_boosting.py --dataset=breast_cancer --trees=3 --max_depth=2 --learning_rate=0.5`
```
Using 1 trees, train accuracy: 94.3%, test accuracy: 97.6%
Using 2 trees, train accuracy: 96.0%, test accuracy: 97.6%
Using 3 trees, train accuracy: 96.6%, test accuracy: 100.0%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/gradient_boosting_5.svgz)
#### Examples End:
