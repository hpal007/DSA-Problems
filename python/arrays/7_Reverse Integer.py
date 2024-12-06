
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
"""

def is_within_32bit_range(num):
    return -2147483648 <= num <= 2147483647


def reverse(x: int) -> int:
    output = 0
    is_negative = x < 0
    x = abs(x)
    while x > 0:
       r =   x%10
       output = output * 10  + r 
       x = x //10

    if is_negative:
        output = -output
    if is_within_32bit_range(output):
        return output 
    else:
        return 0

reverse(1534236469)