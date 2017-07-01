Aliens Invasion Game
====================
What it is
------------
- A self-playing alien invasion simulation.
- It receives an input csv file representing a world and a number of aliens that are invading.
- The aliens are distributed and start moving randomly in the world.
- When they find each other they both die and destroy the city they got to.
- The game prints on each alien clash and the post-apocalyptic world that results at the end.


How to play
-----------
1. Make sure python is installed
2. Generate the world. Type the following command on the terminal:
```
$python CreateWorld.py number_of_cities

```
number_of_cities is the size of the world to be generated. Use an integer bigger than 4.

3. Run the following command on the terminal:
```
$ python runAlienInvasion.py  World_Map.txt Number_of_alliens

```
World_Map.txt is the file containing the world map. This can be created by CreateWorld.py or be supplied independently if of the correct format.
The Number_of_aliens is the number of aliens that compete.

Assumptions
-----------

It is assumed that the Number_of_aliens is an integer, and that the World_Map.txt exits and is well formed.

We further assume that Number_of_aliens is bigger than 0.


How the code is structured
--------------------------

The Game package contains all the classes necessary to run the game while the Tests folder contains all the unit tests.
The root folder contains the modules for the initial world creation and launching the game, as well as the world map and after-playing world map files.

The object oriented paradigm has been used. There are three classes : (1) The Game class that represents the game overall, defines the action and game progression mechanisms (2) the World class that keeps track of the world as it being destroyed by the alien invasion and (3) the Alien class that defines the properties and movements of each Alien.

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
