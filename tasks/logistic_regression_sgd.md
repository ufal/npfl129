### Assignment: logistic_regression_sgd
#### Date: Deadline: Nov 01, 23:59
#### Points: 5 points
#### Tests: logistic_regression_sgd_tests

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
#### Tests Start: logistic_regression_sgd_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 logistic_regression_sgd.py --data_size=100 --batch_size=10 --iterations=9 --learning_rate=0.5`
```
After iteration 1: train loss 0.3259 acc 94.0%, test loss 0.3301 acc 96.0%
After iteration 2: train loss 0.2321 acc 96.0%, test loss 0.2385 acc 98.0%
After iteration 3: train loss 0.1877 acc 98.0%, test loss 0.1949 acc 98.0%
After iteration 4: train loss 0.1612 acc 98.0%, test loss 0.1689 acc 98.0%
After iteration 5: train loss 0.1435 acc 98.0%, test loss 0.1517 acc 98.0%
After iteration 6: train loss 0.1307 acc 98.0%, test loss 0.1396 acc 98.0%
After iteration 7: train loss 0.1208 acc 98.0%, test loss 0.1304 acc 96.0%
After iteration 8: train loss 0.1129 acc 98.0%, test loss 0.1230 acc 96.0%
After iteration 9: train loss 0.1065 acc 98.0%, test loss 0.1170 acc 96.0%
Learned weights 2.77 -0.60 0.12
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_1.svgz)
- `python3 logistic_regression_sgd.py --data_size=95 --test_size=45 --batch_size=5 --iterations=9 --learning_rate=0.5`
```
After iteration 1: train loss 0.2429 acc 96.0%, test loss 0.3187 acc 93.3%
After iteration 2: train loss 0.1853 acc 96.0%, test loss 0.2724 acc 93.3%
After iteration 3: train loss 0.1590 acc 96.0%, test loss 0.2525 acc 93.3%
After iteration 4: train loss 0.1428 acc 96.0%, test loss 0.2411 acc 93.3%
After iteration 5: train loss 0.1313 acc 98.0%, test loss 0.2335 acc 93.3%
After iteration 6: train loss 0.1225 acc 96.0%, test loss 0.2258 acc 93.3%
After iteration 7: train loss 0.1159 acc 96.0%, test loss 0.2220 acc 93.3%
After iteration 8: train loss 0.1105 acc 96.0%, test loss 0.2187 acc 93.3%
After iteration 9: train loss 0.1061 acc 96.0%, test loss 0.2163 acc 93.3%
Learned weights -0.61 3.61 0.12
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_2.svgz)
- `python3 logistic_regression_sgd.py --data_size=95 --test_size=45 --batch_size=1 --iterations=9 --learning_rate=0.7`
```
After iteration 1: train loss 0.1141 acc 96.0%, test loss 0.2268 acc 93.3%
After iteration 2: train loss 0.0867 acc 96.0%, test loss 0.2150 acc 91.1%
After iteration 3: train loss 0.0797 acc 98.0%, test loss 0.2320 acc 88.9%
After iteration 4: train loss 0.0753 acc 96.0%, test loss 0.2224 acc 88.9%
After iteration 5: train loss 0.0692 acc 96.0%, test loss 0.2154 acc 88.9%
After iteration 6: train loss 0.0749 acc 98.0%, test loss 0.2458 acc 88.9%
After iteration 7: train loss 0.0638 acc 96.0%, test loss 0.2190 acc 88.9%
After iteration 8: train loss 0.0644 acc 98.0%, test loss 0.2341 acc 88.9%
After iteration 9: train loss 0.0663 acc 98.0%, test loss 0.2490 acc 88.9%
Learned weights -1.07 7.33 -0.40
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/logistic_regression_sgd_3.svgz)
#### Tests End:
