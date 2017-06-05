# -*- coding: utf-8 -*-
from Game.World import World
import os.path

class TestWorld :
    def test_createWorld(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        W = World(f)

        expectedMap = {'Hambu': [('north', 'Hamba'),('east', 'Hambi')],
                        'Hamba': [('west','Hambu'),('east','Hambi')],
                        'Hambi': [('north','Hamba'),('west','Hambu')]
                        }
        assert W.worldMap == expectedMap


    def test_eraseCityAndRoads(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        W = World(f)

        W.eraseCityAndRoads('Hamba')

        expectedMap =  {'Hambu': [('east', 'Hambi')],
                        'Hambi': [('west','Hambu')]
                        }
        assert W.worldMap == expectedMap


    def test_randomCity(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        W = World(f)

        random = W.randomCity()

        assert random == 'Hamba' or random == 'Hambu' or random == 'Hambi'


    def test_connectedCities(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        W = World(f)

        cities1 = W.connectedCities('Hamba')
        cities2 = W.connectedCities('Hambu')

        assert cities1 == ['Hambu','Hambi']
        assert cities2 == ['Hamba','Hambi']        
