### Assignment: isnt_it_ironic_open
#### Date: Deadline: Jan 05, 23:59
#### Points: up to 10 bonus points

This is an extended version of `isnt_it_ironic` competition to a so-called
_open_ track. The differences against the original competition are:
- the general idea is to achieve the highest score, ideally state-of-the-art
- you can use any framework and any algorithm, including code you did not
  write yourself (but of course do not share code outside teams)
- you can use any unannotated data
- use **only** the manual annotations (i.e., labels of irony) from the training
  data, do not search for or create more

The test set tweets without annotations
[are available here](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/isnt_it_ironic.test.zip).
They can be loaded for example using the `Dataset` class from the
[isnt_it_ironic.py](https://github.com/ufal/npfl129/tree/past-1920/labs/07/isnt_it_ironic.py)
template.

Your submission in ReCodEx should consist of:
- exactly one `.txt` file consisting of the test set annotations, containing
  on every line either a number `0` or a number `1`;
- at least one `.py` file with the implementation you utilized to generate the
  test set annotations (this file is not executed, it is only for me to
  understand what approach you took)

**Note that the baseline is now 65%, which is a bit more than the best solution
of `isnt_it_ironic`.**
