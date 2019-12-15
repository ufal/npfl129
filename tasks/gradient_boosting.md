### Assignment: gradient_boosting
#### Date: Deadline: Jan 05, 23:59
#### Points: 5 points
#### Examples: gradient_boosting_example

Using the [gradient_boosting.py](https://github.com/ufal/npfl129/tree/master/labs/08/gradient_boosting.py)
template, train gradient boosted decision tree forest for classification.

#### Examples Start: gradient_boosting_example
- `--max_depth=1 --learning_rate=0.2 --n_estimators=1`
```
Train acc: 93.4%
Test acc: 92.9%
```
![Gradient boosted trees visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gradient_boosting_1.svg)
- `--max_depth=1 --learning_rate=0.2 --n_estimators=2`
```
Train acc: 96.3%
Test acc: 95.2%
```
![Gradient boosted trees visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gradient_boosting_2.svg)
- `--max_depth=1 --learning_rate=0.2 --n_estimators=3`
```
Train acc: 99.3%
Test acc: 97.6%
```
![Gradient boosted trees visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gradient_boosting_3.svg)
- `--max_depth=2 --learning_rate=0.5 --l2=0.1 --n_estimators=3`
```
Train acc: 100.0%
Test acc: 100.0%
```
![Gradient boosted trees visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gradient_boosting_4.svg)
#### Examples End:
