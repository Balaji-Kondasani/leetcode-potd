'''
Time Complexity -- O(n)
Space Complexity -- O(1)
'''

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        minimum_path=0
        for path in range(len(points)-1):
            a=points[path]
            b=points[path+1]

            dx=abs(b[0]-a[0])
            dy=abs(b[1]-a[1])

            minimum_path+=(min(dx,dy)+abs(dx-dy))
        return minimum_path
        