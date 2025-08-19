class Board:
    """Класс, который описывает игровое поле."""

    board_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def make_move(self, x, y, symbol):
        self.board[x][y] = symbol

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        # Проверка по вертикали и горизонтали
        for i in range(self.board_size):
            if all(self.board[i][j] == player for j in range(self.board_size)):
                return True
            if all(self.board[j][i] == player for j in range(self.board_size)):
                return True
        # Проверка по диагонали
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player):
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def __str__(self):
        return f'Объект игрового поля размером {self.board_size}x{self.board_size}'
