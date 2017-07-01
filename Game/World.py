# -*- coding: utf-8 -*-
import random

class World:
    '''Define the world of the Game

    Has a worldMap : CityName -> [(CityName, direction)] that lists all the cities
    and the cities with which they are connected.
    Can erase a city from the Map
    Can return a random city
    Can return connected cities to a certain city
    '''

    def __init__(self,citiesFile):
        self.worldMap = {}
        self.createWorld(citiesFile)

    def createWorld(self,citiesFile):
        '''Create the world

        Assume that the input file entries are unique and no two cities have the
        same name'''

        with open(citiesFile, "r") as f:
            data = f.readlines()
            for line in data:
                rawInfo = line.split()
                name = rawInfo[0]
                self.worldMap[name] = []

                for connection in rawInfo[1:]:
                    pair = connection.split('=')
                    self.worldMap[name].append((pair[0],pair[1]))


    def eraseCityAndRoads(self,cityName):
        '''Erase a city from the world  '''

        del self.worldMap[cityName]
        for city , roads in self.worldMap.items():
            for direction,destination in roads[:]:
                if(destination == cityName):
                    roads.remove((direction,destination))

    def randomCity(self):
        '''Return a random city that is not destroyed'''

        return random.choice(list(self.worldMap.keys()))

    def connectedCities(self,city):
        '''Return all the cities that connect to the input city'''

        connectedCities = []
        cityTuples = self.worldMap[city]

        for cityTuple in cityTuples:
            connectedCities.append(cityTuple[1])

        return connectedCities
