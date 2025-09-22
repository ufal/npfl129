### Assignment: nli_competition
#### Date: Deadline: Jan 6, 22:00
#### Points: 4 points+5 bonus

In this [competition task](https://ufal.mff.cuni.cz/courses/npfl129/2425-winter#competitions) you will be solving the Native
Language Identification. In that task, you get an English essay writen by
a non-native individual and your goal is to identify their native language.

We will be using NLI Shared Task 2013 data, which contains documents in 11
languages. For each language, the train and test sets contain 1000 and 100
documents, respectively. Particularly interesting is the fact that humans are
quite bad in this task (in a simplified setting, human professionals achieve
40-50% accuracy), while machine learning models can achieve high performance.

Because the data is not publicly available, you can download it only through
ReCodEx. Please do not distribute it. The template
[nli_competition.py](https://github.com/ufal/npfl129/tree/past-2425/labs/11/nli_competition.py)
can then be used to load the dataset as usual.

The performance of your system is measured using _accuracy_ of correctly
predicted documents and your goal is to achieve at least 78% accuracy.
Note that you can use **any sklearn algorithm** to solve this exercise.
