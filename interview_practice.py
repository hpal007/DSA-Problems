
# 1. Reverse a string 
def rev_string(v):
    return v[::-1]

# 2. Find a missing number
def missing_number_from_array(arr, t):
    sum_of_all_number = t*(t+1)//2
    return sum_of_all_number - sum(arr)

# 3. Given a list and a target value, find two numbers that add up to the target.
def two_sum(nums, target):
    s = {}
    for i, el in enumerate(nums):
        if target - el in s:
            return s[target - el], i
        else:
            s[el]= i

# 4. Write a function to remove duplicates from a list while preserving order.
def remove_duplicate_from_list(arr):
    # return set(arr)
    new_arr = []
    for el in arr:
        if el not in new_arr:
            new_arr.append(el)
    return new_arr
        

# 5. Sort given list without using sortted funtion (bubble sort)
def sort_list(lst):
    l = len(lst)
    for i in range(l):
        for j in range(l-i-1):
            if lst[j] > lst[j+1]:
                 lst[j],lst[j+1] = lst[j+1] ,lst[j]
    return lst
# 6. Merge sorted list 
def sorted_list(lst1, lst2):
    lst_merged = []
    i = 0
    j = 0
    while i<len(lst1) and j<len(lst2) :
        if lst1[i] < lst2[j]:
            lst_merged.append(lst1[i]) 
            i +=1     
        else:
            lst_merged.append(lst2[j])
            j +=1
    lst_merged += lst1[i:] + lst2[j:] #remaining values in array 
    return lst_merged

# 7. check palindrome 
def is_palindrome(s):
    s =  "".join([el for el in s.lower() if el.isalnum()])
    if s == s[::-1]:
        return True
    return False

def first_non_repeating(st):
    from collections import Counter

    fq = Counter(st)
    print
    print(f"fq: {fq}")
    for el in st:
        if fq[el] ==1:
            return el

def binary_search(arr, t):
    l = 0
    h = len(arr)-1

    while l<=h:
        mid = (h+l)//2
        if arr[mid] == t:
            return mid
        
        elif arr[mid] > t:
            h = mid -1
            
        else:
           l = mid +1
    return -1


if __name__ == "__main__":
    # print(rev_string("Harish"))
    # print(missing_number_from_array([1,2,3,5,6], 6))
    # print(two_sum([0, 2, 11,7], 9))
    # print(remove_duplicate_from_list([1,2,3,2,4,5,6,5,4]))
    # print(sort_list([1,10,2,5,3,8,9]))
    # print(sorted_list([1,2,3,8,9],[4,5,6,7,10]))
    # print(is_palindrome("A man a plan a canal Panama"))
    # print(first_non_repeating("abacabad"))
    print(binary_search([1,2,3,4,5], 5))
