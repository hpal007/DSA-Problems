"""
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.
Example
remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]

"""

def remove_duplicates(arr):
    seen = []
    for el in arr:
        if el not in seen:
            seen.append(el)
    return seen

print(remove_duplicates([1, 1, 1, 2, 2, 3, 4, 5]))


# Time Complexity: O(n) 
# Space Complexity: O(n) 