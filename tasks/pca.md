### Assignment: pca
#### Date: Deadline: Feb 28, 23:59
#### Points: 3 points
#### Examples: pca_examples

Using the [pca.py](https://github.com/ufal/npfl129/tree/master/labs/11/pca.py)
template, implement the PCA computation with both
- power iteration algorithm,
- SVD decomposition.

#### Examples Start: pca_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 pca.py --max_iter=20`
```
Test set accuracy: 90.76%
```
- `python3 pca.py --max_iter=20 --pca=1`
```
Test set accuracy: 30.64%
```
- `python3 pca.py --max_iter=20 --pca=5`
```
Test set accuracy: 68.96%
```
- `python3 pca.py --max_iter=20 --pca=10`
```
Test set accuracy: 80.44%
```
- `python3 pca.py --max_iter=20 --pca=20`
```
Test set accuracy: 87.76%
```
- `python3 pca.py --max_iter=20 --pca=50`
```
Test set accuracy: 89.92%
```
- `python3 pca.py --max_iter=20 --pca=100`
```
Test set accuracy: 90.68%
```
- `python3 pca.py --max_iter=20 --pca=200`
```
Test set accuracy: 90.88%
```
#### Examples End:
