import random


def coord_to_index(x_coord, y_coord):
    return 3 - y_coord, x_coord - 1


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for row in range(3)] for col in range(3)]
        self.display_board()

    def display_board(self):
        print(9 * '-',
              f'| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} |',
              f'| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} |',
              f'| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} |',
              9 * '-', sep='\n')

    def check_game_status(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return f'{self.board[1][1]} wins'
        for index in range(3):
            if self.board[0][index] == self.board[1][index] == self.board[2][index] != ' ':
                return f'{self.board[0][index]} wins'
            if self.board[index][0] == self.board[index][1] == self.board[index][2] != ' ':
                return f'{self.board[index][0]} wins!'
        if not any(' ' in row for row in self.board):
            return 'Draw!'

    def user_move(self):
        while True:
            try:
                x, y = map(int, input("Enter the Coordinates: ").split())
                x, y = coord_to_index(x, y)
                if not self.board[x][y].isspace():
                    print("This cell is occupied! Choose another one!")
                else:
                    return x, y
            except ValueError:
                print(" You should enter numbers!")
            except IndexError:
                print("Coordinates should be from 1 to 3!")

    def ai_move(self):
        print('Making move level "easy"')
        x, y = coord_to_index(random.randint(1, 3), random.randint(1, 3))
        while not self.board[x][y].isspace():
            x, y = coord_to_index(random.randint(1, 3), random.randint(1, 3))
        return x, y

    def player_move(self, x, y, play):
        self.board[x][y] = play
        self.display_board()

    def play(self):
        while any(' ' in row for row in self.board):
            params = input("Input command: ").split()
            if len(params) <= 2:
                if len(params) == 1 and params[0] == "exit":
                    exit()
                else:
                    print("Bad parameters!")
            elif len(params) == 3:
                player1, player2 = params[1:]
                if player1 == "easy":
                    self.player_move(*self.ai_move(), "X")
                elif player1 == player2 == "user":
                    self.player_move(*self.user_move(), "O")
                elif player2 == "easy":
                    self.player_move(*self.ai_move(), "O")
                if self.check_game_status():
                    print(self.check_game_status())


TicTacToe().play()

