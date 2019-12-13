def surfaceArea(A):
    '''
    A toy consists of cubes stacked on a 2D board.
    The 2D board has H rows and W columns. The board is divided
    into 1x1 cells. Each cell at coordinate (i, j) contains
    an integer A_i,j corresponding to the number of unit
    cubes stacked at (i, j).

    Calculate the price of the toy given that the price is
    equal to the 3D surface of the toy.

    inputs:
    A_i,j   array   a list containing H lists of size W, with the
                    number of blocks stacked at location (i, j).

    constraints:

    1 <= H, W <= 100

    outputs:
    The surface area of the toy
    '''
    H = len(A)
    W = len(A[0])
    # Location of adjacent/neighbouring stacks of cubes
    adj = [(0,1), (1,0), (0,-1), (-1,0)]

    # surface area
    sur = 0

    for i in range(H):
        for j in range(W):
            # Top & bottom surface of the stack
            sur += 2
            # check adjacent stacks
            for n, m in adj:
                # Check if at edge of toy
                if i + n >= H or i + n < 0 or j + m >= W or j + m < 0:
                    sur += A[i][j]
                # Check if next stack is taller
                elif A[i+n][j+m] >= A[i][j]:
                    continue
                else:
                    # Add the surface area on that side of the stack
                    sur += A[i][j] - A[i+n][j+m]

    return sur

if __name__ == '__main__':
    a1 = [[1]]
    a2 = [[1, 3, 4],[2, 2, 3],[1, 2, 4]]

    print(surfaceArea(a1))
    print(surfaceArea(a2))