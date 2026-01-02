'''
Approach 1
Time Complexity -- O(n)
Space  Complexity -- O(n)
'''

#Approach 1
result=set()
class Solution(object):
    def repeatedNTimes(self, nums):
        result=set()
        for i in nums:
            if i in result:
                return i
            else:
                result.add(i)

'''                
Approach 2
Time Complexity -- O(n)
Space Complexity -- O(1)
'''        

#Approach2
class Solution(object):
    def repeatedNTimes(self, nums):
        for i in range(2,len(nums)):
            if nums[i]==nums[i-1] or nums[i]==nums[i-2]:
                return nums[i]
        return nums[0]
        