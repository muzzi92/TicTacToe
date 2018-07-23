import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from game import Game

class TestGame(object):

    def test_has_an_array_of_positions(self):
        game = Game()
        assert game.positions == ['1', '2', '3', '4', '5', '6', '7', '8', '9']