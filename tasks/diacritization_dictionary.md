### Assignment: diacritization_dictionary
#### Date: Deadline: Dec 01, 23:59
#### Points: 4 points+5 bonus

The `diacritization_dictionary` is an extension of the `diacritization` competition.
In addition to the [original training data](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/fiction-train.txt),
in this task you can also use a [dictionary providing all known diacritized
variants](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/fiction-dictionary.txt)
of all word forms present in the training _and testing_ data, available again under
[CC BY-NC-SA license](https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/fiction-train.LICENSE).

The rules of the competition is the same as of the `diacritization` competition,
except that
- you can utilize the dictionary, both during training and inference;
- in order to pass, you need to achieve at least **95%** word accuracy.

The [diacritization_dictionary.py](https://github.com/ufal/npfl129/tree/master/labs/05/diacritization_dictionary.py)
module provides a `Dictionary` class, which loads the dictionary
(downloading it if necessary), exposing it in `Dictionary.variants` field
as a mapping from undiacritized word form to a list of known diacritized
variants.

Note that the `fiction-dictionary.txt` is available during ReCodEx evaluation,
so **you must not submit it to ReCodEx**.
