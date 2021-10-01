### Assignment: nli_competition
#### Date: Deadline: Jan 05, 23:59
#### Points: 5 points+5 bonus

In this [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2021-winter#competitions) you will be solving the Native
Language Identification. In that task, you get an English essay writen by
a non-native individual and your goal is to identify their native language.

We will be using NLI Shared Task 2013 data, which contains documents in 11
languages. For each language, the train, development and test sets contain
900, 100 and 100 documents, respectively. Particularly interesting is the fact
that humans are quite bad in this task (in a simplified settings, human professionals
achieve 40-50% accuracy), while machine learning models can achive
high performance.

Because the data is not publicly available, you can download it only through
ReCodEx. Please do not distribute it. To load the dataset, use the
[nli_competition.py](https://github.com/ufal/npfl129/tree/past-2021/labs/10/nli_competition.py)
template.

The performance of your system is measured using _accuracy_ of correctly
predicted documents and your goal is to achieve at least 77% accuracy.
Note that you can use **any sklearn algorithm** to solve this exercise.
