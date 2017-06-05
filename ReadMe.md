Aliens Invasion Game
====================

How to play
-----------

1. Make sure python is installed
2. Run the following command on the terminal:
```
$ python runAlienInvasion.py inputFile.txt Number_of_alliens

```
InputFile.txt one of the provided game world files of the format world_map_*
The Number_of_aliens is the number of aliens that compete.

Assumptions
-----------

It is assumed that the Number_of_aliens is an integer, and that the inputFile.txt exits
 and is well formed.

We further assume that Number_of_aliens is bigger than 0, that it is smaller than
the number of cities in the input file and significantly smaller for a large number of cities in the input file.

We finally assume that the cities in the inputFile.txt are unique and that the world
that they represent is well formed i.e it makes up a simple connected graph.



To run the tests
---------------
1. install pytest
```
$ pip install -r Tests/Requirements.txt

```

2. Run the following command on the terminal:
```
$ py.test -v

```
