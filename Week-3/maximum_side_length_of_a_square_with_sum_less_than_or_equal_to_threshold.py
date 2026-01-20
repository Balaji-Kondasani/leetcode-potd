class Solution:
    def maxSideLength(self, mat, threshold):
        rows = len(mat)
        cols = len(mat[0])

        # Build prefix sum matrix
        prefix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                prefix[i][j] = mat[i][j] \
                               + (prefix[i-1][j] if i > 0 else 0) \
                               + (prefix[i][j-1] if j > 0 else 0) \
                               - (prefix[i-1][j-1] if i > 0 and j > 0 else 0)

        # Helper function to get sum of square submatrix
        def sumSquare(i, j, r2, c2):
            total = prefix[r2][c2]
            if i > 0:
                total -= prefix[i-1][c2]
            if j > 0:
                total -= prefix[r2][j-1]
            if i > 0 and j > 0:
                total += prefix[i-1][j-1]
            return total

        best = 0

        for i in range(rows):
            for j in range(cols):
                # k is offset, side length = k+1
                for k in range(best, min(rows - i, cols - j)):
                    r2 = i + k
                    c2 = j + k

                    s = sumSquare(i, j, r2, c2)

                    if s <= threshold:
                        best = k + 1
                    else:
                        break

        return best
