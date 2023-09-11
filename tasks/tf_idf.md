### Assignment: tf_idf
#### Date: Deadline: Dec 5, 7:59 a.m.
#### Points: 3 points
#### Tests: tf_idf_tests

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/past-2223/labs/08/tf_idf.py)
template, perform classification of text documents from the
[20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/). To represent the
documents, use TF and/or IDF weights, which you implement manually (without
using the `sklearn.feature_extraction` module in any way). Classify test set
documents using the majority class of the $k$ most similar training documents
(evaluated using cosine similarity) and report macro F1-score; utilizing the
k-nearest neighbors classifier from sklearn is fine.

#### Tests Start: tf_idf_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=False, IDF=False, k=1: 25.7%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --tf`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=True, IDF=False, k=1: 16.1%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --tf --idf`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=True, IDF=True, k=1: 48.3%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --idf`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=False, IDF=True, k=1: 46.5%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=5 --idf`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=False, IDF=True, k=5: 48.3%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=15 --idf`
```
Number of unique terms with at least two occurrences: 13120
F-1 score for TF=False, IDF=True, k=15: 49.8%
```
- `python3 tf_idf.py --train_size=2000 --test_size=500 --k=15 --idf`
```
Number of unique terms with at least two occurrences: 20414
F-1 score for TF=False, IDF=True, k=15: 57.2%
```
- `python3 tf_idf.py --train_size=2000 --test_size=500 --k=15 --tf --idf`
```
Number of unique terms with at least two occurrences: 20414
F-1 score for TF=True, IDF=True, k=15: 59.5%
```
#### Tests End:
