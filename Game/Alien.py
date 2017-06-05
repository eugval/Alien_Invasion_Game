# -*- coding: utf-8 -*-
import random

class Alien:
    '''Defines properties and movements of an alien

    Has a unique id and a city that it currently resides
    Can move to another city
    '''

    def __init__(self, alienId, city):
        self.id = alienId
        self.city = city

    def move(self, world):
        '''Return at random one of the accessible cities'''

        connectedCities = world.connectedCities(self.city)

        if(not connectedCities):
            return False

        newCity = random.choice(connectedCities)

        self.city = None

        return newCity
