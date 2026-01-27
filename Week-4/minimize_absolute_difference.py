'''
Time Complexity -- O(nlog(n))
Space Complexity -- O(1)
'''
class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff=float('inf')
        result=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<min_diff:
                min_diff=abs(arr[i]-arr[i+1])

        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==min_diff:
                result.append([arr[i],arr[i+1]])
        
        return result    