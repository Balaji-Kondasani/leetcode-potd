'''
Approach-1
Time Complexity -- O(n^2) = O(nlogn)+O(n*m)
Space Complexity -- O(n)
'''


#Approach-1
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        

class Solution:
    def flatten(self, root):
        result=[]
        temp=root
        while temp:
            result.append(temp.data)
            if temp.bottom:
                temp2=temp.bottom
                while temp2:
                    result.append(temp2.data)
                    temp2=temp2.bottom
            temp=temp.next
        result.sort()
        root2=None
        for i in result:
            newnode=Node(i)
            if root2 is None:
                root2=newnode
            else:
                temp=root2
                while temp.bottom is not None:
                    temp=temp.bottom
                temp.bottom=newnode
        return root2

'''
Approach-2
Time Complexity -- n*O(2m) ~ O(2mn)
Space Complexity -- O(n)
'''

#Approach 2
class Solution:
    def merge_lists(self,list1,list2):
        dummyNode=Node(0)
        result=dummyNode
        while list1 and list2:
            if list1.data<list2.data:
                result.bottom=list1
                result=list1
                list1=list1.bottom
            else:
                result.bottom=list2
                result=list2
                list2=list2.bottom
            result.next=None
        if list1:
            result.bottom=list1
        if list2:
            result.bottom=list2
        return dummyNode.bottom
            
    def flatten(self, root):
        if root is None or root.next is None:
            return root
        returned_head=self.flatten(root.next)
        return self.merge_lists(returned_head,root)
            