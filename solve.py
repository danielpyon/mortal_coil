import numpy as np

class Board:
    def __init__(self, state):
        # board tracks "visited" for each pos
        self.board = state
        # current position for solve
        self.pos = (0, 0)

    def set_pos(self, x, y):
        self.pos = (x, y)

    def solve(self, path=''):
        '''
        Returns the solution if it exists, otherwise None.
        Starts search at self.pos
        '''
        x, y = self.pos
        L, R = self.valid_pos(x, y - 1), self.valid_pos(x, y + 1)
        U, D = self.valid_pos(x - 1, y), self.valid_pos(x + 1, y)
        if not (L or R or U or D):
            return None

        for direction in ['U', 'R', 'D', 'L']:
            moved = self.move(direction)
            
            if self.valid_sol():
                return path
            if len(moved) == 0:
                return None
            
            if self.solve(path + direction):
                return path + direction

            for (a, b) in moved:
                self.board[a, b] = False
            self.pos = moved[0]

        return False

    def valid_sol(self):
        return self.board.all()

    def in_bounds(self, x, y):
        h, w  = self.board.shape
        return 0 <= x < h and 0 <= y < w

    def valid_pos(self, x, y):
        return self.in_bounds(x, y) and not self.board[x, y]

    def move(self, direction):
        x, y = self.pos
        h, w = self.board.shape
        if not self.valid_pos(x, y):
            return []
        L, R = self.valid_pos(x, y - 1), self.valid_pos(x, y + 1)
        U, D = self.valid_pos(x - 1, y), self.valid_pos(x + 1, y)
        if not eval(direction):
            return []

        # coords to update
        if direction == 'L':
            # y, y - 1, y - 2, ... , 0
            coords = zip([x] * (y + 1), range(y, -1, -1))
        elif direction == 'D':
            coords = zip(range(x, w), [y] * (w - x))
        elif direction == 'R':
            coords = zip([x] * (h - y), range(y, h))
        else:
            coords = zip(range(x, -1, -1), [y] * (x + 1))

        moved = []
        for (a, b) in coords:
            if not self.valid_pos(a, b):
                # stop
                break
            self.board[a, b] = True
            moved.append((a, b))
            self.pos = a, b

        # return which positions were affected for backtracking
        return moved

if __name__ == '__main__':
    # n rows, m cols
    n, m = 4, 4

    # covered tiles
    covered = [(3, 0), (2, 2)]

    state = np.zeros((n, m), dtype=bool)

    for block in covered:
        x, y = block
        state[x, y] = True

    game = Board(state)
    game.set_pos(3, 1)
    path = game.solve()

    print(game.board)

    print(path)
