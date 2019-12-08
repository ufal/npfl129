### Assignment: svm_multiclass
#### Date: Deadline: Dec 22, 23:59
#### Points: 3 points
#### Examples: svm_multiclass_examples

Extend a solution to the `smo_algorithm` assignment to handle multiclass
classification, using the [svm_multiclass.py](https://github.com/ufal/npfl129/tree/master/labs/07/svm_multiclass.py)
template.

#### Examples Start: svm_multiclass_examples
- `--classes=4 --C=1 --kernel=linear --test_size=640 --num_passes=5 --seed=42 --tolerance=0.0001`
```
96.72
```
- `--classes=3 --C=1 --kernel=rbf --kernel_gamma=1 --test_size=339 --num_passes=5 --seed=42 --tolerance=0.0001`
```
99.12
```
- `--classes=5 --C=1 --kernel=poly --kernel_degree=3 --kernel_gamma=1 --test_size=701 --num_passes=5 --seed=42 --tolerance=0.0001`
```
98.72
```
- `--classes=10 --C=2 --kernel=rbf --kernel_gamma=1 --test_size=1547 --num_passes=5 --seed=42 --tolerance=0.0001`
```
91.73
```
#### Examples End:
