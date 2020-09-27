### Assignment: diacritization
#### Date: Deadline: Nov 24, 23:59
#### Points: 5 points+6 bonus

The goal of the `diacritization` competition is to learn to add diacritics to
the given Czech text. We will use a small collection of
[fiction books](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/fiction-train.txt),
which is available under [CC BY-NC-SA license](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/fiction-train.LICENSE).
Note that these texts are the only allowed training data, you cannot use any
other Czech texts to train or evaluate your model. At test time, you will be
given a text without diacritics and you should return it including diacritical
marks – to be explicit, we only consider diacritized letters `áčďéěíňóřšťúůýž`
and their uppercase variants.

The [diacritization.py](https://github.com/ufal/npfl129/tree/past-1920/labs/04/diacritization.py)
template shows how to load the training data, downloading it if needed,
it shows how to save a compressed trained estimator and how to load it in
`recodex_predict` method.

Each sentence in the data is stored on a single line, with exactly one
space character separating input words. The performance of your system is
measured using _word accuracy_ (the percentage of words you diacritized
correctly, as computed by the
[diacritization_eval.py](https://github.com/ufal/npfl129/tree/past-1920/labs/04/diacritization_eval.py)
script) and your goal is to achieve at least **86.5%**. You can use any sklearn
algorithm which does not use decision trees to solve this assignment (so no
random forests, extra trees, gradient boosting, AdaBoost, …).
