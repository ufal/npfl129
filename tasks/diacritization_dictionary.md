### Assignment: diacritization_dictionary
#### Date: Deadline: Nov 25, 22:00
#### Points: 4 points+4 bonus

The `diacritization_dictionary` is an extension of the `diacritization` competition.
In addition to the [original training data](https://ufal.mff.cuni.cz/~courses/npfl129/2425/datasets/fiction-train.txt),
in this task you can also use a [dictionary providing all known diacritized
variants](https://ufal.mff.cuni.cz/~courses/npfl129/2425/datasets/fiction-dictionary.txt)
of word forms present in the training _and testing_ data, available again under
[CC BY-NC-SA license](https://ufal.mff.cuni.cz/~courses/npfl129/2425/datasets/fiction-dictionary.LICENSE).
The dictionary is not guaranteed to contain all words from the training and
testing data, but if it contains a word, all valid Czech diacritization variants
should be present.

The rules of the competition are the same as of the `diacritization` competition,
except that
- you can utilize the dictionary, both during training and inference;
- in order to pass, you need to achieve at least **95%** word accuracy.

The [diacritization_dictionary.py](https://github.com/ufal/npfl129/tree/past-2425/labs/06/diacritization_dictionary.py)
module provides a `Dictionary` class, which loads the dictionary
(downloading it if necessary), exposing it in `Dictionary.variants` field
as a mapping from undiacritized word form to a list of known diacritized
variants.

Note that the `fiction-dictionary.txt` is available in ReCodEx during evaluation.
