### Assignment: pca
#### Date: Deadline: Jan 7, 22:00
#### Points: 3 points
#### Tests: pca_tests
#### Examples: pca_examples

Using the [pca.py](https://github.com/ufal/npfl129/tree/master/labs/11/pca.py)
template, implement the PCA computation with both
- power iteration algorithm,
- singular value decomposition (SVD).

#### Tests Start: pca_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 pca.py --max_iter=5`
```
Test set accuracy: 90.48%
```

2. `python3 pca.py --max_iter=5 --pca=1`
```
Test set accuracy: 30.36%
```

3. `python3 pca.py --max_iter=5 --pca=5`
```
Test set accuracy: 68.76%
```

4. `python3 pca.py --max_iter=5 --pca=10`
```
Test set accuracy: 80.32%
```

5. `python3 pca.py --max_iter=5 --pca=20`
```
Test set accuracy: 87.56%
```

6. `python3 pca.py --max_iter=5 --pca=50`
```
Test set accuracy: 89.88%
```

7. `python3 pca.py --max_iter=5 --pca=100`
```
Test set accuracy: 90.32%
```

8. `python3 pca.py --max_iter=5 --pca=200`
```
Test set accuracy: 90.28%
```
#### Tests End:
#### Examples Start: pca_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

- `python3 pca.py --max_iter=1000 --solver=lbfgs`
```
Test set accuracy: 89.88%
```

- `python3 pca.py --max_iter=1000 --pca=1 --solver=lbfgs`
```
Test set accuracy: 30.84%
```

- `python3 pca.py --max_iter=1000 --pca=5 --solver=lbfgs`
```
Test set accuracy: 68.96%
```

- `python3 pca.py --max_iter=1000 --pca=10 --solver=lbfgs`
```
Test set accuracy: 80.52%
```

- `python3 pca.py --max_iter=1000 --pca=20 --solver=lbfgs`
```
Test set accuracy: 87.76%
```

- `python3 pca.py --max_iter=1000 --pca=50 --solver=lbfgs`
```
Test set accuracy: 89.92%
```

- `python3 pca.py --max_iter=1000 --pca=100 --solver=lbfgs`
```
Test set accuracy: 90.08%
```

- `python3 pca.py --max_iter=1000 --pca=200 --solver=lbfgs`
```
Test set accuracy: 89.80%
```
#### Examples End:
