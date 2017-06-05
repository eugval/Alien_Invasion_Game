# -*- coding: utf-8 -*-
from Game.Game import Game
import os.path

class TestGame:
    def test_createAliens(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        G = Game(f,2)

        aliens = G.aliens

        assert len(aliens) == 2
        assert aliens[0].id == 2
        assert aliens[1].id == 1
        assert aliens[0].city != aliens[1].city


    def test_playGame(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        G = Game(f,1)

        G.playGame()
        aliens = G.aliens
        finalMap = G.world.worldMap

        expectedMap = {'Hambu': [('north', 'Hamba'),('east', 'Hambi')],
                        'Hamba': [('west','Hambu'),('east','Hambi')],
                        'Hambi': [('north','Hamba'),('west','Hambu')]
                        }

        assert len(aliens) == 1
        assert aliens[0].id == 1
        assert finalMap == expectedMap
