"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example :
Input: nums = [1,2,3,1]
Output: true
Hint: Use sets

"""


# def is_contains_duplicates(arr):
#     return len(set(arr)) != len(arr) 


def is_contains_duplicates(arr):
    sets = set()
    for el in arr:
        if el in sets:
            return True
        sets.add(el)
    return False
            
     

print(f"Result: {is_contains_duplicates([1,2,3,1])}")

# Time Complexity: O(n) 
# Space Complexity: O(n)