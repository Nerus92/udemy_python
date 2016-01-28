class TicTacToe(object):

    def __init__(self):
        self.init_game()
        print 'Welcome to TicTacToe!'
        print 'Here is the grid'
        self.print_grid()
        while self.no_winner() and self.grid_not_full():
            input = raw_input()
            if input == "quit":
                break

    def print_grid(self):
        counter = 0
        for line in self.grid:
            self.print_line(line)
            if counter < 2:
                self.print_line_separation()
            counter += 1

    def no_winner(self):
        return True

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
        self.grid = 3 * [3 * [" "]]
        self.player1_marker = "X"
        self.player2_marker = "O"


if __name__ == '__main__':
    TicTacToe()
