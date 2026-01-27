'''
Time Complexity -- O(nlog(n))
Space Complexity -- O(1)
'''

class Solution(object):
    def minimumDifference(self, nums, k):
        
        nums.sort()
        i,j=0,0
        min_diff=float("inf")
        while j<len(nums):
            if j-i+1==k:
                min_diff=min(min_diff,nums[j]-nums[i])
                i+=1
            j+=1
        return min_diff