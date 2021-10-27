### Assignment: logistic_regression_sgd
#### Date: Deadline: Nov 01, 23:59
#### Points: 5 points
#### Tests: logistic_regression_sgd_tests

Starting with the [logistic_regression_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/03/logistic_regression_sgd.py),
implement minibatch SGD for logistic regression.

#### Tests Start: logistic_regression_sgd_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 logistic_regression_sgd.py --data_size=100 --batch_size=10 --epochs=9 --learning_rate=0.5`
```
After epoch 1: train loss 0.3259 acc 94.0%, test loss 0.3301 acc 96.0%
After epoch 2: train loss 0.2321 acc 96.0%, test loss 0.2385 acc 98.0%
After epoch 3: train loss 0.1877 acc 98.0%, test loss 0.1949 acc 98.0%
After epoch 4: train loss 0.1612 acc 98.0%, test loss 0.1689 acc 98.0%
After epoch 5: train loss 0.1435 acc 98.0%, test loss 0.1517 acc 98.0%
After epoch 6: train loss 0.1307 acc 98.0%, test loss 0.1396 acc 98.0%
After epoch 7: train loss 0.1208 acc 98.0%, test loss 0.1304 acc 96.0%
After epoch 8: train loss 0.1129 acc 98.0%, test loss 0.1230 acc 96.0%
After epoch 9: train loss 0.1065 acc 98.0%, test loss 0.1170 acc 96.0%
Learned weights 2.77 -0.60 0.12
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_1.svgz)
- `python3 logistic_regression_sgd.py --data_size=95 --test_size=45 --batch_size=5 --epochs=9 --learning_rate=0.5`
```
After epoch 1: train loss 0.2429 acc 96.0%, test loss 0.3187 acc 93.3%
After epoch 2: train loss 0.1853 acc 96.0%, test loss 0.2724 acc 93.3%
After epoch 3: train loss 0.1590 acc 96.0%, test loss 0.2525 acc 93.3%
After epoch 4: train loss 0.1428 acc 96.0%, test loss 0.2411 acc 93.3%
After epoch 5: train loss 0.1313 acc 98.0%, test loss 0.2335 acc 93.3%
After epoch 6: train loss 0.1225 acc 96.0%, test loss 0.2258 acc 93.3%
After epoch 7: train loss 0.1159 acc 96.0%, test loss 0.2220 acc 93.3%
After epoch 8: train loss 0.1105 acc 96.0%, test loss 0.2187 acc 93.3%
After epoch 9: train loss 0.1061 acc 96.0%, test loss 0.2163 acc 93.3%
Learned weights -0.61 3.61 0.12
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_2.svgz)
- `python3 logistic_regression_sgd.py --data_size=95 --test_size=45 --batch_size=1 --epochs=9 --learning_rate=0.7`
```
After epoch 1: train loss 0.1141 acc 96.0%, test loss 0.2268 acc 93.3%
After epoch 2: train loss 0.0867 acc 96.0%, test loss 0.2150 acc 91.1%
After epoch 3: train loss 0.0797 acc 98.0%, test loss 0.2320 acc 88.9%
After epoch 4: train loss 0.0753 acc 96.0%, test loss 0.2224 acc 88.9%
After epoch 5: train loss 0.0692 acc 96.0%, test loss 0.2154 acc 88.9%
After epoch 6: train loss 0.0749 acc 98.0%, test loss 0.2458 acc 88.9%
After epoch 7: train loss 0.0638 acc 96.0%, test loss 0.2190 acc 88.9%
After epoch 8: train loss 0.0644 acc 98.0%, test loss 0.2341 acc 88.9%
After epoch 9: train loss 0.0663 acc 98.0%, test loss 0.2490 acc 88.9%
Learned weights -1.07 7.33 -0.40
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_3.svgz)
#### Tests End:
