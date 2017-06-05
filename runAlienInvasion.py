# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import sys
    from Game.Game import Game


    game = Game(sys.argv[1],sys.argv[2])
    game.playGame()
    game.printResults()
