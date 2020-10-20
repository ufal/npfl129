### Assignment: logistic_regression_sgd
#### Date: Deadline: Nov 03, 23:59
#### Points: 5 points
#### Examples: logistic_regression_sgd_examples

Starting with the [logistic_regression_sgd.py](https://github.com/ufal/npfl129/tree/master/labs/03/logistic_regression_sgd.py),
implement minibatch SGD for logistic regression.

#### Examples Start: logistic_regression_sgd_examples
Note that your results may sometimes be slightly different (for example because of varying floating point arithmetic on your CPU).
- `python3 logistic_regression_sgd.py --data_size=100 --batch_size=10 --iterations=9 --learning_rate=0.5`
```
After iteration 1: train loss 0.3464 acc 90.0%, test loss 0.3369 acc 84.0%
After iteration 2: train loss 0.2324 acc 96.0%, test loss 0.2397 acc 92.0%
After iteration 3: train loss 0.1840 acc 94.0%, test loss 0.1952 acc 94.0%
After iteration 4: train loss 0.1566 acc 98.0%, test loss 0.1686 acc 94.0%
After iteration 5: train loss 0.1392 acc 98.0%, test loss 0.1513 acc 96.0%
After iteration 6: train loss 0.1271 acc 98.0%, test loss 0.1394 acc 96.0%
After iteration 7: train loss 0.1178 acc 98.0%, test loss 0.1303 acc 96.0%
After iteration 8: train loss 0.1103 acc 98.0%, test loss 0.1229 acc 96.0%
After iteration 9: train loss 0.1041 acc 98.0%, test loss 0.1169 acc 96.0%
Learned weights 2.81 -0.59 0.19
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/logistic_regression_sgd_1.svgz)
- `python3 logistic_regression_sgd.py --data_size=90 --batch_size=5 --iterations=9 --learning_rate=0.2`
```
After iteration 1: train loss 0.4005 acc 86.7%, test loss 0.4404 acc 80.0%
After iteration 2: train loss 0.3736 acc 88.9%, test loss 0.4110 acc 80.0%
After iteration 3: train loss 0.3604 acc 86.7%, test loss 0.3967 acc 80.0%
After iteration 4: train loss 0.3520 acc 86.7%, test loss 0.3880 acc 80.0%
After iteration 5: train loss 0.3475 acc 86.7%, test loss 0.3836 acc 80.0%
After iteration 6: train loss 0.3446 acc 86.7%, test loss 0.3809 acc 82.2%
After iteration 7: train loss 0.3424 acc 86.7%, test loss 0.3791 acc 84.4%
After iteration 8: train loss 0.3409 acc 86.7%, test loss 0.3780 acc 84.4%
After iteration 9: train loss 0.3400 acc 86.7%, test loss 0.3773 acc 84.4%
Learned weights 0.09 1.74 -0.03
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2021/tasks/figures/logistic_regression_sgd_2.svgz)
#### Examples End:
