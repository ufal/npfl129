### Assignment: k_nearest_neighbors
#### Date: Deadline: ~~Nov 14~~ Nov 21, 7:59 a.m.
#### Points: 3 points
#### Tests: k_nearest_neighbors_tests

Starting with the [k_nearest_neighbors.py](https://github.com/ufal/npfl129/tree/master/labs/05/k_nearest_neighbors.py),
implement k-nearest neighbors algorithm for classifying MNIST, without using the
`sklearn.neighbors` module or `scipy.spatial` module in any way.

#### Tests Start: k_nearest_neighbors_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=100`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 73.60%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_1.svgz)
- `python3 k_nearest_neighbors.py --k=3 --p=2 --weights=uniform --test_size=500 --train_size=100`
```
K-nn accuracy for 3 nearest neighbors, L_2 metric, uniform weights: 66.80%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_2.svgz)
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 90.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_3.svgz)
- `python3 k_nearest_neighbors.py --k=5 --p=2 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 5 nearest neighbors, L_2 metric, uniform weights: 88.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_4.svgz)
- `python3 k_nearest_neighbors.py --k=5 --p=1 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 5 nearest neighbors, L_1 metric, uniform weights: 87.00%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_5.svgz)
- `python3 k_nearest_neighbors.py --k=5 --p=3 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 5 nearest neighbors, L_3 metric, uniform weights: 89.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_6.svgz)
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 94.40%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_7.svgz)
- `python3 k_nearest_neighbors.py --k=9 --p=2 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 9 nearest neighbors, L_2 metric, uniform weights: 92.80%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_8.svgz)
- `python3 k_nearest_neighbors.py --k=9 --p=2 --weights=inverse --test_size=500 --train_size=5000`
```
K-nn accuracy for 9 nearest neighbors, L_2 metric, inverse weights: 93.00%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_9.svgz)
- `python3 k_nearest_neighbors.py --k=9 --p=2 --weights=softmax --test_size=500 --train_size=5000`
```
K-nn accuracy for 9 nearest neighbors, L_2 metric, softmax weights: 94.00%
```
![Test visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2223/tasks/figures/k_nearest_neighbors_10.svgz)
#### Tests End:
