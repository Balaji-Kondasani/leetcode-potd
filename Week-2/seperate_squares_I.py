class Solution:
    def check(self, squares, midY, total):
        bottomArea = 0.0

        for square in squares:
            y = square[1]
            l = square[2]

            bottomY = y
            topY = y + l

            if midY >= topY:
                # full square below
                bottomArea += l * l
            elif midY > bottomY:
                # partial square below
                bottomArea += (midY - bottomY) * l

        # Is bottom area more than above?
        return bottomArea >= total / 2.0

    def separateSquares(self, squares):
        low = float("inf")
        high = float("-inf")
        total = 0.0

        for square in squares:
            y = square[1]
            l = square[2]

            total += l * l
            low = min(low, y)
            high = max(high, y + l)

        resultY = 0.0

        while high - low > 1e-5:
            midY = low + (high - low) / 2.0
            resultY = midY

            if self.check(squares, midY, total):
                # bottom area is more than half, move down
                high = midY
            else:
                low = midY

        return resultY
