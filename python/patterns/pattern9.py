def binary_number_triangle(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

    *  
    **
    ***  
    **
    *

    """

    for i in range(1,n+1):
        start = 1
        if i%2 ==0:
            start = 0
        for j in range(i):
            print(start, end=" ")
            start = 1 - start
            
        print()
        


binary_number_triangle(5)