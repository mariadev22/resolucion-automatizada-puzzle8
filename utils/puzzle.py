import random
import copy

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

class Board:
    # Generar tablero solucionable
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = self.generate_random_board()

    def generate_random_board(self):
        flat_goal = sum(GOAL_STATE, [])
        while True:
            flat_board = flat_goal[:]
            random.shuffle(flat_board)
            if self.is_solvable(flat_goal) % 2 == 0 and self.is_solvable(flat_board) % 2 == 0:
                return [flat_board[i:i+3] for i in range(0, 9, 3)]
            elif self.is_solvable(flat_goal) % 2 != 0 and self.is_solvable(flat_board) % 2 != 0:
                return [flat_board[i:i+3] for i in range(0, 9, 3)]

    def is_solvable(self, flat_board):
        count = 0
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] and flat_board[j] and flat_board[i] > flat_board[j]:
                    count += 1
        return count
    
    def display_console(self):
        for row in self.board:
            print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    # Vecinos cercanos
    def get_neighbors(self):
        neighbors = []
        x, y = self.find_zero()

        for dx, dy in DIRECTIONS.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = copy.deepcopy(self.board)
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbor = Board(new_board)
                neighbors.append(neighbor)
        return neighbors
    
    def to_tuple(self):
        return tuple(tuple(row) for row in self.board)
    
    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board == other.board
        return False
    
    def __hash__(self):
        return hash(self.to_tuple())


