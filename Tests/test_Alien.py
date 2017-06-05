# -*- coding: utf-8 -*-
from Game.Alien import Alien
from Game.World import World
import os.path

class TestAlien:
    def test_move(self):
        f = os.path.join(os.path.dirname(__file__), 'world_map_test.txt')
        w = World(f)
        al1 = Alien(1,"Hambu")
        al2 = Alien(2, "Hambi")

        newC1 = al1.move(w)
        newC2 = al2.move(w)

        assert newC1 == "Hamba" or newC1 == "Hambi"
        assert newC2 == "Hamba" or newC2 == "Hambu"
