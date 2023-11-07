### Assignment: tf_idf
#### Date: Deadline: Nov 21, 7:59 a.m.
#### Points: 3 points
#### Tests: tf_idf_tests

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/master/labs/06/tf_idf.py)
template, perform classification of text documents from the
[20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/). To represent the
documents, use TF and/or IDF weights, which you implement manually (without
using the `sklearn.feature_extraction` module in any way). Classify test set
documents using `sklearn.linear_model.LogisticRegression` trained on the
given training data, and report macro F1-score.

#### Tests Start: tf_idf_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=45`
```
Number of unique terms with at least two occurrences: 14155
F-1 score for TF=False, IDF=False: 47.7%
```

2. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=45 --tf`
```
Number of unique terms with at least two occurrences: 14155
F-1 score for TF=True, IDF=False: 43.5%
```

3. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=45 --idf`
```
Number of unique terms with at least two occurrences: 14155
F-1 score for TF=False, IDF=True: 57.4%
```

4. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=45 --tf --idf`
```
Number of unique terms with at least two occurrences: 14155
F-1 score for TF=True, IDF=True: 59.9%
```

5. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=45`
```
Number of unique terms with at least two occurrences: 27814
F-1 score for TF=False, IDF=False: 57.8%
```

6. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=45 --tf`
```
Number of unique terms with at least two occurrences: 27814
F-1 score for TF=True, IDF=False: 54.7%
```

7. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=45 --idf`
```
Number of unique terms with at least two occurrences: 27814
F-1 score for TF=False, IDF=True: 68.0%
```

8. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=45 --tf --idf`
```
Number of unique terms with at least two occurrences: 27814
F-1 score for TF=True, IDF=True: 70.9%
```
#### Tests End:
