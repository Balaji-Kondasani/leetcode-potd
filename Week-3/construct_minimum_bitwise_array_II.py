'''
Approach 2
Time Complexity -- O(n)
Space Complexity -- O(1)

Optimal Approach 
'''



class Solution:
    def minBitwiseArray(self, nums):
        result = []

        for num in nums:
            if num == 2:
                result.append(-1)
                continue

            found = False
            for j in range(1, 32):
                if (num & (1 << j)) > 0:   # set bit
                    continue

                # we found an unset bit at jth position
                result.append(num ^ (1 << (j - 1)))  # toggle (j-1)th bit
                found = True
                break

            if not found:
                result.append(-1)

        return result
