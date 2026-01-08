'''
Approach 1
Recursion + Memoization
Time Complexity -- O(m*n)
Space Complexity -- O(m*n)
'''

class Solution:
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        NEG_INF = -10**9
        
        # DP table initialized with NEG_INF
        dp = [[NEG_INF] * (n + 1) for _ in range(m + 1)]

        def solve(i, j):
            # Base case
            if i == m or j == n:
                return NEG_INF

            if dp[i][j] != NEG_INF:
                return dp[i][j]

            val = nums1[i] * nums2[j]

            take_i_j = val + solve(i + 1, j + 1)
            skip_i = solve(i, j + 1)
            skip_j = solve(i + 1, j)

            dp[i][j] = max(val, take_i_j, skip_i, skip_j)
            return dp[i][j]

        return solve(0, 0)
