### Assignment: kernel_approximation
#### Date: Deadline: ~~Dec 08~~ Dec 15, 23:59
#### Points: 3 points
#### Examples: kernel_approximation_examples

Using the [kernel_approximation.py](https://github.com/ufal/npfl129/tree/master/labs/08/kernel_approximation.py)
template, implement the RFF and Nyström approximations of an RBF kernel.

#### Examples Start: kernel_approximation_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 kernel_approximation.py --original`
```
Test set accuracy: 89.64%
```
- `python3 kernel_approximation.py --original --svm`
```
Test set accuracy: 94.68%
```
- `python3 kernel_approximation.py --rff=300`
```
Test set accuracy: 84.36%
```
- `python3 kernel_approximation.py --rff=800`
```
Test set accuracy: 91.64%
```
- `python3 kernel_approximation.py --nystroem=100`
```
Test set accuracy: 90.80%
```
- `python3 kernel_approximation.py --nystroem=300`
```
Test set accuracy: 93.28%
```
#### Examples End:
