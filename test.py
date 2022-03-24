from solve import Board, solve
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
    
    print(solve(state))