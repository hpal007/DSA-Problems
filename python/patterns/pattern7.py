def diamond_star_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

    * * * * * * * * * 
      * * * * * * *
        * * * * *
          * * *
            *

    """
    for i in range(1,n+1):
        #space 
        for _ in range(n-i):
            print("", end=" ")
        #Star
        for _ in range(2*i-1):
            print("*", end="")
        #space
        for _ in range(n-i):
            print("", end=" ")
        print()

    for i in range(n,0, -1):
        #space 
        for _ in range(n-i):
            print("", end=" ")
        #Star
        for _ in range(2*i-1):
            print("*", end="")
        #space
        for _ in range(n-i):
            print("", end=" ")
        print()

diamond_star_pattern(3)