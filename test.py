from solve import Board
import numpy as np

if __name__ == '__main__':
    # n rows, m cols
    n, m = 3, 5

    # covered tiles
    covered = [(1, 1), (2, 3)]

    state = np.zeros((n, m), dtype=bool)

    for block in covered:
        x, y = block
        state[x, y] = True
    
    game = Board(state)
    game.set_pos(2, 4)
    path = game.solve()
    game.reset()
    print(path)