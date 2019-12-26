### Assignment: gaussian_mixture
#### Date: Deadline: Jan 12, 23:59
#### Points: 4 points
#### Examples: gaussian_mixture_examples

Cluster given input by fitting a Gaussian mixture using the
[gaussian_mixture.py](https://github.com/ufal/npfl129/tree/master/labs/09/gaussian_mixture.py)
template. After every iteration, print out the current negative
log likelihood of the model.

#### Examples Start: gaussian_mixture_examples
- `--clusters=3 --examples 90 --iterations 8 --seed 44`
```
Loss after iteration 1: 387.6
Loss after iteration 2: 384.5
Loss after iteration 3: 382.0
Loss after iteration 4: 379.5
Loss after iteration 5: 376.8
Loss after iteration 6: 373.6
Loss after iteration 7: 367.3
Loss after iteration 8: 358.7
```
![Gaussian Mixture visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gaussian_mixture_1.svg)
- `--clusters=5 --examples 135 --iterations 10 --seed 44`
```
Loss after iteration 1: 620.5
Loss after iteration 2: 612.4
Loss after iteration 3: 608.8
Loss after iteration 4: 606.7
Loss after iteration 5: 605.1
Loss after iteration 6: 603.6
Loss after iteration 7: 602.1
Loss after iteration 8: 600.5
Loss after iteration 9: 599.0
Loss after iteration 10: 597.2
```
![Gaussian Mixture visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/1920/tasks/figures/gaussian_mixture_2.svg)
#### Examples End:
