### Assignment: mlp_classification_sgd
#### Date: Deadline: Nov 8, 23:59
#### Points: 6 points
#### Examples: mlp_classification_sgd_examples
#### Tests: mlp_classification_sgd_tests

Starting with the [mlp_classification_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/04/mlp_classification_sgd.py),
implement minibatch SGD for multilayer perceptron classification.

#### Examples Start: mlp_classification_sgd_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 mlp_classification_sgd.py --epochs=10 --batch_size=10 --hidden_layer=20`
```
After epoch 1: train acc 79.7%, test acc 80.2%
After epoch 2: train acc 91.9%, test acc 88.3%
After epoch 3: train acc 92.4%, test acc 90.0%
After epoch 4: train acc 96.1%, test acc 93.1%
After epoch 5: train acc 95.3%, test acc 93.1%
After epoch 6: train acc 96.6%, test acc 93.9%
After epoch 7: train acc 97.3%, test acc 94.2%
After epoch 8: train acc 98.2%, test acc 94.9%
After epoch 9: train acc 98.1%, test acc 95.7%
After epoch 10: train acc 97.4%, test acc 95.1%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  -0.07 0.12 0.33 -0.21 -0.16 -0.13 0.02 -0.14 0.01 -0.12 -0.02 -0.04 0.02 0.02 0.05 -0.07 -0.07 -0.08 0.02 0.05 ...
  -0.00 -0.00 0.00 -0.00 0.00 0.00 -0.00 0.00 0.00 -0.00 0.00 0.00 0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 0.00 ...
  0.02 -0.01 0.01 -0.03 0.02 -0.01 0.00 0.01 0.01 -0.01 ...
```
- `python3 mlp_classification_sgd.py --epochs=10 --batch_size=10 --hidden_layer=50`
```
After epoch 1: train acc 91.1%, test acc 89.2%
After epoch 2: train acc 95.9%, test acc 93.5%
After epoch 3: train acc 96.5%, test acc 95.2%
After epoch 4: train acc 96.1%, test acc 94.5%
After epoch 5: train acc 96.3%, test acc 93.5%
After epoch 6: train acc 98.3%, test acc 96.2%
After epoch 7: train acc 98.4%, test acc 96.4%
After epoch 8: train acc 98.3%, test acc 95.7%
After epoch 9: train acc 99.1%, test acc 97.4%
After epoch 10: train acc 98.8%, test acc 97.4%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 0.10 -0.16 0.02 0.13 0.04 0.14 -0.01 0.05 -0.07 -0.08 0.02 -0.16 0.17 -0.19 0.00 -0.17 -0.20 0.10 0.26 ...
  0.00 0.00 -0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 -0.00 -0.00 -0.00 0.00 0.00 0.00 -0.00 -0.00 0.00 -0.00 -0.00 ...
  0.01 -0.00 -0.00 0.00 0.00 0.00 -0.01 0.00 -0.00 -0.00 ...
```
- `python3 mlp_classification_sgd.py --epochs=10 --batch_size=10 --hidden_layer=200`
```
After epoch 1: train acc 95.4%, test acc 93.0%
After epoch 2: train acc 97.9%, test acc 96.6%
After epoch 3: train acc 98.8%, test acc 96.9%
After epoch 4: train acc 98.0%, test acc 95.4%
After epoch 5: train acc 99.6%, test acc 97.7%
After epoch 6: train acc 99.7%, test acc 98.0%
After epoch 7: train acc 97.4%, test acc 95.4%
After epoch 8: train acc 99.7%, test acc 97.5%
After epoch 9: train acc 99.8%, test acc 97.9%
After epoch 10: train acc 99.9%, test acc 97.9%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 -0.09 0.04 -0.09 0.06 0.06 -0.05 -0.04 -0.00 0.02 -0.04 0.02 -0.04 -0.09 -0.10 -0.09 0.06 0.09 -0.01 0.01 ...
  0.00 0.00 0.00 -0.00 0.00 -0.00 -0.00 -0.00 0.00 0.00 0.00 -0.00 0.00 0.00 -0.00 -0.00 0.00 0.00 -0.00 0.00 ...
  -0.00 -0.01 -0.00 -0.00 0.00 -0.00 -0.00 0.00 0.01 0.00 ...
```
#### Examples End:
#### Tests Start: mlp_classification_sgd_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 mlp_classification_sgd.py --epochs=3 --batch_size=10 --hidden_layer=20`
```
After epoch 1: train acc 79.7%, test acc 80.2%
After epoch 2: train acc 91.9%, test acc 88.3%
After epoch 3: train acc 92.4%, test acc 90.0%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  -0.09 0.07 0.21 -0.16 -0.15 -0.07 0.01 -0.09 0.05 -0.11 -0.02 -0.04 0.02 0.03 0.05 -0.07 -0.07 -0.08 0.02 0.05 ...
  -0.00 -0.00 0.00 0.00 0.00 0.00 -0.00 0.00 0.00 -0.00 0.00 -0.00 0.00 0.00 0.00 0.00 -0.00 0.00 0.00 0.00 ...
  0.01 -0.01 0.01 -0.02 0.01 -0.01 0.00 0.01 0.01 -0.01 ...
```
- `python3 mlp_classification_sgd.py --epochs=3 --batch_size=10 --hidden_layer=50`
```
After epoch 1: train acc 91.1%, test acc 89.2%
After epoch 2: train acc 95.9%, test acc 93.5%
After epoch 3: train acc 96.5%, test acc 95.2%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 0.06 -0.13 0.04 0.11 0.04 0.13 0.01 0.05 -0.05 -0.07 0.02 -0.12 0.14 -0.17 -0.03 -0.13 -0.18 0.07 0.19 ...
  0.00 0.00 -0.00 0.00 -0.00 0.00 -0.00 0.00 0.00 -0.00 -0.00 -0.00 0.00 0.00 0.00 0.00 -0.00 0.00 0.00 -0.00 ...
  0.01 0.00 -0.00 0.00 -0.00 0.00 -0.01 -0.00 -0.00 0.00 ...
```
- `python3 mlp_classification_sgd.py --epochs=3 --batch_size=10 --hidden_layer=200`
```
After epoch 1: train acc 95.4%, test acc 93.0%
After epoch 2: train acc 97.9%, test acc 96.6%
After epoch 3: train acc 98.8%, test acc 96.9%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 -0.09 0.04 -0.09 0.06 0.06 -0.05 -0.04 -0.00 0.02 -0.04 0.02 -0.04 -0.09 -0.10 -0.08 0.06 0.09 -0.01 0.00 ...
  0.00 0.00 -0.00 -0.00 0.00 -0.00 0.00 -0.00 0.00 0.00 -0.00 -0.00 -0.00 0.00 -0.00 -0.00 0.00 0.00 -0.00 0.00 ...
  -0.00 -0.00 -0.00 -0.00 0.00 -0.00 -0.00 0.00 0.00 0.00 ...
```
- `python3 mlp_classification_sgd.py --epochs=1 --batch_size=1  --hidden_layer=200 --test_size=1597`
```
After epoch 1: train acc 74.0%, test acc 68.7%
Learned parameters:
  -0.03 0.09 0.05 0.02 -0.07 -0.07 -0.09 0.07 0.02 0.04 -0.10 0.09 0.07 -0.06 -0.06 -0.06 -0.04 0.00 -0.01 -0.04 ...
  0.01 -0.09 0.04 -0.09 0.06 0.06 -0.05 -0.04 -0.00 0.02 -0.04 0.02 -0.04 -0.09 -0.10 -0.08 0.06 0.09 -0.01 0.00 ...
  0.00 0.00 -0.00 -0.00 -0.00 -0.00 -0.00 -0.00 0.00 -0.00 -0.00 -0.00 -0.00 0.00 -0.00 -0.00 -0.00 -0.00 -0.00 0.00 ...
  -0.02 0.01 -0.00 -0.02 0.02 -0.00 0.00 -0.02 0.02 0.01 ...
```
#### Tests End:
