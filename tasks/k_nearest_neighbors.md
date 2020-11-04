### Assignment: k_nearest_neighbors
#### Date: Deadline: Nov 17, 23:59
#### Points: 4 points
#### Examples: k_nearest_neighbors_examples

Starting with the [k_nearest_neighbors](https://github.com/ufal/npfl129/tree/master/labs/05/k_nearest_neighbors.py),
implement k-nearest neighbors algoritm for classifying MNIST.

#### Examples Start: k_nearest_neighbors_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=100`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 67.60%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_1.svgz)
- `python3 k_nearest_neighbors.py --k=2 --p=2 --weights=uniform --test_size=500 --train_size=100`
```
K-nn accuracy for 2 nearest neighbors, L_2 metric, uniform weights: 59.80%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_2.svgz)
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 87.40%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_3.svgz)
- `python3 k_nearest_neighbors.py --k=5 --p=2 --weights=uniform --test_size=500 --train_size=1000`
```
K-nn accuracy for 5 nearest neighbors, L_2 metric, uniform weights: 88.80%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_4.svgz)
- `python3 k_nearest_neighbors.py --k=1 --p=2 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 1 nearest neighbors, L_2 metric, uniform weights: 94.00%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_5.svgz)
- `python3 k_nearest_neighbors.py --k=10 --p=2 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 10 nearest neighbors, L_2 metric, uniform weights: 94.00%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_6.svgz)
- `python3 k_nearest_neighbors.py --k=10 --p=1 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 10 nearest neighbors, L_1 metric, uniform weights: 92.40%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_7.svgz)
- `python3 k_nearest_neighbors.py --k=10 --p=3 --weights=uniform --test_size=500 --train_size=5000`
```
K-nn accuracy for 10 nearest neighbors, L_3 metric, uniform weights: 94.20%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_8.svgz)
- `python3 k_nearest_neighbors.py --k=10 --p=2 --weights=inverse --test_size=500 --train_size=5000`
```
K-nn accuracy for 10 nearest neighbors, L_2 metric, inverse weights: 94.20%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_9.svgz)
- `python3 k_nearest_neighbors.py --k=10 --p=2 --weights=softmax --test_size=500 --train_size=5000`
```
K-nn accuracy for 10 nearest neighbors, L_2 metric, softmax weights: 94.80%
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/k_nearest_neighbors_10.svgz)
#### Examples End:
