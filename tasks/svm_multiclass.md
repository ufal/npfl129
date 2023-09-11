### Assignment: svm_multiclass
#### Date: Deadline: Nov 28, 7:59 a.m.
#### Points: 3 points
#### Tests: svm_multiclass_tests

Extend your solution to the `smo_algorithm` assignment to handle multiclass
classification, using the [svm_multiclass.py](https://github.com/ufal/npfl129/tree/past-2223/labs/07/svm_multiclass.py)
template.

#### Tests Start: svm_multiclass_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 svm_multiclass.py --max_iterations=20 --classes=5 --kernel=poly --kernel_degree=2 --test_size=0.8`
```
Training classes 0 and 1
Done, iteration 20, support vectors 14, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Done, iteration 20, support vectors 12, train acc 100.0%, test acc 99.7%
Training classes 0 and 3
Done, iteration 20, support vectors 13, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Done, iteration 20, support vectors 22, train acc 100.0%, test acc 98.6%
Training classes 1 and 3
Done, iteration 20, support vectors 20, train acc 100.0%, test acc 99.7%
Training classes 1 and 4
Done, iteration 20, support vectors 21, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Done, iteration 20, support vectors 21, train acc 100.0%, test acc 98.3%
Training classes 2 and 4
Done, iteration 20, support vectors 18, train acc 100.0%, test acc 98.6%
Training classes 3 and 4
Done, iteration 20, support vectors 18, train acc 100.0%, test acc 99.0%
Test set accuracy: 98.06%
```
- `python3 svm_multiclass.py --max_iterations=20 --classes=5 --kernel=poly --kernel_degree=3 --test_size=0.8`
```
Training classes 0 and 1
Done, iteration 20, support vectors 16, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Done, iteration 20, support vectors 14, train acc 100.0%, test acc 99.7%
Training classes 0 and 3
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Done, iteration 20, support vectors 20, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Done, iteration 20, support vectors 21, train acc 100.0%, test acc 98.2%
Training classes 1 and 3
Done, iteration 20, support vectors 24, train acc 100.0%, test acc 99.7%
Training classes 1 and 4
Done, iteration 20, support vectors 25, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Done, iteration 20, support vectors 18, train acc 100.0%, test acc 98.3%
Training classes 2 and 4
Done, iteration 20, support vectors 18, train acc 100.0%, test acc 98.3%
Training classes 3 and 4
Done, iteration 20, support vectors 21, train acc 100.0%, test acc 99.0%
Test set accuracy: 98.20%
```
- `python3 svm_multiclass.py --max_iterations=20 --classes=5 --kernel=poly --kernel_degree=3 --kernel_gamma=0.02 --test_size=0.8`
```
Training classes 0 and 1
Done, iteration 20, support vectors 23, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 99.0%
Training classes 0 and 3
Done, iteration 20, support vectors 20, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Done, iteration 20, support vectors 24, train acc 98.6%, test acc 100.0%
Training classes 1 and 2
Done, iteration 20, support vectors 32, train acc 100.0%, test acc 97.5%
Training classes 1 and 3
Done, iteration 20, support vectors 29, train acc 100.0%, test acc 99.0%
Training classes 1 and 4
Done, iteration 20, support vectors 36, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Done, iteration 20, support vectors 32, train acc 100.0%, test acc 97.3%
Training classes 2 and 4
Done, iteration 20, support vectors 18, train acc 100.0%, test acc 99.0%
Training classes 3 and 4
Done, iteration 20, support vectors 21, train acc 100.0%, test acc 99.3%
Test set accuracy: 96.95%
```
- `python3 svm_multiclass.py --max_iterations=20 --classes=5 --kernel=rbf --kernel_gamma=1 --test_size=0.8`
```
Training classes 0 and 1
Done, iteration 20, support vectors 69, train acc 100.0%, test acc 97.9%
Training classes 0 and 2
Done, iteration 20, support vectors 60, train acc 100.0%, test acc 99.3%
Training classes 0 and 3
Done, iteration 20, support vectors 60, train acc 100.0%, test acc 99.3%
Training classes 0 and 4
Done, iteration 20, support vectors 66, train acc 100.0%, test acc 95.5%
Training classes 1 and 2
Done, iteration 20, support vectors 74, train acc 100.0%, test acc 92.6%
Training classes 1 and 3
Done, iteration 20, support vectors 73, train acc 100.0%, test acc 97.2%
Training classes 1 and 4
Done, iteration 20, support vectors 80, train acc 100.0%, test acc 99.6%
Training classes 2 and 3
Done, iteration 20, support vectors 64, train acc 100.0%, test acc 99.3%
Training classes 2 and 4
Done, iteration 20, support vectors 71, train acc 100.0%, test acc 90.9%
Training classes 3 and 4
Done, iteration 20, support vectors 71, train acc 100.0%, test acc 94.5%
Test set accuracy: 92.23%
```
- `python3 svm_multiclass.py --max_iterations=20 --classes=5 --kernel=rbf --kernel_gamma=0.05 --C=3 --test_size=0.8`
```
Training classes 0 and 1
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 100.0%
Training classes 0 and 2
Done, iteration 20, support vectors 15, train acc 100.0%, test acc 99.7%
Training classes 0 and 3
Done, iteration 20, support vectors 15, train acc 100.0%, test acc 100.0%
Training classes 0 and 4
Done, iteration 20, support vectors 19, train acc 100.0%, test acc 100.0%
Training classes 1 and 2
Done, iteration 20, support vectors 24, train acc 100.0%, test acc 98.6%
Training classes 1 and 3
Done, iteration 20, support vectors 22, train acc 100.0%, test acc 99.3%
Training classes 1 and 4
Done, iteration 20, support vectors 28, train acc 100.0%, test acc 98.9%
Training classes 2 and 3
Done, iteration 20, support vectors 24, train acc 100.0%, test acc 98.6%
Training classes 2 and 4
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 99.0%
Training classes 3 and 4
Done, iteration 20, support vectors 17, train acc 100.0%, test acc 99.0%
Test set accuracy: 98.20%
```
#### Tests End:
