'''
Approach - 1
Time Complexity -- O(nlogn)
Space Complexity -- O(1)

Observations -- remove only consequetive bars will result in increase of height and width
                which means we need to find the longest consequetive array in both given arrays and choose 
                the minimum of their lengths to form a square
                length obtained+1 = width/height
'''

class Solution(object):
    def longestConsequetiveSubArray(self,nums):
        j=1
        length=1
        max_length=1
        while j<len(nums):
            if nums[j]-nums[j-1]==1:
                length+=1
            else:
                length=1
            j+=1
            max_length=max(max_length,length)
        return max_length
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()
        print(hBars)
        length1=self.longestConsequetiveSubArray(hBars)
        length2=self.longestConsequetiveSubArray(vBars)
        print(length1,length2)
        side=min(length1,length2)+1
        return side*side
        