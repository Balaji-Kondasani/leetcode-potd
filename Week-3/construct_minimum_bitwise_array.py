'''
Approach 1
Time Complexity -- O(n*i) where i is the given number
Space Complexity -- O(1)

Brute Force -- checking all possibilities
'''

class Solution(object):
    def minBitwiseArray(self, nums):
        result=[-1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(nums[i]):
                if j|j+1==nums[i]:
                    result[i]=j
                    break
        return result                   

'''
Approach 2
Time Complexity -- O()
Space Complexity -- O(1)

Optimal Approach 
'''

