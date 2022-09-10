### Assignment: kmeans
#### Date: Deadline: Feb 13, 23:59
#### Points: 3 points
#### Examples: kmeans_examples
#### Tests: kmeans_tests

Using the [kmeans.py](https://github.com/ufal/npfl129/tree/past-2122/labs/11/kmeans.py)
template, implement the K-Means algorithm with both
- random initialization,
- `kmeans++` initialization.

#### Examples Start: kmeans_examples
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kmeans.py --clusters=5 --examples=150 --iterations=5 --seed=51 --init=random`
```
Cluster assignments:
[2 3 3 4 1 2 1 1 2 3 2 1 1 3 3 4 0 4 4 1 3 1 1 1 1 0 1 3 3 2 3 0 1 0 3 3 0
 0 1 0 1 2 1 1 3 2 1 2 2 1 3 2 2 2 3 2 1 2 1 4 3 3 4 4 2 1 1 1 1 3 1 3 1 4
 1 3 2 1 0 0 1 2 2 0 2 2 3 1 1 1 2 2 4 2 2 1 1 1 2 2 2 3 1 3 1 3 2 1 0 2 2
 3 1 1 1 3 3 0 1 3 4 1 1 4 1 3 1 4 4 3 1 4 1 4 1 1 1 3 1 1 4 2 0 3 1 4 1 2
 2 1]
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kmeans_1.svgz)
- `python3 kmeans.py --clusters=5 --examples=150 --iterations=5 --seed=51 --init=kmeans++`
```
Cluster assignments:
[1 3 3 4 0 1 0 2 1 3 1 2 2 3 3 4 4 4 4 2 3 2 2 2 2 4 2 3 3 0 3 4 0 4 3 3 4
 4 2 4 2 1 0 0 3 1 0 1 1 0 3 1 0 0 3 1 0 1 2 4 3 3 4 4 1 0 2 0 0 3 0 3 0 4
 2 3 1 2 4 4 2 1 1 4 1 1 3 0 2 2 1 1 4 1 1 2 0 2 1 1 1 3 0 3 2 3 1 0 4 1 1
 3 0 2 0 3 0 4 0 3 4 0 2 4 2 3 2 4 4 3 2 4 2 4 2 0 0 3 0 0 4 1 4 3 0 4 2 1
 1 2]
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kmeans_2.svgz)
- `python3 kmeans.py --clusters=7 --examples=200 --iterations=11 --seed=67 --init=random`
```
Cluster assignments:
[2 1 0 4 5 1 4 1 1 2 0 3 6 6 1 6 1 1 0 2 3 2 4 0 6 5 5 4 5 4 4 6 6 1 0 6 4
 4 1 6 4 5 4 4 1 0 2 1 2 2 4 3 2 1 5 2 6 0 5 6 4 2 6 3 1 1 4 5 1 2 4 5 4 5
 1 1 4 2 5 4 4 5 4 2 2 4 4 1 5 0 4 4 4 1 3 0 3 5 4 1 0 4 4 4 4 4 5 4 1 4 4
 2 5 2 6 5 2 2 4 5 4 4 3 3 2 6 1 4 1 6 1 2 3 0 5 6 4 6 4 5 5 2 0 1 6 0 1 4
 4 6 5 1 2 4 0 0 4 0 4 3 5 4 3 4 6 3 6 5 5 6 0 2 6 5 4 5 4 3 2 4 1 2 4 2 4
 2 6 4 4 6 2 4 4 6 6 5 0 2 4 1]
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kmeans_3.svgz)
- `python3 kmeans.py --clusters=7 --examples=200 --iterations=5 --seed=67 --init=kmeans++`
```
Cluster assignments:
[3 1 4 5 0 1 6 1 3 3 4 4 2 2 1 2 1 1 4 3 4 3 5 4 2 0 0 6 0 6 5 2 2 1 4 2 5
 5 1 2 5 0 6 6 1 4 3 1 3 3 5 4 3 1 0 3 2 4 0 2 5 3 2 4 1 1 6 0 1 3 5 0 5 0
 1 1 6 3 0 6 5 0 5 3 3 5 6 1 0 4 5 6 5 1 4 4 2 0 6 1 4 6 5 5 6 5 0 5 1 6 6
 3 0 3 2 0 3 3 5 0 6 6 4 4 3 2 1 6 1 2 1 3 4 4 0 2 6 2 6 0 0 3 4 1 2 4 1 5
 6 2 0 1 3 5 4 4 6 4 6 4 0 5 2 5 2 4 2 0 0 2 4 3 2 0 6 0 5 2 3 5 1 3 6 3 5
 3 2 6 5 2 0 6 6 2 2 0 4 3 6 1]
```
![Example visualization](//ufal.mff.cuni.cz/~straka/courses/npfl129/2122/tasks/figures/kmeans_4.svgz)
#### Examples End:
#### Tests Start: kmeans_tests
_Note that your results may be slightly different (because of varying floating point arithmetic on your CPU)._
- `python3 kmeans.py --clusters=5 --examples=150 --iterations=3 --init=random`
```
Cluster assignments:
[4 3 4 4 3 2 3 3 4 3 4 4 4 3 1 4 3 4 1 2 3 4 3 3 1 3 3 3 3 4 0 3 3 3 4 0 3
 3 4 3 4 3 3 4 4 4 3 0 4 4 4 4 2 3 3 2 4 0 0 3 3 4 4 0 3 2 4 1 3 4 1 4 4 0
 4 3 4 1 3 0 3 4 4 3 4 1 3 4 3 3 4 4 4 3 4 4 1 4 4 3 1 3 1 4 3 3 3 4 4 4 4
 3 4 4 4 4 4 4 2 4 3 4 4 2 3 3 3 4 2 4 4 3 3 2 3 3 2 3 2 0 4 3 3 3 3 3 3 3
 3 4]
```
- `python3 kmeans.py --clusters=5 --examples=150 --iterations=3 --init=kmeans++`
```
Cluster assignments:
[4 1 4 2 3 0 1 1 4 3 4 2 2 3 0 2 3 2 0 0 1 4 3 3 0 3 3 1 3 2 0 1 3 3 2 0 3
 3 4 1 2 3 1 2 4 2 1 0 2 4 2 2 0 1 1 0 2 0 0 1 3 4 2 0 3 0 4 0 3 2 0 4 2 0
 2 1 2 0 3 0 1 2 4 1 4 0 1 2 3 3 2 4 2 1 4 2 0 4 4 1 0 3 0 2 1 3 1 4 2 2 4
 3 2 2 4 4 2 4 0 2 1 4 4 0 3 1 3 4 0 2 4 1 1 0 3 1 0 3 0 0 4 1 1 3 3 1 1 3
 1 2]
```
- `python3 kmeans.py --clusters=7 --examples=200 --iterations=3 --init=random`
```
Cluster assignments:
[6 0 0 3 3 1 1 1 5 4 3 6 5 2 4 4 3 3 4 3 6 3 1 3 0 6 2 0 2 6 2 1 0 3 6 3 1
 3 5 3 3 0 4 3 5 6 3 0 3 3 6 6 3 3 3 5 0 5 3 6 2 2 0 2 2 4 3 3 6 6 6 5 0 2
 1 2 2 6 2 5 0 0 1 2 5 2 2 4 5 3 6 4 6 3 3 5 1 3 3 0 5 3 0 6 2 0 2 3 5 0 3
 1 3 5 6 5 4 2 0 3 2 3 3 6 1 2 2 2 4 3 0 5 5 2 3 5 1 2 6 6 0 5 5 3 3 3 2 6
 0 0 2 0 6 3 3 2 6 0 3 5 4 1 3 5 0 3 0 5 6 3 1 5 0 0 3 0 1 3 5 4 3 3 3 2 3
 3 2 3 6 1 4 3 0 5 5 3 3 5 6 6]
```
- `python3 kmeans.py --clusters=7 --examples=200 --iterations=3 --init=kmeans++`
```
Cluster assignments:
[4 0 0 5 5 2 2 2 2 2 5 4 2 3 2 2 6 6 2 6 4 5 2 1 0 4 3 0 3 4 3 2 0 1 4 6 2
 5 2 5 5 0 2 1 2 4 5 0 1 5 4 4 5 5 5 2 0 2 6 4 3 3 0 3 3 2 5 1 4 4 4 2 0 3
 2 3 3 4 3 2 0 0 2 3 2 3 3 2 2 5 4 2 4 5 1 2 2 5 1 0 2 1 0 4 3 0 3 1 2 0 6
 2 1 2 4 2 2 3 0 5 3 1 1 4 2 3 3 3 2 6 0 2 2 3 1 2 2 3 4 4 0 2 2 1 5 1 3 4
 0 0 3 0 4 1 5 3 4 0 1 2 2 2 6 2 0 1 0 2 4 1 2 2 0 0 5 0 2 1 2 2 1 5 1 3 1
 5 3 5 4 2 2 6 0 2 2 1 6 2 4 4]
```
#### Tests End:
