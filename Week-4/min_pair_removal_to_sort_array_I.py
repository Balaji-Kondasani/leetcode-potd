'''
Approach -1 
Time Complexity -- O(n^2)
Space Complexity -- O(1)
'''


class Solution(object):
    def isSorted(self,nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    def minimumPairRemoval(self, nums):

        found=True
        
        operations=0
        if self.isSorted(nums):
            return operations
        while found:
            operations+=1
            min_sum=float("inf")
            index=-1
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<min_sum:
                    min_sum=nums[i]+nums[i+1]
                    index=i
            nums=nums[0:index]+[min_sum]+nums[index+2:]
            
            if self.isSorted(nums):
                found=False
        return operations
        