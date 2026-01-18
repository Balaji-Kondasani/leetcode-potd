class Solution(object):
    def largestMagicSquare(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # Row wise prefix sum
        rowCumsum = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            rowCumsum[i][0] = grid[i][0]
            for j in range(1, cols):
                rowCumsum[i][j] = rowCumsum[i][j - 1] + grid[i][j]

        # Column wise prefix sum
        colCumsum = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            colCumsum[0][j] = grid[0][j]
            for i in range(1, rows):
                colCumsum[i][j] = colCumsum[i - 1][j] + grid[i][j]

        # iterate from largest square side to smallest
        for side in range(min(rows, cols), 1, -1):

            # check square of length = side starting from all possible cells
            for i in range(rows - side + 1):
                for j in range(cols - side + 1):

                    # target sum = first row sum
                    targetSum = rowCumsum[i][j + side - 1] - (rowCumsum[i][j - 1] if j > 0 else 0)

                    allSame = True

                    # check rows
                    for r in range(i + 1, i + side):
                        rowSum = rowCumsum[r][j + side - 1] - (rowCumsum[r][j - 1] if j > 0 else 0)
                        if rowSum != targetSum:
                            allSame = False
                            break

                    if not allSame:
                        continue

                    # check columns
                    for c in range(j, j + side):
                        colSum = colCumsum[i + side - 1][c] - (colCumsum[i - 1][c] if i > 0 else 0)
                        if colSum != targetSum:
                            allSame = False
                            break

                    if not allSame:
                        continue

                    # check diagonals
                    diag = 0
                    antiDiag = 0
                    for k in range(side):
                        diag += grid[i + k][j + k]
                        antiDiag += grid[i + k][j + side - 1 - k]

                    if diag == targetSum and antiDiag == targetSum:
                        return side

        return 1
