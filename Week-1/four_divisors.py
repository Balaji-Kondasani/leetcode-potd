'''
Approach-1
Time Complexity -- O(sqrt(n))
Space Comlpexity -- O(1)
'''

#Approach-1
import math
class Solution(object):
    def get_divisors(self,num):
        counter=2
        sum_of_divisors=1+num
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                if i*i%num==0:
                    counter+=1
                    sum_of_divisors+=i
                else:
                    counter+=2
                    sum_of_divisors+=(i+num//i)
                if counter>4:
                    continue
        if counter==4:
            return sum_of_divisors
        return 0
    def sumFourDivisors(self, nums):
        sum_of_divisors=0

        for i in nums:
            divisors_sum=self.get_divisors(i)
            if divisors_sum!=0:
                sum_of_divisors+=divisors_sum
        return sum_of_divisors

        