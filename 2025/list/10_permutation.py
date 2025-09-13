"""
Permutation of each other list 
"""


def permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    
    lst1.sort()
    lst2.sort()

    if lst2 == lst1:
        return True
    return False


print(permutation([1,2,3], [2,1,2]))