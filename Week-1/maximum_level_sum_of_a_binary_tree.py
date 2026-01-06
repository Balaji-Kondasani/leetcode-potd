'''
Approach 1
Time Complexity -- O(n)
Space Complexity --O(n)

Technique Used -- DFS
'''

class Solution(object):
    def __init__(self):
        self.hashmap={}
    def dfs(self,root,level):
        if root is None:
            return 
        if level in self.hashmap:
            self.hashmap[level]+=root.val
        else:
            self.hashmap[level]=root.val
        self.dfs(root.left,level+1)
        self.dfs(root.right,level+1)
    def maxLevelSum(self, root):
        self.dfs(root,1)
        min_level=1
        max_value=float("-inf")
        for key,value in self.hashmap.items():
            if value>max_value:
                max_value=value
                min_level=key
        return min_level