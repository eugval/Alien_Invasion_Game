'''Script to create a random input file of the correct format'''

import random
import string
import sys

def generateName(length):
    '''Generate a random name of a given length.
        A minimum length of 1 needs to be input.
    '''

    VOWELS = "aeiou"
    CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
    name = ""

    for i in range(length):
        if i % 2 == 0:
            name += random.choice(CONSONANTS)
        else:
            name += random.choice(VOWELS)

    return  name.capitalize()


def makeWorldFile(worldSize):
    '''Create a file with the initial world map.
        Each row has the city name followed by 1 to 4 directions and the city they lead to.
        Row example:
        Barkouzi north=Milini west=Sunsi
    '''

    if(worldSize<5):
        print("Please make a world with more than 4 cities: The input must be a positive integer bigger than 4.")
        return

    directions = ["north","east","west","south"]
    cities = []

    for i in range(worldSize):
        cityName = generateName(random.randint(2,6))
        cities.append(cityName)

    with open("World_Map.txt","w") as f:
        for city in cities:
            f.write(city + ' ')
            for j in range(random.randint(1,4)):
                connections = []
                nextConnection = random.choice(cities)
                while nextConnection in connections:
                    nextConnection = random.choice(cities)

                f.write(directions[j] +'='+nextConnection+' ')
                connections.append(nextConnection)

            f.write('\n')

def main():
    try:
        cityNumber = int(sys.argv[1])
    except ValueError:
        print("Please use an integer as an argument")
        return

    makeWorldFile(cityNumber)


if __name__ == "__main__":
    main()
