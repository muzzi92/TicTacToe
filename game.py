class Game(object):

    positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    current_player = 'X'

    def take_turn(self, index):
        self.positions[index - 1] = self.current_player
        self.change_player()

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
