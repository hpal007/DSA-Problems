
"""
Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 
"""

# brute force   # TC O(N^2) * O(N) = O(N^3) 
# def is_palindrom(string):
#     s = 0
#     e = len(string) -1
#     while s <=e:
#         if string[s] != string[e]:
#             return False
#         else:
#             s +=1
#             e -=1 
        
#     return True

# def longest_palindrom(string):
#     l = len(string)   
#     longeststring = ""
#     for i in range(l):
#         substirng = ""
#         for j in range(i, l):
#             substirng += string[j]
#             if is_palindrom(substirng):
#                 if len(longeststring) < len(substirng):
#                     longeststring = substirng

#     print(longeststring)
 
# longest_palindrom("babad")


# efficient approch 
# TC = O(N^2) + O(N^2) = O(N^2)

def longestPalindrome(s: str) -> str:
    l = len(s)
    ans = ""
    maxlen = 0

    for mid in range(l):
        i = mid -1
        j = mid + 1
        curlen = 1
        while i >=0 and j < l and s[i] == s[j]:
            i -=1
            j +=1
            curlen +=2
        if curlen > maxlen:
            ans = s[i+1:j]
            maxlen = curlen

    for mid in range(l):
        i = mid
        j = mid + 1
        curlen = 0
        while i >=0 and j < l and s[i] == s[j]:
            i -=1
            j +=1 
            curlen += 2

        if curlen > maxlen:
            ans = s[i+1:j]
            maxlen = curlen           

    return ans

longestPalindrome("cbbd")