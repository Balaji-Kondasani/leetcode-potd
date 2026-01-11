class Solution:
    def NSR(self, heights):
        st = []
        n = len(heights)
        pseudo_index = n
        right = [0] * n

        for i in range(n - 1, -1, -1):
            if not st:
                right[i] = pseudo_index
            else:
                while st and heights[st[-1]] >= heights[i]:
                    st.pop()
                right[i] = pseudo_index if not st else st[-1]
            st.append(i)

        return right

    def NSL(self, heights):
        st = []
        n = len(heights)
        pseudo_index = -1
        left = [0] * n

        for i in range(n):
            if not st:
                left[i] = pseudo_index
            else:
                while st and heights[st[-1]] >= heights[i]:
                    st.pop()
                left[i] = pseudo_index if not st else st[-1]
            st.append(i)

        return left

    def MAH(self, heights):
        n = len(heights)
        right = self.NSR(heights)
        left = self.NSL(heights)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * heights[i]
            if area > max_area:
                max_area = area

        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        height = [0] * m

        # first row histogram
        for i in range(m):
            height[i] = 1 if matrix[0][i] == '1' else 0

        maxA = self.MAH(height)

        # remaining rows
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            maxA = max(maxA, self.MAH(height))

        return maxA
