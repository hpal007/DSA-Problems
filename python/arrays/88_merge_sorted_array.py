from typing import List

# initial solution
# def merge(nums1: List[int], m: int, nums2: List[int], n: int):
#     # output = [0 for el in range(m+n)]

#     nums1[m:] = nums2
#     nums1.sort()


# best solution
def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    i = m - 1  # pointer to last valid element in nums1
    j = n - 1  # pointer to last element in nums2
    k = m + n - 1  # position to end of num1(total length)

    #   merge in reverse  order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # add remaining values from nums2 when j is still not 0, this will happen when length of nums2 is greater then nums 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
