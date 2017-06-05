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


Discussion
--------
This exercise clearly feats the OOP style so I went with it. I split the program into
three classes: (1) Game that encompasses the overall logic of the game and contains the
aliens and the world, (2) World that contains the logic relevant to the cities and how
they evolve and (3) Alien that contains the logic behind the aliens and defines their movement.

The trickiest part of the exercise was to come up with the way and the data structures to correctly
keep track of the cities and the positions of the aliens. Finally I decided that the full
topology of the game's world would be encoded in the worldMap attribute and that the positions of
the aliens would be stored in the alien objects themselves.

The main assumptions that have been made are described above, and mainly concern the input parameters.

This exercise was quite fun to do, I hope you like this solution! :)
