""" 
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

from typing import List

def twoSum_bf(nums: List[int], target: int) -> List[int]:
        result = []
        for el in range(len(nums)):
            for k in range(len(nums)):
                if not k == el:
                    if (nums[el] + nums[k]) == target:
                        result.append(el)
                        result.append(k)
                        return result


def two_sum(nums, target):
     seen = {}

     for index, num in enumerate(nums):
          if (target - num) in seen:
               return [seen[target-num], index]
          seen[num]=index
               


# result = twoSum_bf([2,7,11,15], 9)
# print(result)

result = two_sum([2,7,11,15], 9)
print(result)