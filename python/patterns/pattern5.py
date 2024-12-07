def star_trangle(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

       * 
      * *
     * * * *

    """

    for i in range(n):
        #space 
        for _ in range(n-i):
            print(" ", end=" ")
        #Star
        for _ in range(2*i-1):
            print("*", end=" ")

        #space
        for _ in range(n-i):
            print(" ", end=" ")
        
        print()

star_trangle(5)