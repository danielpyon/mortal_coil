import numpy as np

class Board:
    def __init__(self, state):
        # board tracks "visited" for each pos
        self.board = state
        # copy for reset
        self.__orig = np.copy(state)
        
        # current position for solve
        self.pos = (0, 0)

    def set_pos(self, x, y):
        self.pos = (x, y)
        self.board[x, y] = True

    def reset(self):
        self.board = np.copy(self.__orig)
        self.pos = (0, 0)

    def solve(self, path=''):
        x, y = self.pos
        if self.valid_sol():
            return path

        for direction in ['U', 'R', 'D', 'L']:
            orig, moved = self.move(direction)
            
            if len(moved) == 0:
                continue

            sol = self.solve(path + direction)
            if len(sol) > 0:
                return sol
            else:
                for (a, b) in moved:
                    self.board[a, b] = False
                self.pos = orig

        # dead end
        return ''

    def valid_sol(self):
        return self.board.all()

    def valid_pos(self, x, y):
        h, w = self.board.shape
        return 0 <= x < h and 0 <= y < w and not self.board[x, y]

    def move(self, direction):
        h, w = self.board.shape
        x, y = self.pos
        if direction == 'L':
            coords = zip([x] * (y + 1), range(y, -1, -1))
        elif direction == 'D':
            coords = zip(range(x, w), [y] * (w - x))
        elif direction == 'R':
            coords = zip([x] * (w - y), range(y, w))
        else:
            coords = zip(range(x, -1, -1), [y] * (x + 1))

        moved = []
        for (a, b) in coords:
            if (a, b) == (x, y):
                continue
            if not self.valid_pos(a, b):
                break
            self.board[a, b] = True
            moved.append((a, b))
            self.pos = a, b

        # return which positions were affected for backtracking
        return (x, y), moved

def solve(state):
    n, m = state.shape
    game = Board(state)
    for i in range(n):
        for j in range(m):
            game.set_pos(i, j)
            path = game.solve()
            game.reset()
            if len(path) > 0:
                return (i, j) , path
    return None

if __name__ == '__main__':
    # n rows, m cols
    n, m = 4, 4

    # covered tiles
    covered = [(3, 0), (2, 2)]

    state = np.zeros((n, m), dtype=bool)

    for block in covered:
        x, y = block
        state[x, y] = True

    print(solve(state))