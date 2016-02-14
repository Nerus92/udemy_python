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
        while self.game_continues():
            self.print_grid()
            self.change_player_turn()
            print 'Alright Player {}, your turn:'.format(self.player_turn)
            input = raw_input()
            if input == "quit":
                self.user_requested_exit = True
                break
            if is_invalid_move(input):
                print 'Sorry, you cannot play this'
                self.change_player_turn()
                continue

            if not self.add_player_move(input.split(" ")):
                print 'Sorry, you cannot play this'
                self.change_player_turn()
                continue

        if self.user_requested_exit :
            print "Bye bye!"
        elif self.is_a_winner :
            self.print_grid()
            print "Congratulation Player {}, you won!".format(self.player_turn)
        else :
            print "Game Over, nobody wins."

    def game_continues(self):
        return self.no_winner() and self.grid_not_full() and self.user_wants_to_continue()

    def add_player_move(self, input):
        row = int(input[0]) - 1
        column = int(input[1]) - 1
        if self.grid[row][column] == " " :
            if self.player_turn==1 :
                self.grid[row][column] = self.player1_marker
            else :
                self.grid[row][column] = self.player2_marker
            return True
        else :
            return False

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
        if not self.is_diagonal_winner() and not self.is_vertical_winner() and not self.is_horizontal_winner() :
            return True
        self.is_a_winner = True
        return False

    def is_diagonal_winner(self):
        str1 = self.grid[0][0] + self.grid[1][1] + self.grid[2][2]
        str2 = self.grid[0][2] + self.grid[1][1] + self.grid[2][0]
        if (len(str1.replace(" ", "")) == 3 and str1[0] == str1[1] and str1[0] == str1[2]) or (len(str2.replace(" ", "")) == 3 and str2[0] == str2[1] and str2[0] == str2[2]) :
            return True
        return False

    def is_vertical_winner(self):
        for column in range(0, 2) :
            str = ""
            for line in self.grid :
                str = str + line[column]
            if len(str.replace(" ", "")) == 3 and str[0] == str[1] and str[0] == str[2] :
                return True
        return False

    def is_horizontal_winner(self):
        for line in self.grid :
            str = ""
            for element in line :
                str = str + element
            if len(str.replace(" ", "")) == 3 and str[0] == str[1] and str[0] == str[2] :
                return True
        return False

    def user_wants_to_continue(self):
        return not self.user_requested_exit

    def grid_not_full(self):
        for line in self.grid:
            if " " in line:
                return True
        else:
            self.grid_full = True
            return False

    def print_line(self, line):
        print " " + line[0] + " | " + line[1] + " | " + line[2]

    def print_line_separation(self):
        print "___________"

    def init_game(self):
        self.user_requested_exit = False
        self.player_turn = 2
        self.grid = [[" "] * 3 for n in range(3)]
        self.is_a_winner = False
        self.player1_marker = "X"
        self.player2_marker = "O"


if __name__ == '__main__':
    TicTacToe()
