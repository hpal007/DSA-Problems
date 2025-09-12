"""
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.
Example

missing_number([1, 2, 3, 4, 6], 6) # 5
"""

def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Example usage:
print(missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10], 10))  # Output: 8



# n * (n + 1) // 2 is the formula for the sum of the first n natural numbers.
# We calculate the expected sum of numbers from 1 to n and subtract the actual sum of the