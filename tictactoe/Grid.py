import re


def is_invalid_move(player_move):
    match_obj = re.match(r'[1-3]\s[1-3]', player_move)
    if match_obj:
        return False
    else:
        return True


def print_line(line):
    print " " + line[0] + " | " + line[1] + " | " + line[2]


def print_line_separation():
    print "___________"


class Grid(object):

    def __init__(self):
        self.data = [[" "] * 3 for n in range(3)]
        self.player1_marker = "X"
        self.player2_marker = "O"
        pass

    def process_player_move(self, player_id, player_move):
        if is_invalid_move(player_move):
            return False
        row = int(player_move[0]) - 1
        column = int(player_move[-1]) - 1
        if self.data[row][column] == " ":
            if player_id == 1:
                self.data[row][column] = self.player1_marker
            else:
                self.data[row][column] = self.player2_marker
            return True
        else:
            return False

    def no_winner(self):
        if self.is_diagonal_winner():
            return False
        if self.is_vertical_winner():
            return False
        if self.is_horizontal_winner():
            return False
        return True

    def is_diagonal_winner(self):
        str1 = self.data[0][0] + self.data[1][1] + self.data[2][2]
        str2 = self.data[0][2] + self.data[1][1] + self.data[2][0]
        if (len(str1.replace(" ", "")) == 3 and str1[0] == str1[1] and str1[0] == str1[2]) or (
                    len(str2.replace(" ", "")) == 3 and str2[0] == str2[1] and str2[0] == str2[2]):
            return True
        return False

    def is_vertical_winner(self):
        for column in range(0, 2):
            str = ""
            for line in self.data:
                str = str + line[column]
            if len(str.replace(" ", "")) == 3 and str[0] == str[1] and str[0] == str[2]:
                return True
        return False

    def is_horizontal_winner(self):
        for line in self.data:
            str = ""
            for element in line:
                str = str + element
            if len(str.replace(" ", "")) == 3 and str[0] == str[1] and str[0] == str[2]:
                return True
        return False

    def is_not_full(self):
        for line in self.data:
            if " " in line:
                return True
        else:
            return False

    def display(self):
        counter = 0
        for line in self.data:
            print_line(line)
            if counter < len(self.data) - 1:
                print_line_separation()
            counter += 1
