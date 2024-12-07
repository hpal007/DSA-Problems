def half_diamond_star(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

    *  
    **
    ***  
    **
    *

    """

    for i in range(2*n):
        star = i
        if i>n:
            star = 2*n-i
        for j in range(star):
            print("*", end=" ")
        print()

half_diamond_star(5)