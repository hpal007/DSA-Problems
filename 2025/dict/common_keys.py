"""
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:
{'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""


def merge_dicts(dic1, dic2):
    result = dic1.copy()

    for el in dic2:
        if el in result:
            result[el] += dic2[el]
        else:
            result[el] = dic2[el]

    return result
    





dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1,dict2))