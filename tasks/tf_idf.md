### Assignment: tf_idf
#### Date: Deadline: Dec 06, 23:59
#### Points: 3 points

Using the [tf_idf.py](https://github.com/ufal/npfl129/tree/master/labs/08/tf_idf.py)
template, perform classification of text documents from the
[20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/). To represent the
documents, use TF and/or IDF weights, which you implement manually (without
using the `sklearn.feature_extraction` module in any way). Classify test set
documents using the majority class of the $k$ most similar training documents
(evaluated using cosine similarity) and report macro F1-score; utilizing the
k-nearest neighbors classifier from sklearn is fine.
