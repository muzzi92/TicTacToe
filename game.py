class Game(object):

    positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    current_player = 'X'

    def take_turn(self, input):
        index = input - 1
        if self.is_position_free(index):
            self.positions[index] = self.current_player
            self.change_player()

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


    def is_position_free(self, index):
        return self.positions[index] != 'X' and self.positions[index] != 'O'
