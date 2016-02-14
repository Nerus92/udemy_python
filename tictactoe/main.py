from Grid import Grid


class TicTacToe(object):

    def __init__(self):
        self.user_requested_exit = False
        self.player_turn = 1
        self.grid = Grid()
        self.is_a_winner = False
        print 'Welcome to TicTacToe!'
        print 'Here is the grid'

    def start(self):
        while self.game_has_to_continue():
            self.grid.display()
            print 'Alright Player {}, your turn:'.format(self.player_turn)
            if not self.process_player_input(raw_input()):
                continue
            self.switch_player_turn()

        if self.user_requested_exit:
            print "Bye bye!"
        elif self.is_a_winner:
            self.grid.display()
            self.switch_player_turn()
            print "Congratulation Player {}, you won!".format(self.player_turn)
        else:
            print "Game Over, nobody wins."

    def process_player_input(self, player_input):
        if player_input == "quit":
            self.user_requested_exit = True
            return True
        if not self.grid.process_player_move(self.player_turn, player_input):
            print 'Sorry, you cannot play this'
            return False
        return True

    def game_has_to_continue(self):
        if self.no_winner() and self.grid.is_not_full() and self.user_wants_to_continue():
            return True
        return False

    def no_winner(self):
        if not self.grid.no_winner():
            self.is_a_winner = True
            return False
        return True

    def switch_player_turn(self):
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1

    def user_wants_to_continue(self):
        return not self.user_requested_exit


if __name__ == '__main__':
    game_session = TicTacToe()
    game_session.start()
