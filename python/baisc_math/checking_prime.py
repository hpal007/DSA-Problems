                  
# Brute Force Approach to check prime number 
# TC O(N)
def checkPrime(n):
    cnt = 0
    # Loop through numbers from 1 to n.
    for i in range(1, n+1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

    # If the number of
    # factors is exactly 2
    if cnt == 2:
        # Return True, indicating
        # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else:
        # Return False, indicating
        # that the number is not prime.
        return False


# Optimal Approach 
# TC O(sqrt(N))
           
import math

def checkPrime(n):
    # count the number of factors.
    cnt = 0

    # Loop through numbers from 1
    # to the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

            # If n is not a perfect square,
            # count its reciprocal factor.
            if n // i != i:
                cnt = cnt + 1

    # If the number of
    # factors is exactly 2.
    if cnt == 2:
         # Return true, indicating
         # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else: 
        # Return false, indicating
        # that the number is not prime.
        return False

           
val = checkPrime(4)
print(val)

# https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/