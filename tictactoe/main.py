import re


def is_invalid_move(input):
    match_obj = re.match(r'[1-3]\s[1-3]', input)
    if match_obj:
        return False 
    else:
        return True


class TicTacToe(object):

    def __init__(self):
        self.init_game()
        print 'Welcome to TicTacToe!'
        print 'Here is the grid'
        self.print_grid()
        while self.game_continues():
            print 'Alright Player {}, your turn:'.format(self.player_turn)
            input = raw_input()
            if input == "quit":
                self.user_requested_exit = True
                break
            if is_invalid_move(input):
                print 'Sorry, you cannot play this'
                continue

            self.add_player_move(input.split(" "))

            self.change_player_turn()

            self.print_grid()

    def game_continues(self):
        return self.no_winner() and self.grid_not_full() and self.user_wants_to_continue()

    def add_player_move(self, input):
        row = int(input[0]) - 1
        column = int(input[1]) - 1
        if self.player_turn==1 :
            self.grid[row][column] = self.player1_marker
        else :
            self.grid[row][column] = self.player2_marker

    def print_grid(self):
        counter = 0
        for line in self.grid:
            self.print_line(line)
            if counter < 2:
                self.print_line_separation()
            counter += 1

    def change_player_turn(self):
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1

    def no_winner(self):
        return True

    def user_wants_to_continue(self):
        return not self.user_requested_exit

    def grid_not_full(self):
        for line in self.grid:
            if " " in line:
                return True
        else:
            return False

    def print_line(self, line):
        print " " + line[0] + " | " + line[1] + " | " + line[2]

    def print_line_separation(self):
        print "___________"

    def init_game(self):
        self.user_requested_exit = False
        self.player_turn = 1
        self.grid = [[" "] * 3 for n in range(3)]
        self.player1_marker = "X"
        self.player2_marker = "O"


if __name__ == '__main__':
    TicTacToe()
