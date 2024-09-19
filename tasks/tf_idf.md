### Assignment: tf_idf
#### Date: Deadline: Nov 21, 7:59 a.m.
#### Points: 3 points
#### Tests: tf_idf_tests

**The template changed on Nov 8, please redownload it if you got it sooner
(the `LogisticRegression` needs to get an additional `C=10_000` argument).**

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/past-2324/labs/06/tf_idf.py)
template, perform classification of text documents from the
[20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/). To represent the
documents, use TF and/or IDF weights, which you implement manually (without
using the `sklearn.feature_extraction` module in any way). Classify test set
documents using `sklearn.linear_model.LogisticRegression` trained on the
given training data, and report macro F1-score.

#### Tests Start: tf_idf_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=79`
```
Number of unique terms with at least two occurrences: 12855
F-1 score for TF=False, IDF=False: 40.7%
```

2. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=79 --tf`
```
Number of unique terms with at least two occurrences: 12855
F-1 score for TF=True, IDF=False: 44.5%
```

3. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=79 --idf`
```
Number of unique terms with at least two occurrences: 12855
F-1 score for TF=False, IDF=True: 54.1%
```

4. `python3 tf_idf.py --train_size=1000 --test_size=500 --seed=79 --tf --idf`
```
Number of unique terms with at least two occurrences: 12855
F-1 score for TF=True, IDF=True: 61.8%
```

5. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=79`
```
Number of unique terms with at least two occurrences: 26587
F-1 score for TF=False, IDF=False: 58.4%
```

6. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=79 --tf`
```
Number of unique terms with at least two occurrences: 26587
F-1 score for TF=True, IDF=False: 64.0%
```

7. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=79 --idf`
```
Number of unique terms with at least two occurrences: 26587
F-1 score for TF=False, IDF=True: 64.7%
```

8. `python3 tf_idf.py --train_size=3000 --test_size=500 --seed=79 --tf --idf`
```
Number of unique terms with at least two occurrences: 26587
F-1 score for TF=True, IDF=True: 72.8%
```
#### Tests End:
