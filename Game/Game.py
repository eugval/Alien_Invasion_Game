# -*- coding: utf-8 -*-
from World import World
from Alien import Alien
import os.path

class Game:
    '''Define the Main game setup

    Count the aliens left alive and the rounds played
    Contain the world and the aliens
    Play the game
    Write the result into a file
    '''

    def __init__(self, citiesFile, alienNumber):
        self.aliensAlive = int(alienNumber)
        self.round = 0
        self.world = World(citiesFile)
        self.aliens = []
        self.createAliens(int(alienNumber))


    def createAliens(self,alienID):
        '''Create the aliens for the Game

          If more aliens are input than cities, the number of aliens is made equal to the number of cities.
        '''

        if(alienID>len(self.world.worldMap)):
            alienID=len(self.world.worldMap)

        while alienID > 0 :
            city = self.world.randomCity()
            if (not self.__alienFound(city)):
                self.aliens.append(Alien(alienID,city))
                alienID -= 1


    def playGame(self):
        '''Play the Game:

        An alien makes a move to a new city
        If there is another alien there, both die and the city (and its roads) is destroyed
        Stop after 10 000 moves or if no aliens are left alive
        write remaining cities to a file at the end
        '''

        print("\n \n ******* Let's Play the Game!! ********* \n")

        while self.round < 10000 and self.aliensAlive > 0:
            for alien in self.aliens:
                newCity = alien.move(self.world)

                if(not newCity):
                    continue

                residentAlien = self.__alienFound(newCity)

                if(residentAlien):
                    self.__aliensClash(alien.id,residentAlien,newCity)
                else:
                    alien.city = newCity

            self.round +=1

        self.__writeResults()


    def printResults(self):
        '''Print the results'''

        if(os.path.isfile("Post_Apocalyptic_World_Map.txt")):
            print("\n \n **********    Here is the post-apocalypse World:  ************ :O  \n")
            with open("Post_Apocalyptic_World_Map.txt", 'r') as f:
                print f.read()
        else:
            print("Please play First!")


    def __writeResults(self):
        '''Write the results into a file'''

        with open("Post_Apocalyptic_World_Map.txt","w") as f:
            for cityName, roads in self.world.worldMap.items():
                f.write(cityName + ' ')
                for direction, destination in roads:
                    f.write(direction +'='+destination+' ')
                f.write('\n')


    def __aliensClash(self,alien1Id, alien2Id,city):
        '''Clash of the aliens

        Erase the city and all the paths that connect to it
        Destroy the two aliens
        '''

        print(city + " has been destroyed by alien " + str(alien1Id) + " and alien " + str(alien2Id))
        self.world.eraseCityAndRoads(city)
        self.__removeAlien(alien1Id)
        self.__removeAlien(alien2Id)
        self.aliensAlive -= 2


    def __removeAlien(self,alienId):
        '''Remove the allien from the game'''

        for alien in self.aliens:
            if(alienId == alien.id):
                self.aliens.remove(alien)


    def __alienFound(self,cityName):
        '''Return an alien Id if an alien is found at the given city otherwise return False'''

        for alien in self.aliens:
            if(alien.city == cityName):
                return alien.id
        return False
