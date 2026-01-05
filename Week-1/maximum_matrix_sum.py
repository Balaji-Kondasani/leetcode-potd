'''
Approach - 1
Time Complexity -- O(n^2)
Space Complexity -- O(1)
'''

'''
Approach Explanation 
Matrix contain negative elements 
negative elements can be eliminated by multiplying adjacent elements
goal -- return max sum of array

Observations:
1. for odd number of negative elements -- after operations only one negative remains , which can be negated to smallest
number in array
2. for even number of negative elements -- return absolute sum of all elements in the array
3. find minimum number by tracking absolute sum of every number
'''

#Approach-1 

class Solution(object):
    def checkColumn(self,column,rows,matrix):
        for i in range(rows-1):
            if matrix[i][column]<0 and matrix[i+1][column]<0:
                matrix[i][column]*=-1
                matrix[i+1][column]*=-1

    def maxMatrixSum(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        count=0
        sum_of_elements=0
        min_num=float("inf")
        for i in range(0,rows):
            for j in range(0,cols):
                sum_of_elements+=abs(matrix[i][j])
                if abs(matrix[i][j])<min_num:
                    min_num=abs(matrix[i][j])
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]<0:
                    count+=1
        if count%2==0:
            return sum_of_elements
        else:
            sum_of_elements-=(2*min_num)
            return sum_of_elements
                