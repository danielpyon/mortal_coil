import numpy as np

class Board:
    def __init__(self, state):
        # board tracks "visited" for each pos
        self.board = state
        # current position for solve
        self.pos = (0, 0)

    def set_pos(self, x, y):
        self.pos = (x, y)

    def solve(self, path):
        '''
        Returns the solution if it exists, otherwise None.
        Start the search at (x, y)
        '''
        pass

    def in_bounds(self, x, y):
        h, w  = self.board.shape
        return 0 <= x < h and 0 <= y < w

    def valid_pos(self, x, y):
        return self.in_bounds(x, y) and not self.board[x, y]

    def move(self, direction):
        x, y = self.pos
        h, w = self.board.shape
        if not self.valid_pos(x, y):
            return
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

        for (a, b) in coords:
            if not self.valid_pos(a, b):
                # stop
                break
            self.board[a, b] = True

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
    game.set_pos(2, 0)
    game.move('R')

    print(game.board)
