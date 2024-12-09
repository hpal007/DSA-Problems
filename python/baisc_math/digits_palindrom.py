def is_negative(num):
     return  num >0
            
def isPalindrome(x: int) -> bool:
        og = x
        reversed = 0
        while x>0:
            last_digit = x%10
            x = x//10
            reversed = (10 * reversed) + last_digit
        if is_negative(x):
            return False
        else:
            return reversed == og
        
    
V= isPalindrome(121)
print(V)