### Assignment: tf_idf
#### Date: Deadline: ~~Dec 06~~ Dec 13, 23:59
#### Points: 3 points
#### Tests: tf_idf_tests

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/past-2122/labs/08/tf_idf.py)
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
F-1 score for TF=False, IDF=False, k=1: 25.7%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --tf`
```
F-1 score for TF=True, IDF=False, k=1: 15.9%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --tf --idf`
```
F-1 score for TF=True, IDF=True, k=1: 45.5%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=1 --idf`
```
F-1 score for TF=False, IDF=True, k=1: 44.2%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=5 --idf`
```
F-1 score for TF=False, IDF=True, k=5: 46.9%
```
- `python3 tf_idf.py --train_size=1000 --test_size=500 --k=15 --idf`
```
F-1 score for TF=False, IDF=True, k=15: 50.7%
```
- `python3 tf_idf.py --train_size=2000 --test_size=500 --k=15 --idf`
```
F-1 score for TF=False, IDF=True, k=15: 60.0%
```
- `python3 tf_idf.py --train_size=2000 --test_size=500 --k=15 --tf --idf`
```
F-1 score for TF=True, IDF=True, k=15: 63.0%
```
#### Tests End:
