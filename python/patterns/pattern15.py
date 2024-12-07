def alpha_hill_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern :

         A  
        ABA 
       ABCBA

    """

    for i in range(1, n+1):
        #space
        for _ in range(n-i):
            print("", end=" ")
        #char
        for j in range(1, i+1):
            print(chr(64 +j), end=" ")
            
        #space
        for j in range(i-1,0, - 1 ):
            print(chr(64 +j), end=" ")
        print()


alpha_hill_pattern(3)
