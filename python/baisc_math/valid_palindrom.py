
def isPalindrome( s: str):
    new_s = ""
    for el in s:
        if el.isalnum():
            new_s = new_s+ el.lower()
    start = 0
    end = len(new_s) -1

    while start < end:
        if new_s[start]== new_s[end]:
            start +=1
            end -=1
        else:
            return False
            
    return True



# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = " "

val = isPalindrome(s)
print(val)


# https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/