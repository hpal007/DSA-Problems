from typing import List

# # square of sorted array tc: O(nlogn)
# def sortedSquares(nums: List[int]) -> List[int]:
#         return sorted([el*el for el in nums])



#withoutsort
def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    l = 0
    r = n -1
    index = n -1
    output = [0 for _ in range(n)]
    while l<=r:
        sq_of_left = nums[l] * nums[l]
        sq_of_right = nums[r]* nums[r]
        if sq_of_right>sq_of_left:
            output[index] = sq_of_right
            r -=1
        else: 
            output[index] = sq_of_left
            l+=1

        index -=1
        
    return output

input_list = [-3,-1,0,3,10]
sortedSquares(input_list)