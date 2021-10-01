### Assignment: svm_multiclass
#### Date: Deadline: Dec 01, 23:59
#### Points: 3 points
#### Examples: svm_multiclass_examples

Extend your solution to the `smo_algorithm` assignment to handle multiclass
classification, using the [svm_multiclass.py](https://github.com/ufal/npfl129/tree/past-2021/labs/07/svm_multiclass.py)
template.

#### Examples Start: svm_multiclass_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 svm_multiclass.py --classes=5 --kernel=poly --kernel_degree=2 --test_size=0.8`
```
Training classes 0 and 1
Training finished after iteration 71, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Training finished after iteration 88, train acc 100.0%, test acc 99.7%
Training classes 0 and 3
Training finished after iteration 57, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Iteration 100, train acc 100.0%, test acc 100.0%
Training finished after iteration 122, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Iteration 100, train acc 100.0%, test acc 98.2%
Training finished after iteration 108, train acc 100.0%, test acc 98.2%
Training classes 1 and 3
Training finished after iteration 67, train acc 100.0%, test acc 99.7%
Training classes 1 and 4
Iteration 100, train acc 100.0%, test acc 98.9%
Training finished after iteration 135, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Training finished after iteration 84, train acc 100.0%, test acc 98.0%
Training classes 2 and 4
Training finished after iteration 71, train acc 100.0%, test acc 98.3%
Training classes 3 and 4
Training finished after iteration 75, train acc 100.0%, test acc 98.6%
Test set accuracy: 97.92%
```
- `python3 svm_multiclass.py --classes=5 --kernel=poly --kernel_degree=3 --test_size=0.8`
```
Training classes 0 and 1
Training finished after iteration 40, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Training finished after iteration 29, train acc 100.0%, test acc 99.3%
Training classes 0 and 3
Training finished after iteration 18, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Training finished after iteration 31, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Training finished after iteration 36, train acc 100.0%, test acc 98.2%
Training classes 1 and 3
Training finished after iteration 18, train acc 100.0%, test acc 99.3%
Training classes 1 and 4
Training finished after iteration 41, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Training finished after iteration 44, train acc 100.0%, test acc 97.6%
Training classes 2 and 4
Training finished after iteration 28, train acc 100.0%, test acc 98.3%
Training classes 3 and 4
Training finished after iteration 19, train acc 100.0%, test acc 99.0%
Test set accuracy: 97.64%
```
- `python3 svm_multiclass.py --classes=5 --kernel=poly --kernel_degree=3 --kernel_gamma=0.5 --test_size=0.8`
```
Training classes 0 and 1
Training finished after iteration 69, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Training finished after iteration 41, train acc 100.0%, test acc 99.3%
Training classes 0 and 3
Training finished after iteration 57, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Training finished after iteration 80, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Training finished after iteration 96, train acc 100.0%, test acc 98.2%
Training classes 1 and 3
Training finished after iteration 62, train acc 100.0%, test acc 99.7%
Training classes 1 and 4
Training finished after iteration 76, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Training finished after iteration 98, train acc 100.0%, test acc 98.0%
Training classes 2 and 4
Training finished after iteration 47, train acc 100.0%, test acc 98.3%
Training classes 3 and 4
Training finished after iteration 51, train acc 100.0%, test acc 98.6%
Test set accuracy: 98.06%
```
- `python3 svm_multiclass.py --classes=5 --kernel=rbf --kernel_gamma=1 --test_size=0.8`
```
Training classes 0 and 1
Training finished after iteration 51, train acc 100.0%, test acc 97.9%
Training classes 0 and 2
Training finished after iteration 50, train acc 100.0%, test acc 99.3%
Training classes 0 and 3
Training finished after iteration 43, train acc 100.0%, test acc 99.3%
Training classes 0 and 4
Training finished after iteration 51, train acc 100.0%, test acc 95.5%
Training classes 1 and 2
Training finished after iteration 55, train acc 100.0%, test acc 92.6%
Training classes 1 and 3
Training finished after iteration 48, train acc 100.0%, test acc 97.2%
Training classes 1 and 4
Training finished after iteration 45, train acc 100.0%, test acc 99.6%
Training classes 2 and 3
Training finished after iteration 40, train acc 100.0%, test acc 99.3%
Training classes 2 and 4
Training finished after iteration 42, train acc 100.0%, test acc 90.9%
Training classes 3 and 4
Training finished after iteration 41, train acc 100.0%, test acc 94.5%
Test set accuracy: 92.23%
```
- `python3 svm_multiclass.py --classes=5 --kernel=rbf --kernel_gamma=0.1 --C=3 --test_size=0.8`
```
Training classes 0 and 1
Iteration 100, train acc 100.0%, test acc 100.0%
Training finished after iteration 185, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Iteration 100, train acc 100.0%, test acc 99.7%
Training finished after iteration 128, train acc 100.0%, test acc 99.7%
Training classes 0 and 3
Iteration 100, train acc 100.0%, test acc 100.0%
Training finished after iteration 189, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Iteration 100, train acc 100.0%, test acc 100.0%
Training finished after iteration 140, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Iteration 100, train acc 100.0%, test acc 97.9%
Training finished after iteration 168, train acc 100.0%, test acc 97.9%
Training classes 1 and 3
Iteration 100, train acc 100.0%, test acc 99.7%
Training finished after iteration 114, train acc 100.0%, test acc 99.7%
Training classes 1 and 4
Iteration 100, train acc 100.0%, test acc 98.9%
Training finished after iteration 141, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Iteration 100, train acc 100.0%, test acc 98.3%
Training finished after iteration 129, train acc 100.0%, test acc 98.3%
Training classes 2 and 4
Iteration 100, train acc 100.0%, test acc 99.0%
Training finished after iteration 106, train acc 100.0%, test acc 99.0%
Training classes 3 and 4
Iteration 100, train acc 100.0%, test acc 99.3%
Training finished after iteration 175, train acc 100.0%, test acc 99.3%
Test set accuracy: 97.92%
```
#### Examples End:
