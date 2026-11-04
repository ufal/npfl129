### Assignment: tf_idf
#### Date: Deadline: Nov 17, 22:00
#### Points: 3 points
#### Tests: tf_idf_tests

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/master/labs/06/tf_idf.py)
template, perform classification of text documents from the
[20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/). To represent the
documents, use TF and/or IDF weights, which you implement manually (without
using the `sklearn.feature_extraction` module in any way). Classify test set
documents using a given multi-class classifier trained on the given training data,
and report macro $F_1$-score.

#### Tests Start: tf_idf_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._

1. `python3 tf_idf.py --train_size=1000 --test_size=500`
```
Number of unique terms with at least two occurrences: 13638
F-1 score for TF=False, IDF=False: 41.8%
```

2. `python3 tf_idf.py --train_size=1000 --test_size=500 --tf`
```
Number of unique terms with at least two occurrences: 13638
F-1 score for TF=True, IDF=False: 51.3%
```

3. `python3 tf_idf.py --train_size=1000 --test_size=500 --idf`
```
Number of unique terms with at least two occurrences: 13638
F-1 score for TF=False, IDF=True: 55.3%
```

4. `python3 tf_idf.py --train_size=1000 --test_size=500 --tf --idf`
```
Number of unique terms with at least two occurrences: 13638
F-1 score for TF=True, IDF=True: 60.2%
```

5. `python3 tf_idf.py --train_size=3000 --test_size=500`
```
Number of unique terms with at least two occurrences: 27207
F-1 score for TF=False, IDF=False: 58.1%
```

6. `python3 tf_idf.py --train_size=3000 --test_size=500 --tf`
```
Number of unique terms with at least two occurrences: 27207
F-1 score for TF=True, IDF=False: 64.6%
```

7. `python3 tf_idf.py --train_size=3000 --test_size=500 --idf`
```
Number of unique terms with at least two occurrences: 27207
F-1 score for TF=False, IDF=True: 67.8%
```

8. `python3 tf_idf.py --train_size=3000 --test_size=500 --tf --idf`
```
Number of unique terms with at least two occurrences: 27207
F-1 score for TF=True, IDF=True: 72.4%
```
#### Tests End:
