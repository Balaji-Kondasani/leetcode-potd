'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- DFS
'''

class Solution(object):
    def __init__(self):
        self.maxsum=float("-inf")
    def tree_sum(self,root):
        if root is None:
            return 0
        left_subtree=self.tree_sum(root.left)
        right_subtree=self.tree_sum(root.right)
        return root.val+left_subtree+right_subtree

    def split_tree_sum(self,root,total_sum):
        if root is None:
            return 0
        leftTreeSum=self.split_tree_sum(root.left,total_sum)
        rightTreeSum=self.split_tree_sum(root.right,total_sum)
        sum1=root.val+leftTreeSum+rightTreeSum
        self.maxsum=max(self.maxsum,sum1*(total_sum-sum1))
        return sum1
    def maxProduct(self, root):
        total_sum=self.tree_sum(root)
        self.split_tree_sum(root,total_sum)
        return self.maxsum%1000000007
        
        