### Assignment: mlp_classification_sgd
#### Date: Deadline: Nov 10, 23:59
#### Points: 6 points
#### Examples: mlp_classification_sgd_examples

Starting with the [mlp_classification_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/04/mlp_classification_sgd.py),
implement minibatch SGD for multilayer perceptron classification.

#### Examples Start: mlp_classification_sgd_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 mlp_classification_sgd.py --iterations=10 --batch_size=10 --hidden_layer=20`
```
After iteration 1: train acc 78.1%, test acc 76.3%
After iteration 2: train acc 91.7%, test acc 88.2%
After iteration 3: train acc 94.8%, test acc 91.8%
After iteration 4: train acc 94.7%, test acc 91.6%
After iteration 5: train acc 96.4%, test acc 94.1%
After iteration 6: train acc 96.3%, test acc 92.0%
After iteration 7: train acc 98.2%, test acc 95.0%
After iteration 8: train acc 97.8%, test acc 94.9%
After iteration 9: train acc 98.3%, test acc 95.7%
After iteration 10: train acc 97.6%, test acc 94.4%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  -0.10 0.05 0.32 -0.02 -0.29 0.02 -0.04 -0.17 -0.02 -0.09 0.14 0.22 0.09 -0.11 -0.03 -0.13 -0.17 -0.09 -0.07 0.02 ...
  -0.00 0.00 0.00 0.00 0.00 0.00 -0.00 0.01 0.01 -0.00 0.00 -0.00 0.00 0.00 0.00 0.00 -0.00 0.00 0.00 0.00 ...
  0.01 -0.02 0.01 -0.01 0.02 -0.00 0.00 0.01 0.01 -0.01 ...
```
- `python3 mlp_classification_sgd.py --iterations=10 --batch_size=10 --hidden_layer=50`
```
After iteration 1: train acc 89.9%, test acc 87.6%
After iteration 2: train acc 94.2%, test acc 92.1%
After iteration 3: train acc 97.2%, test acc 93.1%
After iteration 4: train acc 97.0%, test acc 92.8%
After iteration 5: train acc 98.3%, test acc 96.4%
After iteration 6: train acc 98.4%, test acc 95.5%
After iteration 7: train acc 98.9%, test acc 96.4%
After iteration 8: train acc 98.1%, test acc 93.5%
After iteration 9: train acc 99.2%, test acc 96.7%
After iteration 10: train acc 99.5%, test acc 95.9%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  -0.03 0.02 -0.16 0.04 0.16 0.04 0.15 0.03 0.08 -0.07 -0.09 0.04 -0.17 0.16 -0.18 -0.03 -0.14 -0.17 0.09 0.24 ...
  0.00 -0.00 -0.00 0.00 -0.00 -0.00 -0.00 0.00 0.00 -0.00 -0.00 -0.00 0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 0.00 ...
  0.01 -0.01 -0.00 0.01 -0.00 0.01 -0.01 0.00 -0.00 -0.00 ...
```
- `python3 mlp_classification_sgd.py --iterations=10 --batch_size=10 --hidden_layer=200`
```
After iteration 1: train acc 96.0%, test acc 92.8%
After iteration 2: train acc 97.7%, test acc 95.1%
After iteration 3: train acc 98.2%, test acc 94.4%
After iteration 4: train acc 99.3%, test acc 97.0%
After iteration 5: train acc 99.3%, test acc 96.9%
After iteration 6: train acc 99.7%, test acc 96.1%
After iteration 7: train acc 99.9%, test acc 97.4%
After iteration 8: train acc 99.7%, test acc 97.0%
After iteration 9: train acc 100.0%, test acc 97.1%
After iteration 10: train acc 100.0%, test acc 97.6%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 -0.09 0.04 -0.09 0.06 0.06 -0.05 -0.04 -0.00 0.02 -0.04 0.02 -0.04 -0.09 -0.10 -0.08 0.06 0.09 -0.01 0.01 ...
  0.00 0.00 0.00 -0.00 0.00 -0.00 0.00 -0.00 0.00 0.00 0.00 0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 -0.00 0.00 ...
  -0.00 -0.00 0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 0.00 ...
```
- `python3 mlp_classification_sgd.py --iterations=10 --batch_size=1  --hidden_layer=200 --test_size=1597`
```
After iteration 1: train acc 88.0%, test acc 78.3%
After iteration 2: train acc 83.0%, test acc 75.6%
After iteration 3: train acc 91.5%, test acc 82.7%
After iteration 4: train acc 90.5%, test acc 85.3%
After iteration 5: train acc 74.5%, test acc 69.0%
After iteration 6: train acc 85.0%, test acc 78.8%
After iteration 7: train acc 98.0%, test acc 89.4%
After iteration 8: train acc 92.0%, test acc 84.7%
After iteration 9: train acc 99.5%, test acc 90.7%
After iteration 10: train acc 97.5%, test acc 91.7%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 -0.09 0.04 -0.09 0.06 0.06 -0.05 -0.04 -0.00 0.02 -0.05 -0.02 -0.06 -0.13 -0.11 -0.10 0.05 0.08 0.10 0.04 ...
  0.00 -0.00 -0.00 -0.00 -0.00 -0.00 -0.00 -0.01 0.00 -0.00 -0.00 -0.00 -0.00 0.00 -0.00 -0.00 -0.00 -0.00 -0.00 0.00 ...
  -0.03 0.06 -0.06 -0.00 -0.05 -0.04 -0.06 -0.03 0.20 0.02 ...
```
#### Examples End:
