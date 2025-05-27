import random

class Board:
    def __init__(self):
        self.board = self._generate_random_board()

    def _generate_random_board(self):
        board = list(range(9))
        while True:
            random.shuffle(board)
            if self._is_solvable(board):
                return [board[i:i+3] for i in range(0, 9, 3)]

    def _is_solvable(self, number):
        count = 0
        for i in range(len(number)):
            for j in range(i + 1, len(number)):
                if number[i] and number[j] and number[i] > number[j]:
                    count += 1
        return count % 2 == 0

    def display_console(self):
        for row in self.board:
            print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))