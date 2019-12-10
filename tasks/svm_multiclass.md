### Assignment: svm_multiclass
#### Date: Deadline: Dec 22, 23:59
#### Points: 3 points
#### Examples: svm_multiclass_examples

Extend a solution to the `smo_algorithm` assignment to handle multiclass
classification, using the [svm_multiclass.py](https://github.com/ufal/npfl129/tree/master/labs/07/svm_multiclass.py)
template.

**<span class="text-danger">Dec 10: A new argument `args.max_num_passes` was
added to the template, please update.</span>**


#### Examples Start: svm_multiclass_examples
- `--classes=4 --C=1 --kernel=linear --test_size=640 --max_num_passes=5 --seed=42 --tolerance=0.0001`
```
98.12
```
- `--classes=3 --C=1 --kernel=rbf --kernel_gamma=1 --test_size=339 --max_num_passes=5 --seed=42 --tolerance=0.0001`
```
99.12
```
- `--classes=5 --C=1 --kernel=poly --kernel_degree=3 --kernel_gamma=1 --test_size=701 --max_num_passes=1 --seed=42 --tolerance=0.0001`
```
93.87
```
- `--classes=10 --C=2 --kernel=rbf --kernel_gamma=1 --test_size=1547 --max_num_passes=5 --seed=42 --tolerance=0.0001`
```
90.56
```
#### Examples End:
