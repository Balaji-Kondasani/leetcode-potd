'''
Time Complexity -- O(nlog(n))
Space Complexity -- O(1)
'''

class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        i,j=0,len(nums)-1

        max_pair_sum=float("-inf")
        while i<j:
            max_pair_sum=max(max_pair_sum,nums[i]+nums[j])
            i+=1
            j-=1
        return max_pair_sum
        