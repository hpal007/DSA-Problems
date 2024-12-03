""" input
n = 5
l = [0,0,1,1,0]
output = [0,0,0,1,1]
"""

from typing import List
def segregate0and1(nums: List[int], n: int):
    left = 0
    right = n -1

    while(left<right):
        while(nums[left] == 0 and left < right):
            left +=1

        while(nums[right] == 1 and left < right):
            right -=1
        
        if left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1

    print(nums)



l = [0,1,0,1,1,0]
segregate0and1(l, n = 6)